import os

clientes = []

def mostrar_pessoas(pessoa):
    print (f'Nome: {pessoa["nome"]}')
    print (f'Telefone: {pessoa["telefone"]}')

def mostrar_veiculos(veiculos):
    for automovel in veiculos:
        print (f'Veículo: {automovel["veiculo"]}')
        print (f'Ano: {automovel["ano"]}')
        print (f'Placa: {automovel["placa"]}')

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
        veiculos = []
        nome = input ('Insira o nome do cliente:')
        telefone = input ('Insira o telefone:')
        veiculo = input ('Insira o modelo do veículo:')
        ano = input ('Insira o ano:')
        placa = input ('Insira a placa:')

        if not nome or not veiculo:
            print ('Voce não inseriu uma informação válida.\n')

        else:
            cliente = {
                'nome': nome,
                'telefone': telefone,
                'veiculos': veiculos,
                }
            clientes.append(cliente)

            carros = {
                'veiculo': veiculo,
                'ano': ano,
                'placa': placa,
            }
            veiculos.append(carros)

            os.system('cls')

            print ('Cliente adicionado com sucesso.\n')
      
    elif menu == '2':
        print ('--- Clientes Cadastrados ---') 
        if not clientes:
            print ('Nenhum cliente cadastrado.\n')

        else:
            for pessoa in clientes:
                mostrar_pessoas(pessoa)
                mostrar_veiculos(pessoa['veiculos'])
                print ('-' * 30)

    elif menu == '3':
        if not clientes:
            print ('Nenhum cliente cadastrado.')
        else:
            busca = input ('Digite o nome do cliente:\n')

            os.system('cls')

            achoubus = False
            for pessoa in clientes:
                if pessoa['nome'] == busca:
                    achoubus = True
                    mostrar_pessoas(pessoa)
                    mostrar_veiculos(pessoa['veiculos'])
                    print ('-' * 30)

            if not achoubus:
                print ('Pessoa não encontrada.\n')

    elif menu == '4':

        if not clientes:
            print ('Nenhum cliente cadastrado.\n')

        else:
            nome_apagar = input ('Digite o nome do cliente:\n') 
            achoudel = []
            for i, pessoa in enumerate(clientes):
                if pessoa['nome'] == nome_apagar:
                    achoudel.append(i)
                    print(f'Índice: {i}')
                    print (f'Nome: {pessoa["nome"]}') 
                    for automovel in pessoa['veiculos']:
                        print (f'Veículo: {automovel["veiculo"]}')
                        print (f'Placa: {automovel["placa"]}')
                        print ('-' * 30)

            if not achoudel:
                print ('Cliente não encontrado.\n')

            else:
                deletar = input ('Qual cliente deseja remover? [Use os índices como referência.]\n')        
                if deletar.isdigit():
                    deletar = int(deletar)
                    if deletar in achoudel:
                        clientes.pop(deletar)
                        print ('Cliente removido.\n')
                    else:
                        print ('Voce não digitou uma opção correta.\n')
                else:
                    print('Índice incorreto.\n')

    elif menu == '5':
        if not clientes:
            print ('Nenhum cliente cadastrado.\n')

        else:
            edit = input (
            'Oque deseja fazer?\n'
            '1 - Editar dados do cliente.\n'
            '2 - Adicionar veiculo.\n'
            )

            os.system('cls')

            if edit == '1':
                editcli = input ('Qual o nome do cliente que desaja editar?\n')
                achoucli = []

                if not editcli:
                    print ('Você não escolheu nenhum cliente.\n')

                else:
                    for i, pessoa in enumerate(clientes):
                        if pessoa['nome'] == editcli:
                            achoucli.append(i)
                            print(f'Índice: {i}')
                            print (f'Nome: {pessoa["nome"]}') 
                            for automovel in pessoa['veiculos']:
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
                                pessoa = clientes[qual_pessoa_edit]
                                mostrar_pessoas(pessoa)
                                mostrar_veiculos(pessoa['veiculos'])
                                print('-' * 30)

                                qual_campo_edit = input (
                                    'Qual campo deseja editar?\n' 
                                    '1 - Nome:\n'
                                    '2 - Telefone:\n'
                                    '3 - Veículo:\n' 
                                    )

                                os.system('cls')

                                if qual_campo_edit == '1':
                                    novo_nome = input ('Digite o novo nome:\n')
                                    pessoa['nome'] = novo_nome
                                    print ('Nome alterado com sucesso.\n')
                                    print ('-' * 30)

                                elif qual_campo_edit == '2':
                                    novo_telefone = input ('Digite o novo telefone:\n')
                                    pessoa['telefone'] = novo_telefone
                                    print ('Telefone alterado com sucesso.\n')
                                    print ('-' * 30)

                                elif qual_campo_edit == '3':
                                    iveiculo = [] 
                                    for i, automovel in enumerate(pessoa['veiculos']):
                                        iveiculo.append(i)
                                        print (f'Índice: {i}')
                                        print (f'Veículo: {automovel["veiculo"]}')
                                        print (f'Ano: {automovel["ano"]}')
                                        print (f'Placa: {automovel["placa"]}')
                                        print ('-' * 30)
                                    alt_veiculo = input ('Qual veiculo deseja alterar? [Use os índices como referência.]\n')

                                    if alt_veiculo.isdigit():
                                        alt_veiculo = int(alt_veiculo)
                                        if alt_veiculo in iveiculo:
                                            novo_vei = input ('Qual o novo veiculo:\n')
                                            pessoa['veiculos'][alt_veiculo]['veiculo'] = novo_vei
                                            print ('Veiculo alterado com sucesso.\n')
                                            print ('-' * 30)
                                            novo_ano = input ('Qual o novo ano:\n')
                                            pessoa['veiculos'][alt_veiculo]['ano'] = novo_ano
                                            print ('Ano alterado com sucesso.\n')
                                            print ('-' * 30)
                                            nova_placa = input ('Qual a nova placa:\n')
                                            pessoa['veiculos'][alt_veiculo]['placa'] = nova_placa
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
                ipessoa = input ('Digite o nome:\n')
                achouipessoa = []
                for i, pessoa in enumerate(clientes):
                    if pessoa['nome'] == ipessoa:
                        achouipessoa.append(i)
                        print(f'Índice: {i}')
                        print (f'Nome: {pessoa["nome"]}')

                if not achouipessoa:
                    print ('Cliente não encontrado.\n')
                else: 

                    adc_carro = input ('Qual o indice do cliente que deseja editar?\n')

                    os.system('cls')

                    if adc_carro.isdigit():
                        adc_carro = int(adc_carro)
                        if adc_carro in achouipessoa:
                            pessoa = clientes[adc_carro]
                            print (f'Nome: {pessoa["nome"]}')

                            novo_carro = input ('Digite o novo veiculo.\n')
                            novo_ano = input ('Digite o novo ano.\n')
                            nova_placa = input ('Digite a nova placa.\n')
                            novo_veiculo = {
                                'veiculo': novo_carro,
                                'ano': novo_ano,
                                'placa': nova_placa,
                            }
                            pessoa['veiculos'].append(novo_veiculo)
                            print ('Carro adicionado.\n')
                        else:
                            print ('Índice inválido.\n')
                    else:
                        print ('Índice inválido.\n')
                
    elif menu == '6':
        print ('Saindo...')
        break
