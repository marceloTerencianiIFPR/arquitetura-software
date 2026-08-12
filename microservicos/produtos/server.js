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