from time import sleep


# FUNÇÃO MENU PRINCIPAL DO SISTEMA
def menu():
    sleep(0.5)
    print("=" * 70)
    print(' ' * 25, "SEJA BEM VINDO", ' ' * 25)
    print("=" * 70)
    sleep(1)
    print("""
   \033[1;32mMENU PRINCIPAL:\033[m

Selecione uma opção abaixo:

1) Digite zero para adicionar uma vaca leiteira nova [0]
2) Digite um para ver quais vacas leiteiras já foram adicionadas [1]
3) Digite dois, caso deseja buscar por uma vaca [2]
4) Digite três, caso deseje excluir uma vaca de sua lista [3]
5) Digite quatro para sair [4]
""")
    print("=" * 70)
    lista.sort()
    n = leiaInt('Digite: ')
    # adicionar código de vaca
    if n == 0:
        adicionar()
    # ver vacas adicionadas
    if n == 1:
        quantidade()
    # buscar código de vacas por sequência binária
    if n == 2:
        num = leiaInt2('Digite um código de vaca: ')
        busc = buscaBinaria(lista, num)
        if busc:
            sleep(1)
            print(f"a vaca com o código {num} foi enc