# Estudo de Caso: Arquitetura Cliente-Servidor

Para demonstrar a arquitetura Cliente-Servidor, será utilizada uma aplicação simples de troca de mensagens por meio da rede.

A aplicação será formada por dois programas independentes:

* um **cliente**, responsável por iniciar a conexão e enviar mensagens;
* um **servidor**, responsável por aceitar a conexão, receber as mensagens e enviar respostas.

A comunicação será realizada utilizando **sockets TCP**.

---

## Visão geral da arquitetura

O funcionamento básico da aplicação pode ser representado da seguinte forma:

```text
+------------------+                  +------------------+
|     Cliente      |                  |     Servidor     |
|------------------|                  |------------------|
| Inicia conexão   |                  | Aguarda conexão  |
| Envia mensagens  |                  | Recebe mensagens |
| Recebe respostas |                  | Envia respostas  |
+--------+---------+                  +---------+--------+
         |                                      |
         |---------- conexão TCP -------------->|
         |                                      |
         |---------- mensagem ----------------->|
         |                                      |
         |<--------- resposta ------------------|
         |                                      |
```

Nesse exemplo, o cliente inicia a comunicação. O servidor deve estar em execução e aguardando conexões na mesma porta configurada pelo cliente.

---

## Configuração da conexão

O cliente utiliza um endereço IP e uma porta para localizar o servidor.

```python
HOST = "127.0.0.1"
PORT = 5000
```

O endereço `127.0.0.1`, também chamado de `localhost`, indica que o servidor está sendo executado no mesmo computador que o cliente.

A porta `5000` identifica a aplicação dentro do computador.

Para que a comunicação funcione, cliente e servidor devem utilizar:

* o mesmo endereço IP;
* a mesma porta;
* o mesmo protocolo de transporte;
* a mesma codificação das mensagens.

---

## Criação do socket

O cliente cria o socket com a seguinte instrução:

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

O parâmetro `AF_INET` indica que será utilizado o padrão de endereçamento IPv4.

O parâmetro `SOCK_STREAM` indica que a comunicação utilizará o protocolo TCP.

O TCP fornece uma comunicação orientada à conexão. Antes da troca de mensagens, cliente e servidor precisam estabelecer uma conexão.

Além disso, o TCP procura garantir:

* entrega dos dados;
* ordem das mensagens;
* detecção de falhas na conexão;
* retransmissão de dados perdidos.

---

## Estabelecimento da conexão

Após criar o socket, o cliente solicita uma conexão com o servidor:

```python
cliente.connect((HOST, PORT))
```

Nesse momento, o cliente tenta localizar um servidor em execução no endereço `127.0.0.1` e na porta `5000`.

O fluxo pode ser representado da seguinte maneira:

```text
Cliente                              Servidor
   |                                    |
   |------ solicitação de conexão ----->|
   |                                    |
   |<----- conexão estabelecida --------|
   |                                    |
```

Caso nenhum servidor esteja aguardando conexões nessa porta, ocorrerá um erro de conexão.

No código, esse erro é tratado por:

```python
except ConnectionRefusedError:
    print("Não foi possível conectar ao servidor.")
```

---

## Envio de uma mensagem

Depois que a conexão é estabelecida, o usuário pode digitar uma mensagem:

```python
mensagem = input("Cliente: ")
```

Como os sockets transmitem bytes, o texto precisa ser convertido antes de ser enviado.

```python
cliente.sendall(mensagem.encode(CODIFICACAO))
```

O método `encode()` transforma a mensagem de texto em uma sequência de bytes.

A codificação utilizada é UTF-8:

```python
CODIFICACAO = "utf-8"
```

Por exemplo, caso o usuário digite:

```text
Olá, servidor!
```

O cliente envia essa mensagem ao servidor pela conexão TCP.

```text
Cliente                              Servidor
   |                                    |
   |------ "Olá, servidor!" ---------->|
   |                                    |
```

---

## Recebimento da resposta

Após enviar a mensagem, o cliente aguarda uma resposta:

```python
dados = cliente.recv(BUFFER_SIZE)
```

O valor definido para o buffer é:

```python
BUFFER_SIZE = 1024
```

Isso significa que o cliente pode receber até 1024 bytes em cada chamada ao método `recv()`.

O método `recv()` é bloqueante. Portanto, a execução do cliente fica temporariamente parada enquanto nenhuma resposta é enviada pelo servidor.

Quando a resposta chega, ela ainda está representada como bytes.

Por isso, o cliente realiza a conversão para texto:

```python
resposta = dados.decode(CODIFICACAO)
```

Em seguida, a resposta é apresentada ao usuário:

```python
print(f"\nServidor: {resposta}")
```

O fluxo completo de uma mensagem pode ser representado da seguinte maneira:

```text
Cliente                              Servidor
   |                                    |
   |------ "Olá, servidor!" ---------->|
   |                                    |
   |                         recebe a mensagem
   |                         prepara uma resposta
   |                                    |
   |<----- "Mensagem recebida" ---------|
   |                                    |
```

Na tela do cliente, o resultado poderia ser:

```text
Cliente: Olá, servidor!

Servidor: Mensagem recebida
```

---

## Ciclo de comunicação

A troca de mensagens ocorre dentro de uma estrutura de repetição:

```python
while True:
```

Isso permite que cliente e servidor troquem várias mensagens utilizando a mesma conexão.

O ciclo básico é:

```text
1. O cliente lê uma mensagem.
2. O cliente converte a mensagem para bytes.
3. O cliente envia os dados.
4. O cliente aguarda uma resposta.
5. O cliente recebe os dados.
6. O cliente converte os bytes para texto.
7. O cliente apresenta a resposta.
8. O processo é repetido.
```

Esse comportamento pode ser representado da seguinte forma:

```text
+-----------------------+
| Ler mensagem          |
+-----------+-----------+
            |
            v
+-----------------------+
| Converter para bytes  |
+-----------+-----------+
            |
            v
+-----------------------+
| Enviar ao servidor    |
+-----------+-----------+
            |
            v
+-----------------------+
| Aguardar resposta     |
+-----------+-----------+
            |
            v
+-----------------------+
| Receber bytes         |
+-----------+-----------+
            |
            v
+-----------------------+
| Converter para texto  |
+-----------+-----------+
            |
            v
+-----------------------+
| Exibir resposta       |
+-----------+-----------+
            |
            +------ volta ao início
```

---

## Encerramento da comunicação

A palavra `sair` é utilizada para indicar que a conexão deve ser encerrada.

```python
if mensagem.lower() == "sair":
    print("Conexão encerrada pelo cliente.")
    break
```

O método `lower()` transforma a mensagem em letras minúsculas.

Assim, as seguintes entradas são tratadas da mesma forma:

```text
sair
SAIR
Sair
SaIr
```

Depois de enviar a mensagem `sair`, o cliente interrompe a repetição e encerra a conexão.

```text
Cliente                              Servidor
   |                                    |
   |----------- "sair" ---------------->|
   |                                    |
   |------ encerramento da conexão -----|
   |                                    |
```

O cliente também encerra a execução caso receba a palavra `sair` do servidor:

```python
if resposta.lower() == "sair":
    print("O servidor solicitou o encerramento.")
    break
```

---

## Detecção do encerramento do servidor

Caso o servidor encerre a conexão sem enviar uma resposta, o método `recv()` retorna uma sequência vazia.

Essa situação é verificada por:

```python
if not dados:
    print("O servidor encerrou a conexão.")
    break
```

Assim, o cliente não permanece indefinidamente esperando por mensagens de uma conexão que já foi finalizada.

---

## Fechamento automático do socket

O socket é criado utilizando a estrutura `with`:

```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
```

Ao final desse bloco, o socket é fechado automaticamente.

Isso acontece tanto em uma execução normal quanto em determinadas situações de erro.

A utilização de `with` evita que a conexão permaneça aberta desnecessariamente e reduz a possibilidade de vazamento de recursos.

---

## Responsabilidades do cliente

Nesse exemplo, o cliente possui as seguintes responsabilidades:

* criar o socket;
* solicitar a conexão com o servidor;
* ler a mensagem digitada pelo usuário;
* converter a mensagem para bytes;
* enviar os dados ao servidor;
* aguardar uma resposta;
* converter os dados recebidos para texto;
* apresentar a resposta;
* encerrar a conexão quando necessário.

O cliente não define sozinho qual resposta será produzida. Essa responsabilidade pertence ao servidor.

---

## 7.12 Troca de mensagens

Considere a seguinte execução:

```text
Conectado ao servidor em 127.0.0.1:5000
Digite 'sair' para encerrar.

Cliente: Bom dia

Servidor: Você enviou: Bom dia

Cliente: Como vai?

Servidor: Você enviou: Como vai?

Cliente: sair

Conexão encerrada pelo cliente.
```

A comunicação correspondente seria:

```text
Cliente                              Servidor
   |                                    |
   |-------- conexão TCP -------------->|
   |                                    |
   |-------- "Bom dia" ---------------->|
   |<------- "Você enviou: Bom dia" ----|
   |                                    |
   |-------- "Como vai?" -------------->|
   |<------- "Você enviou: Como vai?" --|
   |                                    |
   |-------- "sair" ------------------->|
   |                                    |
   |-------- conexão encerrada ----------|
```

---

## Resumo

O exemplo apresenta uma arquitetura Cliente-Servidor simples baseada em sockets TCP. O cliente inicia a conexão, envia mensagens e aguarda as respostas produzidas pelo servidor. As mensagens são convertidas de texto para bytes antes do envio e novamente convertidas para texto após o recebimento.

Mesmo sendo uma aplicação pequena, o exemplo apresenta elementos fundamentais da arquitetura Cliente-Servidor:

* programas executados separadamente;
* responsabilidades distintas;
* comunicação por rede;
* estabelecimento de conexão;
* envio e recebimento de mensagens;
* protocolo de encerramento;
* tratamento de falhas de conexão.
