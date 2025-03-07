# **Validação de CPF - Sistema Cliente-Servidor (TCP/UDP)**

## **Descrição do Projeto**

Este projeto tem como objetivo implementar um sistema cliente-servidor para validar o número de um **CPF**. O sistema é dividido em duas versões de comunicação: **TCP** e **UDP**, e é composto por quatro componentes principais:

1. **Servidor TCP**: Aceita conexões de clientes e valida o CPF enviado.
2. **Cliente TCP**: Envia o CPF para o servidor TCP e exibe a resposta sobre a validade.
3. **Servidor UDP**: Recebe o CPF via pacote UDP, valida e envia a resposta ao cliente.
4. **Cliente UDP**: Envia o CPF para o servidor UDP e exibe a resposta sobre a validade.

A validação do CPF é realizada verificando sua estrutura e os dois últimos dígitos, conforme a fórmula de cálculo dos dígitos verificadores.

## **Estrutura do Projeto**

```
validador-cpf/
│── src/
│   ├── run.py             # Utilitário para facilitar a execução
│   ├── cpf_utils.py       # Função para validação de CPF
│   ├── tcp_server.py      # Servidor TCP
│   ├── tcp_client.py      # Cliente TCP
│   ├── udp_server.py      # Servidor UDP
│   ├── udp_client.py      # Cliente UDP
│── README.md              # Documentação do projeto
```

## **Como Executar**

### **Execução simplificada**

Execute o servidor TCP ou UDP de uma forma simplificada executando o seguinte comando:

```bash
python run tcp
```
ou

```bash
python run udp
```

### **Execução manual**
### 1. **Rodando o Servidor TCP**

Execute o servidor TCP com o seguinte comando:

```bash
python src/tcp_server.py
```

Este servidor ficará aguardando a conexão dos clientes na porta `65432`.

### 2. **Rodando o Cliente TCP**

Execute o cliente TCP com o seguinte comando:

```bash
python src/tcp_client.py
```

O cliente solicitará que você digite um CPF para validação. O CPF será enviado ao servidor, que retornará a resposta sobre sua validade.

### 3. **Rodando o Servidor UDP**

Execute o servidor UDP com o seguinte comando:

```bash
python src/udp_server.py
```

Este servidor ficará aguardando pacotes UDP na porta `65433`.

### 4. **Rodando o Cliente UDP**

Execute o cliente UDP com o seguinte comando:

```bash
python src/udp_client.py
```

O cliente solicitará que você digite um CPF para validação. O CPF será enviado ao servidor via UDP, que retornará a resposta sobre sua validade.

## **Funcionamento**

1. **Cliente TCP/UDP**: O cliente solicita que o usuário digite um CPF e envia esse CPF para o servidor.
2. **Servidor TCP/UDP**: O servidor recebe o CPF enviado pelo cliente e valida sua estrutura, calculando os dois últimos dígitos.
3. **Validação do CPF**: A validação é realizada conforme a fórmula oficial dos dígitos verificadores do CPF.
4. **Resposta**: O servidor envia a resposta ao cliente, que exibe se o CPF é **válido** ou **inválido**.

### **Algoritmo de Validação de CPF**

O CPF é validado em duas etapas principais:

- **Verificação de formato**: O CPF deve ter 11 dígitos numéricos.
- **Cálculo dos dígitos verificadores**: A função de validação utiliza os 9 primeiros dígitos para calcular dois dígitos verificadores. Se os dígitos verificadores calculados coincidirem com os últimos dois dígitos do CPF, o CPF é considerado válido.

## **Tecnologias Utilizadas**

- **Python 3.x**: Linguagem de programação utilizada para a implementação.
- **Sockets TCP/UDP**: Usados para a comunicação entre cliente e servidor.
- **Biblioteca `rich`**: Utilizada para formatar a saída no terminal de maneira mais visualmente agradável.



