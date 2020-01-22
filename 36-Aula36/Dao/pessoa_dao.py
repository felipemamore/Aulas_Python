import MySQLdb
from Model.pessoa import Pessoa

class PessoaDao:
<<<<<<< HEAD
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM pessoa AS P LEFT JOIN endereço AS E ON P.ENDEREÇO_ID = E.ID"
=======
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM 01_MDG_PESSOA AS P LEFT JOIN 01_MDG_ENDERECO AS E ON P.ENDERECO_ID = E.ID"
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
<<<<<<< HEAD
        comando = f"SELECT * FROM pessoa AS P LEFT JOIN endereço AS E ON P.ENDEREÇO_ID = E.ID WHERE P.ID = {id}"
=======
        comando = f"SELECT * FROM 01_MDG_PESSOA AS P LEFT JOIN 01_MDG_ENDERECO AS E ON P.ENDERECO_ID = E.ID WHERE P.ID = {id}"
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, pessoa:Pessoa):
<<<<<<< HEAD
        comando = f""" INSERT INTO pessoa
=======
        comando = f""" INSERT INTO 01_MDG_PESSOA
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        (
            NOME,
            SOBRENOME,
            IDADE,
<<<<<<< HEAD
            ENDEREÇO_ID
=======
            ENDERECO_ID
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        )
        VALUES
        (
            '{pessoa.nome}',
            '{pessoa.sobrenome}',
            {pessoa.idade},
            {pessoa.endereco.id}

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, pessoa:Pessoa):
<<<<<<< HEAD
        comando = f""" UPDATE pessoa
=======
        comando = f""" UPDATE 01_MDG_PESSOA
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        SET
            NOME = '{pessoa.nome}',
            SOBRENOME ='{pessoa.sobrenome}',
            IDADE = {pessoa.idade},
<<<<<<< HEAD
            ENDEREÇO_ID = {pessoa.endereco.id}
=======
            ENDERECO_ID = {pessoa.endereco.id}
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        WHERE ID = {pessoa.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
<<<<<<< HEAD
        comando = f"DELETE FROM pessoa WHERE ID = {id}"
=======
        comando = f"DELETE FROM 01_MDG_PESSOA WHERE ID = {id}"
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
        self.cursor.execute(comando)
        self.conexao.commit()