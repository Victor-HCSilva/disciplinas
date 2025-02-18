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
    segunda = models.BooleanField(default=False)
    terca = models.BooleanField(default=False)
    quarta = models.BooleanField(default=False)
    sexta = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)
    domingo = models.BooleanField(default=False)
    turno = models.CharField(max_length=10, choices=[
                ('MANHA', 'MANHA'),
                ('TARDE', 'TARDE'),
                ('NOITE', 'NOITE'),
            ], blank=False)

    def __str__(self):
        return self.nome


class Analise(models.Model):
    ch_total = models.IntegerField(default=2400)
    ch_optativa = models.IntegerField(default=200)
    ch_obrigratoria = models.IntegerField(default=1200)
    ch_concluida = models.IntegerField(default=0)
