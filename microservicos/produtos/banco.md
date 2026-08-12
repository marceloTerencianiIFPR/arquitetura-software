# PostgreSQL no Microserviço de Produtos

## 1. Instalar o cliente PostgreSQL

Na pasta `produtos`:

```bash
npm install pg
```

## 2. Adicionar PostgreSQL ao Docker Compose

Na raiz de `microservicos`, use o seguinte `docker-compose.yml`:

```yaml
services:
  produtos:
    build: ./produtos
    ports:
      - "3001:3001"
    environment:
      DATABASE_URL: postgres://postgres:postgres@postgres:5432/produtos_db
    depends_on:
      postgres:
        condition: service_healthy

  pedidos:
    build: ./pedidos
    ports:
      - "3002:3002"
    environment:
      PRODUTOS_URL: http://produtos:3001
    depends_on:
      - produtos

  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: produtos_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d produtos_db"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

## 3. Criar a conexão

Na pasta `produtos`, crie `db.js`:

```javascript
const { Pool } = require("pg");

const pool = new Pool({
  connectionString: process.env.DATABASE_URL
});

module.exports = pool;
```

## 4. Importar a conexão

No início do `server.js`:

```javascript
const db = require("./db");
```

## 5. Criar a tabela

Antes do `app.listen`:

```javascript
async function criarTabela() {
  await db.query(`
    CREATE TABLE IF NOT EXISTS produtos (
      id SERIAL PRIMARY KEY,
      nome VARCHAR(100) NOT NULL,
      preco NUMERIC(10, 2) NOT NULL
    )
  `);

  console.log("Tabela de produtos pronta");
}

criarTabela();
```

## 6. Listar produtos

Substitua a rota `GET /produtos`:

```javascript
app.get("/produtos", async (req, res) => {
  try {
    const resultado = await db.query(
      "SELECT * FROM produtos ORDER BY id"
    );

    res.json(resultado.rows);
  } catch (erro) {
    res.status(500).json({
      erro: "Erro ao buscar produtos"
    });
  }
});
```

## 7. Buscar produto por ID

Substitua a rota `GET /produtos/:id`:

```javascript
app.get("/produtos/:id", async (req, res) => {
  try {
    const resultado = await db.query(
      "SELECT * FROM produtos WHERE id = $1",
      [req.params.id]
    );

    const produto = resultado.rows[0];

    if (!produto) {
      return res.status(404).json({
        erro: "Produto não encontrado"
      });
    }

    res.json(produto);
  } catch (erro) {
    res.status(500).json({
      erro: "Erro ao buscar produto"
    });
  }
});
```

O antigo array `produtos` pode ser removido.

## 8. Criar produtos

Adicione antes do `app.listen`:

```javascript
app.post("/produtos", async (req, res) => {
  const { nome, preco } = req.body;

  if (!nome || preco === undefined || preco <= 0) {
    return res.status(400).json({
      erro: "Nome e preço válido são obrigatórios"
    });
  }

  try {
    const resultado = await db.query(
      `INSERT INTO produtos (nome, preco)
       VALUES ($1, $2)
       RETURNING *`,
      [nome, preco]
    );

    res.status(201).json(resultado.rows[0]);
  } catch (erro) {
    res.status(500).json({
      erro: "Erro ao criar produto"
    });
  }
});
```

## 9. Reconstruir os containers

Na pasta `microservicos`:

```bash
docker compose down
docker compose up --build
```

Aguarde a mensagem:

```text
Tabela de produtos pronta
```

## 10. Cadastrar um produto

No `requests.http` de Produtos:

```http
### Criar produto
POST http://localhost:3001/produtos
Content-Type: application/json

{
  "nome": "Teclado",
  "preco": 150
}

### Listar produtos
GET http://localhost:3001/produtos
```

## 11. Testar a persistência

Recrie os containers:

```bash
docker compose down
docker compose up
```

Consulte novamente:

```http
GET http://localhost:3001/produtos
```

O produto deve permanecer cadastrado no volume `postgres_data`.

## 12. Confirmar a integração com Pedidos

No `requests.http` de Pedidos:

```http
POST http://localhost:3002/pedidos
Content-Type: application/json

{
  "produtoId": 1,
  "quantidade": 2
}
```

O pedido deve retornar os dados do produto armazenado no PostgreSQL e o total calculado.
