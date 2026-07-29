import socket

# Endereço IP do servidor.
# 127.0.0.1 (localhost) indica que o servidor aceitará conexões
# apenas do próprio computador.
HOST = "127.0.0.1"

# Porta utilizada para a comunicação.
# Cliente e servidor devem utilizar a mesma porta.
PORT = 5000

# Quantidade máxima de bytes recebidos em cada leitura.
BUFFER_SIZE = 1024

# Codificação utilizada para converter texto em bytes e vice-versa.
CODIFICACAO = "utf-8"


def iniciar_servidor() -> None:

    # Cria um socket utilizando:
    #
    # AF_INET:
    #   Família de endereços IPv4.
    #   Exemplos: 127.0.0.1, 192.168.1.10.
    #
    # SOCK_STREAM:
    #   Comunicação orientada à conexão utilizando TCP.
    #   O TCP garante a entrega das mensagens e mantém sua ordem.
    #
    # O comando "with" garante que o socket será fechado
    # automaticamente ao final da execução.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:

        # Configura uma opção do socket.
        #
        # SOL_SOCKET:
        #   Indica que a configuração será aplicada ao próprio socket.
        #
        # SO_REUSEADDR:
        #   Permite reutilizar rapidamente a porta caso o programa seja
        #   encerrado e iniciado novamente, evitando o erro:
        #   "Address already in use".
        #
        # Valor 1:
        #   Habilita essa opção.
        servidor.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1
        )

        # Associa o socket ao endereço IP e à porta definidos.
        servidor.bind((HOST, PORT))

        # Coloca o socket em modo servidor.
        #
        # O parâmetro 1 indica que apenas uma conexão ficará na fila
        # de espera enquanto o servidor estiver ocupado.
        servidor.listen(1)

        print(f"Servidor aguardando conexão em {HOST}:{PORT}...")

        # Aguarda um cliente solicitar conexão.
        #
        # Esta chamada é bloqueante: o programa permanece parado
        # até que algum cliente se conecte.
        conexao, endereco = servidor.accept()

        # O objeto "conexao" representa exclusivamente o cliente
        # que acabou de se conectar.
        with conexao:

            print(f"Cliente conectado: {endereco}")
            print("Digite 'sair' para encerrar.\n")

            while True:

                # Aguarda uma mensagem enviada pelo cliente.
                #
                # recv() também é bloqueante.
                # O servidor permanecerá aguardando até receber dados.
                dados = conexao.recv(BUFFER_SIZE)

                # Caso nenhum dado seja recebido,
                # significa que o cliente encerrou a conexão.
                if not dados:
                    print("O cliente encerrou a conexão.")
                    break

                # Converte os bytes recebidos em texto.
                mensagem_cliente = dados.decode(CODIFICACAO)

                print(f"\nCliente: {mensagem_cliente}")

                # Caso o cliente envie "sair",
                # o servidor também encerra a conversa.
                if mensagem_cliente.lower() == "sair":
                    print("O cliente solicitou o encerramento.")
                    break

                # O operador do servidor lê a mensagem recebida
                # e digita manualmente uma resposta.
                resposta = input("Servidor: ")

                # Converte o texto em bytes e envia ao cliente.
                conexao.sendall(resposta.encode(CODIFICACAO))

                # Caso o servidor envie "sair",
                # a conexão também será encerrada.
                if resposta.lower() == "sair":
                    print("Conexão encerrada pelo servidor.")
                    break


if __name__ == "__main__":

    # Trata possíveis erros durante a execução do servidor.
    try:
        iniciar_servidor()

    except ConnectionError as erro:
        print(f"Erro de conexão: {erro}")

    except OSError as erro:
        print(f"Erro no servidor: {erro}")