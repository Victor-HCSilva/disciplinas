from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=200)
    # Outros campos do professor

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    # Outros campos do curso
    
    def __str__(self):
        return self.nome

class NomeDisciplina(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class NomeLocal(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class CargaHoraria(models.Model):
    carga_horaria = models.CharField(max_length=10, blank=False)
    
    def __str__(self):
        return self.carga_horaria

class Codigo(models.Model):
    codigo = models.CharField(max_length=10, blank=False)
    
    def __str__(self):
        return self.codigo


class Disciplina(models.Model):
    nome = models.ForeignKey(NomeDisciplina, on_delete=models.CASCADE)
    codigo = models.ForeignKey(Codigo, on_delete=models.CASCADE)
    descricao = models.TextField(blank=True)
    carga_horaria = models.ForeignKey(CargaHoraria, on_delete=models.CASCADE)
    dia_da_semana = models.CharField(max_length=10, choices=[
                ('segunda', 'Segunda-feira'),
                ('terca', 'Terça-feira'),
                ('quarta', 'Quarta-feira'),
                ('quinta', 'Quinta-feira'),
                ('sexta', 'Sexta-feira'),
                ('sabado', 'Sábado'),
                ('domingo', 'Domingo'),
            ], blank=False)
    horario_inicio = models.CharField(max_length=10, choices=[
                ('Manha', 'Manha'),
                ('Tarde', 'Tarde'),
                ('Noite', 'Noite'),
            ], blank=False)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    grupo = models.IntegerField(blank=False )
    
    def __str__(self):
        return self.nome.nome

