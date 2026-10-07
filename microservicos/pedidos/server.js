require("dotenv").config();

const express = require("express");
const axios = require("axios");
const mongoose = require("mongoose");
const connectDB = require("./db");

const app = express();

const PRODUTOS_URL =
    process.env.PRODUTOS_URL || "http://localhost:3001";

app.use(express.json());

connectDB();


const pedidoSchema = new mongoose.Schema({
    produto_id: Number,
    nome_produto: String,
    preco_unitario: Number,
    quantidade: Number,
    total: Number
});

const Pedido = mongoose.model("Pedido", pedidoSchema);



app.get("/pedidos", async (req, res) => {
    try {
        const resultado = await Pedido.find().sort({ _id: 1 });

        res.json(resultado);
    } catch (erro) {
        res.status(500).json({
            erro: "Erro ao buscar pedidos"
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

        const pedido = await Pedido.create({
            produto_id: produto.id,
            nome_produto: produto.nome,
            preco_unitario: produto.preco,
            quantidade,
            total
        });

        res.status(201).json(pedido);
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



app.get("/pedidos/:id", async (req, res) => {
    try {
        const pedido = await Pedido.findById(req.params.id);

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

app.listen(3002, () => {
    console.log("Pedidos rodando na porta 3002");
});