# models.py

from django.db import models

class Formulario(models.Model):
    PLANETAS_ORIGEM_CHOICES = [
        ('Terra', 'Planeta Terra'),
        ('Namek', 'Planeta Namek'),
        ('Vegeta', 'Planeta Vegeta'),
        ('Outros', 'Outros')
    ]

    RACA_PREFERIDA_CHOICES = [
        ('Terráqueo', 'Terráqueo'),
        ('Sayajin', 'Sayajin'),
        ('Namekuseijin', 'Namekuseijin'),
        ('Androide', 'Androide'),
        ('Outros', 'Outros')
    ]

    TRABALHO_CHOICES = [
        ('Autonomo', 'Autonomo'),
        ('Empregado CLT', 'Empregado CLT'),
        ('Empresario', 'Empresario'),
        ('Tipo Goku', 'Tipo Goku')
    ]

    ACAI_CHOICES = [
        ('Puro', 'Puro'),
        ('Com Banana', 'Com Banana'),
        ('Com Morango', 'Com Morango'),
        ('Com Granola', 'Com Granola'),
        ('Tem gosto de Terra', 'Tem gosto de Terra')
    ]

    TAMANHO_CHOICES = [
        ('500ml', '500ml'),
        ('300ml', '300ml'),
        ('100ml', '100ml'),
        ('Casquinha', 'Casquinha'),
        ('Qual parte do gosto de terra voce nao entendeu?', 'Qual parte do gosto de terra voce nao entendeu?')
    ]

    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    planeta_origem = models.CharField(max_length=20, choices=PLANETAS_ORIGEM_CHOICES)
    raca_preferida = models.CharField(max_length=20, choices=RACA_PREFERIDA_CHOICES)
    trabalho = models.CharField(max_length=20, choices=TRABALHO_CHOICES)
    acai_preferido = models.CharField(max_length=20, choices=ACAI_CHOICES)
    tamanho_preferido = models.CharField(max_length=100, choices=TAMANHO_CHOICES)
    observacoes = models.TextField()


