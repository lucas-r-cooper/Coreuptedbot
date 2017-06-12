#irc_cfg.py
#This configures IRC connection info
#Replace all <BRACKETED INFO> with your own info
#Use only lowercase letters for usernames 
#e.g Coreupted would use CHAN = "#coreupted"
HOST = "irc.chat.twitch.tv"
PORT = 6667
NICK = "<YOUR BOT'S USERNAME>"
PASS = "oauth:<YOUR BOT ACCOUNT'S API KEY>"
CHAN = "#<YOUR CHANNEL>"
RATE = (30/20) # 30 seconds / 20 messges (20 messages per 30 seconds)
POINT_NAME = "points"
POINTS_PER_MINUTE = "10"
FIRST_CHAT_BONUS = 1 #Set to 0 to turn off
FIRST_CHAT_BONUS_POINTS = 1500
