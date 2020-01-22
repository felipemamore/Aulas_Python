class Squad:
    def __init__(self):
        self.id = 0
        self.Nome = ''
        self.Descricao= ''
        self.NumeroPessoas = 0
        self.BackEnd = ''
        self.Framework = ''
        
    def criar(self,Nome,Descricao,NumeroPessoas,BackEnd,Framework,id=0):
        self.id = id
        self.Nome = Nome
        self.Descricao = Descricao
        self.NumeroPessoas = NumeroPessoas
        self.BackEnd = BackEnd
        self.Framework = Framework

    def __str__(self):
        return f'{self.id};{self.Nome};{self.Descricao};{self.NumeroPessoas};{self.BackEnd};{self.Framework}'

squad = Squad()