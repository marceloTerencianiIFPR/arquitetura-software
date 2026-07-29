import socket

# Endereço IP do servidor.
# Deve ser o mesmo utilizado no servidor.
#
# 127.0.0.1 (localhost) indica que o cliente irá se conectar
# ao servidor que está executando no mesmo computador.
HOST = "127.0.0.1"

# Porta utilizada na comunicação.
# Deve ser a mesma porta configurada no servidor.
PORT = 5000

# Quantidade máxima de bytes recebidos em cada leitura.
BUFFER_SIZE = 1024

# Codificação utilizada para converter texto em bytes e vice-versa.
CODIFICACAO = "utf-8"


def iniciar_cliente() -> None:

    # Cria um socket utilizando:
    #
    # AF_INET:
    #   Família de endereços IPv4.
    #
    # SOCK_STREAM:
    #   Comunicação orientada à conexão utilizando TCP.
    #
    # O comando "with" garante que o socket será fechado
    # automaticamente ao final da execução.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:

        # Solicita uma conexão com o servidor.
        #
        # Caso o servidor não esteja em execução,
        # será lançada uma exceção.
        cliente.connect((HOST, PORT))

        print(f"Conectado ao servidor em {HOST}:{PORT}")
        print("Digite 'sair' para encerrar.\n")

        while True:

            # Lê uma mensagem digitada pelo usuário.
            mensagem = input("Cliente: ")

            # Converte o texto para bytes e envia ao servidor.
            cliente.sendall(mensagem.encode(CODIFICACAO))

            # Caso o cliente deseje encerrar a conversa,
            # a conexão será finalizada.
            if mensagem.lower() == "sair":
                print("Conexão encerrada pelo cliente.")
                break

            # Aguarda uma resposta enviada pelo servidor.
            #
            # recv() é uma operação bloqueante.
            # Enquanto o servidor não responder,
            # o cliente permanecerá aguardando.
            dados = cliente.recv(BUFFER_SIZE)

            # Caso nenhum dado seja recebido,
            # significa que o servidor encerrou a conexão.
            if not dados:
                print("O servidor encerrou a conexão.")
                break

            # Converte os bytes recebidos em texto.
            resposta = dados.decode(CODIFICACAO)

            print(f"\nServidor: {resposta}")

            # Caso o servidor envie "sair",
            # o cliente também encerrará a comunicação.
            if resposta.lower() == "sair":
                print("O servidor solicitou o encerramento.")
                break


if __name__ == "__main__":

    # Trata possíveis erros durante a execução do cliente.
    try:
        iniciar_cliente()

    # Ocorre quando o servidor não está em execução
    # ou não está aceitando conexões.
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor.")

    # Trata outros erros relacionados à conexão.
    except ConnectionError as erro:
        print(f"Erro de conexão: {erro}")

    # Trata outros erros do sistema operacional.
    except OSError as erro:
        print(f"Erro no cliente: {erro}")