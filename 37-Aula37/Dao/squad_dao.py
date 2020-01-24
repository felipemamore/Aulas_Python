import MySQLdb
from Model.squad import Squad

class SquadDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM squad"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM squad  WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, squad:Squad):
        comando = f""" INSERT INTO squad
        (
            Nome,
            Descricao,
            NumeroPessoas,
            BackEnd,
            FrameWork
        )
        VALUES
        (
            '{squad.Nome}',
            '{squad.Descricao}',
            {squad.NumeroPessoas},
            '{squad.BackEnd}',
            '{squad.FrameWork}'

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squad:Squad):
        comando = f""" UPDATE squad
        SET
            Nome = '{squad.Nome}',
            Descricao ='{squad.Descricao}',
            NumeroPessoas = {squad.NumeroPessoas},
            BackEnd = {squad.BackEnd}
            Framework = {squad.FrameWork}
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM squad WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()