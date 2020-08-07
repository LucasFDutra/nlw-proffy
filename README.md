Dessa vez fiz apenas o backend da aplicação. mas decidi fazer diferente e fiz ele inteiramente em python
O banco de dados que utilizei foi o postgres.

---
# PARA USAR
Recomendo utilizar o poetry para trabalhar com seus projetos python, então corre lá e instala ele [por aqui](https://python-poetry.org/)

Tendo o poetry instalado, entre na pasta backend pelo terminal e crie uma virtualenv para não bagunçar suas libs no pc, basta digitar o comando:

```shell
$ poetry shell
```

Ele vai se basear no arquivo `pyproject.toml` para criar o ambiente, com o nome `name = "backend"` que foi definido no arquivo, assim como a versão do python que é a 3.8.

Agora basta instalar as dependências, que também estão disponíveis no arquivo `pyproject.toml`, basta digitar:

```shell
$ poetry install
```

E pronto, você tem um ambiente python para rodar sua api.

Eu não utilizei nenhuma lib de migrations, então fiz um esquema meio gambiarra aqui que resolveu pra mim (só até eu ter um tempinho para estudar como utilizar migrations da melhor forma em python).
Para criar as tabelas no seu banco de dados, digite:

```shell
$ poetry run migration_up
```

> OBS.: se reparar o nome dos arquivos de migrations (backend/src/database) vão mudar o nome para ter um _up no final. isso me ajuda a identificar qual migration já rodou, e qual ainda precisa rodar... Eu falei que era meio gambiarra... e caso precise tem o método `migration_down` também. que retira o _up dos arquivos

Para rodar o backend você só precisa digitar o comando:

```shell
$ poetry run dev
```

e pronto, sua aplicação estará rodando na porta 5000

---
# ATENÇÃO

Os comandos de migrations e run dev foram instanciados dentro do arquivo `pyproject.toml` nas linhas

```toml
[tool.poetry.scripts]
dev = "scripts:run_dev"
migration_up = "scripts:up_migration"
migration_down = "scripts:down_migration"
```

mas o código que realmente está rodando por baixo desses comandos está no arquivo `scripts.py`.. então não apague esse arquivo


---
# VARIÁVEIS DE AMBIENTE
Os parâmetros de conexão com o banco estão todos em um arquivo .env, que não está nesse repositório, mas aqui vai ter um arquivo .env_ex que você pode mudar o nome para .env e colocar suas credências


---
# INSTALANDO O POSTGRES
Eu recomendo usar o banco via docker. Acho mais simples de instalar, mas caso queira instalar na sua máquina "de verdade" então siga a documentação [aqui](https://www.postgresql.org/)
mas se quer ir pelo docker, então primeiro instale o docker:

```shell
$ sudo apt install docker.io
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ su $USER
```

Agora basta instalar a imagem do postgres com o comando:

```shell
$ docker run -p 5432:5432  --name postgres-database -e POSTGRES_PASSWORD=1234 -d postgres
```

> Dica: utilize a extensão do [docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) para vscode, que ela ajuda bastante para gerenciar seus containers. E também para visualizar seu banco eu recomendo o [postbird](https://snapcraft.io/postbird)

---
# OS ENDPOINTS
Abra o arquivo `Insomnia_2020-08-07.json` no seu insomnia, e veja as rotas, e como utilizá-las via exemplos. Mas só para não ficar perdido:
- create class: cria o perfil do professor, e sua agenda de aulas
- create connections: grava quando uma conexão foi feita e com qual professor
- list class: mostra as aulas disponíveis de acordo com filtros, que estão sendo passados pelo header
- list connections: mostra quantas conexões foram feitas até agora

---
Bom aproveito, espero que consiga aprender algo novo com essa api escrita em python!!