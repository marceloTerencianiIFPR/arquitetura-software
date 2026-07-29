# O que é Arquitetura de Software?

Embora o termo **arquitetura de software** seja amplamente utilizado na Engenharia de Software, não existe uma única definição universalmente aceita. Ao longo das últimas décadas, pesquisadores e profissionais propuseram diferentes conceituações, enfatizando aspectos como organização estrutural, tomada de decisões, comunicação entre componentes e atendimento aos atributos de qualidade.

Apesar das diferenças de abordagem, todas as definições convergem para uma mesma ideia: **a arquitetura representa a organização fundamental de um sistema e as decisões que orientam sua construção e evolução**.

Neste capítulo serão apresentadas algumas das definições mais influentes da literatura e discutidos os elementos que elas possuem em comum.

---

## As primeiras definições

Durante muitos anos, o desenvolvimento de software concentrou-se principalmente em algoritmos, estruturas de dados e linguagens de programação. Com o aumento da complexidade dos sistemas, tornou-se evidente que apenas boas práticas de programação não eram suficientes para garantir qualidade, manutenção e evolução.

Na década de 1990 surgiu uma das primeiras definições amplamente aceitas para arquitetura de software.

Segundo Perry e Wolf (1992), uma arquitetura de software é composta por três elementos fundamentais:

- **Elementos** (*Elements*);
- **Formas** (*Form*);
- **Fundamentação** (*Rationale*).

Os **elementos** representam os componentes que compõem o sistema.

As **formas** descrevem como esses componentes se relacionam.

Já a **fundamentação** corresponde às razões pelas quais determinadas decisões arquiteturais foram adotadas.

Essa definição trouxe uma importante contribuição para a Engenharia de Software: uma arquitetura não é composta apenas pelos componentes existentes, mas também pelas justificativas das decisões tomadas durante o projeto.

Em outras palavras, conhecer apenas a estrutura do sistema não é suficiente; é necessário compreender por que ela foi construída daquela maneira.

---

## A visão de Bass, Clements e Kazman

Uma das referências mais utilizadas atualmente é apresentada por Bass, Clements e Kazman (2022).

Os autores definem arquitetura como:

> "The software architecture of a program or computing system is the structure or structures of the system, which comprise software elements, the externally visible properties of those elements, and the relationships among them."

**Tradução livre:**

> "A arquitetura de software de um programa ou sistema computacional é a estrutura ou o conjunto de estruturas do sistema, composto pelos elementos de software, pelas propriedades desses elementos que são visíveis externamente e pelos relacionamentos existentes entre eles."

Essa definição destaca três aspectos fundamentais.

### Estruturas

Um sistema pode possuir diferentes estruturas arquiteturais.

Por exemplo:

- estrutura em camadas;
- estrutura de componentes;
- estrutura de implantação;
- estrutura de módulos.

Cada uma delas responde a perguntas diferentes sobre o sistema.

### Elementos

Os elementos arquiteturais correspondem às principais partes do sistema.

Podem ser, por exemplo:

- módulos;
- componentes;
- serviços;
- bancos de dados;
- interfaces;
- processos.

A arquitetura preocupa-se com esses elementos em alto nível, e não com detalhes internos de implementação.

### Relacionamentos

Também é importante compreender como esses elementos interagem.

Alguns exemplos são:

- comunicação via rede;
- chamadas de função;
- troca de mensagens;
- dependências entre módulos.

Esses relacionamentos determinam como o sistema funciona como um todo.

---

## A norma ISO/IEC/IEEE 42010

Outra definição amplamente reconhecida é apresentada pela norma internacional ISO/IEC/IEEE 42010.

Segundo a norma, arquitetura é:

> "The fundamental concepts or properties of a system in its environment embodied in its elements, relationships, and in the principles of its design and evolution."

**Tradução livre:**

> "Os conceitos ou propriedades fundamentais de um sistema em seu ambiente, incorporados em seus elementos, em seus relacionamentos e nos princípios que orientam seu projeto e sua evolução."

Essa definição amplia o conceito ao introduzir dois aspectos importantes.

### O ambiente

Um sistema nunca existe isoladamente.

Ele interage com:

- usuários;
- outros sistemas;
- equipamentos;
- organizações;
- infraestrutura.

Portanto, compreender o ambiente onde o sistema será utilizado faz parte da arquitetura.

### Evolução

Outro aspecto importante é que arquiteturas não são estáticas.

Ao longo da vida útil de um sistema surgem novos requisitos, novas tecnologias e novas restrições.

Uma boa arquitetura deve facilitar essa evolução.

---

## Arquitetura como conjunto de decisões

Em obras mais recentes, diversos autores passaram a enfatizar que arquitetura não é apenas uma estrutura.

Richards e Ford (2020), por exemplo, destacam que a arquitetura é formada pelas decisões significativas que influenciam características importantes do sistema.

Essas decisões incluem, por exemplo:

- arquitetura em camadas ou microsserviços;
- comunicação síncrona ou assíncrona;
- banco de dados relacional ou NoSQL;
- REST ou RPC;
- autenticação centralizada ou distribuída.

Perceba que nenhuma dessas decisões descreve diretamente um algoritmo.

Todas elas definem características estruturais que impactam o comportamento do sistema inteiro.

---

## O que todas as definições possuem em comum?

Embora utilizem terminologias diferentes, praticamente todas as definições apresentadas possuem elementos em comum.

Uma arquitetura sempre envolve:

- uma organização estrutural;
- componentes relevantes;
- relacionamentos entre componentes;
- princípios de projeto;
- decisões arquiteturais;
- preocupação com evolução;
- atendimento aos atributos de qualidade.

Esses elementos aparecem repetidamente na literatura e constituem a essência da arquitetura de software.

---

## Arquitetura, projeto e implementação

Um dos erros mais comuns entre estudantes é utilizar os termos **arquitetura**, **projeto** (*design*) e **implementação** como sinônimos.

Embora estejam relacionados, representam níveis diferentes de abstração.

### Arquitetura

Responde perguntas como:

- Como o sistema será organizado?
- Quais serão seus principais componentes?
- Como esses componentes irão se comunicar?
- Quais tecnologias fundamentais serão utilizadas?

### Projeto (Design)

Define como cada componente será desenvolvido.

Inclui, por exemplo:

- classes;
- interfaces;
- padrões de projeto;
- modelos de dados;
- algoritmos.

### Implementação

Corresponde à escrita do código-fonte.

É nesse nível que são definidos:

- variáveis;
- métodos;
- comandos;
- estruturas de repetição;
- tratamento de exceções.

Em outras palavras:

> **Arquitetura define a organização do sistema.**

> **Projeto define a solução de cada componente.**

> **Implementação transforma essas decisões em código executável.**

---

## Um exemplo simples

Imagine que uma equipe precise desenvolver um sistema de mensagens.

Uma possível sequência de decisões seria:

### Arquitetura

- haverá um cliente e um servidor;
- a comunicação será realizada por TCP;
- existirá apenas um servidor central.

### Projeto

No servidor existirão módulos responsáveis por:

- aceitar conexões;
- receber mensagens;
- responder aos clientes.

No cliente existirão módulos para:

- conectar;
- enviar mensagens;
- receber respostas.

### Implementação

Em Python serão utilizados:

- biblioteca `socket`;
- funções `connect()`;
- `bind()`;
- `listen()`;
- `accept()`;
- `sendall()`;
- `recv()`.

Observe que o código aparece apenas na última etapa.

As decisões arquiteturais foram tomadas muito antes da implementação.

---

## Arquitetura como meio para alcançar qualidade

É importante compreender que arquiteturas não são escolhidas apenas porque "parecem bonitas".

Cada decisão arquitetural procura atender determinados requisitos de qualidade.

Por exemplo:

| Decisão arquitetural | Objetivo principal |
| ---------------------- | ------------------- |
| Arquitetura em camadas | Facilitar manutenção |
| Cliente-Servidor | Distribuir responsabilidades |
| Microserviços | Escalabilidade e independência |
| Cache distribuído | Melhorar desempenho |
| Balanceador de carga | Aumentar disponibilidade |

Assim, diferentes arquiteturas podem atender melhor a diferentes necessidades.

Não existe uma arquitetura universalmente melhor.

Existe a arquitetura mais adequada para determinado contexto.

---

## Resumo

Arquitetura de software pode ser entendida como a organização fundamental de um sistema, composta por seus principais elementos, pelos relacionamentos entre eles e pelas decisões que orientam seu desenvolvimento e evolução. Embora diferentes autores enfatizem aspectos distintos — como estruturas, decisões, ambiente ou atributos de qualidade — todos convergem para a ideia de que a arquitetura representa a visão de mais alto nível do software. Essa visão orienta tanto o projeto quanto a implementação, permitindo construir sistemas mais organizados, compreensíveis, evolutivos e alinhados aos objetivos do negócio.

---

## Leituras recomendadas

- BASS, Len; CLEMENTS, Paul; KAZMAN, Rick. *Software Architecture in Practice*. 4. ed. Addison-Wesley, 2022.

- PERRY, Dewayne E.; WOLF, Alexander L. *Foundations for the Study of Software Architecture*. ACM SIGSOFT Software Engineering Notes, v. 17, n. 4, 1992.

- ISO/IEC/IEEE 42010. *Systems and Software Engineering — Architecture Description*. ISO, 2022.

- RICHARDS, Mark; FORD, Neal. *Fundamentals of Software Architecture*. O'Reilly, 2020.
