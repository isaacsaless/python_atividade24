# Exercício Python 24: Refaça a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um número que você deseja ver a tabuada: '))
for mult in range(1,11):
    mult= num*mult
    print(f'A tabuada do seu múmero é {mult}')