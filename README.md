# Python for Data Portfolio

Status: Em desenvolvimento ativo

Foco: Engenharia de Dados / Data Science / IA & ML

Este repositório documenta minha transição de scripts SQL puros para um ecossistema completo de Ciência de Dados. O foco principal é a integração entre bancos de dados e o processamento eficiente de dados com Python (Futuramente será adicionado as bibliotecas Pandas e NumPy), para seguir os caminhos de Analísta de Dados/ IA & ML .

## Stack

* **Linguagem:** Python 3.13
* **Banco de Dados:** MySQL 
* **Bibliotecas:** SQLite3 e MySQL Connector, Futuramente: (Pandas, Numpy)
* **Infraestrutura:** Docker e Git

---

## Arquitetura do Ambiente

O projeto é totalmente conteinerizado para garantir a reprodutibilidade do ambiente:

### 1. Dockerfile
Define a imagem Python, instalando as dependências listadas em `requirements.txt` e configurando o diretório de trabalho em `/app`.

### 2. Docker Compose
dois serviços principais:
* **mysql**: Container de banco de dados com persistência via volumes locais.
* **python**: Container de aplicação que depende do banco para execução, permitindo o desenvolvimento em tempo real através do espelhamento de pastas.

---

## 📂 Organização do Repositório

| Pasta / Arquivo | Descrição |
| :--- | :--- |
| `python/` | Scripts de processamento e testes de conexão. |
| `docker-compose.yml` | Configuração da rede e serviços dos containers. |
| `requirements.txt` | Bibliotecas necessárias (Pandas, Numpy, SQLite). |
| `Dockerfile` | Receita para construção da imagem Python. |

---

## Como Executar

Para subir todo o ambiente (Banco + Python), utilize o comando abaixo na raiz do projeto:

```bash
docker-compose up --build
pip install -r requirements.txt
```
> Necessário ter o Docker baixado para acessar banco.


Se por acaso der algum erro, provavelmente a porta 3306 do seu computador esta em uso, feche o MySQL ou outro banco de dados que esteja aberto no seu computador que esteja usando essa porta, caso nao consiga, mude no arquivo docker-compose.yml:
```yml
    ports:
      - "3306:3306"  --->>  "3307:3306" (ou porta vazia)
    volumes:
      ...
```

depois renomei o arquivo `.env-example` para `.env` e mude as informaçoes da sua preferencia.
```python
MYSQL_ROOT_PASSWORD='CHANGE-ME' -> 123456
MYSQL_DATABASE='CHANGE-ME' -> bancodedados
MYSQL_USER='CHANGE-ME' -> usuario
MYSQL_PASSWORD='CHANGE-ME' -> 123
MYSQL_HOST='localhost' 
```

