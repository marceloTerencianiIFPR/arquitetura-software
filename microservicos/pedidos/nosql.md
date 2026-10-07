# Persistência com MongoDB em uma Arquitetura de Microserviços

Até este momento, os microsserviços de **Produtos** e **Pedidos** utilizavam PostgreSQL para persistência dos dados.

Nesta etapa, modificaremos a arquitetura para utilizar dois bancos de dados diferentes:

- **Produtos:** continuará utilizando PostgreSQL;
- **Pedidos:** passará a utilizar MongoDB.

Essa abordagem permite observar que cada microsserviço pode utilizar a tecnologia de persistência mais adequada às suas necessidades.

A arquitetura ficará conceitualmente assim:

```text
Cliente
   |
   +--------------------+
   |                    |
   v                    v
Produtos :3001       Pedidos :3002
   |                    |
   v                    v
PostgreSQL           MongoDB
                         |
                         |
                         +---- HTTP ----> Produtos :3001
```

O microsserviço de **Pedidos** continuará consultando o microsserviço de **Produtos** através de uma requisição HTTP para obter os dados do produto.

---

## 1. Acessando o microsserviço de Pedidos

Entre na pasta:

```bash
cd microservicos/pedidos
```

---

## 2. Removendo o PostgreSQL

O microsserviço de Pedidos não utilizará mais o pacote `pg`.

Remova a dependência:

```bash
npm uninstall pg
```

---

## 3. Instalando o Mongoose

O Mongoose será utilizado para realizar a comunicação entre a aplicação Node.js e o MongoDB.

Como os computadores do laboratório utilizam **Node.js 16**, será utilizada a versão `6.13.8` do Mongoose:

```bash
npm install mongoose@6.13.8
```

Também utilizaremos o `dotenv` para carregar as variáveis de ambiente:

```bash
npm install dotenv
```

Ao final, as principais dependências do `package.json` serão semelhantes a:

```json
"dependencies": {
    "axios": "^1.19.0",
    "dotenv": "^18.0.6",
    "express": "^5.2.1",
    "mongoose": "^6.13.8"
}
```

---

# 4. Configurando a conexão com o MongoDB

Crie um arquivo:

```text
.env
```

dentro da pasta:

```text
microservicos/pedidos
```

Adicione a variável:

```env
DATABASE_URL=SUA_URL_DO_MONGODB
```

Por exemplo, para uma instalação local do MongoDB:

```env
DATABASE_URL=mongodb://localhost:27017/pedidos_db
```

Se estiver utilizando **MongoDB Atlas**, utilize a URL fornecida pelo serviço.

> Não publique o arquivo `.env` no GitHub, pois ele pode conter usuário, senha e outras informações sensíveis.

Um arquivo `.env_exemplo` pode ser mantido no repositório:

```env
DATABASE_URL=
```

---

# 5. Alterando o arquivo `db.js`

Anteriormente, a conexão com o PostgreSQL era realizada utilizando `pg`:

```javascript
const { Pool } = require("pg");

const pool = new Pool({
    connectionString: process.env.DATABASE_URL
});

module.exports = pool;
```

Agora utilizaremos o Mongoose.

Substitua o conteúdo de `db.js` por:

```javascript
require("dotenv").config();

const mongoose = require("mongoose");

const connectDB = async () => {
    try {
        await mongoose.connect(process.env.DATABASE_URL);

        console.log("MongoDB conectado com sucesso");
    } catch (error) {
        console.error(
            "Erro ao conectar ao MongoDB:",
            error
        );

        process.exit(1);
    }
};

module.exports = connectDB;
```

Observe que agora `db.js` exporta uma função chamada:

```javascript
connectDB
```

Essa função será chamada pelo servidor quando a aplicação for iniciada.

---

# 6. Alterando o `server.js`

No início do arquivo, carregue as variáveis de ambiente e importe o Mongoose:

```javascript
require("dotenv").config();

const express = require("express");
const axios = require("axios");
const mongoose = require("mongoose");
const connectDB = require("./db");

const app = express();
```

A URL do serviço de Produtos continua sendo utilizada:

```javascript
const PRODUTOS_URL =
    process.env.PRODUTOS_URL || "http://localhost:3001";
```

Configure o Express:

```javascript
app.use(express.json());
```

Em seguida, conecte a aplicação ao MongoDB:

```javascript
connectDB();
```

---

# 7. Criando o Schema de Pedido

No PostgreSQL, anteriormente criávamos uma tabela:

```sql
CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    produto_id INTEGER NOT NULL,
    nome_produto VARCHAR(100) NOT NULL,
    preco_unitario NUMERIC(10, 2) NOT NULL,
    quantidade INTEGER NOT NULL,
    total NUMERIC(10, 2) NOT NULL
);
```

No MongoDB não precisamos criar uma tabela.

Utilizando o Mongoose, definimos um **Schema** que representa a estrutura dos documentos de Pedido:

```javascript
const pedidoSchema = new mongoose.Schema({
    produto_id: Number,
    nome_produto: String,
    preco_unitario: Number,
    quantidade: Number,
    total: Number
});
```

Agora criamos o Model:

```javascript
const Pedido = mongoose.model(
    "Pedido",
    pedidoSchema
);
```

O objeto `Pedido` será utilizado para realizar as operações no banco de dados.

---

# 8. Listando pedidos

Anteriormente, utilizando PostgreSQL:

```javascript
const resultado = await db.query(
    "SELECT * FROM pedidos ORDER BY id"
);

res.json(resultado.rows);
```

Com Mongoose podemos utilizar:

```javascript
const resultado = await Pedido.find()
    .sort({ _id: 1 });

res.json(resultado);
```

A rota completa fica:

```javascript
app.get("/pedidos", async (req, res) => {
    try {
        const resultado = await Pedido.find()
            .sort({ _id: 1 });

        res.json(resultado);
    } catch (erro) {
        res.status(500).json({
            erro: "Erro ao buscar pedidos"
        });
    }
});
```

### Comparação

PostgreSQL:

```sql
SELECT * FROM pedidos ORDER BY id;
```

Mongoose:

```javascript
Pedido.find().sort({ _id: 1 });
```

---

# 9. Criando um pedido

O cliente enviará:

```http
POST /pedidos
```

com um JSON semelhante a:

```json
{
    "produtoId": 1,
    "quantidade": 2
}
```

Antes de criar o pedido, o microsserviço de Pedidos consulta o microsserviço de Produtos:

```javascript
const resposta = await axios.get(
    `${PRODUTOS_URL}/produtos/${produtoId}`,
    {
        timeout: 3000
    }
);
```

A resposta contém os dados atuais do produto:

```javascript
const produto = resposta.data;
```

Calculamos o total:

```javascript
const total =
    produto.preco * quantidade;
```

---

# 10. Inserindo o pedido no MongoDB

No PostgreSQL utilizávamos:

```javascript
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
```

Com Mongoose, a mesma operação fica:

```javascript
const pedido = await Pedido.create({
    produto_id: produto.id,
    nome_produto: produto.nome,
    preco_unitario: produto.preco,
    quantidade,
    total
});
```

E retornamos:

```javascript
res.status(201).json(pedido);
```

Observe que não precisamos escrever um comando `INSERT`.

---

# 11. Por que armazenar os dados do produto dentro do pedido?

O documento de Pedido armazena:

```javascript
{
    produto_id,
    nome_produto,
    preco_unitario,
    quantidade,
    total
}
```

Poderíamos armazenar apenas:

```javascript
{
    produto_id,
    quantidade
}
```

e consultar o microsserviço de Produtos sempre que o pedido fosse exibido.

Entretanto, isso criaria um problema.

Considere que hoje exista:

```text
Mouse
Preço: R$ 80,00
```

Um cliente compra duas unidades:

```text
2 × R$ 80,00 = R$ 160,00
```

Depois, o preço do produto muda para:

```text
R$ 100,00
```

O pedido original deve continuar registrando que a compra ocorreu por:

```text
R$ 80,00 por unidade
```

Por isso armazenamos uma cópia dos dados relevantes do produto no momento da criação do pedido.

---

# 12. Buscando um pedido pelo ID

No PostgreSQL utilizávamos:

```javascript
const resultado = await db.query(
    "SELECT * FROM pedidos WHERE id = $1",
    [req.params.id]
);

const pedido = resultado.rows[0];
```

Com Mongoose:

```javascript
const pedido = await Pedido.findById(
    req.params.id
);
```

A rota fica:

```javascript
app.get("/pedidos/:id", async (req, res) => {
    try {
        const pedido = await Pedido.findById(
            req.params.id
        );

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
```

---

# 13. IDs no MongoDB

Uma diferença importante pode ser observada nos identificadores.

No PostgreSQL utilizávamos:

```text
1
2
3
4
```

porque a tabela possuía:

```sql
id SERIAL PRIMARY KEY
```

No MongoDB, os documentos recebem automaticamente um `_id`, normalmente utilizando `ObjectId`.

Exemplo:

```json
{
    "_id": "6706bc83941f6a72ed73da11",
    "produto_id": 1,
    "nome_produto": "Teclado",
    "preco_unitario": 150,
    "quantidade": 2,
    "total": 300
}
```

Consequentemente, para consultar esse pedido utilizaremos:

```http
GET /pedidos/6706bc83941f6a72ed73da11
```

---

# 14. Removendo a criação da tabela

Como estamos utilizando MongoDB, não precisamos mais da função:

```javascript
async function criarTabela() {
    // ...
}
```

Nem da chamada:

```javascript
criarTabela();
```

O MongoDB criará a coleção quando o primeiro documento for inserido.

---

# 15. Executando os microsserviços

Precisamos dos dois microsserviços em execução.

## Terminal 1 — Produtos

Entre na pasta:

```bash
cd microservicos/produtos
```

Execute:

```bash
npm run dev
```

O serviço deverá iniciar na porta:

```text
3001
```

---

## Terminal 2 — Pedidos

Entre na pasta:

```bash
cd microservicos/pedidos
```

Execute:

```bash
npm run dev
```

Uma execução correta deverá apresentar mensagens semelhantes a:

```text
Pedidos rodando na porta 3002
MongoDB conectado com sucesso
```

---

# 16. Testando a aplicação

## Consultar os produtos

```http
GET http://localhost:3001/produtos
```

Exemplo de resposta:

```json
[
    {
        "id": 1,
        "nome": "Teclado",
        "preco": "150.00"
    },
    {
        "id": 2,
        "nome": "Mouse",
        "preco": "80.00"
    }
]
```

---

## Criar um pedido

```http
POST http://localhost:3002/pedidos
```

Body:

```json
{
    "produtoId": 1,
    "quantidade": 2
}
```

O microsserviço de Pedidos irá:

1. receber `produtoId` e `quantidade`;
2. consultar o microsserviço de Produtos;
3. recuperar nome e preço do produto;
4. calcular o valor total;
5. criar um documento no MongoDB;
6. retornar o pedido criado.

Uma resposta será semelhante a:

```json
{
    "_id": "6706bc83941f6a72ed73da11",
    "produto_id": 1,
    "nome_produto": "Teclado",
    "preco_unitario": 150,
    "quantidade": 2,
    "total": 300
}
```

---

## Listar os pedidos

```http
GET http://localhost:3002/pedidos
```

---

## Buscar um pedido

Copie o `_id` de um pedido e utilize:

```http
GET http://localhost:3002/pedidos/ID_DO_PEDIDO
```

Por exemplo:

```text
http://localhost:3002/pedidos/6706bc83941f6a72ed73da11
```

---

# 17. Comparando PostgreSQL e MongoDB

Após a alteração, temos duas formas diferentes de persistência dentro da mesma arquitetura.

| Operação | PostgreSQL | Mongoose |
|---|---|---|
| Buscar todos | `SELECT * FROM pedidos` | `Pedido.find()` |
| Buscar por ID | `SELECT ... WHERE id = $1` | `Pedido.findById(id)` |
| Inserir | `INSERT INTO ...` | `Pedido.create()` |
| Estrutura | Tabela | Coleção |
| Registro | Linha | Documento |
| Identificador | `SERIAL` | `ObjectId` |
| Modelo | Relacional | Documentos |

---

# 18. Arquitetura resultante

Ao final desta etapa:

```text
                   ┌──────────────────┐
                   │     Cliente      │
                   └────────┬─────────┘
                            │
             ┌──────────────┴──────────────┐
             │                             │
             ▼                             ▼
    ┌─────────────────┐           ┌─────────────────┐
    │    Produtos     │           │     Pedidos     │
    │   Porta 3001    │◄──────────│   Porta 3002    │
    └────────┬────────┘    HTTP   └────────┬────────┘
             │                             │
             ▼                             ▼
      ┌────────────┐                ┌────────────┐
      │ PostgreSQL │                │  MongoDB   │
      └────────────┘                └────────────┘
```

Temos, portanto, uma arquitetura na qual cada microsserviço:

- possui sua própria responsabilidade;
- possui sua própria persistência;
- não acessa diretamente o banco de dados de outro microsserviço;
- comunica-se com outros serviços através de HTTP.

Esse princípio é importante em arquiteturas de microserviços: **o banco de dados pertence ao serviço responsável pelos seus dados**.