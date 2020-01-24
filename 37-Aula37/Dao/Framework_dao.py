import MySQLdb
from Model.Framework import FrameWork

class FrameworkDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM **Framework"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM Framework**  WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, framework:FrameWork):
        comando = f""" INSERT INTO framework
        (
            Nome
            
        )
        VALUES
        (
            '{framework.Nome}'
            

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, framework:Framework):
        comando = f""" UPDATE framework**
        SET
            Nome = '{framework.Nome}',
           
        WHERE ID = {framework.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM framework** WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()