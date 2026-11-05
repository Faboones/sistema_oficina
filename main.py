import os
import unicodedata
import banco

def mostrar_pessoas(pessoa):
    print (f'Nome: {pessoa["nome"]}')
    print (f'Telefone: {pessoa["telefone"]}')
    print ('.' * 30)

def mostrar_veiculos(veiculos):
    for automovel in veiculos:
        print (f'Veículo: {automovel["veiculo"]}')
        print (f'Ano: {automovel["ano"]}')
        print (f'Placa: {automovel["placa"]}')
        print ('.' * 30)

try:
    while True:
        menu = input (
        'Menu principal:\n'
        '1 - Cadastrar cliente.\n'
        '2 - Listar cliente.\n'
        '3 - Buscar cliente.\n'
        '4 - Deletar cliente.\n'
        '5 - Editar.\n'
        '6 - Sair.\n'
        'Escolha uma opção:\n'
        )

        os.system('cls')

        if menu == '1':
            nome = input ('Insira o nome do cliente:').strip().casefold()
            telefone = input ('Insira o telefone:').strip()
            veiculo = input ('Insira o modelo do veículo:').strip().casefold()
            ano = input ('Insira o ano:').strip()
            placa = input ('Insira a placa:').strip().casefold()

            if not nome or not veiculo:
                print ('Voce não inseriu uma informação válida.\n')

            else:
                id_cliente = banco.cadastrar_cliente(nome, telefone)

                banco.cadastrar_veiculo(veiculo, ano, placa, id_cliente)

                os.system('cls')

                print ('Cliente adicionado com sucesso.\n')
        
        elif menu == '2':
            print ('--- Clientes Cadastrados ---') 
            if not banco.encontrar_cliente():
                print ('Nenhum cliente cadastrado.\n')

            else:
                lista_clientes = banco.encontrar_cliente()
                for pessoa in lista_clientes:
                    mostrar_pessoas(pessoa)
                    lista_veiculos = banco.encontrar_veiculo(pessoa["id"])
                    mostrar_veiculos(lista_veiculos)
                    print ('-' * 30)

        elif menu == '3':
            if not banco.encontrar_cliente():
                print ('Nenhum cliente cadastrado.\n')
            else:
                lista_clientes = banco.encontrar_cliente()
                
                busca = input ('Digite o nome do cliente:\n').strip().casefold()

                os.system('cls')

                achoubus = False
                for pessoa in lista_clientes:
                    if pessoa['nome'].strip().casefold() == busca:
                        achoubus = True
                        mostrar_pessoas(pessoa)
                        lista_veiculos = banco.encontrar_veiculo(pessoa["id"])
                        mostrar_veiculos(lista_veiculos)
                        print ('-' * 30)

                if not achoubus:
                    print ('Pessoa não encontrada.\n')

        elif menu == '4':

            if not banco.encontrar_cliente():
                print ('Nenhum cliente cadastrado.\n')

            else:
                lista_clientes = banco.encontrar_cliente()
                nome_apagar = input ('Digite o nome do cliente:\n').strip().casefold() 

                os.system('cls')

                achoudel = []
                for pessoa in lista_clientes:
                    if pessoa['nome'].strip().casefold() == nome_apagar:
                        lista_veiculos = banco.encontrar_veiculo(pessoa["id"])
                        achoudel.append(pessoa["id"])
                        print(f'Índice: {pessoa["id"]}')
                        print (f'Nome: {pessoa["nome"]}') 
                        for automovel in lista_veiculos:
                            print (f'Veículo: {automovel["veiculo"]}')
                            print (f'Placa: {automovel["placa"]}')
                            print ('-' * 30)

                if not achoudel:
                    print ('Cliente não encontrado.\n')

                else:
                    id_cliente = input ('Qual cliente deseja remover? [Use os índices como referência.]\n')        
                    if id_cliente.isdigit():
                        id_cliente = int(id_cliente)
                        if id_cliente in achoudel:
                            banco.deletar_cliente(id_cliente)

                            os.system('cls')

                            print ('Cliente removido.\n')
                        else:
                            print ('Voce não digitou uma opção correta.\n')
                    else:
                        print('Índice incorreto.\n')

        elif menu == '5':
            if not banco.encontrar_cliente():
                print ('Nenhum cliente cadastrado.\n')

            else:
                edit = input (
                'Oque deseja fazer?\n'
                '1 - Editar dados do cliente.\n'
                '2 - Adicionar veículo.\n'
                '3 - Deletar veículo.\n'
                )

                os.system('cls')

                if edit == '1':
                    editcli = input ('Qual o nome do cliente que desaja editar?\n').strip().casefold()
                    achoucli = []

                    if not editcli:
                        print ('Você não escolheu nenhum cliente.\n')

                    else:
                        lista_clientes = banco.encontrar_cliente()
                        for pessoa in lista_clientes:
                            if pessoa['nome'].strip().casefold() == editcli:
                                lista_veiculos = banco.encontrar_veiculo(pessoa["id"])
                                achoucli.append(pessoa["id"])
                                print(f'Índice: {pessoa["id"]}')
                                print (f'Nome: {pessoa["nome"]}') 
                                for automovel in lista_veiculos:
                                    print (f'Veículo: {automovel["veiculo"]}')
                                    print (f'Placa: {automovel["placa"]}')
                                    print ('-' * 30)

                        if not achoucli:
                            print ('Cliente não encontrado.\n')

                        else:
                            qual_pessoa_edit = input ('Qual o indice do cliente que deseja editar?\n')

                            os.system('cls')
                            
                            if qual_pessoa_edit.isdigit():
                                qual_pessoa_edit = int(qual_pessoa_edit)

                                if qual_pessoa_edit in achoucli:
                                    for pessoa in lista_clientes:
                                        if pessoa['id'] == qual_pessoa_edit:
                                            lista_veiculos = banco.encontrar_veiculo(pessoa["id"])
                                            mostrar_pessoas(pessoa)
                                            mostrar_veiculos(lista_veiculos)
                                            print('-' * 30)

                                            qual_campo_edit = input (
                                                'Qual campo deseja editar?\n' 
                                                '1 - Nome:\n'
                                                '2 - Telefone:\n'
                                                '3 - Veículo:\n' 
                                                )

                                            os.system('cls')

                                            if qual_campo_edit == '1':
                                                novo_nome = input ('Digite o novo nome:\n').strip().casefold()
                                                banco.alterar_nome(novo_nome, pessoa['id'])
                                                print ('Nome alterado com sucesso.\n')
                                                print ('-' * 30)

                                            elif qual_campo_edit == '2':
                                                novo_telefone = input ('Digite o novo telefone:\n')
                                                banco.alterar_tel(novo_telefone, pessoa['id'])
                                                print ('Telefone alterado com sucesso.\n')
                                                print ('-' * 30)

                                            elif qual_campo_edit == '3':
                                                lista_veiculos = banco.encontrar_veiculo(pessoa["id"])
                                                iveiculo = []
                                                for automovel in lista_veiculos:
                                                    iveiculo.append(automovel["id"])
                                                    print (f'Índice: {automovel["id"]}')
                                                    print (f'Veículo: {automovel["veiculo"]}')
                                                    print (f'Ano: {automovel["ano"]}')
                                                    print (f'Placa: {automovel["placa"]}')
                                                    print ('-' * 30)
                                                alt_veiculo = input ('Qual veiculo deseja alterar? [Use os índices como referência.]\n')

                                                if alt_veiculo.isdigit():
                                                    alt_veiculo = int(alt_veiculo)

                                                    if alt_veiculo in iveiculo:
                                                        for automovel in lista_veiculos:
                                                            if automovel['id'] == alt_veiculo:
                                                                novo_veiculo = input ('Qual o novo veiculo:\n').strip().casefold()
                                                                banco.alterar_veiculo(novo_veiculo, automovel['id'])
                                                                print ('Veiculo alterado com sucesso.\n')
                                                                print ('-' * 30)
                                                                novo_ano = input ('Qual o novo ano:\n')
                                                                banco.alterar_ano(novo_ano, automovel['id'])
                                                                print ('Ano alterado com sucesso.\n')
                                                                print ('-' * 30)
                                                                nova_placa = input ('Qual a nova placa:\n')
                                                                banco.alterar_placa(nova_placa, automovel['id'])
                                                                print ('Placa alterada com sucesso.\n')
                                                                print ('-' * 30)
                                                    else:
                                                        print ('Opção inválida.\n')  
                                                else:
                                                    print ('Opção inválida.\n')          
                                else:
                                    print ('Opção inválida.\n') 
                            else:
                                print ('Opção inválida.\n')                                  

                elif edit == '2':
                    lista_clientes = banco.encontrar_cliente()
                    ipessoa = input ('Digite o nome:\n').strip().casefold()
                    achouipessoa = []
                    for pessoa in lista_clientes:
                        if pessoa['nome'].strip().casefold() == ipessoa:
                            achouipessoa.append(pessoa["id"])
                            print(f'Índice: {pessoa["id"]}')
                            print (f'Nome: {pessoa["nome"]}')

                    if not achouipessoa:
                        print ('Cliente não encontrado.\n')
                        
                    else: 
                        adc_carro = input ('Qual o indice do cliente que deseja editar?\n')

                        os.system('cls')

                        if adc_carro.isdigit():
                            adc_carro = int(adc_carro)
                            if adc_carro in achouipessoa:
                                for pessoa in lista_clientes:
                                    if pessoa['id'] == adc_carro:

                                        novo_carro = input ('Digite o novo veiculo.\n')
                                        novo_ano = input ('Digite o novo ano.\n')
                                        nova_placa = input ('Digite a nova placa.\n')
                                    
                                        banco.cadastrar_veiculo(novo_carro, novo_ano, nova_placa, pessoa['id'])

                                        os.system('cls')

                                        print ('Carro adicionado.\n')
                            else:
                                print ('Opção inválida.')            
                        else:
                            print ('Opção inválida.')

                elif edit == '3':
                    lista_clientes = banco.encontrar_cliente()
                    ipessoa = input ('Digite o nome:\n').strip().casefold()
                    achouipessoa = []
                    for pessoa in lista_clientes:
                        if pessoa['nome'].strip().casefold() == ipessoa:
                            achouipessoa.append(pessoa["id"])
                            print(f'Índice: {pessoa["id"]}')
                            print (f'Nome: {pessoa["nome"]}')

                    if not achouipessoa:
                        print ('Cliente não encontrado.\n')

                    else: 
                        del_carro = input ('Qual o indice do cliente que deseja editar?\n')

                        os.system('cls')

                        if del_carro.isdigit():
                            del_carro = int(del_carro)
                                                     
                            if del_carro in achouipessoa:
                                for pessoa in lista_clientes:
                                    if pessoa['id'] == del_carro:
                                        lista_veiculos = banco.encontrar_veiculo(pessoa["id"])
                                        iveiculo = []
                                        for automovel in lista_veiculos:
                                            iveiculo.append(automovel["id"])
                                            print (f'Índice: {automovel["id"]}')
                                            print (f'Veículo: {automovel["veiculo"]}')
                                            print (f'Ano: {automovel["ano"]}')
                                            print (f'Placa: {automovel["placa"]}')
                                            print ('-' * 30)

                                        del_veiculo = input ('Qual veículo deseja deletar? [Use os índices como referência.]\n')

                                        os.system('cls')
                                        
                                        if del_veiculo.isdigit():
                                            del_veiculo = int(del_veiculo)
                                        
                                            if del_veiculo in iveiculo:
                                                for automovel in lista_veiculos:
                                                    if automovel['id'] == del_veiculo:
                                                        banco.deletar_carro(del_veiculo)
                                                        print ('Veículo deletado.')
                                            else:
                                                print ('Índice inválido.\n')
                                        else:
                                            print ('Índice inválido.\n')
                        else:
                            print ('Índice inválido.\n')
                  
        elif menu == '6':
            print ('Saindo...')
            break

        else:
            print ('Opção inválida.')

finally:
    banco.encerrar()
