# Sistema de Gerenciamento de Oficina Mecânica

Aplicação desenvolvida em Python como projeto prático de aprendizado e aplicação de conceitos de programação, com o objetivo de criar um sistema para gerenciamento de clientes e veículos de uma oficina mecânica.

O projeto foi desenvolvido do zero, desde a construção da lógica de programação até a integração com banco de dados SQLite, utilizando uma interface de linha de comando (CLI).

## Funcionalidades

- Cadastro de clientes com nome e telefone.
- Cadastro de veículos associados aos clientes.
- Listagem de clientes e seus respectivos veículos.
- Busca de clientes pelo nome.
- Edição de informações dos clientes e veículos.
- Exclusão de clientes e veículos.
- Validação de dados de entrada.
- Tratamento de erros e exceções.
- Armazenamento persistente das informações em banco de dados.

## Tecnologias e conceitos utilizados

- **Python 3:** desenvolvimento da aplicação e implementação das regras de negócio.
- **SQLite:** armazenamento e gerenciamento dos dados.
- **SQL:** operações de consulta, inserção, atualização e exclusão (CRUD).
- **Programação modular:** separação entre a lógica principal e as operações de banco de dados.
- **Tratamento de exceções:** prevenção e tratamento de entradas inválidas e erros durante a execução.
- **Git e GitHub:** versionamento e disponibilização do código-fonte.

## Organização do projeto

- `main.py`: contém a lógica principal, menus, interações com o usuário e funcionalidades do sistema.
- `banco.py`: responsável pela conexão com o SQLite e pelas operações de manipulação dos dados.
- `oficina.db`: banco de dados SQLite, criado automaticamente durante a execução.

## Como executar

**Pré-requisitos:**
- Python 3 instalado.

**Passos:**

1. Clone este repositório ou baixe os arquivos.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

```bash
python main.py
```

O banco de dados SQLite e suas tabelas são criados automaticamente na primeira execução.

Não são necessárias bibliotecas externas para executar a versão atual.

## Interface e funcionamento

O sistema utiliza uma interface de linha de comando (CLI), permitindo que o usuário navegue pelos menus e execute as operações diretamente pelo terminal.

A escolha por esse formato teve como objetivo priorizar o desenvolvimento da lógica, das operações de gerenciamento de dados e da integração com o banco de dados.

## Objetivo e aprendizado

Este projeto foi desenvolvido com o propósito de consolidar conhecimentos adquiridos durante os estudos de programação, colocando em prática conceitos de Python e SQL em uma aplicação funcional.

Durante o desenvolvimento, foram trabalhados conceitos como:
- Construção de lógica de programação.
- Manipulação de estruturas de dados.
- Organização e reutilização de funções.
- Validação de informações.
- Persistência de dados.
- Relacionamento entre tabelas.
- Operações CRUD utilizando SQLite.
- Separação de responsabilidades entre módulos.

## Status do projeto

**Concluído — Versão 1.0.0**

Aplicação funcional executada pelo terminal, com operações de gerenciamento de clientes e veículos e armazenamento persistente em banco de dados SQLite.