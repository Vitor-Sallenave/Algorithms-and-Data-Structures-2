def azulejo(r, c, l, rb, cb):
    # Acessando a variável global
    global nt

    # Verificando o tamanho do lado do azulejo
    if l > 1:
        nt += 1
        l /= 2
        rnb, cnb = 0, 0

        if (rb < (r + l)) and (cb < (c + l)):
            rnb = rb
            cnb = cb
        else:
            rnb = r + l - 1
            cnb = c + l - 1
            azulejo(r, c, l, rnb, cnb)

        if (rb >= (r + l)) and (cb < (c + l)):
            rnb = rb
            cnb = cb
        else:
            rnb = r + l
            cnb = c + l - 1
            azulejo(r + l, c, l, rnb, cnb)

        if (rb >= (r + l)) and (cb >= (c + l)):
            rnb = rb
            cnb = cb
        else:
            rnb = r + l
            cnb = c + l
            azulejo(r + l, c + l, l, rnb, cnb)

        if (rb < (r+l)) and (cb >= (c + l)):
            rnb = rb
            cnb = cb
        else:
            rnb = r + l - 1
            cnb = c + l
            azulejo(r, c + l, l, rnb, cnb)


# Número total de chamadas da função
nt = 0

# Tamanho do quadrado
n = 8

# Coordenadas do buraco
rb, cb = 3, 5

# Testando
azulejo(1, 1, n, rb, cb)
