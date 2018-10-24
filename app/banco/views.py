from django.shortcuts import render, redirect
from django.views.generic import CreateView, View, ListView, DetailView
from .models import Matter, Question, Test
from django.urls import reverse_lazy

class Home(View):
	def get(self, request):
		return render(request, 'base.html')

class CadastrarDisciplina(CreateView):
	model = Matter
	success_url = reverse_lazy('banco:home')
	template_name = 'banco/add-disciplina.html'
	fields = ['teacher', 'name']

class CadastrarQuestao(CreateView):
	model = Question
	success_url = reverse_lazy('banco:home')
	template_name = 'banco/add-questao.html'
	fields = ['teacher' ,'matter', 'statement', 'alternative_one', 'alternative_two', 'alternative_three', 'alternative_four', 'correct_alternative']

class CriarProva(CreateView):
	model = Test
	success_url = reverse_lazy('banco:home')
	template_name = 'banco/criar-prova.html'
	fields = ['teacher', 'matter']

class ListarDisciplinas(ListView):
	model = Matter
	template_name = 'banco/listar-disciplinas.html'

	def get_context_data(self, **kwargs):
		kwargs['disciplinas'] = Matter.objects.filter(teacher = self.request.user)
		return super(ListarDisciplinas, self,).get_context_data(**kwargs)

class ListarQuestoes(ListView):
	model = Question
	template_name = 'banco/listar-questoes.html'

	def get_context_data(self, **kwargs):
		kwargs['questoes'] = Question.objects.filter(teacher = self.request.user)
		return super(ListarQuestoes, self).get_context_data(**kwargs)

class DetalhesQuestao(DetailView):
	model = Question
	template_name = 'banco/detalhes-questao.html'