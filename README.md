# CRUD Users Management

Um pequeno projeto de CRUD para gestão de usuários utilizando um banco de dados fictício.

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Sobre o Projeto

Este projeto consiste em uma aplicação web simples de CRUD (Create, Read, Update, Delete) que permite a gestão de usuários em um banco de dados simulado. O objetivo é demonstrar conceitos básicos de desenvolvimento web e manipulação de dados.

## Instalação

Para rodar este projeto localmente, siga as instruções abaixo:

1. Clone o repositório:

    ```bash
    git clone https://github.com/anadevti/crud-users-management.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd crud-users-management
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install -r requirements.txt
    ```

4. Execute a aplicação:

    ```bash
    python main.py
    ```

5. Acesse o sistema no seu navegador, utilizando o endereço:

    ```
    http://localhost:5000
    ```

## Uso

Após iniciar a aplicação, você poderá:

- **Criar Usuários:** Adicione novos usuários ao banco de dados.
- **Listar Usuários:** Visualize todos os usuários cadastrados.
- **Editar Usuários:** Atualize informações de usuários existentes.
- **Deletar Usuários:** Remova usuários do banco de dados.

## Estrutura do Projeto

```text
crud-users-management/
│
├── database/          # Configurações e scripts relacionados ao banco de dados
├── routes/            # Definições de rotas da aplicação
├── static/            # Arquivos estáticos como CSS, JS e imagens
├── templates/         # Templates HTML para renderização
├── .gitignore         # Arquivos e diretórios ignorados pelo Git
├── LICENSE            # Licença do projeto
├── README.md          # Documentação do projeto
└── main.py            # Arquivo principal da aplicação
```

## Tecnologias Utilizadas

- **Python 3.8+**
- **Flask** - Microframework web para Python
- **HTML5 & CSS3** - Estrutura e estilização das páginas
- **SQLite** - Banco de dados leve para simulação

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um [issue](https://github.com/anadevti/crud-users-management/issues) ou enviar um [pull request](https://github.com/anadevti/crud-users-management/pulls).

1. Faça um Fork do projeto
2. Crie uma nova Branch (`git checkout -b feature/sua-feature`)
3. Faça o Commit das suas alterações (`git commit -m 'Adicione sua feature'`)
4. Envie para o Branch (`git push origin feature/sua-feature`)
5. Abra um Pull Request

## Licença

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais informações.

