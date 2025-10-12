# 🧩 CRUD Flask - Banco de Dados Fictício  

Este projeto foi desenvolvido com o objetivo de **praticar os conceitos fundamentais de CRUD (Create, Read, Update, Delete)** usando o **framework Flask** em Python.  

O sistema permite **cadastrar, listar, editar e remover usuários**, armazenando os dados em um **banco de dados fictício** baseado em **listas e dicionários**, sem o uso de um banco real.  

---

## 🚀 Funcionalidades

- ✅ Adicionar novos usuários  
- 📋 Listar usuários cadastrados  
- ✏️ Editar nome e e-mail de um usuário específico  
- 🗑️ Remover usuários da lista  
- 🧠 Simulação de banco de dados com listas e dicionários  
- 🧪 Testes automatizados com Pytest (incluindo delays visuais)

---

## 🧱 Tecnologias utilizadas

- [Python 3.12](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)
- [Pytest](https://docs.pytest.org/en/latest/)

---

## 📂 Estrutura do projeto


Crud_estudo/
│
├── app.py # Arquivo principal do Flask
├── database/
│ └── fic_data.py # "Banco de dados" fictício
├── templates/
│ └── index.html # Página principal
├── static/
│ └── javaScript.js # Script de apoio (edição, interação etc.)
├── tests/
│ └── test_user_crud.py # Testes automatizados do CRUD
├── README.md
└── requirements.txt

---

## ⚙️ Como rodar o projeto localmente

### 

1️⃣ Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/crud-flask-usuarios.git
cd crud-flask-usuarios

2️⃣ Criar e ativar um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux ou Mac
venv\Scripts\activate      # Windows

3️⃣ Instalar as dependências
pip install -r requirements.txt

4️⃣ Rodar o servidor Flask
python app.py


Acesse no navegador:
👉 http://127.0.0.1:5000/

🧪 Rodando os testes

Para rodar os testes automatizados (com delays visuais):

pytest -s -v


Saída esperada:

🧩 Adding user...
✅ User added successfully!
🔄 Updating user...
✅ Update complete!
🗑️ Removing user...
✅ All tests passed!

💡 Sobre o projeto

Este projeto tem fins educacionais e foi criado para praticar a lógica de back-end com Flask antes de trabalhar com bancos reais como SQLite ou PostgreSQL.


📜 Licença

Este projeto é livre para estudo, modificação e uso pessoal.
Sinta-se à vontade para usar como base para seus próprios aprendizados!

💻 Desenvolvido por Felipe Hoffmann
📬 [https://www.linkedin.com/in/felipe-hoffmann-viana-8898b6329/]
