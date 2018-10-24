from django.urls import include, path
from django.conf.urls import include, url

from . import views as banco

app_name = 'banco'

urlpatterns = [
	path('', banco.Home.as_view(), name='home'),
	path('cadastrar/disciplina/', banco.CadastrarDisciplina.as_view(), name='cadastrar-disciplina'),
	path('cadastrar/questao/', banco.CadastrarQuestao.as_view(), name='cadastrar-questao'),
	path('criar/prova/', banco.CriarProva.as_view(), name='criar-prova'),
	path('listar/disciplinas/', banco.ListarDisciplinas.as_view(), name='listar-disciplinas'),
	path('listar/questoes/', banco.ListarQuestoes.as_view(), name='listar-questoes'),
	path('detalhes/<pk>', banco.DetalhesQuestao.as_view(), name='detalhes'),

]