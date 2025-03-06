import socket
from rich.console import Console

console = Console()

HOST = '127.0.0.1'
PORT = 65432

cpf = console.input("[bold yellow]Digite um CPF para validar:[/bold yellow] ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(cpf.encode())
    resposta = client.recv(1024).decode()
    console.print(f"[bold blue]Resposta do servidor:[/bold blue] {resposta}")