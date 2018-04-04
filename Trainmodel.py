from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os


bot = ChatBot('MIT4')

bot.set_trainer(ListTrainer)

	
for _files in os.listdir('data_files'):
	MIT4=open('data_files/'+_files,'r').readlines()
	bot.train(MIT4)

