import socket
from rich.console import Console
from rich.panel import Panel
from cpf_utils import validar_cpf

console = Console()

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    server.bind((HOST, PORT))
    console.print(Panel("[bold green]Servidor UDP iniciado![/bold green]", expand=False))

    while True:
        data, addr = server.recvfrom(1024)
        cpf = data.decode()

        console.print(f"[cyan]Recebido de {addr}:[/cyan] {cpf}")
        
        resposta = "[bold green]Válido[/bold green]" if validar_cpf(cpf) else "[bold red]Inválido[/bold red]"
        server.sendto(resposta.encode(), addr)