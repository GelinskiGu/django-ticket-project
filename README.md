# Bar System Django Application

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

* [Descrição](#descricao)
* [Funcionalidades Principais](#funcionalidades)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Configuração do Ambiente](#env-config)
* [Configuração do Banco de dados](#db)
* [Executando a Aplicação](#executando-aplicacao)
* [Próximas Implementações](#proximas-implementacoes)

## Descrição <a name="descricao"></a>
Este repositório contém um sistema interno de gerenciamento de vendas de um estabelecimento de comidas. Ele permite que vendedores do estabelecimento façam login e realizem o registro de vendas para quem prepara os pedidos receba as informações dessas vendas. O sistema foi desenvolvido em Python com FrontEnd sendo Bootstrap, utilizando Docker, Django e PostgreSQL como banco de dados. 

## Funcionalidades Principais: <a name="funcionalidades"></a>

* Autenticação de usuários: Os vendedores podem fazer login no sistema para acessar as funcionalidades.
* Listagem de Produtos: Na página inicial, os produtos são exibidos por categorias, como bebidas, comidas, doces, entre outros.
* Carrinho de Compras: Os vendedores podem adicionar produtos ao carrinho, especificando as quantidades desejadas.
* Página do Carrinho: Exibe as informações dos produtos selecionados, incluindo preço total, imagem e quantidade.
* Página de Status do Pedido: Mostra o status atual dos pedidos, com os pedidos em andamento exibidos primeiro, seguidos pelos pedidos finalizados.
* Finalização do Pedido: Os pedidos podem ser marcados como concluídos nesta página.

## Tecnologias Utilizadas: <a name="tecnologias-utilizadas"></a>

* Python: Linguagem de programação utilizada para desenvolver o sistema.
* Django: Framework web utilizado para a construção do site.
* PostgreSQL: Banco de dados utilizado para armazenar os dados do sistema.
* Docker: Containers onde estão as imagens do projeto.
* Vercel: Hospedagem da base de dados PostgreSQL.
* Render: Plataforma de hospedagem utilizada para realizar o deploy do projeto.
* Cloudinary: Serviço utilizado para hospedar as imagens utilizadas no sistema.
* Bootstrap: Framework de CSS utilizado para criar o frontend do site.

## Configuração do Ambiente <a name="env-config"></a>

1. Certifique-se de ter o Python instalado em sua máquina. Você pode baixar o Python em **https://www.python.org/downloads/**.

2. Clone o repositório:

  ```shell
  git clone https://github.com/GelinskiGu/django-ticket-project.git
  ```

3. Navegue até o diretório raiz.

  ```shell
  cd djangoapp
  ```

4. Crie um ambiente virtual para isolar as dependências do projeto.

  ```shell
  python -m venv myenv
  ```

5. Ative o ambiente virtual.
* No Windows:

  ```shell
  myenv\Scripts\activate
  ```
* No Linux/Mac:

  ```shell
  source myenv/bin/activate
  ```

6. Instale as dependências do projeto.

  ```shell
  pip install -r requirements.txt
  ```


## Configuração do Banco de Dados <a name="db"></a>


1. Copie o arquivo **.env-example** para **.env**.

  ```shell
  cp .env-example .env
  ```

2. Abra o arquivo **.env**.

3. Atualize as variáveis do banco de dados com as informações corretas.

  ```shell
  DB_ENGINE=django.db.backends.postgresql
  POSTGRES_DB=nome_do_banco_de_dados
  POSTGRES_USER=nome_do_usuario
  POSTGRES_PASSWORD=senha_do_usuario
  POSTGRES_HOST=host_do_banco_de_dados
  POSTGRES_PORT=porta_do_banco_de_dados
  ```

  Certifique-se de substituir os valores **"CHANGE-ME"** pelas informações corretas do seu banco de dados PostgreSQL.

## Executando a Aplicação <a name="executando-aplicacao"></a>

1. Aplique as migrações para criar as tabelas do banco de dados.

  ```shell
  python manage.py migrate
  ```

2. Colete e sirva os arquivos estáticos.

  ```shell
  python manage.py collectstatic
  ```

3. Inicie o servidor de desenvolvimento.

  ```shell
  python manage.py runserver
  ```

4. Acesse a aplicação em seu navegador através do endereço **http://127.0.0.1:8000/**.

## Proximas Implementações: <a name="proximas-implementacoes"></a>
Aqui estão algumas melhorias planejadas para o projeto:
- Refatorar todo o Front-End, utilizando ReactJS e Tailwind CSS;
- Implementar Django REST Framework;
- Hospedar no Microsoft Azure;
- Refatorar código, pois é muito antigo e não segue normas de Clean Code;
