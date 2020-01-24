class Squad:
    def __init__(self):
        self.id = 0
        self.Nome = ''
        self.Descricao= ''
        self.NumeroPessoas = 0
        self.BackEnd = ''
        self.FrameWork = ''
        
    def criar(self,Nome,Descricao,NumeroPessoas,BackEnd,FrameWork,id=0):
        self.id = id
        self.Nome = Nome
        self.Descricao = Descricao
        self.NumeroPessoas = NumeroPessoas
        self.BackEnd = BackEnd
        self.FrameWork = FrameWork
        print('\n**'*10,self.__str__())

    def __str__(self):
        return f'{self.id};{self.Nome};{self.Descricao};{self.NumeroPessoas};{self.BackEnd};{self.FrameWork}'

squad = Squad()