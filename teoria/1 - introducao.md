# Introdução

A arquitetura de software é um dos pilares da Engenharia de Software moderna. À medida que os sistemas computacionais evoluíram em tamanho, complexidade e criticidade, tornou-se insuficiente concentrar o desenvolvimento apenas na implementação de funcionalidades. Passou a ser necessário planejar como os diferentes elementos do sistema seriam organizados, como se comunicariam e de que maneira atenderiam aos requisitos de qualidade, como desempenho, segurança, disponibilidade, escalabilidade e manutenibilidade.

Em projetos de pequeno porte, muitas decisões estruturais podem parecer simples ou até mesmo implícitas. Entretanto, à medida que um sistema cresce, decisões tomadas no início do desenvolvimento podem impactar significativamente sua evolução, seus custos de manutenção e sua capacidade de adaptação a novas demandas. Nesse contexto, a arquitetura de software desempenha um papel fundamental ao estabelecer uma visão de alto nível da solução antes que detalhes de implementação sejam definidos.

Embora frequentemente associada apenas à estrutura de um sistema, a arquitetura envolve também as decisões técnicas que justificam essa estrutura. Segundo Perry e Wolf (1992), a arquitetura de software é composta por três elementos fundamentais: **elementos**, **formas** (relacionamentos) e **fundamentação** (*rationale*), evidenciando que uma arquitetura não descreve apenas os componentes de um sistema, mas também os motivos que levaram às decisões adotadas.

Ao longo das últimas décadas, diversos pesquisadores propuseram definições para arquitetura de software. Apesar das diferenças de enfoque, existe um consenso de que a arquitetura representa a organização fundamental de um sistema, incluindo seus componentes, relacionamentos e princípios que orientam sua evolução. A norma **ISO/IEC/IEEE 42010** sintetiza essa visão ao definir arquitetura como a organização fundamental de um sistema, incorporada em seus elementos, nas relações entre eles e com o ambiente, bem como nos princípios que orientam seu projeto e evolução.

Bass, Clements e Kazman (2022) reforçam essa perspectiva ao afirmar que a arquitetura corresponde às estruturas do sistema necessárias para compreender seu funcionamento, incluindo os elementos de software, suas propriedades externamente visíveis e os relacionamentos existentes entre eles. Essa definição destaca que a arquitetura não se preocupa com todos os detalhes internos de implementação, mas com aqueles aspectos relevantes para o entendimento, desenvolvimento e evolução do sistema.

É comum que estudantes confundam arquitetura com tecnologias específicas, linguagens de programação ou diagramas UML. Embora esses elementos possam fazer parte da documentação arquitetural, eles não constituem, isoladamente, a arquitetura de um software. Da mesma forma, padrões de projeto (*Design Patterns*), frameworks ou bibliotecas representam decisões de implementação que podem ou não decorrer da arquitetura escolhida.

Outra confusão frequente consiste em considerar arquitetura apenas como um desenho produzido nas fases iniciais do desenvolvimento. Na prática, a arquitetura acompanha todo o ciclo de vida do software, sendo continuamente refinada conforme novos requisitos surgem e novas restrições são identificadas. Richards e Ford (2020) observam que arquiteturas modernas são, frequentemente, resultado de decisões incrementais tomadas ao longo da evolução do sistema, e não apenas de um planejamento inicial completamente definido.

Neste material, a arquitetura de software será estudada sob uma perspectiva prática. Inicialmente serão discutidos os conceitos fundamentais, as principais definições presentes na literatura e as diferenças entre arquitetura, projeto e implementação. Em seguida, serão apresentados os principais estilos arquiteturais utilizados na indústria, suas características, vantagens, limitações e contextos de aplicação.

Como estudo de caso, será utilizada uma aplicação simples desenvolvida em Python baseada no estilo arquitetural **Cliente-Servidor**. Embora seja um exemplo reduzido, ele reúne diversos conceitos fundamentais da arquitetura de software, como separação de responsabilidades, comunicação entre componentes, interfaces, distribuição e organização estrutural. A partir desse exemplo, será possível compreender como decisões arquiteturais influenciam diretamente a implementação de um sistema e como diferentes representações, como diagramas de pacotes, componentes, implantação e sequência, permitem visualizar aspectos distintos da mesma arquitetura.

Ao final deste capítulo, espera-se que o leitor seja capaz de compreender o papel da arquitetura de software no desenvolvimento de sistemas, reconhecer sua importância para a qualidade do software e identificar arquiteturas em aplicações reais, estabelecendo uma base sólida para o estudo dos demais tópicos da disciplina.

---

## Objetivos de aprendizagem

Ao concluir este capítulo, o estudante deverá ser capaz de:

* compreender o conceito de arquitetura de software e sua importância no desenvolvimento de sistemas;
* diferenciar arquitetura, projeto e implementação;
* reconhecer que arquiteturas são compostas tanto por estruturas quanto por decisões arquiteturais;
* compreender o papel da arquitetura na obtenção de atributos de qualidade do software;
* identificar os principais estilos arquiteturais utilizados no desenvolvimento de sistemas;
* analisar uma aplicação cliente-servidor sob a perspectiva arquitetural, relacionando conceitos teóricos com uma implementação prática.

---

## Referências citadas

BASS, Len; CLEMENTS, Paul; KAZMAN, Rick. **Software Architecture in Practice**. 4. ed. Boston: Addison-Wesley, 2022.

ISO/IEC/IEEE. **42010: Systems and Software Engineering — Architecture Description**. Geneva: ISO, 2022.

PERRY, Dewayne E.; WOLF, Alexander L. **Foundations for the Study of Software Architecture**. *ACM SIGSOFT Software Engineering Notes*, v. 17, n. 4, p. 40–52, 1992.

RICHARDS, Mark; FORD, Neal. **Fundamentals of Software Architecture: An Engineering Approach**. Sebastopol: O'Reilly Media, 2020.
