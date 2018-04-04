from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import subprocess





bot = ChatBot('MIT4')
bot.set_trainer(ListTrainer)

while True:
	print('\n***********WELCOME TO MIT4 CHATBOT***********\n')

	print('Enter [CHAT] to chat to the bot or [GOOGLE] for the bot to Google for you')
	ch =input()


	if(str(ch)=='CHAT' or str(ch)=='Chat' or str(ch)=='chat'):
		time.sleep(2)
		subprocess.call('espeak "FEEL FREE AS YOU CHAT TO YOUR VIRTUAL FRIEND"',shell=True)
		print('\nFEEL FREE AS YOU CHAT TO YOUR VIRTUAL FRIEND\n')
		time.sleep(2)
		subprocess.call('espeak "Enter your message to start chatting to the bot"',shell=True)
		print('Enter your message to start chatting to the bot\n')
		while True:
		
			print('  You:  ')
			request =input()
			
			if( str(request) != ''):
				response = bot.get_response(request)
				#subprocess.call(request, shell=True)
				if str(response) != '':
					if (request.strip() != 'Bye' or request.strip() != 'BYE' or request.strip() != 'Goodbye' or request.strip() != 'GoodBye' or request.strip() != 'goodbye' or request.strip() != 'GOODBYE'or request.strip() != 'bye'):
			
	
						print('  Bot:  ')
						print(response)

					if (request.strip() == 'Bye'  or request.strip() == 'BYE' or request.strip() == 'GoodBye' or request.strip() == 'goodbye' or request.strip() == 'GoodBye' or request.strip() == 'GOODBYE'or request.strip() == 'bye'):
						print('  Bot:  ')
						subprocess.call('espeak "Goodbye, it was nice chatting to you"',shell=True)
						print('\nGoodbye, it was nice chatting to you')
						time.sleep(3)
						break
	
				else:
					subprocess.call('espeak "I have no idea what that means,, Would you please teach me how to respond on that"',shell=True)
					print('\n  Bot: \nI have no idea what that means,, Would you please teach me how to respond on that\n')
		
					while True:
						possibleAnwser =input()
						if str(possibleAnwser) != '':
							print('Is ('+possibleAnwser +') the correct way of aswering that question? enter [y/n]')
							choice = input()
							if (choice.strip() == 'y' or choice.strip() == 'yes' or choice.strip() == 'Y' or choice.strip() == 'YES' or choice.strip() == 'Yes'):
								with open('data_files/newdata.txt','a') as f:
									f.write(request+'\n')
									f.write(possibleAnwser+'\n\n')
									f.flush()
									f.flush()
									MIT4 = open('data_files/newdata.txt','r').readlines()
									bot.train(MIT4)
									break
							else:
								subprocess.call('espeak "Enter the correct respond please"',shell=True)
								print('Enter the correct respond please')
						else:
							subprocess.call('espeak "Please teach me how to answer that question"',shell=True)
							print('\n  Bot:  \nPlease teach me how to answer that question\n')
			
					subprocess.call('espeak "THANK YOU! NOW I KNOW"',shell=True)	
					print('\n  Bot:  \nTHANK YOU!! NOW I KNOW\n')
			else:
				subprocess.call('espeak "Enter something please"',shell=True)	
				print('\n  Bot:\nEnter something please')
	if(ch.strip() == 'google' or ch.strip() == 'Google' or ch.strip() == 'GOOGLE'):

		options = Options()

		options.add_argument("--headless")
		try:
			driver = webdriver.Firefox(firefox_options=options)
		except FileNotFoundError:
			driver = webdriver.Firefox(firefox_options=options, executable_path='/usr/local/bin/geckodriver')
		print("\nFIREFOX HEADLESS BROWER INVOKED!")
		while True:
			print('\nINPUT YOUR SEARCH QUERY TO SEARCH OR ENTER [EXIT] TO QUIT THE GOOGLE SEARCH\n')
			inputedQuery= input()
			#subprocess.call(str(inputedQuery), shell=True)
			if (inputedQuery.strip() == 'exit' or inputedQuery.strip() == 'EXIT' or inputedQuery.strip() == 'Exit'):
				subprocess.call('espeak "EXITING FROM GOOGLE SEARCH...."',shell=True)	
				print('EXITING FROM GOOGLE SEARCH....')
				time.sleep(3)
				break

			else:
		
				CustomizeSearchQueary = inputedQuery.replace(' ','+')
				driver.get('http://www.google.com/search?q=' + CustomizeSearchQueary)
				results = driver.execute_script("""return document.elementFromPoint(arguments[0],arguments[1],arguments[2]);""", 350, 230,230).text
				with open('data_files/searchHistory.txt','a') as f:
					f.write(inputedQuery+'\n')
					f.write(results+'\n\n')
					f.close()
				#subprocess.call(str(results), shell=True)
				print (results)
	


	else:
		subprocess.call('espeak "Enter your choice [CHAT or GOOGLE]"',shell=True)	
		print('Enter your choice [CHAT or GOOGLE]')
	
			


