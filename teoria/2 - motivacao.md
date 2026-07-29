# Motivação

Ao ouvir a palavra **arquitetura**, é comum pensar imediatamente em edifícios, pontes ou grandes obras da engenharia civil. De fato, a origem da palavra está relacionada à arte e à técnica de projetar construções. Entretanto, o conceito de arquitetura é muito mais amplo e pode ser aplicado a praticamente qualquer sistema composto por elementos que precisam ser organizados para cumprir um objetivo.

Considere, por exemplo, a construção de uma residência. Antes que qualquer tijolo seja assentado, é elaborado um projeto arquitetônico. Esse projeto não especifica a marca dos parafusos, a composição química do concreto ou o fabricante das torneiras. Em vez disso, define aspectos fundamentais, como a quantidade de pavimentos, a disposição dos cômodos, a circulação entre os ambientes, a localização das instalações elétricas e hidráulicas e as restrições impostas pelo terreno.

Essas decisões orientam toda a construção. Alterá-las durante a obra costuma ser caro e complexo, pois afetam diversas outras partes do projeto.

Esse mesmo princípio pode ser observado em diferentes áreas.

Uma cidade possui uma arquitetura urbana que organiza ruas, avenidas, áreas residenciais, regiões comerciais e espaços públicos. Um hospital possui uma arquitetura organizacional que distribui setores como emergência, centro cirúrgico, enfermarias e laboratórios de maneira a facilitar o atendimento aos pacientes. Até mesmo um computador apresenta uma arquitetura, composta por processador, memória, dispositivos de entrada e saída e barramentos de comunicação.

Em todos esses exemplos, existe um aspecto em comum: a arquitetura define **como os principais elementos de um sistema estão organizados e como eles se relacionam entre si**.

## Estrutura antes dos detalhes

Imagine que duas pessoas recebam a seguinte tarefa:

> Construir uma biblioteca.

A primeira pessoa começa imediatamente comprando estantes, mesas e cadeiras. A segunda inicia perguntando:

- Quantas pessoas utilizarão a biblioteca?
- Quantos livros serão armazenados?
- Como será a circulação?
- Onde ficará a recepção?
- Haverá salas de estudo?

Embora ambas possam chegar ao mesmo resultado, a segunda abordagem tende a produzir uma solução mais organizada, mais eficiente e mais fácil de expandir futuramente.

O mesmo ocorre no desenvolvimento de software.

Antes de escrever código, é importante compreender como o sistema será organizado, quais serão seus principais componentes e como esses componentes irão interagir. Essa visão de alto nível constitui a arquitetura do software.

## Arquitetura não é apenas desenho

Quando se fala em arquitetura, muitas pessoas imaginam imediatamente diagramas ou plantas.

Embora diagramas sejam ferramentas importantes para representar uma arquitetura, eles não são a arquitetura em si.

Da mesma forma que uma planta baixa representa uma casa, mas não é a própria casa, um diagrama UML representa uma arquitetura, mas não a substitui.

A arquitetura corresponde às decisões fundamentais sobre a organização do sistema. Os diagramas são apenas uma forma de documentar essas decisões.

## Arquitetura está presente em todos os sistemas

Independentemente do seu tamanho, todo sistema possui uma arquitetura.

Um programa simples desenvolvido durante uma disciplina também possui uma organização interna, ainda que bastante reduzida.

Por exemplo:

- um programa que realiza apenas um cálculo pode possuir apenas um módulo;
- um sistema de gerenciamento acadêmico pode possuir dezenas de módulos especializados;
- um serviço de streaming pode ser composto por centenas de componentes distribuídos em milhares de servidores.

A diferença entre esses exemplos não está na existência da arquitetura, mas na sua complexidade.

Em sistemas maiores, compreender essa organização torna-se indispensável para que equipes de desenvolvimento consigam trabalhar simultaneamente sem comprometer a qualidade do software.
