import socket
from rich.console import Console

console = Console()

HOST = '127.0.0.1'
PORT = 65433

cpf = console.input("[bold yellow]Digite um CPF para validar:[/bold yellow] ")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.sendto(cpf.encode(), (HOST, PORT))
    resposta, _ = client.recvfrom(1024)
    console.print(f"[bold blue]Resposta do servidor:[/bold blue] {resposta.decode()}")