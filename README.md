# 🧩 CRUD Flask - Banco de Dados Fictício

Este projeto tem o objetivo de praticar os conceitos fundamentais de CRUD (Create, Read, Update, Delete) utilizando Flask em Python. Os dados são armazenados em um "banco de dados" fictício implementado com listas e dicionários — ideal para fins didáticos antes de migrar para um banco real.

---

## 🚀 O que o projeto faz

- Cadastrar novos usuários (nome e e-mail)
- Listar usuários cadastrados
- Editar um usuário existente
- Remover usuários
- Simulação de persistência em memória (listas/dicionários)
- Testes automatizados com pytest

---

## 🧱 Tecnologias

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
├── README.md
└── requirements.txt

---

## ⚙️ Como executar localmente

1. Clone o repositório

   git clone https://github.com/FelipeHoffmannV/Crud_estudo.git
   cd Crud_estudo

2. Crie e ative um ambiente virtual

   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate    # Windows

3. Instale dependências

   pip install -r requirements.txt

4. Execute a aplicação

   python app.py

Acesse em: http://127.0.0.1:5000/

---

## 🧪 Rodando os testes

Para executar os testes com pytest:

   pytest -s -v

Os testes cobrem o fluxo básico do CRUD (adicionar, listar, editar, remover).

---

## Observações

- Este projeto usa armazenamento em memória: ao reiniciar a aplicação os dados são perdidos.
- É recomendado migrar para um banco real (SQLite, PostgreSQL, etc.) para persistência duradoura.

---

## Licença

Uso livre para estudos e aprendizado.

---

Desenvolvido por Felipe Hoffmann
https://www.linkedin.com/in/felipe-hoffmann-viana-8898b6329/