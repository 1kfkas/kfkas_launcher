
# Upload

def Upload():

    print('\nAviso : Tenha certeza de que seu arquivo está na pasta "Upload"')

    fileName = './Upload/'+str(input('\nNome do arquivo : '))

    files = m.find(fileName)

    if(files):
        m.delete(files[0])

    file = m.upload(fileName)

# Download

def Download():

    print('\nAviso : Tenha certeza de que existe esse arquivo na sua conta')

    fileName = str(input('\nNome do arquivo : '))
    file = m.find(fileName)
    m.download(file)

# Connection

def CheckInternet():

    import requests, sys

    url = 'http://mega.nz'
    internet = False

    while not internet:

        timeout = 5
    
        try:
            request = requests.get(url, timeout=timeout)
            print('\nInternet Conectada')
            internet = True
        except (requests.ConnectionError, requests.Timeout) as exception:
            print('\nInternet Não Conectada')
            print('\nTentar Novamente ?')
            print('\n1 : Sim\n2 : Não')
            choose = int(input('\nEscolher : '))

            if choose == 2:
                internet = True
                exit

#

CheckInternet()

# Login

from mega import Mega

mega = Mega()

print('\nSessão de Login')

email = str(input('\nEmail : '))
password = str(input('\nSenha : '))

print('\nEntrando...')

m = mega.login(email, password)

program = True
    
while program:

    print('\nEscolha uma opção : ')
    print('\n1 : Upload\n2 : Download (Em manutenção)\n3 : Sair')
    choose = int(input('\nEscolher : '))

    if(choose==1):
        Upload()
    elif(choose==2):
        program = True
    elif(choose==3):
        program = False

print('\nPrograma Fechado')
