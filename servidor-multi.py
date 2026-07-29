import socket
import threading

HOST = "0.0.0.0"
PORT = 5000
BUFFER_SIZE = 1024
ENCODING = "utf-8"

conexoes_ativas = 0
lock = threading.Lock()


def alterar_conexoes_ativas(valor):
    global conexoes_ativas

    with lock:
        conexoes_ativas += valor
        print(f"Conexões ativas: {conexoes_ativas}")


def atender_cliente(conexao, endereco):
    print(f"\n[+] Cliente conectado: {endereco}")
    alterar_conexoes_ativas(1)

    try:
        while True:
            dados = conexao.recv(BUFFER_SIZE)

            if not dados:
                print(f"[-] Cliente {endereco} encerrou a conexão.")
                break

            mensagem = dados.decode(ENCODING).strip()

            print(f"[{endereco}] Mensagem recebida: {mensagem}")

            if mensagem.lower() == "sair":
                print(f"[-] Cliente {endereco} solicitou o encerramento.")
                break

            try:
                valores = mensagem.split()

                if len(valores) != 2:
                    raise ValueError

                numero1 = float(valores[0])
                numero2 = float(valores[1])

                soma = numero1 + numero2
                resposta = str(soma)

            except ValueError:
                resposta = (
                    "Erro: informe dois números separados por espaço "
                    "ou digite 'sair'."
                )

            conexao.sendall(resposta.encode(ENCODING))

    except ConnectionResetError:
        print(f"[!] A conexão com {endereco} foi interrompida.")

    except OSError as erro:
        print(f"[!] Erro na comunicação com {endereco}: {erro}")

    finally:
        conexao.close()
        alterar_conexoes_ativas(-1)
        print(f"[x] Cliente desconectado: {endereco}")


def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    servidor.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    servidor.bind((HOST, PORT))
    servidor.listen()

    print("=" * 50)
    print("Servidor de soma iniciado")
    print(f"Endereço: {HOST}")
    print(f"Porta: {PORT}")
    print("Formato esperado: numero1 numero2")
    print("Para encerrar o cliente, envie: sair")
    print("=" * 50)

    try:
        while True:
            conexao, endereco = servidor.accept()

            thread_cliente = threading.Thread(
                target=atender_cliente,
                args=(conexao, endereco),
                daemon=True
            )

            thread_cliente.start()

    except KeyboardInterrupt:
        print("\nServidor encerrado pelo usuário.")

    finally:
        servidor.close()
        print("Socket do servidor fechado.")


if __name__ == "__main__":
    iniciar_servidor()