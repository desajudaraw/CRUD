
import psycopg2

# Conectar ao banco de dados
conexão = psycopg2.connect(dbname="nome_do_seu_local",
                        user="seu_usuario",
                        password="sua_senha",
                        port="sua_porta",
                        host="localhost")

# Criar um cursor para executar comandos SQL
cursor = conexão.cursor()

#CREATE/CRIAR
Comando = 'INSERT INTO tb_cadastro (nome, cpf, email) VALUES (\'joão\', \'20309867821\', \'eugostodearroz@gamil.com\');'
cursor.execute(Comando)
conexão.commit()

#READ/LER
comando = 'select * from tb_cadastro;'
cursor.execute(comando)
resultado = cursor.fetchall()  # Chamando o método fetchall()
print(resultado)

#UPDATE/UPDATE

comando = f'UPDATE tb_cadastro SET nome = \'augusto\'  WHERE cpf = \'20309867821\''
cursor.execute(comando)
conexão.commit()


#DELETE/DELETAR

comando = f"DELETE FROM tb_cadastro WHERE nome = 'augusto'"
cursor.execute(comando)
conexão.commit()

# Fechar a conexão
cursor.close()
conexão.close()

