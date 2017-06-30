import irc_cfg
import sqlite3
import core_functions

db_conn = sqlite3.connect('bot.db')
conn_cursor = db_conn.cursor()
owner = irc_cfg.CHAN[1:]

def createreward(command, reward_name, chat_message, cost):
    #Create a user reward
    #Make sure exceptions get handled properly
    #These are not protected (they can be deleted by the user)
    cost = int(cost)
    t = (command, reward_name, chat_message, cost, 'N') #N for not protected
    conn_cursor.execute("INSERT INTO rewards values(?,?,?,?,?);", t)
    db_conn.commit()

def candeletereward(command):
    #Lets you know if the reward is protected
    #Protected rewards are built in, usually require some computation
    #returns 1 if command exists + is not protected, else returns 0
    t = (command,)
    conn_cursor.execute("SELECT COUNT(*) FROM rewards WHERE command = ? AND protected='N'", t)
    result = conn_cursor.fetchone()
    return result[0]

def deletereward(command):
    t = (command,)
    conn_cursor.execute("DELETE FROM rewards WHERE command = ?", t)
    db_conn.commit()

def redeemreward(user,command):
    #Return False if can't redeem
    #Return whisper if taken
    #whisper executed on bot.py
    t = (command,)
    conn_cursor.execute("SELECT whisper_message, cost FROM rewards WHERE command = ?",t)
    result = conn_cursor.fetchall()
    whisper = result[0][0]
    cost = result[1][0]
    if core_functions.cantakepoints(user, cost):
        takepoints(user,cost)
        return whisper
    else:
        return False

def getrewards():
    #return list of commands
    conn_cursor.execute("SELECT command FROM rewards")
    data = conn_cursor.fetchall()
    columns = [elt[0] for elt in data]
    return columns

