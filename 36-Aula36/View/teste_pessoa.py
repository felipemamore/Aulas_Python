import sys
<<<<<<< HEAD
sys.path.append('/Felipe/15-01-19/AulasPython/36-Aula36')
=======
sys.path.append('/Users/mdgranemann/Documents/Github/AlunosPython/TrabalhosPython/36-Aula36')
>>>>>>> 610437df3e0dc623c762d4abffbaddd99a72576c
from Controller.pessoa_controller import PessoaController
from Model.pessoa import Pessoa

pessoa = Pessoa()
pessoa.nome = 'Draeta1'
pessoa.sobrenome = 'Lindao'
pessoa.idade = 49
pessoa.endereco.logradouro = 'Rua dos Pombos1'
pessoa.endereco.numero = '0'
pessoa.endereco.complemento = 'casa muito engraçada'
pessoa.endereco.bairro = 'sem nome'
pessoa.endereco.cidade = 'gaspar'
pessoa.endereco.cep = '11111-000'

controller = PessoaController()
#id_salvo = controller.salvar(pessoa)
#pessoa_endereco = controller.buscar_por_id(id_salvo)
#print(pessoa_endereco)
print(controller.buscar_por_id(1))