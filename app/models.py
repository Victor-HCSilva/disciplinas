from django.db import models

class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    carga_horaria = models.CharField(max_length=10, choices=[
        ('15h', '15h'),
                ('20h', '20h'),
                ('30h', '30h'),
                ('54h', '54h'),
                ('60h', '60h'),
                ('90h', '90h'),
            ], blank=False)
    professor = models.CharField(max_length=200)
    curso = models.CharField(max_length=10, choices=[('C&T', 'C&T')], blank=False)
    grupo = models.IntegerField(blank=False )
    dia_da_semana = models.CharField(max_length=10, choices=[
                ('segunda', 'Segunda-feira'),
                ('terca', 'Terça-feira'),
                ('quarta', 'Quarta-feira'),
                ('quinta', 'Quinta-feira'),
                ('sexta', 'Sexta-feira'),
                ('sabado', 'Sábado'),
                ('domingo', 'Domingo'),
            ], blank=False)
    
    turno = models.CharField(max_length=10, choices=[
                ('MANHA', 'MANHA'),
                ('TARDE', 'TARDE'),
                ('NOITE', 'NOITE'),
            ], blank=False)
    
    def __str__(self):
        return self.nome

