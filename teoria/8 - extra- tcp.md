# TCP e Sockets

Para que duas aplicações consigam trocar informações através de uma rede, é necessário utilizar um protocolo de transporte. Na Internet, os dois protocolos mais utilizados são o **TCP (Transmission Control Protocol)** e o **UDP (User Datagram Protocol)**. A escolha entre eles depende das necessidades da aplicação.

---

# O que é o TCP?

O **Transmission Control Protocol (TCP)** é um protocolo da camada de transporte responsável por estabelecer uma comunicação confiável entre dois processos executando em computadores diferentes.

Diferentemente do UDP, o TCP estabelece uma conexão antes da troca de dados e utiliza mecanismos para garantir que as mensagens sejam entregues corretamente.

As principais características do TCP são:

- orientado à conexão;
- entrega confiável dos dados;
- controle de erros;
- controle de sequência das mensagens;
- controle de fluxo;
- retransmissão de segmentos perdidos.

Essas características fazem do TCP a escolha ideal para aplicações em que a perda de dados não é aceitável, como sistemas bancários, aplicações Web, e-mails e transferência de arquivos.

---

# Comunicação orientada à conexão

Antes que cliente e servidor possam trocar mensagens, é necessário estabelecer uma conexão.

Esse processo garante que ambos estejam preparados para iniciar a comunicação.

De forma simplificada, o fluxo é:

```text
Cliente                    Servidor

   SYN  --------------------->

        <---------------- SYN + ACK

   ACK  --------------------->
```

Esse procedimento é conhecido como **Three-Way Handshake** (aperto de mão em três etapas).

Somente após essa etapa a troca de dados pode começar.

---

# Transferência dos dados

Depois que a conexão é estabelecida, cliente e servidor podem trocar mensagens.

```
Cliente                         Servidor

Mensagem ----------------------->

         <---------------------- Resposta
```

Durante essa comunicação, o TCP acompanha quais dados já foram enviados e quais já foram recebidos.

Caso algum segmento seja perdido durante a transmissão, ele poderá ser reenviado automaticamente. Além disso, o protocolo utiliza números de sequência e confirmações (ACK) para garantir que os dados sejam entregues corretamente e na ordem adequada.

---

# Encerramento da conexão

Quando a comunicação termina, a conexão também deve ser encerrada.

Cada lado informa que deseja finalizar a comunicação utilizando mensagens de encerramento.

```text
Cliente                    Servidor

FIN ------------------------->

      <------------------- ACK

      <------------------- FIN

ACK ------------------------->
```

Esse procedimento garante que ambos os lados saibam que a sessão foi finalizada corretamente.

---

# O que é um Socket?

Embora o TCP seja responsável pela comunicação entre computadores, os programas não utilizam o protocolo diretamente.

Eles utilizam uma abstração chamada **socket**.

Um **socket** representa um ponto de comunicação entre duas aplicações.

Quando um programa deseja enviar ou receber dados utilizando TCP, ele cria um socket e realiza todas as operações de comunicação por meio dele.

Uma conexão lógica é identificada por um socket composto por:

- endereço IP de origem;
- porta de origem;
- endereço IP de destino;
- porta de destino.

Cada conexão TCP possui um socket único.

---

# Socket na prática

No exemplo desenvolvido em Python, o cliente cria um socket com a instrução:

```python
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Os parâmetros utilizados possuem o seguinte significado:

- `AF_INET`: comunicação utilizando endereços IPv4;
- `SOCK_STREAM`: comunicação utilizando o protocolo TCP.

Depois da criação do socket, o cliente solicita a conexão com o servidor:

```python
cliente.connect((HOST, PORT))
```

A partir desse momento, toda a comunicação ocorrerá por meio desse socket.

---

# Enviando dados

Após a conexão ser estabelecida, o cliente pode enviar uma mensagem.

```python
cliente.sendall(mensagem.encode("utf-8"))
```

O método `sendall()` transmite todos os bytes da mensagem ao servidor.

---

# Recebendo dados

Para receber uma resposta, utiliza-se o método `recv()`.

```python
dados = cliente.recv(1024)
```

Esse método fica aguardando até que alguma informação seja enviada pelo servidor.

Quando os dados chegam, eles são convertidos novamente para texto.

```python
resposta = dados.decode("utf-8")
```

---

# Fluxo completo da comunicação

O funcionamento da aplicação pode ser resumido pelo seguinte diagrama.

```text
                 TCP

+---------+                      +----------+
| Cliente |                      | Servidor |
+---------+                      +----------+
     |                                 |
     |------ connect() --------------->|
     |                                 |
     |<----- conexão estabelecida -----|
     |                                 |
     |------ sendall() --------------->|
     |                                 |
     |<-------- recv() ----------------|
     |                                 |
     |------ sendall() --------------->|
     |                                 |
     |<-------- recv() ----------------|
     |                                 |
     |--------- close() -------------->|
```

Observe que o cliente e o servidor permanecem utilizando a mesma conexão durante toda a troca de mensagens.

---

# TCP × UDP

| TCP | UDP |
| ------ | ----- |
| Orientado à conexão | Não orientado à conexão |
| Comunicação confiável | Comunicação não confiável |
| Garante entrega dos dados | Não garante entrega |
| Mantém a ordem das mensagens | Não garante ordem |
| Possui controle de fluxo | Não possui controle de fluxo |
| Maior sobrecarga | Menor sobrecarga |

Em aplicações como chats, sistemas Web, bancos de dados e transferência de arquivos, normalmente utiliza-se TCP devido à necessidade de confiabilidade.

Já aplicações como transmissões de vídeo, jogos online e chamadas de voz frequentemente utilizam UDP, priorizando menor atraso na comunicação.

---

# Resumo

O TCP é um protocolo de transporte orientado à conexão que fornece uma comunicação confiável entre aplicações executando em computadores diferentes. Antes da troca de dados, cliente e servidor estabelecem uma conexão por meio do **Three-Way Handshake**. Durante a comunicação, o TCP controla a ordem das mensagens, detecta erros e confirma o recebimento dos dados. Os programas acessam esses recursos por meio de **sockets**, que representam os pontos de comunicação entre duas aplicações e permitem enviar e receber dados através da rede.
