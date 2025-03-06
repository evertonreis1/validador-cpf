import socket
from rich.console import Console
from rich.panel import Panel
from cpf_utils import validar_cpf

console = Console()

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    console.print(Panel("[bold green]Servidor TCP iniciado![/bold green]", expand=False))

    while True:
        conn, addr = server.accept()
        console.print(f"[cyan]Cliente conectado:[/cyan] {addr}")

        with conn:
            while True:
                cpf = conn.recv(1024).decode()
                if not cpf:
                    break
                resposta = "[bold green]Válido[/bold green]" if validar_cpf(cpf) else "[bold red]Inválido[/bold red]"
                conn.sendall(resposta.encode())