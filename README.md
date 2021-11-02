### Сборка образов

В корне репозитория выполните команду:

```bash
docker-compose build
```
### Запуск контейнеров

```bash
docker-compose up -d
```
При первом запуске данный процесс может занять несколько минут.

### Далее применение миграций:

```bash
docker-compose run web python manage.py makemigrations
```
```bash
docker-compose run web python manage.py migrate
```
#### Создание суперпользователя

```bash
docker-compose run web python manage.py createsuperuser
```
### Проект доступен по адресу http://127.0.0.1:8000 
  (админ панель http://127.0.0.1:8000/admin/)

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```
