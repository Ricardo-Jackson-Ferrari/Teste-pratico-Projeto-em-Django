from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='nome')
    last_name = models.CharField(max_length=100, verbose_name='sobrenome')
    age = models.PositiveSmallIntegerField(verbose_name='idade')
    birthday = models.DateField(verbose_name='data de nascimento')
    email = models.EmailField(max_length=255, verbose_name='e-mail')
    nickname = models.CharField(
        null=True, blank=True, max_length=100, verbose_name='apelido'
    )
    note = models.TextField(null=True, blank=True, verbose_name='observação')

    def get_full_name(self) -> str:
        full_name = (
            f'{self.first_name.title()} {self.last_name.title()}'.strip()
        )
        return full_name.strip()

    def __str__(self) -> str:
        return self.get_full_name()

    class Meta:
        verbose_name = 'Pessoa'
