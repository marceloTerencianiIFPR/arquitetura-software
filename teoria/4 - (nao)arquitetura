# O que **NÃO** é Arquitetura de Software?

Após compreender o conceito de arquitetura de software, é importante esclarecer um aspecto que costuma gerar dúvidas entre estudantes e até mesmo entre profissionais iniciantes: **nem toda decisão de desenvolvimento é uma decisão arquitetural**.

Na prática, é comum encontrar afirmações como:

- "A arquitetura do sistema é Java."
- "Nossa arquitetura é Spring Boot."
- "A arquitetura está representada neste diagrama UML."
- "A arquitetura é o banco de dados PostgreSQL."

Embora todos esses elementos façam parte do desenvolvimento de software, nenhum deles representa, isoladamente, a arquitetura do sistema.

Uma boa forma de compreender esse conceito é pensar na construção de uma casa. A arquitetura define a disposição dos cômodos, a circulação, a estrutura e a organização da edificação. Já a cor das paredes, o modelo das portas ou o tipo de piso são decisões importantes, mas pertencem a outro nível de detalhamento.

Da mesma forma, em software, a arquitetura estabelece a organização geral da solução. Diversas outras decisões são tomadas posteriormente durante o projeto detalhado e a implementação.

---

# Arquitetura não é linguagem de programação

Uma das confusões mais frequentes consiste em associar arquitetura à linguagem utilizada no desenvolvimento.

Considere os seguintes sistemas:

- um sistema desenvolvido em Java;
- um sistema desenvolvido em Python;
- um sistema desenvolvido em C#.

Esses três sistemas podem possuir exatamente a mesma arquitetura.

Da mesma forma, dois sistemas escritos na mesma linguagem podem possuir arquiteturas completamente diferentes.

A linguagem influencia a implementação, mas não determina a organização arquitetural do sistema.

Por exemplo, uma arquitetura Cliente-Servidor pode ser implementada utilizando:

- Java;
- Python;
- C++;
- Go;
- Rust.

A arquitetura permanece a mesma, independentemente da linguagem escolhida.

---

# Arquitetura não é framework

Frameworks fornecem soluções prontas para problemas recorrentes de implementação.

Alguns exemplos são:

- Spring Boot;
- Django;
- ASP.NET Core;
- Laravel.

Embora muitos frameworks incentivem determinadas organizações internas, eles não constituem uma arquitetura.

É perfeitamente possível desenvolver dois sistemas utilizando o mesmo framework e obter arquiteturas bastante distintas.

Por exemplo:

- um sistema monolítico utilizando Spring Boot;
- um conjunto de microsserviços utilizando Spring Boot.

O framework permanece o mesmo.

A arquitetura mudou completamente.

---

# Arquitetura não é banco de dados

Outro equívoco comum consiste em afirmar que "a arquitetura do sistema é PostgreSQL" ou "a arquitetura utiliza MongoDB".

Na realidade, a escolha do banco de dados representa uma decisão tecnológica.

A arquitetura preocupa-se principalmente com questões como:

- haverá um banco centralizado ou distribuído?
- diferentes serviços possuirão bancos independentes?
- como ocorrerá o acesso aos dados?

Somente depois dessas decisões é que se escolhe a tecnologia mais adequada.

---

# Arquitetura não é um diagrama

Durante o desenvolvimento, diversos diagramas podem ser produzidos.

Entre eles:

- diagrama de classes;
- diagrama de componentes;
- diagrama de implantação;
- diagrama de sequência;
- diagrama de pacotes.

Esses diagramas **representam** aspectos da arquitetura.

Eles não são a arquitetura propriamente dita.

Assim como uma planta baixa representa uma casa sem ser a própria casa, um diagrama UML representa decisões arquiteturais, mas não as substitui.

Além disso, uma única arquitetura normalmente exige diferentes diagramas para ser completamente compreendida.

Cada diagrama evidencia uma perspectiva distinta do sistema.

---

# Arquitetura não é um algoritmo

Algoritmos descrevem como resolver um problema específico.

Por exemplo:

- ordenar uma lista;
- calcular o menor caminho em um grafo;
- realizar uma busca binária;
- validar um CPF.

Essas decisões pertencem ao nível da implementação.

A arquitetura preocupa-se com perguntas diferentes.

Por exemplo:

- onde esse algoritmo será executado?
- qual componente será responsável por ele?
- quais módulos poderão utilizá-lo?
- como ele se comunica com o restante do sistema?

Em outras palavras, a arquitetura define **onde** um algoritmo pertence; o algoritmo define **como** determinada tarefa será realizada.

---

# Arquitetura não é código

Ao abrir um projeto de software, normalmente encontramos milhares de linhas de código.

Classes.

Métodos.

Funções.

Variáveis.

Estruturas de repetição.

Tratamento de exceções.

Nada disso, isoladamente, constitui a arquitetura.

O código representa a implementação das decisões arquiteturais.

É possível modificar milhares de linhas de código sem alterar a arquitetura.

Da mesma forma, uma única decisão arquitetural pode exigir alterações em centenas de arquivos.

---

# Arquitetura não é interface gráfica

Outro equívoco frequente consiste em associar arquitetura às telas do sistema.

Uma interface moderna, bonita e intuitiva não implica uma boa arquitetura.

Da mesma forma, um sistema com aparência simples pode possuir uma arquitetura extremamente robusta.

A interface gráfica preocupa-se principalmente com a interação entre usuário e sistema.

A arquitetura preocupa-se com a organização interna do software.

São aspectos complementares, mas distintos.

---

# Arquitetura não é apenas documentação

Algumas organizações produzem extensos documentos arquiteturais contendo dezenas de diagramas.

Outras praticamente não documentam suas decisões.

Independentemente da quantidade de documentação produzida, o sistema continua possuindo uma arquitetura.

A documentação apenas registra as decisões tomadas.

Uma arquitetura pode existir mesmo sem documentação formal.

Entretanto, sua ausência torna mais difícil compreender, manter e evoluir o sistema.

---

# Então, o que realmente caracteriza uma arquitetura?

Uma decisão pode ser considerada arquitetural quando influencia significativamente o comportamento global do sistema.

Por exemplo:

- dividir o sistema em camadas;
- utilizar uma arquitetura Cliente-Servidor;
- adotar microsserviços;
- utilizar comunicação por eventos;
- separar banco de dados por serviço;
- definir mecanismos de autenticação centralizados.

Essas decisões afetam praticamente todo o software.

Alterá-las posteriormente costuma exigir elevado esforço e impacto em diversas partes do sistema.

Já decisões como:

- nome de variáveis;
- organização de métodos;
- escolha entre `for` e `while`;
- estilo de indentação;
- nome das classes;

normalmente pertencem ao nível do projeto detalhado ou da implementação.

---

# Comparando diferentes níveis de decisão

| Não é arquitetura | É arquitetura |
| ------------------- | --------------- |
| Linguagem de programação | Organização dos componentes |
| Framework | Estilo arquitetural |
| Banco de dados específico | Estratégia de persistência |
| Diagrama UML | Modelo arquitetural representado |
| Algoritmos | Distribuição das responsabilidades |
| Código-fonte | Estrutura geral do sistema |
| Interface gráfica | Comunicação entre componentes |
| Nome das classes | Organização dos módulos |

---

# Exemplo

Considere uma aplicação de comércio eletrônico.

## Decisões arquiteturais

- haverá um serviço para catálogo;
- um serviço para pagamentos;
- outro para estoque;
- comunicação via API REST;
- autenticação centralizada.

## Decisões de projeto

- utilizar o padrão Repository;
- aplicar Injeção de Dependência;
- utilizar Strategy para cálculo de frete.

## Decisões de implementação

- utilizar Java 21;
- Spring Boot 3;
- PostgreSQL;
- Hibernate;
- método `calcularFrete()`;
- variável `valorTotal`.

Observe que apenas o primeiro conjunto influencia a estrutura global do sistema.

---

# Resumo

Arquitetura de software não corresponde à linguagem de programação, ao framework, ao banco de dados, aos diagramas UML, aos algoritmos ou ao código-fonte. Esses elementos fazem parte do desenvolvimento de software, mas pertencem a níveis distintos de abstração. A arquitetura concentra-se nas decisões estruturais que organizam o sistema, definem a distribuição de responsabilidades, estabelecem a comunicação entre os componentes e orientam sua evolução ao longo do tempo. Compreender essa distinção é essencial para evitar que decisões de implementação sejam confundidas com decisões arquiteturais.
