def ordenar_parte(parte, ordem='asc'):
    # Esta função ordena uma string de dígitos em ordem crescente (asc) ou decrescente (desc)
    if ordem == 'asc':
        return ''.join(sorted(parte))  # Ordena a parte em ordem crescente
    else:
        return ''.join(sorted(parte, reverse=True))  # Ordena a parte em ordem decrescente

def ordenar_numero(numero):
    # Converte o número para string para facilitar a manipulação
    numero_str = str(numero)
    
    # Verifica se o número é decimal
    if '.' in numero_str:
        # Separa a parte inteira e a parte decimal
        parte_inteira, parte_decimal = numero_str.split('.')
        
        # Ordena a parte inteira e a parte decimal
        numero_ordenado_menor = f"{ordenar_parte(parte_inteira)}.{ordenar_parte(parte_decimal)}"
        numero_ordenado_maior = f"{ordenar_parte(parte_inteira, 'desc')}.{ordenar_parte(parte_decimal, 'desc')}"
    else:
        # Ordena os dígitos do número inteiro
        numero_ordenado_menor = ordenar_parte(numero_str)
        numero_ordenado_maior = ordenar_parte(numero_str, 'desc')
    
    # Retorna os números ordenados em ambas as ordens
    return numero_ordenado_menor, numero_ordenado_maior

# Solicita ao usuário que insira um número
numero_escolhido = input('Escolha um número inteiro ou decimal com mais de um dígito: ')

# Chama a função para ordenar o número
numero_ordenado_menor, numero_ordenado_maior = ordenar_numero(numero_escolhido)

# Exibe os resultados ordenados
print(f'Seu número ordenado do menor para o maior fica assim: {numero_ordenado_menor}')
print(f'Seu número ordenado do maior para o menor fica assim: {numero_ordenado_maior}')