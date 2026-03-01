from django.test import TestCase
from .models import Aluno
from django.urls import reverse


class AlunoModelTest(TestCase):

    def test_criar_aluno(self):
        aluno = Aluno.objects.create(
            nome="Teste",
            idade=20,
            email="teste@email.com"
        )

        self.assertEqual(aluno.nome, "Teste")
        self.assertTrue(aluno.matriculado)

class AlunoViewTest(TestCase):

    def test_lista_alunos_status(self):
        response = self.client.get('/alunos/')
        self.assertEqual(response.status_code, 200)