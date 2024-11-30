# Task Manager

### Hexlet tests and linter status:
[![Actions Status](https://github.com/evisorexx/Task_Manager/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/evisorexx/Task_Manager/actions)

### CodeClimate Quality status:
[![Maintainability](https://api.codeclimate.com/v1/badges/f167f185058c7b66e5d5/maintainability)](https://codeclimate.com/github/evisorexx/Task_Manager/maintainability)

### Render deploy:
[![Deploy on Render](https://render.com/images/deploy-to-render-button.svg)](https://python-project-52-a18a.onrender.com)

<h3>Менеджер задач</h3>
<p>Веб-приложение для менеджмента задач.
Реализовано на фреймворке <b>Django 5.1.2</b>, для визуала использовались базовая система шаблонов Django и библиотека Django-bootstrap 5. Данные при разработке сохраняются во встроенном <b>sqlite</b>, на проде - используется <b>PostgreSQL</b>.
<ul>
  <li>Регистрация и аутентификация пользователей.</li>
  <li>Проект выполнен в соответсвии с CRUD: пользователей, статусов, меток, задач.</li>
  <li>Доступ к статусам, меткам и задачам имеют только те, кто прошел аутентификацию.</li>
  <li>Пока задаче присвоен статус или метка, ее нельзя удалить.</li>
  <li>Присутсвует фильтрация задач.</li>
  <li>Оформлена локализация RU/EN. По умолачанию используется английский язык.</li>
  <li>Подключен сервис для отслеживания и сбора ошибок <a href='https://rollbar.com'>Rollbar</a></li>
</ul>
<h3>Переменные окружения</h3>
<p><b>Для корректной работы, вы должны иметь env-файл в корне проекта со следующими переменными:</b></p>
<pre>
SECRET_KEY = ВАШ_СЕКРЕТНЫЙ_ТОКЕН
DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME
ROLLBAR = ВАШ_ТОКЕН_ДОСТУПА_В_ROLLBAR
</pre>
<h3>Установка</h3>
<pre>
$ git clone https://github.com/evisorexx/Task_Manager
$ cd Task_Manager
$ make setup (включает в себя развертку локального сервера)
# Переход в браузере по ссылке http://127.0.0.1:8000/
</pre>
