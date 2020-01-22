import sys
<<<<<<< HEAD
sys.path.append('/Felipe/15-01-19/AulasPython/36-Aula36')
=======
sys.path.append('/Users/mdgranemann/Documents/Github/AlunosPython/TrabalhosPython/36-Aula36')
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
from Controller.endereco_controller import EnderecoController
from Model.endereco import Endereco

end = Endereco()
end.logradouro = 'Rua dos Pombos123'
end.numero = '0'
end.complemento = 'casa muito engraçada'
end.bairro = 'sem nome'
end.cidade = 'gaspar'
end.cep = '11111-000'
end.id = 123

contr=  EnderecoController()
id_salvo = contr.salvar(end)
print(contr.buscar_por_id(id_salvo))