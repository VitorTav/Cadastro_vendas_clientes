import sqlite3

# Conectar ao banco de dados (ou criar um novo banco de dados)
conn = sqlite3.connect('sistema_vendas_contatos.db')
cursor = conn.cursor()

# Criar a tabela de contatos
cursor.execute('''
CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT,
    telefone TEXT
)
''')

# Criar a tabela de vendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY,
    contato_id INTEGER,
    data TEXT,
    produto TEXT,
    quantidade INTEGER,
    preco REAL,
    FOREIGN KEY (contato_id) REFERENCES contatos (id)
)
''')

# Função para inserir um novo contato
def inserir_contato(nome, email, telefone):
    cursor.execute('''
    INSERT INTO contatos (nome, email, telefone)
    VALUES (?, ?, ?)
    ''', (nome, email, telefone))
    conn.commit()

# Função para inserir uma nova venda
def inserir_venda(contato_id, data, produto, quantidade, preco):
    cursor.execute('''
    INSERT INTO vendas (contato_id, data, produto, quantidade, preco)
    VALUES (?, ?, ?, ?, ?)
    ''', (contato_id, data, produto, quantidade, preco))
    conn.commit()

# Função para exibir todos os contatos
def exibir_todos_os_contatos():
    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()
    for contato in contatos:
        print(contato)

# Função para exibir todas as vendas
def exibir_todas_as_vendas():
    cursor.execute('SELECT * FROM vendas')
    vendas = cursor.fetchall()
    for venda in vendas:
        print(venda)

# Função para exibir vendas por contato
def exibir_vendas_por_contato(contato_id):
    cursor.execute('''
    SELECT * FROM vendas
    WHERE contato_id = ?
    ''', (contato_id,))
    vendas = cursor.fetchall()
    for venda in vendas:
        print(venda)

# Função para calcular o total de vendas por produto
def total_vendas_por_produto():
    cursor.execute('''
    SELECT produto, SUM(quantidade * preco) as total
    FROM vendas
    GROUP BY produto
    ''')
    total_vendas = cursor.fetchall()
    for venda in total_vendas:
        print(f'Produto: {venda[0]}, Total Vendas: ${venda[1]:.2f}')

# Função para calcular o total de vendas por dia
def total_vendas_por_dia():
    cursor.execute('''
    SELECT data, SUM(quantidade * preco) as total
    FROM vendas
    GROUP BY data
    ''')
    total_vendas = cursor.fetchall()
    for venda in total_vendas:
        print(f'Data: {venda[0]}, Total Vendas: ${venda[1]:.2f}')

# Programa principal
def main():
    print("Sistema de Vendas e Contatos")
    while True:
        print("\nMenu:")
        print("1. Inserir novo contato")
        print("2. Inserir nova venda")
        print("3. Exibir todos os contatos")
        print("4. Exibir todas as vendas")
        print("5. Exibir vendas por contato")
        print("6. Total de vendas por produto")
        print("7. Total de vendas por dia")
        print("8. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            inserir_contato(nome, email, telefone)
        elif escolha == '2':
            contato_id = int(input("ID do contato: "))
            data = input("Data (YYYY-MM-DD): ")
            produto = input("Produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            inserir_venda(contato_id, data, produto, quantidade, preco)
        elif escolha == '3':
            exibir_todos_os_contatos()
        elif escolha == '4':
            exibir_todas_as_vendas()
        elif escolha == '5':
            contato_id = int(input("ID do contato: "))
            exibir_vendas_por_contato(contato_id)
        elif escolha == '6':
            total_vendas_por_produto()
        elif escolha == '7':
            total_vendas_por_dia()
        elif escolha == '8':
            break
        else:
            print("Opção inválida")

# Chamar a função principal
if __name__ == "__main__":
    main()

# Fechar a conexão com o banco de dados
conn.close()