Проект для работы с паролями
В данном файле описаны основные используемые команды и основные состовляющие проекта и шаги его построения

1. Работа с виртуальным окружением

virtualenv -p /usr/bin/python3 venv_myproject - создание виртуального окружения
source venv_myproject/bin/activate - активация виртуально окружения



2. Работа с django и pip (делается с активированым виртуальным окружением)

pip3 install django - установка django
django-admin startproject project_password - создание проекта django
python3 manage.py runserver 0.0.0.0:8000 - запуск проекта

2.1 Приложения внутри проекта
python3 manage.py startapp healthapp - создание приложения в django
healthapp - вспомогельное приложение для проверки работоспособности проекта
