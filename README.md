# Aloodak
Aloodak is a Telegram bot that reports the air pollution status in various cities in the world. The version specific to Tehran, Iran is available at 
[@Aloodak](https://t.me/Aloodak). 

## Setup
To run Aloodak, you need a Telegram Bot ([Create one here](https://t.me/BotFather)) a channel and an API key from IQAir ([Get one here](https://www.iqair.com/dashboard/api)). Then, you need to create a `config.conf.json` file in Aloodak's root directory.

```bash
git clone https://github.com/frowzyispenguin/aloodak.git
cd aloodak
python3 -m venv .env
source .env/bin/activate
pip3 install -r ./requirements.txt
cp config.example.json config.conf.json
editor config.conf.json
```

## Usage
You can use a cronjob to run the bot every n minutes. The main instance of Aloodak runs once every 30 minutes. Please note that Aloodak won't post a new post to your channel if the measurement doesn't change from last time it ran. It will also send all its messages in silenced mode. (No notifications will be sent)

```bash
30 * * * * /PATH/TO/aloodak/.env/bin/python3 /PATH/TO/aloodak/main.py
```

## Contributions
Aloodak is always evolving and pull requests are always appreciated. if you encounter a bug, don't hesitate to make an issue or better yet, a pull request!

## License & DMCA
Unless otherwise noted, this project is licensed under the GNU GPLv3 license. See the accompanying LICENSE file for more information.

We take any DMCA requests very seriously, so if any of our assets are violating your intellectual properties, don't hesitate to contact us through the issues feature of GitHub.