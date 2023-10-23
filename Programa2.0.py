import string
from time import sleep

def tabela_acentos(chave):
    caracteres_com_acentos = string.ascii_letters + "áéíóúâêîôûãõàèìòùäëïöüÁÉÍÓÚÂÊÎÔÛÃÕÀÈÌÒÙÄËÏÖÜ"
    tabela = {}
    for i, char in enumerate(caracteres_com_acentos):
        tabela[char] = caracteres_com_acentos[(i + chave) % len(caracteres_com_acentos)]
    return tabela

def encriptacao_descriptacao(frase, chave):
    caracter_com_acento_substituido = tabela_acentos(chave)
    frase_modificada = ""
    caracteres_especiais = {
        ' ': '%',
        '%': ' ',
        '!': '_',
        '_': '!',
        '?': '|',
        '|': '?',
        '.': ')',
        ')': '.',
        ',': '/',
        '/': ',',
        '$': '(',
        '(': '$',
        '&': '#',
        '#': '&',
        '@': '^',
        '^': '@',
        '*': ':',
        ':': '*',
        '-': '[',
        '[': '-',
        'ç': '>',
        '>': 'ç',
        'Ç': '<',
        '<': 'Ç'
    }

    for caracter in frase:
        if ord(caracter) == 199 or ord(caracter) == 231:
            caracter_modificado = caracteres_especiais.get(caracter, caracter)
            frase_modificada += caracter_modificado
        elif caracter in caracter_com_acento_substituido:
            frase_modificada += caracter_com_acento_substituido[caracter]
        elif caracter.isalpha():
            caracter_maiusculo_ou_minusculo = ord('a') if caracter.islower() else ord('A')
            index_do_caracter = ( (ord(caracter)) - caracter_maiusculo_ou_minusculo + chave ) % 26
            frase_modificada += chr(caracter_maiusculo_ou_minusculo + index_do_caracter)
        else:
            caracter_modificado = caracteres_especiais.get(caracter, caracter)
            frase_modificada += caracter_modificado
    return frase_modificada

while True:
    print("Escolha uma opção:")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    print("3 - Sair")

    try:
        escolha = int(input("Digite o número da opção desejada: "))
        if type(escolha) != int:
            raise ValueError
        else:
            if escolha == 1:
                frase = str(input("Digite uma frase para criptografar: "))
                chave = int(input("Digite a chave de criptografia (um número inteiro): "))
                frase_criptografada = encriptacao_descriptacao(frase, chave)
                print("Frase criptografada:", frase_criptografada)
            elif escolha == 2:
                frase = str(input("Digite uma frase para descriptografar: "))
                chave = int(input("Digite a chave de descriptografia (um número inteiro): "))
                frase_descriptografada = encriptacao_descriptacao(frase, -chave)
                print("Frase descriptografada:", frase_descriptografada)
            elif escolha == 3:
                print("Saindo do programa...")
                sleep(1.5)
                print("Até logo")
                break
            else:
                print("Opção inválida! Por favor, escolha as opções 1, 2 ou 3.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, digite um número válido entre as opções apresentadas!")
