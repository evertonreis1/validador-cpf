import socket
from rich.console import Console


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        while True:
            cpf = console.input("\n[bold yellow]Digite um CPF para validar (ou 'sair' para encerrar):[/bold yellow] ").strip()
            
            if cpf.lower() == 'sair':
                console.print("[bold cyan]Encerrando o cliente...[/bold cyan]")
                break

            client.sendto(cpf.encode(), (HOST, PORT))
            resposta, _ = client.recvfrom(1024)
            console.print(f"[bold blue]Resposta do servidor:[/bold blue] {resposta.decode()}")


HOST = '127.0.0.1'
PORT = 65433

console = Console()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Cliente interrompido![/bold red]")
        exit(0)