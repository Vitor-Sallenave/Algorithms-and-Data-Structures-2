def linha():
    print('==' * 40)


def Questao():
    linha()
    print(f'{"TRABALHO EC1 - QUESTÃO 1":^75}')
    linha()
    print('\n◼ Digite uma sequência de bits ("0"s e "1"s), onde todos\nos bits "1"s\
aparecem antes dos bits "0"s: ')


def Observacoes():
    print('\n* Obs1: a inserção do dígito "-1" encerra a leitura de dados !\n')


def Cabecalho():
    print('\n')
    Questao()
    Observacoes()
    linha()


def LeVetor():
    vet = list()
    i = 1
    num = 0
    print('\n')
    while num != -1:
        num = int(input(f"Digite t {i}° valor da sequência (0 ou 1): "))
        if num == 1 or num == 0:
            vet.append(num)
        i += 1

    return vet


def PrintaVetor(vet):
    cadeia = str()
    linha()
    for elem in vet:
        cadeia += str(elem)
    print(f'\nSeu vetor (tamanho = {len(vet)}): {cadeia}\n')
    linha()

    return cadeia


def Verificador(vet):
    # Mudanças observadas ao longo da leitura do vetor
    mudou = 0

    # O primeiro número sempre deve ser 1
    i = vet[0]

    if i == 0:
        return False
    else:
        for elem in vet[1:]:
            if elem != i:
                mudou += 1
            i = elem

    return False if mudou > 1 else True


def VerificaVetor(vet):
    if Verificador(vet) is False:
        print('O vetor inserido não é válido!')
        exit()


def Contagem(vet):
    # Verificando se t vetor é vazio
    if len(vet) != 0:
        # Verificando se t vetor é único
        if len(vet) == 1:
            return vet[0]
        else:
            if vet[len(vet) - 1] == 1:
                return Contagem(vet[:len(vet) - 1]) + 1
            else:
                return Contagem(vet[:len(vet) - 1])


def main():
    Cabecalho()
    vetor = LeVetor()
    bits = PrintaVetor(vetor)
    VerificaVetor(vetor)
    print(f'\nHá um total de {Contagem(vetor)} "1"s no vetor {bits}')


main()
