const express = require("express");
const axios = require("axios");

const app = express();

app.use(express.json());

const pedidos = [];

app.get("/pedidos", (req, res) => {
    res.json(pedidos);
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

app.use(express.json());

app.listen(3002, () => {
    console.log("Pedidos rodando na porta 3002");
});