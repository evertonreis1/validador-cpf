import socket
import time
from rich.console import Console

console = Console()

HOST = '127.0.0.1'
PORT = 65432
RETRY_INTERVAL = 1
MAX_RETRIES = 5

def wait_for_server(host, port):
    retries = 0
    while True:
        if retries >= MAX_RETRIES:
            console.print("[bold red]Número máximo de tentativas excedido. Servidor indisponível. Encerrando...[/bold red]")
            exit(1)
        try:
            with socket.create_connection((host, port), timeout=3):
                console.print("[bold green]Servidor está disponível![/bold green]")
                return
        except (socket.error, ConnectionRefusedError):
            console.print("[bold red]Servidor indisponível. Tentando novamente...[/bold red]")
            retries += 1
            time.sleep(RETRY_INTERVAL)

wait_for_server(HOST, PORT)

cpf = console.input("[bold yellow]Digite um CPF para validar:[/bold yellow] ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(cpf.encode())
    resposta = client.recv(1024).decode()
    console.print(f"[bold blue]Resposta do servidor:[/bold blue] {resposta}")