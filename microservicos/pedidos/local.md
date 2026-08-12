# Microserviço de Pedidos

## 1. Criar e iniciar o projeto

Na pasta `microservicos`:

```bash
mkdir pedidos
cd pedidos
npm init -y
npm install express
npm install axios
npm install --save-dev nodemon
```

## 2. Configurar o Nodemon

No `package.json`:

```json
"scripts": {
  "dev": "nodemon server.js"
}
```

## 3. Criar o servidor

Crie o arquivo `server.js`:

```javascript
const express = require("express");
const axios = require("axios");

const app = express();

app.use(express.json());

const pedidos = [];

app.get("/pedidos", (req, res) => {
  res.json(pedidos);
});

app.get("/pedidos/:id", (req, res) => {
  const pedido = pedidos.find(
    p => p.id === Number(req.params.id)
  );

  if (!pedido) {
    return res.status(404).json({
      erro: "Pedido não encontrado"
    });
  }

  res.json(pedido);
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
      `http://localhost:3001/produtos/${produtoId}`,
      {
        timeout: 3000
      }
    );

    const produto = resposta.data;

    const pedido = {
      id: pedidos.length + 1,
      produto,
      quantidade,
      total: produto.preco * quantidade
    };

    pedidos.push(pedido);

    res.status(201).json(pedido);
  } catch (erro) {
    if (erro.response?.status === 404) {
      return res.status(400).json({
        erro: "Produto não encontrado"
      });
    }

    return res.status(503).json({
      erro: "Serviço de Produtos indisponível"
    });
  }
});

app.listen(3002, () => {
  console.log("Pedidos rodando na porta 3002");
});
```

## 4. Executar

Mantenha o microserviço de Produtos rodando e, em outro terminal, execute:

```bash
npm run dev
```

## 5. Criar as requisições de teste

Crie o arquivo `requests.http`:

```http
### Listar pedidos
GET http://localhost:3002/pedidos

### Buscar pedido por ID
GET http://localhost:3002/pedidos/1

### Criar pedido
POST http://localhost:3002/pedidos
Content-Type: application/json

{
  "produtoId": 1,
  "quantidade": 2
}
```

## 6. Testar os erros

Produto inexistente:

```http
POST http://localhost:3002/pedidos
Content-Type: application/json

{
  "produtoId": 999,
  "quantidade": 2
}
```

Quantidade inválida:

```http
POST http://localhost:3002/pedidos
Content-Type: application/json

{
  "produtoId": 1,
  "quantidade": 0
}
```

Para testar a indisponibilidade, desligue o microserviço de Produtos e tente criar um pedido.
