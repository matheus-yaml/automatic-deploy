import mysql.connector
import os

uuser = 'root'
ppassowrd = 'root'
hhost = 'mysql'
ddatabase = 'agenda'


def ver_por_nome():
    conexao = mysql.connector.connect(user=uuser, password=ppassowrd, host=hhost, database=ddatabase)
    cursor = conexao.cursor()

    while True:
        nome = str(input('Nome para consulta: '))
        while len(nome) == 0 or len(nome) > 30 or nome in '1 2 3 4 5 6 7 8 9 0':
            if len(nome) > 30:
                print('Tente novamente, use no maximo 30 caracteres: ')
                nome = str(input('Nome para consulta: '))
            elif len(nome) == 0:
                print('Tente novamente, esse campo não pode ficar vazio: ')
                nome = str(input('Nome para consulta: '))
            elif nome in '1 2 3 4 5 6 7 8 9 0':
                print('Tente novamente, esse campo não pode conter números: ')
                nome = str(input('Nome para consulta: '))
        break

    cursor.execute(f'select nome, telefone, celular, id from agenda.contatos where nome like "%{nome}%"')
    for (nome, telefone, celular, id) in cursor:
        print(f'Nome: {nome:20} Telefone: {telefone}    Celulat{celular}   ID {id}')


def ver_por_telefone():
    conexao = mysql.connector.connect(user=uuser, password=ppassowrd, host=hhost, database=ddatabase)
    cursor = conexao.cursor()

    while True:
        try:
            telefone = int(input('Telefone para consulta: '))
            if len(str(telefone)) == 10:
                break
            else:
                print('Tente novamente, use 10 caracteres (ddd + 9999-9999): ')
        except:
            print('Ops... Tente novamente')

    telefone = str(telefone)
    telefone = f'({telefone[0:2]}){telefone[2:6]}-{telefone[6:10]}'

    cursor.execute(f'select nome, telefone, celular, id from agenda.contatos where telefone = "{telefone}"')
    for (nome, telefone, celular, id) in cursor:
        print(f'Nome: {nome:20} Telefone: {telefone}    Celulat{celular}   ID {id}')
    conexao.close()
    cursor.close()


def ver_por_celular():
    conexao = mysql.connector.connect(user=uuser, password=ppassowrd, host=hhost, database=ddatabase)
    cursor = conexao.cursor()

    while True:
        try:
            celular = int(input('Celular para consulta: '))
            if len(str(celular)) == 11:
                break
            else:
                print('Tente novamente, use 11 caracteres (ddd + 99999-9999): ')
        except:
            print('Ops... Tente novamente')

    celular = str(celular)
    celular = f'({celular[0:2]}){celular[2:7]}-{celular[7:11]}'

    cursor.execute(f'select nome, telefone, celular, id from agenda.contatos where celular = "{celular}"')
    for (nome, telefone, celular, id) in cursor:
        print(f'Nome: {nome:20} Telefone: {telefone}    Celulat{celular}   ID {id}')
    conexao.close()
    cursor.close()


def ver_por_id():
    conexao = mysql.connector.connect(user=uuser, password=ppassowrd, host=hhost, database=ddatabase)
    cursor = conexao.cursor()

    while True:
        try:
            id = int(input('ID para consulta: '))
            if len(str(id)) > 0:
                break
            else:
                print('Este campo não pode ficar vazio')
        except:
            print('Ops... Este campo não pode ficar vazio')

    id = str(id)
    id = f'{id}'

    cursor.execute(f'select nome, telefone, celular, id from agenda.contatos where id = "{id}"')
    for (nome, telefone, celular, id) in cursor:
        print(f'Nome: {nome:20} Telefone: {telefone}    Celulat{celular}   ID {id}')
    conexao.close()
    cursor.close()

def ver_todos():
    conexao = mysql.connector.connect(user=uuser, password=ppassowrd, host=hhost, database=ddatabase)
    cursor = conexao.cursor()
    cursor.execute('select nome, telefone, celular, id from agenda.contatos')

    for (nome, telefone, celular, id) in cursor:
        print(f'Nome: {nome:20} Telefone: {telefone}    Celular {celular}   ID {id}')
    input('[ENTER]')
    conexao.close()
    cursor.close()



def exibir():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print('''
            ------------------------------------
            VAMOS CONSULTAR A NOSSA AGENDA!

            CONSULTA POR NOME               [ 1 ]
            CONSULTA POR TELEFONE           [ 2 ]
            CONSULTA POR CELULAR            [ 3 ]
            CONSULTA POR ID                 [ 4 ]
            CONSULTAR TODOS OS CONTATOS     [ 5 ]
            SAIR                            [ 6 ]

            -----------------------------------
            ''')
            opcao = 0  # int(input('Escolha uma das opcoes acima: '))
            if opcao > 5 or opcao < 1:
                opcao = int(input('Escolha apenas uma das OPCOES ACIMA: '))


        except:
            print('Ops... APENAS NÚMEROS, tente novamente! ')

        else:
            if opcao == 1:
                ver_por_nome()
            elif opcao == 2:
                ver_por_telefone()
            elif opcao == 3:
                ver_por_celular()
            elif opcao == 4:
                ver_por_id()
            elif opcao == 5:
                ver_todos()
            elif opcao == 6:
                break

