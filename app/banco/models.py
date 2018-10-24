from django.db import models
from app.core.models import UUIDUser, CreateUpdateModel

class Matter(CreateUpdateModel):
	name = models.CharField(max_length = 255, verbose_name = 'nome')
	teacher = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'teachers', verbose_name = 'professor')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'professor'
		verbose_name_plural = 'professores'

class Question(CreateUpdateModel):
	teacher = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'users', verbose_name = 'professor')
	matter = models.ForeignKey(Matter, on_delete = models.CASCADE, related_name = 'matters', verbose_name = 'materia')
	statement = models.TextField(verbose_name = 'enunciado')
	image = models.ImageField(upload_to = 'images/', verbose_name = 'imagem', blank = True, null = True)
	alternative_one = models.CharField(max_length = 255, verbose_name = 'alternativa 1')
	alternative_two = models.CharField(max_length = 255, verbose_name = 'alternativa 2')
	alternative_three = models.CharField(max_length = 255, verbose_name = 'alternativa 3')
	alternative_four = models.CharField(max_length = 255, verbose_name = 'alternativa 4')
	correct_alternative = models.CharField(max_length = 255, verbose_name = 'alternativa correta')

	def __str__(self):
		return self.statement

	class Meta:
		verbose_name = 'questao'
		verbose_name_plural = 'questoes'

class Test(CreateUpdateModel):
	teacher = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, related_name = 'teach', verbose_name = 'professor')
	matter = models.ForeignKey(Matter, on_delete = models.CASCADE, related_name = 'matte', verbose_name = 'materia')
	questions = models.ManyToManyField(Question, related_name = 'questions', verbose_name = 'questoes')

	def __str__(self):
		return 'Prova da disciplina: ' + self.teacher.first_name

	class Meta:
		verbose_name = 'prova'
		verbose_name_plural = 'provas' 

