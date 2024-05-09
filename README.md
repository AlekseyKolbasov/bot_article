# bot_article

Необходимо реализовать простого телеграм-бота, который будет запоминать ссылки, которые вы ему присылаете, и отдавать их по запросу. Хранить их он будет в БДL, которую можно запустить на своем компьютере.

Бот должен обрабатывать две команды /start, /get_article. Первая команда выводит информационное меню бота

```
Привет! Я бот, который поможет не забыть прочитать статьи, найденные тобой в интернете :))
- Чтобы я запомнил статью, достаточно передать мне ссылку на нее. К примеру https://example.com
- Чтобы получить случайную статью, достаточно передать мне команду /get_article.
Но помни! Отдавая статью тебе на прочтение, она больше не хранится в моей базе. Так что тебе точно нужно ее изучить!!!
```

Ссылка на бота: https://t.me/ne_na_dopsu_bot

Инструкция для запуска собственного бота.
1) Установить интепретатор python версии 3.11 или выше.
2) Необходимо создать виртуально окружение. Это можно сделать введя в локальную комдную строку <python -m venv name>. Активировать это окружение: в Windows name\Scripts\activate.bat, для Linux или MacOS source venv/bin/activate
3) Необходимо добавить библиотеки в созданное окружение pip install -r requirements.txt
4) Необходимо создать своего бота в телеграмме. Для этого нужно начать чат с https://t.me/BotFather и получить от него HTTP API
5) Необходимо вставить полученный от отца ботов HTTP API в текстовый файл API_TOKEN и сохранить его.
6) Необходимо запустить программу командой python main.py
7) Готово!
   
