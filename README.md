<h1>Телеграм бот для мониторинга и управления серверами Counter-Strike 1.6 на хостинге MyArena</h1>

<p>
  <a href="https://github.com/m1nz1k/myarena_cs_telegram_monitoring">
    <img src="https://img.shields.io/github/license/m1nz1k/myarena_cs_telegram_monitoring" alt="GitHub License">
  </a>
  <img src="https://img.shields.io/badge/python-3.x-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/aiogram-2.x-blue" alt="aiogram Version">
  <img src="https://img.shields.io/badge/postgresql-latest-blue" alt="PostgreSQL Version">
  <img src="https://img.shields.io/badge/sqlalchemy-latest-blue" alt="SQLAlchemy Version">
  <img src="https://img.shields.io/badge/requests-latest-blue" alt="Requests Version">
  <img src="https://img.shields.io/badge/python--dotenv-latest-blue" alt="python-dotenv Version">
</p>

<h2>Описание проекта</h2>
<p>
  Этот проект представляет собой Telegram бота, который предназначен для мониторинга и управления серверами Counter-Strike 1.6 на хостинге MyArena. Бот разработан на языке Python 3 и использует различные библиотеки, такие как aiogram, PostgreSQL, SQLAlchemy (Gino), requests и python-dotenv.
</p>

<h2>Возможности</h2>
<ul>
  <li>Добавление сервера по токену и присвоение ему названия.</li>
  <li>Переключение между серверами и удаление серверов.</li>
  <li>
    Просмотр статуса сервера:
    <ul>
      <li>Включен, выключен или находится в процессе включения.</li>
      <li>Название сервера.</li>
      <li>Тип сервера.</li>
      <li>Адрес сервера.</li>
      <li>Локация сервера.</li>
      <li>Текущая карта.</li>
      <li>Онлайн игроков.</li>
      <li>Остаток дней аренды сервера.</li>
    </ul>
  </li>
  <li>
    Управление сервером:
    <ul>
      <li>Включение, выключение и перезапуск сервера.</li>
      <li>Отправка команд в консоль сервера.</li>
    </ul>
  </li>
</ul>

<h2>Требования</h2>
<ul>
  <li>Python 3.x</li>
  <li>aiogram 2.x</li>
  <li>PostgreSQL</li>
  <li>SQLAlchemy (Gino)</li>
  <li>requests</li>
  <li>python-dotenv</li>
</ul>

<h2>Установка и запуск</h2>
<ol>
  <li>Клонируйте репозиторий:<br><code>git clone https://github.com/m1nz1k/myarena_cs_telegram_monitoring.git</code></li>
  <li>Перейдите в каталог проекта:<br><code>cd myarena_cs_telegram_monitoring</code></li>
  <li>Создайте виртуальное окружение:<br><code>python3 -m venv venv</code></li>
  <li>Активируйте виртуальное окружение:<br><code>source venv/bin/activate</code> (для Linux/macOS) или <code>venv\Scripts\activate</code> (для Windows)</li>
  <li>Установите зависимости:<br><code>pip install -r requirements.txt</code></li>
  <li>Настройте базу данных PostgreSQL и заполните файл .env:<br>
    <pre>BOT_TOKEN=your_telegram_bot_token
ip=localhost
PGUSER=your_postgresql_username
PGPASSWORD=your_postgresql_password
DATABASE=gino</pre>
  </li>
  <li>Запустите файл app.py.</li>
</ol>

<h2>Использование</h2>
<p>Начните диалог с ботом в Telegram. Весь процесс управления ботом осуществляется с помощью Inline меню.</p>

<h2>Конфигурация</h2>
<p>В папке data находится файл config.py, в котором есть список admins. Укажите user_id вашего аккаунта Telegram в этом списке.</p>

<h2>Лицензия</h2>
<p>Этот проект лицензируется в соответствии с лицензией <a href="https://opensource.org/licenses/MIT">MIT</a>.</p>

<h2>Автор</h2>
<p>Автор: Евгений a.k.a EvilLolaBunny a.k.a M1nz1k<br>
GitHub: <a href="https://github.com/m1nz1k">M1nz1k</a></p>

<h2>Содействие</h2>
<p>Любой вклад в улучшение проекта приветствуется. Вы можете создать issue или Pull Request.</p>
