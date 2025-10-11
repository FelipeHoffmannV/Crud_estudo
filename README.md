# Crud_estudo

Este projeto é um CRUD simples desenvolvido para fins de estudo, utilizando o framework Flask em Python.

## Objetivo

O objetivo principal deste projeto é praticar e aprender conceitos de desenvolvimento web, rotas, templates e manipulação de dados em Python com Flask.

## Banco de Dados

No momento, o projeto utiliza um banco de dados fake, implementado com listas e dicionários em memória para simular o armazenamento de usuários. Os dados não são persistidos após o encerramento da aplicação.

O arquivo [`database/fic_data.py`](database/fic_data.py) contém a lista de usuários utilizada como banco de dados fake.

## Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
crud_estudo/
│
├── app.py               # Arquivo principal da aplicação Flask
├── database/             # Pasta contendo arquivos relacionados ao banco de dados
│   └── fic_data.py      # Arquivo com a "base de dados" fake (listas e dicionários)
│
├── templates/           # Pasta contendo os templates HTML
│   ├── base.html        # Template base com o cabeçalho e rodapé comuns
│   ├── index.html       # Página inicial
│   ├── create.html      # Página para criar um novo usuário
│   ├── read.html        # Página para exibir detalhes de um usuário
│   ├── update.html      # Página para editar um usuário existente
│   └── delete.html      # Página para confirmar a exclusão de um usuário
│
└── static/              # Pasta para arquivos estáticos (CSS, JavaScript, imagens)
    └── style.css        # Arquivo de estilo CSS
```

## Como Executar o Projeto

Para executar o projeto em sua máquina, siga os passos abaixo:

1. Certifique-se de ter o Python 3.x instalado.
2. Clone este repositório para sua máquina.
3. Navegue até a pasta do projeto no terminal.
4. Instale as dependências necessárias com o comando: `pip install -r requirements.txt`
5. Execute o arquivo `app.py` com o comando: `python app.py`
6. Abra o navegador e acesse `http://127.0.0.1:5000/`

## Funcionalidades

As principais funcionalidades deste CRUD incluem:

- Criar um novo usuário (Create)
- Ler e exibir detalhes de um usuário (Read)
- Atualizar as informações de um usuário existente (Update)
- Excluir um usuário (Delete)

## Tecnologias Utilizadas

As principais tecnologias e ferramentas utilizadas no desenvolvimento deste projeto são:

- Python 3.x
- Flask
- HTML
- CSS/BootStrap 5



