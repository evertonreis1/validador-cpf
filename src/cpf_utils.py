from rich import print

def validar_cpf(cpf: str) -> bool:
    cpf = ''.join([c for c in cpf if c.isdigit()])
    if len(cpf) != 11:
        return False
    
    def calcular_digito(cpf_parcial):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(len(cpf_parcial) + 1, 1, -1)))
        resto = (soma * 10) % 11
        return '0' if resto == 10 else str(resto)
    
    return cpf[-2:] == calcular_digito(cpf[:9]) + calcular_digito(cpf[:10])