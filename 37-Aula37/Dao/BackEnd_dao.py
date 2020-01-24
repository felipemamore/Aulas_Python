import MySQLdb
from Model.BackEnd import BackEnd

class BackEndDao:
    conexao = MySQLdb.connect(host='localhost', database='aulabd', user='root', passwd='')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM **BackEnd"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM BackEnd**  WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, framework:FrameWork):
        comando = f""" INSERT INTO backend**
        (
            Nome
            
        )
        VALUES
        (
            '{backend.Nome}'
            

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, backend:Backend):
        comando = f""" UPDATE backend**
        SET
            Nome = '{backend.Nome}',
           
        WHERE ID = {backend.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM backend** WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()