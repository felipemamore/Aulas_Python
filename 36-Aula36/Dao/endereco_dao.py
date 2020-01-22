import MySQLdb
from Model.endereco import Endereco

class EnderecoDao:
<<<<<<< HEAD
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM endereço"
=======
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM 01_MDG_ENDERECO"
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
<<<<<<< HEAD
        comando = f"SELECT * FROM endereço WHERE ID = {id}"
=======
        comando = f"SELECT * FROM 01_MDG_ENDERECO WHERE ID = {id}"
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, endereco:Endereco):
<<<<<<< HEAD
        comando = f""" INSERT INTO endereço
=======
        comando = f""" INSERT INTO 01_MDG_ENDERECO
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        (
            LOGRADOURO,
            NUMERO,
            COMPLEMENTO,
            BAIRRO,
            CIDADE,
            CEP
        )
        VALUES
        (
            '{endereco.logradouro}',
            '{endereco.numero}',
            '{endereco.complemento}',
            '{endereco.bairro}',
            '{endereco.cidade}',
            '{endereco.cep}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, endereco:Endereco):
<<<<<<< HEAD
        comando = f""" UPDATE endereço
=======
        comando = f""" UPDATE 01_MDG_ENDERECO
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        SET
            LOGRADOURO = '{endereco.logradouro}',
            NUMERO = '{endereco.numero}',
            COMPLEMENTO = '{endereco.complemento}',
            BAIRRO = '{endereco.bairro}',
            CIDADE = '{endereco.cidade}',
            CEP = '{endereco.cep}'
        WHERE ID = {endereco.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
<<<<<<< HEAD
        comando = f"DELETE FROM endereço WHERE ID = {id}"
=======
        comando = f"DELETE FROM 01_MDG_ENDERECO WHERE ID = {id}"
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        self.cursor.execute(comando)
        self.conexao.commit()