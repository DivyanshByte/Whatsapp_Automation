from selenium import webdriver
import sys
driver = webdriver.Edge(executable_path = 'H:\\edgedriver_win64\\Edge.exe')
driver.get('https://web.whatsapp.com/')
input('Enter anything after scanning QR code: ')
while(True):
	pyn = int(input("Mode 1 -> Single, 2-> Many, 3-> Exit: "))
	if pyn == 1:
		name = input('Enter the name of user or group : ')
		user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
		user.click()

		option = int(input("What Do You Want To Send (1 - Text Message, 2 - Video/Image, 3 - Document, Any Other No. - Exit): "))

		if option == 1:
			msg = input('Enter your message : ')
			count = int(input('Enter the count : '))
			msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
			for i in range(count):
			    msg_box.send_keys(msg)
			    button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]")
			    button.click()

		elif option ==2:
			vim = input("Enter The Path Of The File: ")
			cm = input("Enter Caption(Press Only Enter To add No Caption): ")
			ab = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]')
			ab.click()
			vib = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input')
			vib.send_keys(vim)
			cb = driver.find_element_by_class_name("_2S1VP")
			cb.send_keys(cm)
			vibs = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
			vibs.click()

		elif option == 3:
			dm = input("Enter The Path Of The File: ")
			cm = input("Enter Caption(Press Only Enter To add No Caption): ")
			ab = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]')
			ab.click()
			db = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button/input')
			db.send_keys(dm)
			cb = driver.find_element_by_class_name("_2S1VP")
			cb.send_keys(cm)
			dbs = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
			dbs.click()
		else:
			sys.exit()


	elif pyn == 2:
		un = int(input("Enter The Number of Users or Groups: "))
		names = []
		for unn in range(un):
			namei = input('Enter the name of user or group ' + str(unn) + ": ")
			names.append(namei)
		option = int(input("What Do You Want To Send (1 - Text Message, 2 - Video/Image, 3 - Document, Any Other No. - Exit): "))
		if option == 1:
			msg = input('Enter your message : ')
			count = int(input('Enter the count : '))

		elif option ==2:
			vim = input("Enter The Path Of The File: ")
			cm = input("Enter Caption(Press Only Enter To add No Caption): ")

		elif option == 3:
			dm = input("Enter The Path Of The File: ")
			cm = input("Enter Caption(Press Only Enter To add No Caption): ")

		else:
			sys.exit()

		for name in names:
			user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
			user.click()

			if option == 1:
				msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
				for i in range(count):
				    msg_box.send_keys(msg)
				    button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]")
				    button.click()

			elif option ==2:
				ab = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]')
				ab.click()
				vib = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input')
				vib.send_keys(vim)
				cb = driver.find_element_by_class_name("_2S1VP")
				cb.send_keys(cm)
				vibs = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
				vibs.click()

			elif option == 3:
				ab = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]')
				ab.click()
				db = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button/input')
				db.send_keys(dm)
				cb = driver.find_element_by_class_name("_2S1VP")
				cb.send_keys(cm)
				dbs = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
				dbs.click()


	else:
		sys.exit()







