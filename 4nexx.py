import random
import datetime
import os
from time import sleep

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# GERADOR DE TITULOS

lista_ascii = [
'''
$$\   $$\ $$\   $$\                               
$$ |  $$ |$$$\  $$ |                              
$$ |  $$ |$$$$\ $$ | $$$$$$\  $$\   $$\ $$\   $$\ 
$$$$$$$$ |$$ $$\$$ |$$  __$$\ \$$\ $$  |\$$\ $$  |
\_____$$ |$$ \$$$$ |$$$$$$$$ | \$$$$  /  \$$$$  / 
      $$ |$$ |\$$$ |$$   ____| $$  $$<   $$  $$<  
      $$ |$$ | \$$ |\$$$$$$$\ $$  /\$$\ $$  /\$$\ 
      \__|\__|  \__| \_______|\__/  \__|\__/  \__|
''',
'''
                .-') _   ('-.  ) (`-.     ) (`-.      
               ( OO ) )_(  OO)  ( OO ).    ( OO ).    
    .---.  ,--./ ,--,'(,------.(_/.  \_)-.(_/.  \_)-. 
   / .  |  |   \ |  |\ |  .---' \  `.'  /  \  `.'  /  
  / /|  |  |    \|  | )|  |      \     /\   \     /\  
 / / |  |_ |  .     |/(|  '--.    \   \ |    \   \ |  
/  '-'    ||  |\    |  |  .--'   .'    \_)  .'    \_) 
`----|  |-'|  | \   |  |  `---. /  .'.  \  /  .'.  \  
     `--'  `--'  `--'  `------''--'   '--''--'   '--'
''',
'''
                                                                                                    
                                                                                                    
       444444444  NNNNNNNN        NNNNNNNN                                                          
      4::::::::4  N:::::::N       N::::::N                                                          
     4:::::::::4  N::::::::N      N::::::N                                                          
    4::::44::::4  N:::::::::N     N::::::N                                                          
   4::::4 4::::4  N::::::::::N    N::::::N    eeeeeeeeeeee  xxxxxxx      xxxxxxxxxxxxxx      xxxxxxx
  4::::4  4::::4  N:::::::::::N   N::::::N  ee::::::::::::ee x:::::x    x:::::x  x:::::x    x:::::x 
 4::::4   4::::4  N:::::::N::::N  N::::::N e::::::eeeee:::::eex:::::x  x:::::x    x:::::x  x:::::x  
4::::444444::::444N::::::N N::::N N::::::Ne::::::e     e:::::e x:::::xx:::::x      x:::::xx:::::x   
4::::::::::::::::4N::::::N  N::::N:::::::Ne:::::::eeeee::::::e  x::::::::::x        x::::::::::x    
4444444444:::::444N::::::N   N:::::::::::Ne:::::::::::::::::e    x::::::::x          x::::::::x     
          4::::4  N::::::N    N::::::::::Ne::::::eeeeeeeeeee     x::::::::x          x::::::::x     
          4::::4  N::::::N     N:::::::::Ne:::::::e             x::::::::::x        x::::::::::x    
          4::::4  N::::::N      N::::::::Ne::::::::e           x:::::xx:::::x      x:::::xx:::::x   
        44::::::44N::::::N       N:::::::N e::::::::eeeeeeee  x:::::x  x:::::x    x:::::x  x:::::x  
        4::::::::4N::::::N        N::::::N  ee:::::::::::::e x:::::x    x:::::x  x:::::x    x:::::x 
        4444444444NNNNNNNN         NNNNNNN    eeeeeeeeeeeeeexxxxxxx      xxxxxxxxxxxxxx      xxxxxxx
''',
'''
  d8 8b  8                   
 dP8 8Ybm8 .d88b Yb dP Yb dP 
dPw8 8  "8 8.dP'  `8.   `8.  
   8 8   8 `Y88P dP Yb dP Yb
'''
]

escolher_titulo = random.choice(lista_ascii)
print(escolher_titulo)

while True:

    validar_email = 0
    validar_relacionamento = 0
    validar_reprocessamento = 0

    sleep(1)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # ESCOLHER SAUDACAO (POR HORARIO)
    horario = datetime.datetime.now().hour
    manha = -1 < horario < 12
    tarde = 11 < horario < 18
    noite = 18 < horario < 24
    if manha:
        saudacao = 'Bom dia'
    elif tarde:
        saudacao = 'Boa tarde'
    else:
        saudacao = 'Boa noite'

    # SELECIONAR PRÓXIMO MES - FATURAMENTO
    data_atual = datetime.datetime.now()
    proximo_mes = data_atual.month % 12 + 1
    ano = data_atual.year if proximo_mes > 1 else data_atual.year + 1
    data_proximo_mes = datetime.datetime(year=ano, month=proximo_mes, day=1)

    # Adiciona "SEXTOU!!" se for sexta-feira
    dia_semana = datetime.datetime.now().weekday()
    if dia_semana == 4:
        sextou = ' Silvano! \033[1;36mSextou!!!!\033[m'
    else:
        sextou = ' Silvano!'

    # MENU INICIAL
    print(f'''{saudacao} {sextou}

[1] Gerador de e-mails
[2] Templates de relacionamento
[3] Gerador de comentário
[4] WTCM
[5] Reprocessamento Stone
        ''')
    opcao_inicial = input('Digite a opção desejada: ')

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    # 1 -> GERADOR DE E-EMAILS
    if opcao_inicial == '1':
        while validar_email == 0:
            print('''
\033[1;36mGERADOR DE E-MAILS\033[m

[1] E-mail Pagseguro
[2] E-mail de aceite Projeto Vizzoo
[3] E-mail conclusão Alpha7
[S] Voltar
              ''')
            opcao_email = input('Digite a opção desejada: ')

            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

            # 1.1 -> E-MAIL PAGSEGURO
            if opcao_email == '1':
                print('\033[1;36mGERADOR DE E-MAIL PAGSEGURO\033[m')
                sleep(1)
                razao_social = input('Insira a razão social: ')
                cnpj = input('Insira o CNPJ: ')
                id = input('Insira o DsName do cliente: ')
                caixa_postal = input('Insira o id caixa postal do cliente: ')
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print(f'''
Prezados, {saudacao}!

Referente aos DSNames desse cliente, segue abaixo:

Razão Social: {razao_social}
CNPJ: {cnpj}
ID: {id}

RET.ANT.{id}XXX.680.{caixa_postal}  
RET.FIN.{id}XXX.680.{caixa_postal}   
RET.TRA.{id}XXX.680.{caixa_postal}  ''')
                terminar = input('Digite enter para sair: ')
                validar_email = 1

            # 1.2 -> E-MAIL ACEITE VIZZOO
            elif opcao_email == '2':
                print('\033[1;36mGERADOR DE E-MAIL ACEITE - PROJETO VIZZOO\033[m')
                sleep(1)
                input('''
              _
             | |
             | |===( )   //////
             |_|   |||  | o o|
                    ||| ( c  )                  ____
                     ||| \= /                  ||   \_
                      ||||||                   ||     |
                      ||||||                ...||__/|-"
                      ||||||             __|________|__
                        |||             |______________|
                        |||             || ||      || ||
                        |||             || ||      || ||
------------------------|||-------------||-||------||-||-------
                        |__>            || ||      || ||

      \033[31mFoi mal, ainda estou desenvolvendo isso....\033[m

      ''')
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')

            elif opcao_email == '3':
                print('\033[1;36mGERADOR DE E-MAIL CONCLUSÃO - ALPHA7\033[m')
                sleep(1)
                razao_social = input('Insira a razão social: ')
                cnpj = input('Insira o CNPJ: ')
                relacionamentos_bancarios = input('Digite os relacionamentos bancários pendentes: ')
                caixa_postal = input('Insira a caixa postal do cliente: ')
                senha = input('Digite a senha do cliente: ')
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                print(f'''
Prezados, {saudacao}!

Notificamos a conclusão da implantação.

Cliente:
- Os relatórios de baixa, para a gestão de cartões estão OK, dependendo da Alpha7
parametrizar no seu sistema;
- Fica em aberto o(s) seguinte(s) relacionamento(s) bancário(s): {relacionamentos_bancarios}. Sugerimos verificar o andamento com o(s) gerente(s) bancário(s);
- O faturamento iniciará a partir do mês {proximo_mes:02}/{ano}, conforme proposta assinada, que
previa 90 dias ou a conclusão da implantação para início do faturamento mensal;
Alpha7:
- Caixa Postal: {caixa_postal}
- Senha: {senha}
- CNPJ: {cnpj}
- Relatórios entregues diariamente;
- Entrar em contato com cliente para parametrizar a integração dos RELATÓRIOS
de baixa;

Informamos que as pendências pontuadas e, inclusões de novas lojas, serão
tratadas pela equipe de implantacao.cartoes@nexxera.com ;

Nossa equipe de suporte estará disponível para qualquer problema que
identificarem nos processos já "em produção", a partir de {proximo_mes:02} de {2024} através dos
contatos: suporte@nexxera.com / (48) 2106-5656
Ficamos à disposição.           
                  ''')
                terminar = input('Digite enter para sair: ')
                validar_email = 1

            elif opcao_email.upper() == 'S':
                validar_email = 1

            else:
                print('\033[1;31mEssa opção não é valida\033[m')

    # 2 -> TEMPLATE DE RELACIONAMENTO
    elif opcao_inicial == '2':
        while validar_relacionamento == 0:
            print('''
\033[1;36mTEMPLATES DE RELACIONAMENTO\033[m

[1] Intervan | VALECARD X ACCESSTAGE
[2] Intervan | AEGEA X FINNET (REDECARD)
[S] Voltar
              ''')
            opcao_relacionamento = input('Digite a opção desejada: ')

            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

            if opcao_relacionamento == '1':
                print('\033[1;36mTEMPLATE VALECARD X ACCESSTAGE\033[m')
                sleep(1)
                cnpj = input('Digite o CNPJ do cliente: ')
                dsname = input('Informe o Dsname do cliente: ').upper()
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')

                print(f'''==== VALECARD.VALECARD (19798) ====

MÁSCARA ENTRADA BANCO:
ARQUIVO_CONCILIACAO_%y%m%d_{dsname}.txt

MÁSCARA SAÍDA BANCO:
REM.EXT.{cnpj}.230.%d%m%Y&C(5)

SCRIPT APÓS A RECEPÇÃO DO BANCO:
/home/skyline/scripts/inte_rvs/Judge /home/skyline/scripts/inte_rvs/judge.cfg ACCESSTAGE.OPERADORAS &F

ESTAÇÃO(BANCO):
14946''')

                continuar = input('Digite enter para continuar: ')
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')

                print(f'''
==== CAIXA ACCESSTAGE.OPERADORAS (34776) ====

MÁSCARA ENTRADA CLIENTE:
REM.EXT.{cnpj}.230

MÁSCARA SAÍDA CLIENTE:
{dsname}.V%d%m%y%H%M%S.TMP

SCRIPT P/ VALIDAÇÃO CLIENTE:
/home/skyline/scripts/todos/FromDos &F

SCRIPT ENVIO:
submit maxdelay=unlimited EXT-{dsname} process snode=$(ESTACAO)
step01 copy from (file=$(FORIGEM) pnode)
           to   (file=$(FDESTINO) disp=new snode)
step02 if (step01 eq 0) then
       run task snode sysopts="sub2acc $(FDESTINO) nexxera"
       eif
;


CAIXA POSTAL:
ACCESSTAGE.VALECARD-EXTRATO-67616128000155

NOME:
ACCESSTAGE - VALECARD - EXTRATO
      ''')
                terminar = input('Digite enter para sair: ')
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
                validar_relacionamento = 1

            elif opcao_relacionamento == '2':
                print('\033[1;36mTEMPLATE VALECARD X ACCESSTAGE\033[m')
                sleep(1)
                input('''
              _
             | |
             | |===( )   //////
             |_|   |||  | o o|
                    ||| ( c  )                  ____
                     ||| \= /                  ||   \_
                      ||||||                   ||     |
                      ||||||                ...||__/|-"
                      ||||||             __|________|__
                        |||             |______________|
                        |||             || ||      || ||
                        |||             || ||      || ||
------------------------|||-------------||-||------||-||-------
                        |__>            || ||      || ||

      \033[31mFoi mal, ainda estou desenvolvendo isso....\033[m

      ''')
                if os.name == 'nt':
                    os.system('cls')
                else:
                    os.system('clear')
            
            elif opcao_relacionamento.upper() == 'S':
                validar_relacionamento = 1

            else:
                print('\033[1;31mEssa opção não é valida\033[m')
            
    # 3 -> GERADOR DE COMENTÁRIO
    elif opcao_inicial == '3':
        input('''
              _
             | |
             | |===( )   //////
             |_|   |||  | o o|
                    ||| ( c  )                  ____
                     ||| \= /                  ||   \_
                      ||||||                   ||     |
                      ||||||                ...||__/|-"
                      ||||||             __|________|__
                        |||             |______________|
                        |||             || ||      || ||
                        |||             || ||      || ||
------------------------|||-------------||-||------||-||-------
                        |__>            || ||      || ||

      \033[31mFoi mal, ainda estou desenvolvendo isso....\033[m

      ''')
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    # 4 -> WTCM
    elif opcao_inicial == '4':
        input('''
              _
             | |
             | |===( )   //////
             |_|   |||  | o o|
                    ||| ( c  )                  ____
                     ||| \= /                  ||   \_
                      ||||||                   ||     |
                      ||||||                ...||__/|-"
                      ||||||             __|________|__
                        |||             |______________|
                        |||             || ||      || ||
                        |||             || ||      || ||
------------------------|||-------------||-||------||-||-------
                        |__>            || ||      || ||

      \033[31mFoi mal, ainda estou desenvolvendo isso....\033[m

      ''')
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    elif opcao_inicial == '5':
        while validar_reprocessamento == 0:
            print('''
\033[1;36mREPROCESSAMENTO - STONE\033[m
A Stone não realiza o reprocessamento de arquivos, mas disponiblizam um banco de dados para obtermos os retroativos.''')
            usuario = input('INSIRA SEU USUÁRIO DA DEMO: ').upper()
            nome_mapa = input('Insira um nome para o mapa (separe com "_"): ').upper()
            cnpj = input('Insira o CNPJ do cliente (apenas números): ')
            stone_code = input('Insira o Stone Code do cliente: ')
            caixa_postal = input('Insira o ID da caixa postal do cliente: ')
            dias_retroativos = input('Insira o número de dias retroativos: ')
            if os.name == 'nt':
                    os.system('cls')
            else:
                    os.system('clear')
            input('A partir de agora, você deve copiar os códigos completos informados na tela (enter para continuar).')    
            if os.name == 'nt':
                    os.system('cls')
            else:
                    os.system('clear')
            input(f'vi {nome_mapa}.ini')
            if os.name == 'nt':
                    os.system('cls')
            else:
                    os.system('clear')
            input(f'''[{nome_mapa}]
authorization0={cnpj};{stone_code};RET.EXT.{stone_code}.390.{caixa_postal}''')
            if os.name == 'nt':
                    os.system('cls')
            else:
                    os.system('clear')
            input(f'esc + :wq')
            if os.name == 'nt':
                    os.system('cls')
            else:
                    os.system('clear')
            input(f'''/home/skyline/scripts/stone/StoneGetFiles.sh.run ~/operacoes/DEMO.{usuario}/mailbox/{nome_mapa}.ini -r {dias_retroativos}
''')
            if os.name == 'nt':
                    os.system('cls')
            else:
                    os.system('clear')
            input('cd ~/scripts/stone/python/reprocessamento')
            if os.name == 'nt':
                    os.system('cls')
            else:
                    os.system('clear')
            input(f'''for i in *RET.EXT.{stone_code}.390.{caixa_postal}* ; do mv -v $i /var/spool/nexxera/skyline/recebe/ident/$(basename $i | cut -f1 -d\$) ; sleep 1 ; done ''')
            validar_reprocessamento = 1
    else:   
        print('\033[31mEssa opção não é válida\033[m')
    
