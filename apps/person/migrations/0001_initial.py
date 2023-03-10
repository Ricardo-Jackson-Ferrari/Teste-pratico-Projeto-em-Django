# Generated by Django 4.1.4 on 2022-12-16 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'first_name',
                    models.CharField(max_length=100, verbose_name='nome'),
                ),
                (
                    'last_name',
                    models.CharField(max_length=100, verbose_name='sobrenome'),
                ),
                ('age', models.SmallIntegerField(verbose_name='idade')),
                (
                    'birthday',
                    models.DateField(verbose_name='data de nascimento'),
                ),
                (
                    'email',
                    models.EmailField(max_length=255, verbose_name='e-mail'),
                ),
                (
                    'nickname',
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name='apelido',
                    ),
                ),
                (
                    'note',
                    models.TextField(
                        blank=True, null=True, verbose_name='observação'
                    ),
                ),
            ],
            options={
                'verbose_name': 'Pessoa',
            },
        ),
    ]
