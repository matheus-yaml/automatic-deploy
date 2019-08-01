import mysql.connector
from exibir_contatos import ver_todos
import os

uuser = 'root'
ppassowrd = 'root'
hhost = 'mysql'
ddatabase = 'agenda'


def remover():
    conexao = mysql.connector.connect(user=uuser, password=ppassowrd, host=hhost, database=ddatabase)
    cursor = conexao.cursor()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('PAINEL DE REMOÇÃO DE CONTATOS, USE COM CUIDADO')
        input('ENTER para continuar')

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                print('''
    
                    ---------AGENDA-------------

                    REMOVER CONTATO         [ 1 ]
                    SAIR                    [ 2 ]

                    -----------------------------    
                                                ''')
                opcao = int(input('Escolha apenas uma das OPCOES ACIMA: '))
                if opcao > 2 or opcao < 1:
                    opcao = int(input('Escolha 1 ou 2: '))
                else:
                    break
            except:
                print('Ops... APENAS NÚMEROS, tente novamente! ')
                input('\n[ENTER]')
        if opcao == 2:
            break

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            ver_todos()
            try:
                id = ''
                if len(str(id)) < 1:
                    id = int(input('Digite um ID PARA DELETAR o contato: '))

            except:
                print('Ops... Este campo não pode ficar vazio \n')
                input('ENTER')


            else:
                cursor.execute(f"delete from agenda.contatos where id = '{id}'")
                print(f'Contato com id {id} deletado com sucesso!')
                conexao.commit()
                #cursor.close()
                #conexao.close()
                break



