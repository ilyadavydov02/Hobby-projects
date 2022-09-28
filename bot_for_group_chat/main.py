#Here is my hobby project, a chatbot for group chat that can respond to certain commands and exclude from the chat.
#If desired, you can implement other functions.
#The bot was written for a group chat with my friends, here is a much shorter version, with a demonstration of the main ideas.
#Below I will write how I used the bot when it had a much larger code.
#The bot is written in Python for the VK social network using the VK_API library for social network developers.

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import time
import urllib3
import requests
import random
import socket
import pickle

#Here I connect the account to the python file.
#The original version has an account id and a personal secret token.
#Of course, this is not here.
vk = vk_api.VkApi(token='here is key for bot account')
longpoll = VkBotLongPoll(vk, *here is account-id*)

#The two main functions of the program are sending messages and excluding from the chat.
def write_msg(chat_id, message, random_id):
    vk.method('messages.send', {'chat_id': chat_id, 'message': message, 'random_id' : random_id})
def kick(chat_id, user_id):
    vk.method('messages.removeChatUser', {'chat_id': chat_id, 'user_id': user_id})

#Words to be used
for_example_1 = "Hello my friend!"
for_example_2 = "Bye-bye"
for_example_3 = "Sorry, you wrote a forbidden word. I have to exclude you."

#The principle of the program: after receiving a message, the bot reads the chat id and the user who sent it, as well as the message itself.
#Then, depending on the program code, it can respond to the user, exclude him or simply ignore him.
try:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            request = event.object['text']
            if "Hello" in request:
                write_msg(event.chat_id, for_example_1, 0)
            elif "Bye" in request:
                write_msg(event.chat_id, for_example_2, 0)
            elif "The forbidden word":
                write_msg(event.chat_id, for_example_3, 0)
                write_msg(event.chat_id, for_example_2, 0)
                kick(event.chat_id, event.user_id)

#This is just a demonstration of the basic functions of the bot, but it can be expanded as much as imagination allows.
#For example, we arranged days when the bot was excluded from the chat for bad words.
#Sometimes we also used a counter when the bot showed us what our balance of "bad" words was and, for example, excluded it when we reached 5.
#You can also implement any other options, for example, with video, photo, random and time-bound.
#If desired, the bot can be used for commercial purposes, however, there are many similar ones now.
#
#P.S. I use the word "we" because I wrote this bot for myself and my friends, however, this is exclusively my project, if that's important.
