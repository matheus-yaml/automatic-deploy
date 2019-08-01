from inserir_contato import inserir
from exibir_contatos import exibir
from remover_contatos import remover
from atualizar_contatos import atualizar
import os

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        print('''

        ---------AGENDA-------------

        ADCIONAR CONTATOS       [ 1 ]
        ATUALIZAR CONTATOS      [ 2 ]
        REMOVER CONTATOS        [ 3 ]
        VER CONTATOS            [ 4 ]
        SAIR DA AGENDA          [ 5 ]

        -----------------------------    
        ''')
        opcao = 0 #int(input('Escolha uma das opcoes acima: '))
        if opcao > 5 or opcao < 1:
            opcao =int(input('Escolha apenas uma das OPCOES ACIMA: '))

    except:
        input('Ops... APENAS NÚMEROS, tente novamente! [ENTER]')



    if opcao == 1:
        inserir()
    elif opcao == 2:
        atualizar()
    elif opcao == 3:
        remover()
    elif opcao == 4:
        exibir()
    elif opcao == 5:
        break