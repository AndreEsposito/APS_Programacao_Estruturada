def remover_acentos(frase):
    caracteres_acentuados = "áéíóúâêîôûãõàèìòùäëïöü"
    caracteres_sem_acento = "aeiouaeiouaoaeiouaeiou"
    converte_caracteres = str.maketrans(caracteres_acentuados, caracteres_sem_acento)
    return frase.translate(converte_caracteres)

def criptografa(frase, chave):
    frase_sem_acentos = remover_acentos(frase)
    frase_criptografada = ""
    caracteres_especiais = {
        ' ': '%',
        '!': '_',
        '?': '|',
        '.': '-',
        ',': '/',
        '%': '$',
        '$': '&',
        '&': '#',
        '#': '!',
        '@': '?',
        '*': ':',
        '+': ',',
        '-': '[',
        '*': ']',
        '/': '(',
        'ç': '>',
        'Ç': '<'
    }
    for caracter in frase_sem_acentos:
        if caracter.isalpha():
            if ord(caracter) == 199 or ord(caracter) == 231:
                caracter_modificado = caracteres_especiais.get(caracter, caracter)
                frase_criptografada += caracter_modificado
            else:
                caracter_maiusculo_ou_minusculo = ord('a') if caracter.islower() else ord('A')
                index_do_caracter = ( (ord(caracter)) - caracter_maiusculo_ou_minusculo + chave ) % 26
                frase_criptografada += chr(caracter_maiusculo_ou_minusculo + index_do_caracter)
        else:
            caracter_modificado = caracteres_especiais.get(caracter, caracter)
            frase_criptografada += caracter_modificado

    return frase_criptografada

def descriptografa(frase_criptografada, chave):
    frase_descriptografada = ""
    caracteres_especiais = {
        '%': ' ',
        '_': '!',
        '|': '?',
        '-': '.',
        '/': ',',
        '$': '%',
        '&': '$',
        '#': '&',
        '!': '#',
        '?': '@',
        ':': '*',
        ',': '+',
        '[': '-',
        ']': '*',
        '(': '/',
        '>': 'ç',
        '<': 'Ç'
    }
    for caracter in frase_criptografada:
        if caracter.isalpha():
            caracter_maiusculo_ou_minusculo = ord('a') if caracter.islower() else ord('A')
            index_do_caracter = ( (ord(caracter)) - caracter_maiusculo_ou_minusculo - chave ) % 26
            frase_descriptografada += chr(caracter_maiusculo_ou_minusculo + index_do_caracter)
        else:
            caracter_modificado = caracteres_especiais.get(caracter, caracter)
            frase_descriptografada += caracter_modificado
    
    return frase_descriptografada

while True:
    print("Escolha uma opção:")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    print("3 - Sair")

    try:
        escolha = int(input("Digite o número da opção desejada: "))
        if type(escolha) != int:
            raise ValueError

        if escolha == 1:
            frase = str(input("Digite uma frase para criptografar: "))
            chave = int(input("Digite a chave de criptografia (um número inteiro): "))
            frase_criptografada = criptografa(frase, chave)
            print("Frase criptografada:", frase_criptografada)
        elif escolha == 2:
            frase = str(input("Digite uma frase para descriptografar: "))
            chave = int(input("Digite a chave de descriptografia (um número inteiro): "))
            frase_descriptografada = descriptografa(frase, chave)
            print("Frase descriptografada:", frase_descriptografada)
        elif escolha == 3:
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha as opções 1, 2 ou 3.")
    except ValueError as e:
        print(f"Erro: {e}. Por favor, digite um número válido entre as opções apresentadas!")
