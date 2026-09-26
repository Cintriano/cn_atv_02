# Django + Gunicorn + Nginx + PostgreSQL (Docker)

Estrutura com 3 containers:

- **web**: aplicação Django rodando com Gunicorn.
- **nginx**: proxy reverso, também serve `static/` e `media/` diretamente dos volumes.
- **db**: PostgreSQL.

A aplicação de exemplo (`uploader`) permite enviar arquivos, que são salvos no volume
Docker `media_data`.

## Como rodar

```bash
cp .env.example .env
# edite o .env se quiser trocar usuário/senha/secret key

docker compose up --build
```

Acesse: http://localhost/

## Criar um superusuário (opcional, para acessar /admin/)

```bash
docker compose exec web python manage.py createsuperuser
```

## Estrutura de volumes

- `postgres_data` → dados do PostgreSQL.
- `media_data` → arquivos enviados pelos usuários (upload). Compartilhado entre `web` e `nginx`.
- `static_data` → arquivos estáticos coletados pelo `collectstatic`. Compartilhado entre `web` e `nginx`.

## Estrutura de pastas

```
.
├── docker-compose.yml
├── .env.example
├── django_app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── entrypoint.sh
│   ├── manage.py
│   ├── core/            # settings, urls, wsgi
│   └── uploader/         # app de upload de arquivos
└── nginx/
    ├── Dockerfile
    └── nginx.conf
```
