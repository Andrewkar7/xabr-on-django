# Проект "Xabr"
# Командная разработка по методологии Agile:Scrum
# Сайт для обучения

## Базовая документация к проекту

Основные системные требования:

* Ubuntu 20.04 LTS
* Python 3.8
* PostgreSQL 12
* Django 3.1
* Зависимости (Python) из requirements.txt

#### Установка необходимого ПО
#### обновляем информацию о репозиториях
```
apt update
```
#### Установка nginx, СУБД PostgreSQL, Git, virtualenv
```
apt install nginx
apt install postgresql postgresql-contrib
apt install git-core
apt install python3-venv
apt install gunicorn
```
#### Настраиваем виртуальное окружение
Клонируем репозиторий:
```
git clone git@github.com:Dmitrii2019/xabr.git /opt/venv/xabr/src
cd xabr/
```
Создаем и активируем виртуальное окружение:
```
python3 -m venv xabr_env
source xabr_env/bin/activate
```
Ставим зависимости:
```
pip3 install -r requirements.txt
```
#### Выполнение миграций и сбор статических файлов проекта
Выполняем миграции:
```
python3 manage.py migrate
```
Собираем статику:
```
python3 manage.py collectstatic
```
#### Суперпользователь
```
python3 manage.py createsuperuser
```
к примеру (логин/пароль): admin:admin
#### Заполнить базу данных тестовыми данными (не обязательно)
```
python3 manage.py fill_db

```
#### Импортируем данные (не обязательно)
```
python manage.py loaddata db.json
```
#### Тест запуска
```
python3 manage.py runserver
```
#### Назначение прав доступа
```
chown -R xabr /home/xabr_env/
chmod -R 755 /home/xabr_env/xabr/
```
####  Настроийка gunicorn
создаем файл
```
sudo nano /etc/systemd/system/gunicorn.service
```
заполнить его
```

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=django
Group=www-data
WorkingDirectory=/home/xabr_env/xabr/
ExecStart=/home/xabr_env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/xabr_env/xabr/xabr.sock geekshop.wsgi

[Install]
WantedBy=multi-user.target

```
Активирование и запуск сервиса

```
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn
```
Настройки параметров для nginx
```
sudo nano /etc/nginx/sites-available/xabr


server {
    listen 80;
    server_name 151.248.117.226; ### server_name необхоимо написать ip-адрес сервера

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/xabr_env/xabr;
    }

    location /media/ {
        root /home/xabr_env/xabr;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/xabr_env/xabr/xabr.sock;
    }
}

```
#### Активировать сайт
```
sudo ln -s /etc/nginx/sites-available/xabr /etc/nginx/sites-enabled
```
Перезапускаем службу «nginx» и добавляем разрешения в сетевой экран:
```
sudo systemctl restart nginx
```
#### После этого в браузере можно ввести ip-адрес сервера и откроется проект.