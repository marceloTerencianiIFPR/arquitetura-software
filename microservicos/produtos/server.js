const express = require("express");
const db = require("./db");

const app = express();

app.use(express.json());

const produtos = [
    { id: 1, nome: "Teclado", preco: 150 },
    { id: 2, nome: "Mouse", preco: 80 },
    { id: 3, nome: "Monitor", preco: 900 }
];

/*app.get("/produtos", (req, res) => {
    res.json(produtos);
});*/

app.get("/produtos", async (req, res) => {
    try {
        const resultado = await db.query(
            "SELECT * FROM produtos ORDER BY id"
        );

        res.json(resultado.rows);
    } catch (erro) {
        res.status(500).json({
            erro: "Erro ao buscar produtos"
        });
    }
});

/*app.get("/produtos/:id", (req, res) => {
    const produto = produtos.find(
        p => p.id === Number(req.params.id)
    );

    if (!produto) {
        return res.status(404).json({ erro: "Produto não encontrado" });
    }

    res.json(produto);
});*/

app.get("/produtos/:id", async (req, res) => {
    try {
        const resultado = await db.query(
            "SELECT * FROM produtos WHERE id = $1",
            [req.params.id]
        );

        const produto = resultado.rows[0];

        if (!produto) {
            return res.status(404).json({
                erro: "Produto não encontrado"
            });
        }

        res.json(produto);
    } catch (erro) {
        res.status(500).json({
            erro: "Erro ao buscar produto"
        });
    }
});

app.post("/produtos", async (req, res) => {
    const { nome, preco } = req.body;

    if (!nome || preco === undefined || preco <= 0) {
        return res.status(400).json({
            erro: "Nome e preço válido são obrigatórios"
        });
    }

    try {
        const resultado = await db.query(
            `INSERT INTO produtos (nome, preco)
       VALUES ($1, $2)
       RETURNING *`,
            [nome, preco]
        );

        res.status(201).json(resultado.rows[0]);
    } catch (erro) {
        res.status(500).json({
            erro: "Erro ao criar produto"
        });
    }
});

async function criarTabela() {
    await db.query(`
        CREATE TABLE IF NOT EXISTS produtos (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        preco NUMERIC(10, 2) NOT NULL
        )
    `);

    console.log("Tabela de produtos pronta");
}

criarTabela();

app.listen(3001, () => {
    console.log("Produtos rodando na porta 3001");
});