# you_telegram_bot

Hello everyone, this project is for quickly getting started with "you chat" (https://you.com).

"you.com" git:
    
    https://github.com/You-OpenSource/You-Python

ENV-params:
    
    Add params to file ".env"

    BOT_TOKEN - telegram bot token (create with "https://t.me/BotFather")
    YOU_TOKEN - token for "you.com" (https://api.betterapi.net/)

Access list:
    
    Add to file "witelist.txt" user-id's for access to bot (each id from a new line)

    User-id can be found in "https://t.me/getmyid_bot"

Launch options:
    
    DEV:
        install: requirements.txt
        run: in project folder "python main.py"

    PROD:
        install: docker and docker-compose
        install: make
        run: in project folder "make up"