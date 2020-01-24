import MySQLdb
from Model.SGBD import SGBD

class SGBDDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM **SGBD"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM SGBD**  WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, sgbd:SGBD):
        comando = f""" INSERT INTO backend**
        (
            Nome
            
        )
        VALUES
        (
            '{sgbd.Nome}'
            

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, sgbd:SGBD):
        comando = f""" UPDATE backend**
        SET
            Nome = '{sgbd.Nome}',
           
        WHERE ID = {sgbd.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM sgbd** WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()