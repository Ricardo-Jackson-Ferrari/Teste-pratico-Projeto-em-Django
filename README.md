<p align="center">
  <a href="https://www.djangoproject.com" target="blank"><img src="https://code.djangoproject.com/raw-attachment/ticket/24953/django-hexbin.png" width="200" alt="Django Logo" /></a>
</p>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como executar</a>
</p>


<hr>

<a id="-tecnologias"></a>

## Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

<hr>

<a id="-projeto"></a>

## 💻 Projeto

O projeto a seguir é referente a um teste prático. 

Esclarecimentos:
- A escolha de usar CBV(Class-Based Views) para esse projeto foi devido a rápida implementação e ganho no momento de testar.
- A escolha do SQLite foi motivada pela baixa dependência no caso de teste da aplicação.
- No que se refere aos requisitos poucas coisas estão diferentes, entre elas: Email como campo único, funcionalidade de exclusão de pessoa e cobertura de testes.


<p align="center">
  <img alt="Adicionar pessoa" src=".github/media/adicionar_pessoa.jpg" width="100%">
</p>

<p align="center">
  <img alt="Listar pessoas" src=".github/media/listar_pessoas.jpg" width="100%">
</p>

<p align="center">
  <img alt="Atualizar pessoa" src=".github/media/atualizar_pessoa.jpg" width="100%">
</p>

<p align="center">
  <img alt="Confirmar remoção de pessoa" src=".github/media/confirmacao_deletar_pessoa.jpg" width="100%">
</p>

<p align="center">
  <img alt="Deletar pessoa" src=".github/media/deletar_pessoa.jpg" width="100%">
</p>

<p align="center">
  <img alt="Admin Django" src=".github/media/admin_django.jpg" width="100%">
</p>

<p align="center">
  <img alt="Cobertura de teste" src=".github/media/cobertura_de_teste.jpg" width="100%">
</p>

<a id="-como-executar"></a>

## 🚀 Como executar

### 💻 Pré-requisitos
 **Antes de começar, verifique se você atendeu aos seguintes requisitos:**

- Você tem uma máquina `< Windows / Linux / Mac >`.

- Você tem python na versão 3.11 ou superior instalado em sua máquina.

- clone ou baixe o repositório.

## Com o ambiente virtual ativo:

### Como instalar localmente (Sem dependências de desenvolvimento):

- Acesse a pasta do projeto no terminal execute:

```console
cd app
cp env .env
pip install -r requirements.txt
poetry install
```

### Como instalar localmente (Com dependências de desenvolvimento):

```console
cd app
cp env .env
pip install -r requirements-dev.txt
poetry install
```

**OBS. Não se esqueça de alterar o arquivo .env que foi gerado a partida da cópia de exemplo "env" que vem na raíz do projeto.**


### A aplicação já vem com um super usuário para acessar a parte administrativa do django 
```
  Usuário: admin
  Senha: 123456
```

## 👨‍💻 Ativando a aplicação
Para executar o servidor localmente (Com o ambiente virtual ativo):

```console
python manage.py runserver
```

Agora é possível acessar a aplicação em http://localhost:8000/

E o painel administrativo em http://localhost:8000/admin

## 👨‍💻 Caso queira executar os testes basta ter instalado as dependências de desenvolvimento e executar:

```console
coverage run -m pytest
coverage html
python -m http.server 9000 --directory htmlcov
```

Agora é possível acessar a cobertura de testes em http://localhost:9000/