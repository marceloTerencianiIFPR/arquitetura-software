# Containers dos Microserviços

## 1. Dockerfile de Produtos

Na pasta `produtos`, crie o arquivo `Dockerfile`, sem extensão:

```dockerfile
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3001

CMD ["npm", "run", "dev"]
```

## 2. `.dockerignore` de Produtos

Na pasta `produtos`, crie `.dockerignore`:

```dockerignore
node_modules
npm-debug.log
.env
```

## 3. Dockerfile de Pedidos

Na pasta `pedidos`, crie o arquivo `Dockerfile`, sem extensão:

```dockerfile
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3002

CMD ["npm", "run", "dev"]
```

## 4. `.dockerignore` de Pedidos

Na pasta `pedidos`, crie `.dockerignore`:

```dockerignore
node_modules
npm-debug.log
.env
```

## 5. Configurar a URL do serviço de Produtos

No `server.js` de Pedidos, após criar o `app`, adicione:

```javascript
const PRODUTOS_URL =
  process.env.PRODUTOS_URL || "http://localhost:3001";
```

Na chamada do Axios, use:

```javascript
const resposta = await axios.get(
  `${PRODUTOS_URL}/produtos/${produtoId}`,
  {
    timeout: 3000
  }
);
```

No ambiente local, será usado:

```text
http://localhost:3001
```

No Docker, será usado:

```text
http://produtos:3001
```

## 6. Criar o Docker Compose

Na raiz da pasta `microservicos`, crie `docker-compose.yml`:

```yaml
services:
  produtos:
    build: ./produtos
    ports:
      - "3001:3001"

  pedidos:
    build: ./pedidos
    ports:
      - "3002:3002"
    environment:
      PRODUTOS_URL: http://produtos:3001
    depends_on:
      - produtos
```

## 7. Subir os containers

Desligue os serviços executados localmente com Nodemon. Na pasta `microservicos`, execute:

```bash
docker compose up --build
```

## 8. Testar os serviços

Produtos:

```http
GET http://localhost:3001/produtos
```

Pedidos:

```http
GET http://localhost:3002/pedidos
```

Criar um pedido:

```http
POST http://localhost:3002/pedidos
Content-Type: application/json

{
  "produtoId": 1,
  "quantidade": 2
}
```

## 9. Encerrar os containers

No terminal em que o Docker Compose está rodando, pressione:

```text
Ctrl + C
```

Para remover os containers e a rede criada:

```bash
docker compose down
```
