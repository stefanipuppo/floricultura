# Ilha Verde

Ilha Verde é um sistema de gestão de floricultura desenvolvido em Django. Este projeto tem como objetivo permitir o gerenciamento de plantas, incluindo funcionalidades para listar, visualizar detalhes, adicionar, editar e deletar plantas.
## Sobre o Projeto

Este projeto foi uma experiência leve e divertida para mim, pois sou apaixonado por plantas. Nomeei o projeto de "Ilha Verde" como uma referência à "Ilha da Magia", Florianópolis, onde moro.


## Funcionalidades

- **Listagem de Plantas:** Visualize todas as plantas cadastradas.
- **Detalhes da Planta:** Veja informações detalhadas sobre cada planta.
- **Adicionar Planta:** Adicione novas plantas ao sistema.
- **Editar Planta:** Edite as informações das plantas existentes.
- **Deletar Planta:** Remova plantas do sistema.

## Tecnologias Utilizadas

- **Python**
- **Django**
- **SQLite**
- **HTML/CSS**

## Como Rodar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/stefanipuppo/ilhaverde.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd ilhaverde
    ```

3. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Aplique as migrações:
    ```bash
    python manage.py migrate
    ```

6. Rode o servidor:
    ```bash
    python manage.py runserver
    ```

7. Acesse o sistema em `http://127.0.0.1:8000/`.

### Informações sobre as Plantas:
   - **Nome**
   - **Espécie**
   - **Descrição** 
   - **Preço** 

### Contribuição:

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.
