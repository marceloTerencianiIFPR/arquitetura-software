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