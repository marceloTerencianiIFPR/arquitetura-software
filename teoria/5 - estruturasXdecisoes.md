# Estruturas × Decisões Arquiteturais

Até este ponto, foi apresentado que a arquitetura de software corresponde à organização fundamental de um sistema. Entretanto, ainda existe uma dúvida comum: **a arquitetura é composta apenas pela estrutura do software ou também pelas decisões tomadas durante seu projeto?**

A resposta é **ambas**.

As primeiras definições de arquitetura enfatizavam principalmente as **estruturas** do sistema, ou seja, seus componentes e relacionamentos. Com o amadurecimento da área, pesquisadores passaram a reconhecer que conhecer apenas a estrutura não é suficiente. É igualmente importante compreender **por que** determinadas escolhas foram realizadas.

Em outras palavras, uma arquitetura não é composta apenas por **o que existe**, mas também por **por que existe daquela forma**.

---

# O que são estruturas arquiteturais?

Uma **estrutura arquitetural** representa uma forma de observar o sistema.

Cada estrutura evidencia determinados aspectos da arquitetura e responde a um conjunto específico de perguntas.

Segundo Bass, Clements e Kazman (2022), um sistema normalmente possui **múltiplas estruturas**, pois nenhuma representação é suficiente para descrever completamente sua arquitetura.

Por exemplo:

- Como o software está dividido?
- Quais módulos dependem uns dos outros?
- Como ocorre a comunicação entre os componentes?
- Em quais servidores o sistema será executado?

Cada uma dessas perguntas conduz a uma estrutura arquitetural diferente.

---

# Principais estruturas arquiteturais

Embora existam diversas formas de representar uma arquitetura, algumas estruturas aparecem com frequência no desenvolvimento de software.

## Estrutura de módulos

Mostra como o sistema é organizado logicamente.

Exemplo:

```
Sistema

├── Cadastro
├── Financeiro
├── Estoque
└── Relatórios
```

Essa estrutura responde perguntas como:

- Como o sistema foi dividido?
- Quais módulos existem?
- Quais dependências existem entre eles?

---

## Estrutura de componentes

Mostra os principais componentes executáveis e suas interfaces.

Por exemplo:

```
Cliente

↓

API

↓

Serviço de Pedidos

↓

Banco de Dados
```

Essa estrutura preocupa-se principalmente com a interação entre componentes.

---

## Estrutura de implantação

Representa onde cada componente será executado.

Por exemplo:

```
Cliente Web

↓

Servidor de Aplicação

↓

Servidor de Banco de Dados
```

Essa estrutura auxilia na compreensão da infraestrutura necessária para executar o sistema.

---

## Estrutura de execução

Mostra como processos, threads e componentes interagem durante a execução.

É particularmente importante em sistemas concorrentes e distribuídos.

---

# Estruturas são diferentes de diagramas

É importante observar que uma estrutura arquitetural não é sinônimo de um diagrama específico.

Uma mesma estrutura pode ser representada utilizando diferentes notações.

Por exemplo, a estrutura de componentes pode ser documentada por meio de:

- UML;
- C4 Model;
- ArchiMate;
- diagramas próprios da organização.

O diagrama é apenas uma forma de representar a estrutura.

---

# O que são decisões arquiteturais?

Se as estruturas mostram **como** o sistema está organizado, as decisões arquiteturais explicam **por que** ele foi organizado dessa maneira.

Uma decisão arquitetural corresponde a uma escolha que possui impacto significativo sobre o sistema como um todo.

Essas decisões normalmente são difíceis de alterar posteriormente e influenciam atributos de qualidade, custos de manutenção e capacidade de evolução.

Richards e Ford (2020) observam que arquiteturas modernas são compostas por um conjunto de decisões significativas que orientam a construção e a evolução do software.

---

# Exemplos de decisões arquiteturais

Considere um sistema de comércio eletrônico.

Durante seu desenvolvimento podem surgir decisões como:

- utilizar arquitetura em camadas;
- adotar microsserviços;
- separar autenticação em um serviço próprio;
- utilizar comunicação assíncrona entre pedidos e estoque;
- manter banco de dados independente para cada serviço.

Todas essas decisões afetam diversos componentes simultaneamente.

Caso uma delas seja modificada futuramente, várias partes do sistema precisarão ser alteradas.

Por isso elas são consideradas decisões arquiteturais.

---

# O que NÃO é uma decisão arquitetural?

Nem toda decisão importante possui caráter arquitetural.

Por exemplo:

- utilizar Java em vez de C#;
- utilizar IntelliJ ou VS Code;
- nomear uma variável como `contador`;
- utilizar `for` em vez de `while`;
- ordenar métodos alfabeticamente.

Essas decisões influenciam a implementação, mas dificilmente modificam a organização geral do sistema.

---

# Estruturas mostram o resultado; decisões explicam as escolhas

Considere dois sistemas.

Ambos possuem exatamente a seguinte estrutura.

```
Cliente

↓

Servidor

↓

Banco de Dados
```

Visualmente, eles parecem idênticos.

Entretanto, suas decisões arquiteturais podem ser completamente diferentes.

### Sistema A

- prioriza simplicidade;
- atende poucos usuários;
- executa em apenas um servidor;
- possui baixa demanda de processamento.

### Sistema B

- atende milhões de usuários;
- utiliza replicação de banco;
- balanceamento de carga;
- cache distribuído;
- alta disponibilidade.

A estrutura geral continua semelhante.

As decisões arquiteturais são bastante diferentes.

É justamente esse conjunto de decisões que explica por que dois sistemas aparentemente iguais podem apresentar desempenhos, custos e capacidades de evolução completamente distintos.

---

# Um exemplo prático

Considere a aplicação Cliente-Servidor que será desenvolvida nesta disciplina.

Algumas **estruturas** da arquitetura são:

- um cliente;
- um servidor;
- comunicação via rede;
- separação entre processamento e interface.

Algumas **decisões arquiteturais** são:

- utilizar comunicação TCP;
- centralizar todo o processamento no servidor;
- permitir múltiplos clientes;
- manter protocolo textual simples;
- separar cliente e servidor em processos independentes.

Observe que as estruturas descrevem **o que existe**.

As decisões explicam **por que** essas estruturas foram escolhidas.

---

# Por que documentar decisões arquiteturais?

Imagine que, após cinco anos, uma equipe precise evoluir um sistema.

Ao analisar apenas os diagramas, os desenvolvedores conseguem visualizar a estrutura existente.

Entretanto, eles não sabem:

- por que foi escolhido um banco relacional;
- por que determinados serviços são independentes;
- por que existe uma fila de mensagens;
- por que determinadas funcionalidades estão desacopladas.

Sem essas informações, existe grande risco de que modificações eliminem características importantes do sistema.

Por esse motivo, muitas organizações mantêm registros conhecidos como **Architecture Decision Records (ADR)**.

Um ADR documenta, de forma simples:

- a decisão tomada;
- o problema que motivou essa decisão;
- as alternativas consideradas;
- as consequências esperadas.

Essa prática facilita a manutenção e preserva o conhecimento arquitetural ao longo da vida do software.

---

# Estruturas e decisões são complementares

Uma arquitetura completa combina dois tipos de informação.

As estruturas descrevem os elementos e seus relacionamentos.

As decisões justificam por que essas estruturas foram escolhidas.

Separadamente, cada uma fornece apenas parte da informação.

Juntas, permitem compreender tanto **como** o sistema foi organizado quanto **por que** essa organização foi adotada.

---

# Comparação

| Estruturas Arquiteturais | Decisões Arquiteturais |
| --------------------------- | ------------------------ |
| Mostram a organização do sistema. | Explicam as escolhas realizadas. |
| Descrevem componentes e relacionamentos. | Descrevem justificativas e restrições. |
| Respondem "como o sistema está organizado?". | Respondem "por que ele foi organizado dessa forma?". |
| São representadas por diagramas e modelos. | São registradas em documentos, ADRs ou especificações. |
| Tendem a ser relativamente estáveis. | Evoluem conforme novos requisitos surgem. |

---

# Exemplo completo

Imagine o desenvolvimento de um sistema bancário.

### Estruturas

- Aplicativo móvel;
- API de serviços;
- Serviço de autenticação;
- Serviço de pagamentos;
- Banco de dados.

### Decisões arquiteturais

- autenticação centralizada;
- comunicação REST;
- criptografia TLS;
- banco de dados replicado;
- microsserviços independentes;
- filas para processamento de pagamentos.

As estruturas mostram **quais componentes existem**.

As decisões mostram **por que eles foram organizados dessa maneira**.

---

# Resumo

Arquiteturas de software são compostas tanto por **estruturas** quanto por **decisões arquiteturais**. As estruturas representam os componentes do sistema e os relacionamentos existentes entre eles, permitindo visualizar a organização da solução sob diferentes perspectivas. As decisões arquiteturais registram as escolhas que moldaram essa organização, justificando por que determinadas alternativas foram adotadas em detrimento de outras. Enquanto as estruturas descrevem **o que** compõe a arquitetura, as decisões explicam **por que** ela foi construída dessa forma. Juntas, essas duas dimensões permitem compreender plenamente uma arquitetura de software e facilitam sua evolução ao longo do tempo.
