def divisao_e_resto( a, b):
    div = int(a/b)
    res = int(a%b)
    return (div, res)


n1, n2 = (10, 3)

print('###################################################')
print('')

print('Numero 1:', n1)
print('Numero 2:', n2)
divisao, resto = divisao_e_resto(n1, n2)
print('divisão:', divisao)
print('resto:', resto)
print('')

n1, n2 = (50, 35)

print('###################################################')
print('')

print('Numero 1:', n1)
print('Numero 2:', n2)
divisao, resto = divisao_e_resto(n1, n2)
print('divisão:', divisao)
print('resto:', resto)

print('')

