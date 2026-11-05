import sqlite3

conexao = sqlite3.connect("oficina.db")
conexao.execute("PRAGMA foreign_keys = ON")
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()


cursor.execute ('''    
    CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT,
    telefone TEXT
    )
    ''');

cursor.execute ('''    
    CREATE TABLE IF NOT EXISTS veiculos(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    veiculo TEXT,
    ano INTEGER,
    placa TEXT,
    cliente_id INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
    )
    ''');

conexao.commit()

def cadastrar_cliente(nome, telefone):    
    cursor.execute('''
        INSERT INTO clientes (nome, telefone)
        VALUES (?, ?)        
        ''', (nome, telefone)
        );
    
    conexao.commit()

    id_cliente = cursor.lastrowid
    return id_cliente

def cadastrar_veiculo(veiculo, ano, placa,id_cliente):
    cursor.execute ('''
        INSERT INTO veiculos (veiculo, ano, placa, cliente_id)
        VALUES (?,?,?,?)
        ''', (veiculo, ano, placa, id_cliente)
        );

    conexao.commit()

def encontrar_cliente():
    cursor.execute('''
        SELECT * FROM clientes''')
    lista_clientes = cursor.fetchall()
    return lista_clientes

def encontrar_veiculo(id_cliente):
    cursor.execute('''
        SELECT * FROM veiculos
        WHERE cliente_id = ?
        ''', (id_cliente,)
        );
    lista_veiculos = cursor.fetchall()
    return lista_veiculos

def alterar_nome(novo_nome, id_cliente):
    cursor.execute('''
        UPDATE clientes
        SET nome = ?
        WHERE id = ?
        ''',(novo_nome, id_cliente)
        );

    conexao.commit()

def alterar_tel(novo_telefone, id_cliente):
    cursor.execute('''
        UPDATE clientes
        SET telefone = ?
        WHERE id = ?
        ''',(novo_telefone, id_cliente)
        );

    conexao.commit()

def alterar_veiculo(novo_veiculo, id_cliente):
    cursor.execute('''
        UPDATE veiculos
        SET veiculo = ?
        WHERE id = ?
        ''',(novo_veiculo, id_cliente)
        );

    conexao.commit()

def alterar_ano(novo_ano, id_cliente):
    cursor.execute('''
        UPDATE veiculos
        SET ano = ?
        WHERE id = ?
        ''',(novo_ano, id_cliente)
        );

    conexao.commit()

def alterar_placa(novo_placa, id_cliente):
    cursor.execute('''
        UPDATE veiculos
        SET placa = ?
        WHERE id = ?
        ''',(novo_placa, id_cliente)
        );

    conexao.commit()

def deletar_cliente (id_cliente):
    cursor.execute('''
    DELETE FROM clientes
    WHERE id = ?
    ''', (id_cliente,)
    );

    conexao.commit()

def deletar_carro (id_veiculo):
    cursor.execute('''
    DELETE FROM veiculos
    WHERE id = ?
    
    ''',(id_veiculo,)
    );
    conexao.commit()

def encerrar():
    conexao.close()
