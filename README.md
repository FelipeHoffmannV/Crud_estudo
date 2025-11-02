
# CRUD de Usuários com Flask, SQLAlchemy e SQLite

Projeto profissional para gerenciamento de usuários utilizando **Flask** e **SQLAlchemy** com persistência em **SQLite**. Inclui interface web responsiva, rotas RESTful, testes automatizados e estrutura modular.

---

## Sumário

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Visão Geral

Este sistema CRUD permite cadastrar, listar, editar e remover usuários, armazenando os dados em banco SQLite via SQLAlchemy. O projeto segue boas práticas de organização, separando modelos, rotas, templates e scripts estáticos.

---

## Funcionalidades

- Adicionar novos usuários
- Listar usuários cadastrados
- Editar nome e e-mail de usuários
- Remover usuários
- Persistência de dados com SQLite
- Interface web responsiva (Bootstrap)
- Testes automatizados com Pytest

---

## Tecnologias

- Python 3.12+
- Flask
- Flask-SQLAlchemy
- Bootstrap 5
- Font Awesome
- Pytest

---

## Estrutura do Projeto

```
Crud_estudo/
│
├── app.py                  # Inicialização do Flask e registro de rotas
├── database/
│   ├── db.sqlite3          # Banco de dados SQLite
│   └── initdb.py           # Inicialização do banco
├── instance/
│   └── db.sqlite3          # Banco de dados (alternativo)
├── models/
│   └── user.py             # Modelo User
├── routes/
│   └── users_route.py      # Rotas de usuário
├── static/
│   └── javaScript.js       # Scripts JS para interação
├── templates/
│   └── index.html          # Página principal
├── tests/
│   └── test_user_crud.py   # Testes automatizados
├── README.md
└── LICENSE
```

---

## Instalação

1. Clone o repositório:

	```bash
	git clone https://github.com/SEU_USUARIO/crud-flask-usuarios.git
	cd crud-flask-usuarios
	```

2. Crie e ative um ambiente virtual:

	```bash
	python -m venv venv
	venv\Scripts\activate      # Windows
	# ou
	source venv/bin/activate   # Linux/Mac
	```

3. Instale as dependências:

	```bash
	pip install flask flask_sqlalchemy pytest
	```

---

## Uso

1. Execute o servidor Flask:

	```bash
	python app.py
	```

2. Acesse a aplicação em:

	[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Testes

Para rodar os testes automatizados:

```bash
pytest -s -v
```

Os testes cobrem as principais operações do CRUD e exibem mensagens de progresso.

---

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork este repositório
2. Crie uma branch com sua feature (`git checkout -b minha-feature`)
3. Commit suas alterações (`git commit -m 'Minha feature'`)
4. Faça o push para o GitHub (`git push origin minha-feature`)
5. Abra um Pull Request

---

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

Desenvolvido por Felipe Hoffmann
[LinkedIn](https://www.linkedin.com/in/felipe-hoffmann-viana-8898b6329/)

## 💡 Sobre o projeto

Este projeto tem fins educacionais e serve para praticar a lógica de back-end com Flask e persistência de dados com SQLite.

---

## 📜 Licença

Este projeto é livre para estudo, modificação e uso pessoal.

---

💻 Desenvolvido por Felipe Hoffmann
📬 [https://www.linkedin.com/in/felipe-hoffmann-viana-8898b6329/]
