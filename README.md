# Bar System Django Application

Descrição

## Configuração do Ambiente

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


## Configuração do Banco de Dados


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

## Executando a Aplicação

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
