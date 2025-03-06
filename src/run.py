import subprocess
import argparse
import time
import atexit


def start_process(command):
    return subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def stop_process(process):
    if process:
        process.terminate()
        process.wait()

def main():
    parser = argparse.ArgumentParser(description="Executa o servidor e cliente TCP ou UDP.")
    parser.add_argument("protocolo", choices=["tcp", "udp"], help="Escolha entre TCP ou UDP.")
    args = parser.parse_args()

    server_script = f"{args.protocolo}_server.py"
    client_script = f"{args.protocolo}_client.py"

    print(f"Iniciando servidor {args.protocolo.upper()}...")
    server_process = start_process(["python3", server_script])

    atexit.register(stop_process, server_process)

    time.sleep(1)
    
    try:
        print(f"Iniciando cliente {args.protocolo.upper()}...")
        subprocess.run(["python3", client_script])
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário, finalizando...")
    finally:
        stop_process(server_process)

if __name__ == "__main__":
    main()
