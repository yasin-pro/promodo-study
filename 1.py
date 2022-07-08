import os

import pyfiglet

import time

from tqdm import tqdm

from datetime import datetime

from playsound import playsound

from colorama import Fore, Back, Style

# class for beep
class Beep:

	# constructer
	def __init__(self):
		pass

	# a method for give current time
	def current(self):

		now = datetime.now()

		current_time = now.strftime("%H:%M:%S")

		return current_time

	# a method for give 20m after current time
	def after_current_twenty(self):

		now = datetime.now()

		final_min = int(now.strftime("%M")) + 25

		current_time = now.strftime("%H:%M:%S")

		time_list = current_time.split(':')

		time_list[1] = str(final_min)

		final_time = ':'.join(time_list)

		return final_time

	# a method for start promodor
	def start(self , count):

		self.count = count

		if self.count == 3:

			print()
			print(Fore.GREEN+' [+] ' + Fore.WHITE+'Your are done ;)'+Style.RESET_ALL)
			print()
			print()
			print(Fore.GREEN+' [+] ' + Fore.WHITE+'Go rest 30 min'+Style.RESET_ALL)
			print()

			self.close()

		print()
		print(Fore.GREEN+' [+] ' + Fore.WHITE+'Start your task :)'+Style.RESET_ALL)
		print()

		final_time = self.after_current_twenty()

		status_promodo = True

		status_progress = True

		while status_promodo :

			current_time = self.current()

			if current_time == final_time:

				print()
				print(Fore.RED+' [-] ' + Fore.WHITE+'Go to rest 5 min :)'+Style.RESET_ALL)
				print()

				playsound('beep.mp3')

				for i in tqdm(range(0, int(5*59.5)), desc =">>>"):

					time.sleep(1.0)

				os.system("clear")

				self.count += 1

				self.start(self.count)

				status_promodo =  False

			else:

				if status_progress : 

					for i in tqdm(range(0, int(25*59.5)), desc =">>>"):

						time.sleep(1.0)

					status_progress = False

					status_promodo = True

			
	# a method for close program
	def close(self):

		exit()

# Main Function
def main():

	os.system("clear")

	beep = Beep()

	print()
	print('****************************************************************')  
	print()
	print(Fore.RED + pyfiglet.figlet_format("Dirty - Hacker") + Style.RESET_ALL)
	print()
	print('****************************************************************')
	print("\n*          My github is : https://github.com/yasin-pro/        *")
	print()
	print('****************************************************************')
	print()

	print()
	question = input(Fore.RED+' [?] ' + Fore.WHITE+'Are you want to start ? '+Style.RESET_ALL)
	print()

	if question == 'Y' or question == 'y' :

		beep.start(0)

if __name__=='__main__' : main()