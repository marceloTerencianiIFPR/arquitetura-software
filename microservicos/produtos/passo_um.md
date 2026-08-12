# Microserviço de Produtos

## 1. Criar e iniciar o projeto

Na pasta `microservicos`:

```bash
mkdir produtos
cd produtos
npm init -y
npm install express
npm install --save-dev nodemon
```

## 2. Configurar o Nodemon

No `package.json`, ajuste a seção `scripts`:

```json
"scripts": {
  "dev": "nodemon server.js"
}
```

## 3. Criar o servidor

Crie o arquivo `server.js`:

```javascript
const express = require("express");

const app = express();

app.use(express.json());

const produtos = [
  { id: 1, nome: "Teclado", preco: 150 },
  { id: 2, nome: "Mouse", preco: 80 },
  { id: 3, nome: "Monitor", preco: 900 }
];

app.get("/produtos", (req, res) => {
  res.json(produtos);
});

app.get("/produtos/:id", (req, res) => {
  const produto = produtos.find(
    p => p.id === Number(req.params.id)
  );

  if (!produto) {
    return res.status(404).json({ erro: "Produto não encontrado" });
  }

  res.json(produto);
});

app.listen(3001, () => {
  console.log("Produtos rodando na porta 3001");
});
```

## 4. Executar

```bash
npm run dev
```

## 5. Testar

- Todos os produtos: <http://localhost:3001/produtos>
- Produto por ID: <http://localhost:3001/produtos/2>
