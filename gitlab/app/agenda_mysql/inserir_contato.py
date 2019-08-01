import mysql.connector
from mysql.connector import errorcode
import traceback


uuser = 'root'
ppassowrd = 'root'
hhost = 'mysql'
ddatabase = 'agenda'



######################
def Telefone():
    global telefone
    while True:
        try:
            telefone = int(input('Telefone do contato: '))
            if len(str(telefone)) == 10:
                break
            else:
                print('Tente novamente, use 10 caracteres (ddd + 9999-9999): ')
        except:
            print('Ops... Tente novamente')
    return telefone

def Celular():
    global celular
    while True:
        try:
            celular = int(input('Celular do contato: '))
            if len(str(celular)) == 11:
                break
            else:
                print('Tente novamente, use 11 caracteres (ddd + 99999-9999): ')
        except:
            print('Ops... Tente novamente')
    return celular





def inserir():
    global telefone, celular
    conexao = mysql.connector.connect(user=uuser, password=ppassowrd, host=hhost, database=ddatabase)
    while True:
        nome = str(input('Nome do contato: '))
        if len(nome) > 30:
            print('Tente novamente, use no maximo 30 caracteres: ')
            nome = str(input('Nome do contato: '))
        elif len(nome) == 0:
            print('Tente novamente, esse campo não pode ficar vazio: ')
            nome = str(input('Nome do contato: '))
        elif nome in '1 2 3 4 5 6 7 8 9 0':
            print('Tente novamente, esse campo não pode conter números: ')
            nome = str(input('Nome do contato: '))
        break

    Telefone()
    Celular()

    telefone = str(telefone)
    celular = str(celular)
    telefone = f'({telefone[0:2]}){telefone[2:6]}-{telefone[6:10]}'
    celular = f'({celular[0:2]}){celular[2:7]}-{celular[7:11]}'

    contato = (nome, telefone, celular)

    cursor = conexao.cursor()

    while True:
        try:

            inserir_contato = ('insert into agenda.contatos(nome, telefone, celular) values (%s, %s, %s)')
            cursor.execute(inserir_contato, contato)
        except Exception as trace:

                print(f'''
    ------------------------------------------------------------------------------------------------------------
    
                {trace}
    
    ------------------------------------------------------------------------------------------------------------''')
                print('Você digitou um dado já existente no banco de dados.\n')
                trace = traceback.format_exc()

            # if 'celular' in trace:
            #     print('Insira o celular novamente!')


            # if 'telefone' in trace:
            #     print('Insira o telefone novamente!')
                Telefone()
                Celular()

                telefone = str(telefone)
                celular = str(celular)
                telefone = f'({telefone[0:2]}){telefone[2:6]}-{telefone[6:10]}'
                celular = f'({celular[0:2]}){celular[2:7]}-{celular[7:11]}'
                contato = (nome, telefone, celular)

        else:
            print(f'\ncontato {nome.upper()} adcionado ao Banco de dados com sucesso. \nTelefone: {telefone} \nCelular: {celular}')
            input('[ENTER]')
            conexao.commit()
            cursor.close()
            conexao.close()
            break









