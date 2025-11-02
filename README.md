
# 🧩 CRUD Flask com SQLite

Este projeto é um CRUD de usuários desenvolvido com **Flask** e **SQLAlchemy**, utilizando **SQLite** como banco de dados. O objetivo é praticar os conceitos fundamentais de CRUD (Create, Read, Update, Delete) em Python com persistência real de dados.

---

## 🚀 Funcionalidades

<<<<<<< HEAD
- ✅ Adicionar novos usuários
- 📋 Listar usuários cadastrados
- ✏️ Editar nome e e-mail de um usuário
- 🗑️ Remover usuários
- 🗄️ Persistência de dados com SQLite
- 🧪 Testes automatizados com Pytest

---

## 🧱 Tecnologias utilizadas

- [Python 3.12+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Pytest](https://docs.pytest.org/en/latest/)

---

## 📂 Estrutura do projeto

```
Crud_estudo/
│
├── app.py                  # Arquivo principal do Flask
├── database/
│   ├── db.sqlite3          # Banco de dados SQLite
│   └── initdb.py           # Inicialização do banco
├── instance/
│   └── db.sqlite3          # Banco de dados (pasta instance)
├── models/
│   └── user.py             # Modelo User
├── routes/
│   └── users_route.py      # Rotas de usuário
├── static/
│   └── javaScript.js       # Scripts JS
├── templates/
│   └── index.html          # Página principal
├── tests/
│   └── test_user_crud.py   # Testes automatizados
=======
- Python 3.12
- Flask
- Bootstrap 5 (front-end)
- JavaScript (scripts de interação)
- Pytest (testes)

---

## 📂 Estrutura do repositório

Crud_estudo/
├── app.py                 # Aplicação Flask (rotas e lógica)
├── database/
│   └── fic_data.py        # "Banco de dados" em memória (listas/dicionários)
├── templates/
│   └── index.html         # Página principal
├── static/
│   └── javaScript.js      # Scripts do front-end
├── tests/
│   └── test_user_crud.py  # Testes automatizados com pytest
>>>>>>> 6197a6c50d9bcbd3d8457fe330061851128333d7
├── README.md
└── LICENSE
```

---

## ⚙️ Como rodar o projeto localmente

1️⃣ Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/crud-flask-usuarios.git
cd crud-flask-usuarios
```

2️⃣ Crie e ative um ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# ou
source venv/bin/activate   # Linux/Mac
```

3️⃣ Instale as dependências

```bash
pip install flask flask_sqlalchemy pytest
```

4️⃣ Rode o servidor Flask

```bash
python app.py
```

Acesse no navegador:
👉 http://127.0.0.1:5000/

---

## 🧪 Rodando os testes

Para rodar os testes automatizados:

```bash
pytest -s -v
```

---

## 💡 Sobre o projeto

Este projeto tem fins educacionais e serve para praticar a lógica de back-end com Flask e persistência de dados com SQLite.

---

## 📜 Licença

Este projeto é livre para estudo, modificação e uso pessoal.

---

💻 Desenvolvido por Felipe Hoffmann
📬 [https://www.linkedin.com/in/felipe-hoffmann-viana-8898b6329/]
