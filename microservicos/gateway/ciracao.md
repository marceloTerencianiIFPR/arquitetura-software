# API Gateway dos Microserviços

O Gateway fornece uma entrada única para os microserviços:

```text
Cliente → Gateway :3000
               ├── /produtos → Produtos :3001
               └── /pedidos  → Pedidos :3002
```

## 1. Criar o projeto

Na pasta `microservicos`:

```bash
mkdir gateway
cd gateway
npm init -y
npm install express axios
npm install --save-dev nodemon
```

## 2. Configurar os scripts

No `package.json`:

```json
"scripts": {
  "start": "node server.js",
  "dev": "nodemon server.js"
}
```

## 3. Criar o servidor

Crie `gateway/server.js`:

```javascript
const express = require("express");
const axios = require("axios");

const app = express();

app.use(express.json());

const PRODUTOS_URL =
  process.env.PRODUTOS_URL || "http://localhost:3001";

const PEDIDOS_URL =
  process.env.PEDIDOS_URL || "http://localhost:3002";

app.use("/produtos", async (req, res) => {
  try {
    const resposta = await axios({
      method: req.method,
      url: `${PRODUTOS_URL}${req.originalUrl}`,
      data: req.body,
      params: req.query,
      timeout: 3000
    });

    res.status(resposta.status).json(resposta.data);
  } catch (erro) {
    if (erro.response) {
      return res.status(erro.response.status).json(erro.response.data);
    }

    return res.status(503).json({
      erro: "Serviço de Produtos indisponível"
    });
  }
});

app.use("/pedidos", async (req, res) => {
  try {
    const resposta = await axios({
      method: req.method,
      url: `${PEDIDOS_URL}${req.originalUrl}`,
      data: req.body,
      params: req.query,
      timeout: 5000
    });

    res.status(resposta.status).json(resposta.data);
  } catch (erro) {
    if (erro.response) {
      return res.status(erro.response.status).json(erro.response.data);
    }

    return res.status(503).json({
      erro: "Serviço de Pedidos indisponível"
    });
  }
});

app.listen(3000, () => {
  console.log("Gateway rodando na porta 3000");
});
```

## 4. Criar o Dockerfile

Na pasta `gateway`, crie `Dockerfile`, sem extensão:

```dockerfile
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]
```

## 5. Criar o `.dockerignore`

Na pasta `gateway`, crie `.dockerignore`:

```dockerignore
node_modules
npm-debug.log
.env
```

## 6. Adicionar ao Docker Compose

Dentro de `services` no `docker-compose.yml`, adicione:

```yaml
gateway:
  build: ./gateway
  ports:
    - "3000:3000"
  environment:
    PRODUTOS_URL: http://produtos:3001
    PEDIDOS_URL: http://pedidos:3002
  depends_on:
    - produtos
    - pedidos
```

Produtos e Pedidos permanecem acessíveis diretamente pelas portas `3001` e `3002`.

## 7. Reconstruir os containers

Na pasta `microservicos`:

```bash
docker compose down
docker compose up --build
```

Aguarde:

```text
Gateway rodando na porta 3000
```

## 8. Testar pelo Gateway

```http
### Criar produto
POST http://localhost:3000/produtos
Content-Type: application/json

{
  "nome": "Mouse",
  "preco": 80
}

### Listar produtos
GET http://localhost:3000/produtos

### Buscar produto por ID
GET http://localhost:3000/produtos/1

### Criar pedido
POST http://localhost:3000/pedidos
Content-Type: application/json

{
  "produtoId": 1,
  "quantidade": 2
}

### Listar pedidos
GET http://localhost:3000/pedidos

### Buscar pedido por ID
GET http://localhost:3000/pedidos/1
```

O cliente pode agora acessar Produtos e Pedidos por uma única porta: `3000`.
