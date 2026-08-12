# PostgreSQL no Microserviço de Pedidos

## 1. Instalar o cliente PostgreSQL

Na pasta `pedidos`:

```bash
npm install pg
```

## 2. Criar a conexão

Na pasta `pedidos`, crie `db.js`:

```javascript
const { Pool } = require("pg");

const pool = new Pool({
  connectionString: process.env.DATABASE_URL
});

module.exports = pool;
```

## 3. Criar o segundo banco

Na raiz de `microservicos`, crie a pasta `banco` e o arquivo `banco/init.sql`:

```sql
CREATE DATABASE pedidos_db;
```

## 4. Configurar o Docker Compose

Use o seguinte `docker-compose.yml`:

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
      DATABASE_URL: postgres://postgres:postgres@postgres:5432/pedidos_db
    depends_on:
      postgres:
        condition: service_healthy
      produtos:
        condition: service_started

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
      - ./banco/init.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres -d produtos_db"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
```

O arquivo `init.sql` é executado somente na primeira inicialização do volume. Para recriá-lo:

```bash
docker compose down -v
docker compose up --build
```

> O comando `docker compose down -v` remove os dados existentes no volume.

## 5. Criar a tabela de pedidos

No início do `server.js` de Pedidos, importe a conexão:

```javascript
const db = require("./db");
```

Antes do `app.listen`, adicione:

```javascript
async function criarTabela() {
  await db.query(`
    CREATE TABLE IF NOT EXISTS pedidos (
      id SERIAL PRIMARY KEY,
      produto_id INTEGER NOT NULL,
      nome_produto VARCHAR(100) NOT NULL,
      preco_unitario NUMERIC(10, 2) NOT NULL,
      quantidade INTEGER NOT NULL,
      total NUMERIC(10, 2) NOT NULL
    )
  `);

  console.log("Tabela de pedidos pronta");
}

criarTabela();
```

## 6. Código completo do servidor

Arquivo `pedidos/server.js`:

```javascript
const express = require("express");
const axios = require("axios");
const db = require("./db");

const app = express();

app.use(express.json());

const PRODUTOS_URL =
  process.env.PRODUTOS_URL || "http://localhost:3001";

app.get("/pedidos", async (req, res) => {
  try {
    const resultado = await db.query(
      "SELECT * FROM pedidos ORDER BY id"
    );

    res.json(resultado.rows);
  } catch (erro) {
    res.status(500).json({
      erro: "Erro ao buscar pedidos"
    });
  }
});

app.get("/pedidos/:id", async (req, res) => {
  try {
    const resultado = await db.query(
      "SELECT * FROM pedidos WHERE id = $1",
      [req.params.id]
    );

    const pedido = resultado.rows[0];

    if (!pedido) {
      return res.status(404).json({
        erro: "Pedido não encontrado"
      });
    }

    res.json(pedido);
  } catch (erro) {
    res.status(500).json({
      erro: "Erro ao buscar pedido"
    });
  }
});

app.post("/pedidos", async (req, res) => {
  const { produtoId, quantidade } = req.body;

  if (!produtoId || !quantidade || quantidade <= 0) {
    return res.status(400).json({
      erro: "produtoId e quantidade válida são obrigatórios"
    });
  }

  try {
    const resposta = await axios.get(
      `${PRODUTOS_URL}/produtos/${produtoId}`,
      {
        timeout: 3000
      }
    );

    const produto = resposta.data;
    const total = produto.preco * quantidade;

    const resultado = await db.query(
      `INSERT INTO pedidos (
        produto_id,
        nome_produto,
        preco_unitario,
        quantidade,
        total
      )
      VALUES ($1, $2, $3, $4, $5)
      RETURNING *`,
      [
        produto.id,
        produto.nome,
        produto.preco,
        quantidade,
        total
      ]
    );

    res.status(201).json(resultado.rows[0]);
  } catch (erro) {
    if (erro.response?.status === 404) {
      return res.status(400).json({
        erro: "Produto não encontrado"
      });
    }

    if (erro.code === "ECONNREFUSED" || erro.code === "ECONNABORTED") {
      return res.status(503).json({
        erro: "Serviço de Produtos indisponível"
      });
    }

    return res.status(500).json({
      erro: "Erro ao criar pedido"
    });
  }
});

async function criarTabela() {
  await db.query(`
    CREATE TABLE IF NOT EXISTS pedidos (
      id SERIAL PRIMARY KEY,
      produto_id INTEGER NOT NULL,
      nome_produto VARCHAR(100) NOT NULL,
      preco_unitario NUMERIC(10, 2) NOT NULL,
      quantidade INTEGER NOT NULL,
      total NUMERIC(10, 2) NOT NULL
    )
  `);

  console.log("Tabela de pedidos pronta");
}

criarTabela();

app.listen(3002, () => {
  console.log("Pedidos rodando na porta 3002");
});
```

## 7. Reconstruir os containers

Na pasta `microservicos`:

```bash
docker compose down
docker compose up --build
```

Aguarde as mensagens:

```text
Tabela de produtos pronta
Tabela de pedidos pronta
```

## 8. Testar

Crie um produto:

```http
POST http://localhost:3001/produtos
Content-Type: application/json

{
  "nome": "Teclado",
  "preco": 150
}
```

Crie um pedido:

```http
POST http://localhost:3002/pedidos
Content-Type: application/json

{
  "produtoId": 1,
  "quantidade": 2
}
```

Liste os pedidos:

```http
GET http://localhost:3002/pedidos
```

## 9. Confirmar a persistência

Reinicie os containers:

```bash
docker compose down
docker compose up
```

Consulte novamente:

```http
GET http://localhost:3002/pedidos
```

O pedido deve continuar armazenado no banco `pedidos_db`.

## 10. Referência lógica entre os bancos

O pedido armazena:

- `produto_id`: referência lógica ao produto;
- `nome_produto`: nome no momento da compra;
- `preco_unitario`: preço no momento da compra;
- `quantidade`;
- `total`.

Não existe uma chave estrangeira entre `pedidos_db` e `produtos_db`. Alterações futuras no preço do produto não modificam pedidos anteriores.
