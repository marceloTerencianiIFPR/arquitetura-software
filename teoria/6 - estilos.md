# Estilos Arquiteturais

Ao desenvolver um sistema, uma das primeiras decisões arquiteturais consiste em definir **como seus componentes serão organizados**. Ao longo da evolução da Engenharia de Software, observou-se que diversos sistemas compartilhavam formas semelhantes de organização. Essas soluções recorrentes passaram a ser conhecidas como **estilos arquiteturais** (*Architectural Styles*).

Em termos gerais, um estilo arquitetural estabelece um conjunto de princípios para organizar componentes, definir responsabilidades e determinar a forma como eles interagem. Em vez de especificar exatamente como um sistema deve ser implementado, um estilo fornece uma estrutura geral que pode ser adaptada às necessidades de cada projeto.

Segundo Shaw e Garlan (1996), um estilo arquitetural define uma família de sistemas em termos de um padrão de organização estrutural. Cada estilo especifica os tipos de componentes, os conectores utilizados para a comunicação entre eles e as restrições que governam sua composição.

Dessa forma, escolher um estilo arquitetural significa adotar um modelo de organização que servirá como base para as principais decisões do projeto.

---

# O que caracteriza um estilo arquitetural?

Embora existam dezenas de estilos arquiteturais descritos na literatura, todos procuram responder às mesmas perguntas fundamentais:

- Como o sistema será dividido?
- Quais responsabilidades cada componente possuirá?
- Como os componentes irão se comunicar?
- Como novos componentes poderão ser adicionados?
- Como o sistema poderá evoluir ao longo do tempo?

As respostas variam conforme o estilo adotado.

Em alguns casos, privilegia-se a simplicidade. Em outros, busca-se alta disponibilidade, escalabilidade, flexibilidade ou facilidade de manutenção.

Por esse motivo, **não existe um estilo arquitetural universalmente melhor**. Existe apenas o estilo mais adequado para determinado contexto.

---

# Estilo arquitetural × padrão arquitetural

Na literatura e na indústria, é comum encontrar os termos **estilo arquitetural** (*Architectural Style*) e **padrão arquitetural** (*Architectural Pattern*) sendo utilizados como sinônimos. Embora estejam intimamente relacionados, alguns autores fazem uma distinção.

De maneira simplificada:

- **Estilo arquitetural** descreve uma forma geral de organização do sistema.
- **Padrão arquitetural** apresenta uma solução mais específica para um problema recorrente.

Por exemplo:

- Cliente-Servidor pode ser considerado um estilo arquitetural.
- MVC pode ser tratado como um padrão arquitetural aplicado principalmente ao desenvolvimento de interfaces.

Na prática, muitos livros utilizam ambas as expressões de forma intercambiável.

Neste material, será adotado o termo **estilo arquitetural**, por representar uma visão mais ampla da organização dos sistemas.

---

# Estilo arquitetural × padrão de projeto

Outra confusão frequente ocorre entre **estilos arquiteturais** e **padrões de projeto** (*Design Patterns*).

Os estilos arquiteturais atuam em um nível elevado de abstração.

Os padrões de projeto atuam dentro dos componentes definidos pela arquitetura.

Por exemplo:

Uma arquitetura Cliente-Servidor pode utilizar:

- Factory;
- Singleton;
- Observer;
- Strategy;
- Repository.

Nenhum desses padrões altera a arquitetura do sistema.

Eles apenas organizam melhor o código de cada componente.

Em outras palavras:

> A arquitetura organiza o sistema.

> Os padrões de projeto organizam o código.

---

# Principais estilos arquiteturais

Ao longo das próximas aulas serão estudados diversos estilos arquiteturais. Os mais utilizados atualmente são:

- Cliente-Servidor;
- Arquitetura em Camadas;
- MVC (Model-View-Controller);
- Microkernel;
- Pipes and Filters;
- Arquitetura Orientada a Eventos (Event-Driven);
- Microsserviços.

Cada um deles apresenta vantagens, limitações e contextos de aplicação distintos.

---

# Cliente-Servidor

O estilo Cliente-Servidor organiza o sistema em dois grandes grupos de componentes.

O **cliente** solicita serviços.

O **servidor** processa essas solicitações e devolve uma resposta.

```
Cliente  ─────────►  Servidor

        Requisição

Cliente  ◄─────────  Servidor

         Resposta
```

Esse modelo é amplamente utilizado em:

- aplicações Web;
- sistemas bancários;
- jogos online;
- sistemas acadêmicos;
- aplicações móveis.

Será o primeiro estilo estudado nesta disciplina.

---

# Arquitetura em Camadas

Na arquitetura em camadas, o sistema é organizado em níveis, cada um responsável por uma função específica.

Uma organização bastante comum é:

```
Apresentação

↓

Negócio

↓

Persistência

↓

Banco de Dados
```

Cada camada comunica-se preferencialmente apenas com as camadas adjacentes.

Essa separação facilita:

- manutenção;
- reutilização;
- testes;
- organização do código.

É uma das arquiteturas mais utilizadas em sistemas corporativos.

---

# MVC (Model–View–Controller)

O MVC surgiu com o objetivo de separar responsabilidades relacionadas à interface do usuário.

O padrão divide a aplicação em três componentes principais.

**Model**

Responsável pelos dados e regras de negócio.

**View**

Responsável pela interface apresentada ao usuário.

**Controller**

Responsável por receber as ações do usuário e coordenar a interação entre modelo e interface.

```
Usuário

↓

Controller

↙       ↘

Model   View
```

Grande parte dos frameworks modernos adota esse padrão, como:

- Spring MVC;
- ASP.NET MVC;
- Laravel;
- Ruby on Rails.

---

# Pipes and Filters

Nesse estilo, o processamento é dividido em etapas independentes.

Cada etapa recebe dados, realiza um processamento e envia o resultado para a próxima.

```
Entrada

↓

Filtro A

↓

Filtro B

↓

Filtro C

↓

Saída
```

Exemplos de aplicação:

- compiladores;
- processamento de imagens;
- processamento de áudio;
- análise de dados.

Sua principal vantagem é a facilidade de reutilização e composição dos filtros.

---

# Microkernel

O estilo Microkernel organiza o sistema em torno de um núcleo reduzido responsável pelas funcionalidades essenciais.

Novas funcionalidades são adicionadas como plugins.

```
Plugins

↕

Microkernel
```

Esse estilo é comum em:

- sistemas operacionais;
- IDEs;
- plataformas extensíveis.

Por exemplo:

- Eclipse;
- Visual Studio Code.

---

# Arquitetura Orientada a Eventos

Nesse estilo, os componentes comunicam-se através de eventos.

Um componente produz eventos.

Outro componente reage quando esses eventos ocorrem.

```
Produtor

↓

Evento

↓

Consumidor
```

Essa abordagem reduz o acoplamento entre os componentes e facilita o desenvolvimento de sistemas distribuídos.

É bastante utilizada em:

- Internet das Coisas (IoT);
- sistemas financeiros;
- monitoramento em tempo real;
- aplicações em nuvem.

---

# Microsserviços

A arquitetura de microsserviços divide o sistema em diversos serviços independentes.

Cada serviço:

- possui responsabilidade própria;
- pode ser desenvolvido independentemente;
- pode utilizar tecnologias diferentes;
- pode ser implantado separadamente.

```
Cliente

↓

API Gateway

├── Usuários

├── Pedidos

├── Estoque

└── Pagamentos
```

Essa arquitetura facilita:

- escalabilidade;
- implantação contínua;
- independência entre equipes.

Por outro lado, aumenta significativamente a complexidade da comunicação e da infraestrutura.

---

# Como escolher um estilo arquitetural?

A escolha de um estilo arquitetural depende de diversos fatores.

Entre eles:

- tamanho do sistema;
- quantidade de usuários;
- requisitos de desempenho;
- necessidade de escalabilidade;
- facilidade de manutenção;
- equipe disponível;
- prazo;
- orçamento.

Não existe uma arquitetura perfeita para todos os projetos.

Por exemplo:

- um sistema desenvolvido por um único programador dificilmente necessita de microsserviços;
- uma plataforma utilizada por milhões de usuários pode exigir soluções distribuídas.

O papel do arquiteto consiste justamente em selecionar o estilo mais adequado para cada contexto.

---

# É possível combinar estilos?

Sim.

Na prática, poucos sistemas utilizam apenas um estilo arquitetural.

Considere uma aplicação Web moderna.

Ela pode utilizar simultaneamente:

- Cliente-Servidor (comunicação entre navegador e servidor);
- Arquitetura em Camadas (organização interna do servidor);
- MVC (interface Web);
- Microsserviços (divisão dos serviços);
- Arquitetura Orientada a Eventos (integração assíncrona entre serviços).

Portanto, os estilos arquiteturais não são mutuamente exclusivos.

Eles frequentemente são combinados para atender diferentes necessidades do sistema.

---

# Comparando os principais estilos

| Estilo | Principal característica | Aplicações comuns |
| --------- | -------------------------- | ------------------- |
| Cliente-Servidor | Separa clientes e servidores | Web, sistemas distribuídos |
| Camadas | Organiza responsabilidades em níveis | Sistemas corporativos |
| MVC | Separa interface, controle e dados | Aplicações Web |
| Pipes and Filters | Processamento em etapas independentes | Compiladores, ETL |
| Microkernel | Núcleo mínimo com extensões | IDEs, sistemas operacionais |
| Event-Driven | Comunicação baseada em eventos | IoT, sistemas distribuídos |
| Microsserviços | Serviços independentes | Plataformas de grande escala |

---

# Exemplo

Imagine o desenvolvimento de um sistema acadêmico.

A comunicação entre o navegador do aluno e o servidor caracteriza o estilo **Cliente-Servidor**.

Internamente, o servidor pode estar organizado em **camadas**.

A interface Web pode seguir o padrão **MVC**.

O envio de notificações por e-mail pode utilizar uma **arquitetura orientada a eventos**.

No futuro, módulos como Biblioteca, Financeiro e Matrículas podem ser separados em **microsserviços**.

Perceba que um mesmo sistema pode incorporar diversos estilos arquiteturais simultaneamente.

---

# Resumo

Os estilos arquiteturais representam formas recorrentes de organizar sistemas de software. Cada estilo estabelece princípios para estruturar componentes, definir responsabilidades e organizar a comunicação entre eles. Não existe um estilo ideal para todos os projetos; sua escolha depende dos requisitos funcionais, dos atributos de qualidade desejados e do contexto de desenvolvimento. Na prática, sistemas modernos frequentemente combinam diferentes estilos arquiteturais, aproveitando as vantagens de cada abordagem para construir soluções mais flexíveis, escaláveis e de fácil manutenção.
