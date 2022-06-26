import random


def vic():
    if (tabuleiro[0][0] == 'X' and tabuleiro[0][1] == 'X' and tabuleiro[0][2] == 'X') or (#123
            tabuleiro[1][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[1][2] == 'X') or (#456
            tabuleiro[2][0] == 'X' and tabuleiro[2][1] == 'X' and tabuleiro[2][2] == 'X') or (#789
            tabuleiro[0][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == 'X') or (#159
            tabuleiro[0][0] == 'X' and tabuleiro[1][0] == 'X' and tabuleiro[2][0] == 'X') or ( #147
            tabuleiro[0][1] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][1] == 'X') or (#258
            tabuleiro[0][2] == 'X' and tabuleiro[1][2] == 'X' and tabuleiro[2][2] == 'X') or (#369
            tabuleiro[0][2] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][0] == 'X'):#357
        print('Vitoria do X')
        return True  # x venceu
    elif (tabuleiro[0][0] == 'O' and tabuleiro[0][1] == 'O' and tabuleiro[0][2] == 'O') or (#123
            tabuleiro[1][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[1][2] == 'O') or (#456
            tabuleiro[2][0] == 'O' and tabuleiro[2][1] == 'O' and tabuleiro[2][2] == 'O') or (#789
            tabuleiro[0][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][2] == 'O') or (
            tabuleiro[0][0] == '0' and tabuleiro[1][0] == '0' and tabuleiro[2][0] == 'O') or (  #
            tabuleiro[0][1] == '0' and tabuleiro[1][1] == '0' and tabuleiro[2][1] == '0') or (
            tabuleiro[0][2] == '0' and tabuleiro[1][2] == '0' and tabuleiro[2][2] == '0') or (
            tabuleiro[0][2] == '0' and tabuleiro[1][1] == '0' and tabuleiro[2][0] == '0'):
        print('Vitoria do O')
        return True  # O venceu
    else:
        return False


tabuleiro = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]


def imprimirtab():
    print(f"""
            {tabuleiro[0][0]} |{tabuleiro[0][1]} |{tabuleiro[0][2]} 
            --------
            {tabuleiro[1][0]} |{tabuleiro[1][1]} |{tabuleiro[1][2]} 
            --------
            {tabuleiro[2][0]} |{tabuleiro[2][1]} |{tabuleiro[2][2]} 

          """)


imprimirtab()
win = False

vez=0
while vez!=1 and vez!=2:
    try:
        vez = int(input("escolha um simbolo:\n1=X 2=O:\n"))
    except:
        print()

    if vez!=1 and vez!=2:
        print("Opção invalida")

listapos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while win == False:

    if vez == 1:
        pos = int(input('escolha a posição: '))

        if pos == 1:
            tabuleiro[0][0]='X'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 2:
            tabuleiro[0][1] = 'X'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 3:
            tabuleiro[0][2] = 'X'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 4:
            tabuleiro[1][0] = 'X'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 5:
            tabuleiro[1][1] = 'X'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 6:
            tabuleiro[1][2] = 'X'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 7:
            tabuleiro[2][0] = 'X'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 8:
            tabuleiro[2][1] = 'X'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 9:
            tabuleiro[2][2] = 'X'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        else:
            print('dados incorretos')
        # começar jogada do adversário
        try:
            num = random.choice(listapos)
        except:
            break
        if num == 1:
            tabuleiro[0][0] = 'O'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 2:
            tabuleiro[0][1] = 'O'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 3:
            tabuleiro[0][2] = 'O'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 4:
            tabuleiro[1][0] = 'O'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 5:
            tabuleiro[1][1] = 'O'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 6:
            tabuleiro[1][2] = 'O'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 7:
            tabuleiro[2][0] = 'O'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 8:
            tabuleiro[2][1] = 'O'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 9:
            tabuleiro[2][2] = 'O'
            imprimirtab()
            listapos.remove(num)
            win = vic()
    elif vez == 2:
        pos = int(input('escolha a posição: '))

        if pos == 1:
            tabuleiro[0][0] = 'O'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 2:
            tabuleiro[0][1] = 'O'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 3:
            tabuleiro[0][2] = 'O'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 4:
            tabuleiro[1][0] = 'O'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 5:
            tabuleiro[1][1] = 'O'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 6:
            tabuleiro[1][2] = 'O'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 7:
            tabuleiro[2][0] = 'O'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 8:
            tabuleiro[2][1] = 'O'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        elif pos == 9:
            tabuleiro[2][2] = 'O'
            imprimirtab()
            listapos.remove(pos)
            win = vic()
        else:
            print('dados incorretos')
        # começar jogada do adversário
        try:
            num = random.choice(listapos)
        except:
            break
        if num == 1:
            tabuleiro[0][0] = 'X'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 2:
            tabuleiro[0][1] = 'X'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 3:
            tabuleiro[0][2] = 'X'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 4:
            tabuleiro[1][0] = 'X'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 5:
            tabuleiro[1][1] = 'X'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 6:
            tabuleiro[1][2] = 'X'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 7:
            tabuleiro[2][0] = 'X'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 8:
            tabuleiro[2][1] = 'X'
            imprimirtab()
            listapos.remove(num)
            win = vic()
        elif num == 9:
            tabuleiro[2][2] = 'X'
            imprimirtab()
            listapos.remove(num)
            win = vic()

if win==False:
    print('O jogo termina empatado!!')
finish = input("Aperte qualquer tecla para finalizar o jogo")
print(win)