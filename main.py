import os
import sys
import mysql.connector as mysqCon
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from mysql.connector import Error
from mysql.connector import errorcode
from PIL import Image, ImageTk

try:
	import pyautogui
except:
	import pip
	pip.main(['install', 'pyautogui'])
	pip.main(['install', 'Xlib'])
	import pyautogui

host1 = "****"
database1 = "****"
user1 = "****"
password1 = "****"


def ask_for_Db():
	window1 = Tk(className = "DATABASE")
	window1.tk.call('wm', 'iconphoto', window1._w, PhotoImage(file = 'image/SIT.png'))
	window1.geometry("380x160")
	window1.title("GIVE INFORAMATION ABOUT DATABASE")
	window1.attributes("-topmost", True)

	F0 = Frame(window1, relief = SUNKEN)
	F0.pack(side = LEFT)

	l1 = ["host", "database", "user"]
	l2 = ["HOST", "DATABASE", "USER"]
	entries = []

	for i in range(len(l1)):
		exec("%s2 = Label(F0, font = ('OpenSansCondensed', 12), text = \"  ENTER THE %s:\", width = 30, anchor = \"w\")"%(l1[i], l2[i]))
		exec("%s2.grid(row = %s, column = 0)"%(l1[i], i))
		exec("%sEntry2 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = \"\", insertwidth = 4, justify = 'right')"%(l1[i]))
		exec("%sEntry2.grid(row = %s, column = 1)"%(l1[i], i))
		exec("entries.append(%sEntry2)"%(l1[i]))
	
	password2 = Label(F0, font = ('OpenSansCondensed', 12), text = "  ENTER THE PASSWORD:", width = 30, anchor = "w")
	password2.grid(row = 3, column = 0)
	passwordEntry2 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = "", insertwidth = 4, justify = 'right', show = "*")
	passwordEntry2.grid(row = 3, column = 1)
	
	submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = " OK ", command = lambda: [f for f in [submit_for_db([entry.get() for entry in entries], passwordEntry2.get()), window1.destroy()]])

	submitBtn.grid(row = 4, column = 0)
	window1.mainloop()


def submit_for_db(l1, password_enterred):
	global host1
	global database1
	global user1
	global password1
	host1 = l1[0]
	database1 = l1[1]
	user1 = l1[2]
	password1 = password_enterred
	
def check():
	try:
		db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
		if db.is_connected():
			cursor = db.cursor()
			row = cursor.fetchone()
			db.close()
	except Error as e:
		messagebox.showwarning("ERROR", "THE DATABASE INFORMATION IS WRONG")
		db.close()
		sys.exit()


class checkDb:
	def checkDb():
		if(checkDb.check()):
			window = Tk(className = "CREATE TABLE")
			window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file = 'image/SIT.png'))
			window.geometry("400x100")
			window.title("Create Table in Database")
			window.attributes("-topmost", True)

			Fram1 = Frame(window, relief = SUNKEN)
			Fram1.pack(side = TOP)

			labe1 = Label(Fram1, font = ('OpenSansCondensed', 16, 'bold'), text = "Please click OK button to Create the Table")
			labe1.grid(row = 0, column = 0)

			labe2 = Label(Fram1, font = ('OpenSansCondensed', 10, 'bold'), text = "(If Table isn't created this won't work properly)")
			labe2.grid(row = 1, column = 0)

			create = Button(Fram1, font = ('OpenSansCondensed', 10), width = 10, text = "Create Table", command = lambda: [f() for f in [checkDb.createDb, window.destroy]])
			create.grid(row = 2, column = 0)
			window.mainloop()

	def check():
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor(buffered = True)
				li = ["STUDENT_INFORMATION", "PHOTO", "BOOK"]
				for i in range(len(li)):
					sql = "SELECT * FROM %s"%(li[i])
					cursor.execute(sql)
				db.close()
				return False
		except Error as e:
			db.close()
			return True

	def createDb():
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				cursor.execute("DROP TABLE IF EXISTS STUDENT_INFORMATION")
				cursor.execute("DROP TABLE IF EXISTS PHOTO")
				cursor.execute("DROP TABLE IF EXISTS BOOK")
				sql = "CREATE TABLE STUDENT_INFORMATION(\
						 USN CHAR(10) NOT NULL, \
						 NAME CHAR(18) NOT NULL, \
						 BRANCH CHAR(3) NOT NULL, \
						 SEM CHAR(1) NOT NULL, \
						 ADDRESS CHAR(30) NOT NULL, \
						 PH_NO CHAR(12) NOT NULL, \
						 PROCTOR CHAR(18) NOT NULL)"
				cursor.execute(sql)
				sql = "CREATE TABLE PHOTO(\
						USN CHAR(10) NOT NULL, \
						PHOTO BLOB NOT NULL)"
				cursor.execute(sql)
				sql = "CREATE TABLE BOOK(\
						BOOK_ID CHAR(10) NOT NULL, \
						BOOK_NAME CHAR(20) NOT NULL, \
						BOOK_AUTHOR CHAR(20) NOT NULL, \
						BOOK_DETAILS CHAR(40) NOT NULL)"
				cursor.execute(sql)
				db.commit()
				messagebox.showinfo("CREATE TABLE", "Table was created successfully")
				db.close()
		except Error as e:
			messagebox.showwarning("CAN'T CREATE TABLE", "Table wasn't created due to the error")
			db.close()
			sys.exit()


class admin:
	def admin():
		if(admin.admin_check()):
			window1 = Tk(className = "PASSWORD")
			window1.tk.call('wm', 'iconphoto', window1._w, PhotoImage(file = 'image/SIT.png'))
			window1.geometry("400x70")
			window1.title("PASSWORD FOR THE ADMIN")
			window1.attributes("-topmost", True)
			
			F0 = Frame(window1, relief = SUNKEN)
			F0.pack(side = LEFT)

			password_id1 = Label(F0, font = ('OpenSansCondensed', 12), text = "ENTER THE PASSWORD:", width = 35, anchor = "w")
			password_id1.grid(row = 0, column = 0)
			password_idEntry1 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = "", insertwidth = 4, justify = 'right', show = '*')
			password_idEntry1.grid(row = 0, column = 1)

			submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "SUBMIT", command = lambda: [f for f in [admin.adminDb(password_idEntry1.get()), window1.destroy()]])
			submitBtn.grid(row = 4, column = 0)

			window1.mainloop()

	def admin_check():
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor(buffered = True)
				sql = "SELECT * FROM ADMIN"
				cursor.execute(sql)
				db.close()
				return False
		except Error as e:
			db.close()
			return True

	def adminDb(admin_password):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				sql = "DROP TABLE IF EXISTS ADMIN"
				cursor.execute(sql)
				sql = "CREATE TABLE ADMIN(\
					     PASSWORD CHAR(50) NOT NULL)"
				cursor.execute(sql)
				sql = "INSERT INTO ADMIN(PASSWORD) VALUES('%s')"%(admin_password)
				cursor.execute(sql)
				db.commit()
				messagebox.showinfo("PASSWORD", "Password was stored successfully")
				db.close()
		except Error as e:
			messagebox.showwarning("PASSWORD", "There was a error storing the password")
			db.close()
			sys.exit()


def findSize():
	s = pyautogui.size()
	s = str(s[0]) + "x" + str(s[1])
	return s


def developer():
	window1 = Tk(className = "DEVELOPER")
	window1.geometry("700x150")
	window1.title("DEVELOPER INFORAMATION")
	window1.attributes("-topmost", True)

	F0 = Frame(window1, relief = SUNKEN)
	F0.pack(side = TOP)

	l1 = ["name", "email", "website", "copyright1", "copyright2"]
	l2 = ["Name: SUBRAMANYA G", "Email: subramanyag@outlook.com", "Website: https://subramanyag1234567.wixsite.com/website", "This code is public domain(no copyright)", "You can do whatever you want with it"]
	for i in range(len(l1)):
		exec("%s = Label(F0, font = ('SahadevaItalic', 16), text = \"%s\", fg = \"steel blue\")"%(l1[i], l2[i]))
		exec("%s.grid(row = %s, column = 0)"%(l1[i], i))

	window1.mainloop()


def convertToBinaryData(filename):
	try:		
		#Convert digital data to binary format
		with open(filename, 'rb') as file:
			binaryData = file.read()
		return binaryData
	except:
		messagebox.showwarning("ERROR", "CAN'T FIND THE LOCATION")


def convertToProperFormat(data, filename):
	try:
		# Convert binary data to proper format and write it on Hard Disk
		with open(filename, 'wb') as file:
			file.write(data)
	except:
		messagebox.showwarning("ERROR", "CAN'T FIND THE LOCATION")


class Information:
	def get_name(usn):
		return Information.ask(usn, "NAME")[0]

	def get_branch(usn):
		return Information.ask(usn, "BRANCH")

	def get_sem(usn):
		return Information.ask(usn, "SEM")

	def get_address(usn):
		return Information.ask(usn, "ADDRESS")[0]

	def get_phno(usn):
		return Information.ask(usn, "PH_NO")

	def get_proctor(usn):
		return Information.ask(usn, "PROCTOR")[0]

	def ask(usn, information):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				sql = "SELECT %s FROM STUDENT_INFORMATION WHERE USN = '%s'"%(information, usn)
				cursor.execute(sql)
				results = cursor.fetchall()
				return results[0]
		except IndexError:
			messagebox.showwarning("CAN'T FIND STUDENT", "THE USN ISN'T CORRECT")
			db.rollback()
		except Error as e:
			messagebox.showwarning("CAN'T FIND STUDENT", "THERE IS SOME ERROR")
			db.rollback()
		finally:
			db.close()

	def get_information_book(book_id):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				sql = "SELECT * FROM BOOK WHERE BOOK_ID = '%s'"%(book_id)
				cursor.execute(sql)
				results = cursor.fetchall()
				db.commit()
				db.close()
				return results[0]
		except Error as e:
			messagebox.showwarning("CAN'T FIND INFORMATION", "THERE IS SOME ERROR")
			db.rollback()
			db.close()

	def infBook(usn):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				sql = "SELECT * FROM %s"%(usn)
				cursor.execute(sql)
				results = cursor.fetchall()
				for i in range(len(results)):
					results[i] = Information.get_information_book(results[i][0])
				db.close()
				return results
		except Error as e:
			print(e)
			db.rollback()
			db.close()

	def retrivePhoto(usn):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			cursor = db.cursor(prepared = True)
			sql_fetch_blob_query = """SELECT * from PHOTO where USN = %s"""
			cursor.execute(sql_fetch_blob_query, (usn, ))
			record = cursor.fetchall()
			photo = "image/" + usn + ".png"
			image = record[0][1]
			convertToProperFormat(image, photo)
		except mysqCon.Error as error :
			messagebox.showwarning("CAN'T FIND STUDENT", "THERE IS SOME PROBLEM WITH THE PHOTO")
			db.rollback()
		finally:
			if(db.is_connected()):
				cursor.close()
				db.close()


class BookBank:
	def __init__(self):
		self.root = Tk(className = "Digital Library")
		self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file = 'image/SIT.png'))
		self.root.title("Digital Library")
		s = findSize() 
		self.root.geometry(s)

		menubar = Menu(self.root)
		self.root.config(menu = menubar)
		
		adminMenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Admin", menu = adminMenu)
		adminMenu.add_command(label = "Login to Admin", command = self.login)

		helpMenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Help", menu = helpMenu)
		helpMenu.add_command(label = "Developer", command = developer)

		exitMenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Exit", menu = exitMenu)
		exitMenu.add_command(label = "Quit", command = self.root.destroy)

		Heading = Frame(self.root, width = 100, height = 100, relief = SUNKEN)
		Heading.pack(side = TOP)

		label1 = Label(Heading, font = ('OpenSansCondensed', 30, 'bold'), text = "SIDDAGANGA INSTITUTE OF TECHNOLOGY")
		label1.grid(row = 0, column = 0)

		label2 = Label(Heading, font = ('OpenSansCondensed', 16, 'bold'), text = "B H Road, Tumakuru-572103. Karnataka")
		label2.grid(row = 1, column = 0)

		collegeImage = PhotoImage(file = "image/SIT.png")

		canvas = Canvas()
		canvas.create_image(101, 101, image = collegeImage)
		canvas["width"] = 200
		canvas["height"] = 200
		canvas.pack()
 
		frame0 = Frame(self.root)
		frame0.pack(side = LEFT)

		usn = Label(frame0, font = ('OpenSansCondensed', 20), text = "  USN", width = 15, anchor = "w")
		usn.grid(row = 0, column = 0)

		self.usnEntry = Entry(frame0, font = ('OpenSansCondensed', 20), textvariable = "", insertwidth = 4, justify = 'right')
		self.usnEntry.grid(row = 0, column = 1)

		submitBtn = Button(frame0, padx = 16, pady = 5, font = ('OpenSansCondensed', 16), width = 8, text = "Submit", command = self.Submit)
		submitBtn.grid(row = 0, column = 2)

		l1 = ["name", "branch", "sem", "address", "phno", "proctor"]
		l2 = ["Name", "Branch", "Sem", "Address", "Phone Number", "Proctor Name"]
		
		for i in range(len(l1)):
			exec("%s = Label(frame0, font = ('OpenSansCondensed', 20), text = \"  %s\", width = 15, anchor = \"w\")"%(l1[i], l2[i]))
			exec("%s.grid(row = %s, column = 0)"%(l1[i], i+1))
			exec("self.%sDisplay = Label(frame0, font = ('OpenSansCondensed', 20), text = \"\", anchor = \"w\")"%(l1[i]))
			exec("self.%sDisplay.grid(row = %s, column = 1)"%(l1[i], i+1))
		
		self.img = Label(image = "")
		self.img.place(x = 1600, y = 150)

		frame1 = Frame(self.root, width = 800, height = 700, relief = SUNKEN)
		frame1.pack(side = RIGHT)

		slno0 = Label(frame1, font = ('OpenSansCondensed', 16), text = "Sl.No", width = 10)
		slno0.grid(row = 0, column = 0)
		id0 = Label(frame1, font = ('OpenSansCondensed', 16), text = "ID", width = 10)
		id0.grid(row = 0, column = 1)
		name0 = Label(frame1, font = ('OpenSansCondensed', 16), text = "BOOK NAME", width = 30)
		name0.grid(row = 0, column = 2)
		author0 = Label(frame1, font = ('OpenSansCondensed', 16), text = "BOOK AUTHOR", width = 20)
		author0.grid(row = 0, column = 3)
		details0 = Label(frame1, font = ('OpenSansCondensed', 16), text = "BOOK DETAILS", width = 30)
		details0.grid(row = 0, column = 4)
		
		for i in range(1, 6):
			exec("self.slno%s = Label(frame1, font = ('OpenSansCondensed', 16), text = \"\", width = 10)"%(i))
			exec("self.slno%s.grid(row = %s, column = 0)"%(i, i))
			exec("self.id%s = Label(frame1, font = ('OpenSansCondensed', 16), text = \"\", width = 10)"%(i))
			exec("self.id%s.grid(row = %s, column = 1)"%(i, i))
			exec("self.name%s = Label(frame1, font = ('OpenSansCondensed', 16), text = \"\", width = 30)"%(i))
			exec("self.name%s.grid(row = %s, column = 2)"%(i, i))
			exec("self.author%s = Label(frame1, font = ('OpenSansCondensed', 16), text = \"\", width = 20)"%(i))
			exec("self.author%s.grid(row = %s, column = 3)"%(i, i))
			exec("self.details%s = Label(frame1, font = ('OpenSansCondensed', 16), text = \"\", width = 30)"%(i))
			exec("self.details%s.grid(row = %s, column = 4)"%(i, i))
		
		borrowBtn = Button(frame1, padx = 16, pady = 5, font = ('OpenSansCondensed', 16), width = 8, text = "Borrow", command = self.borrow_book)
		borrowBtn.grid(row = 6, column = 1)

		returnBtn = Button(frame1, padx = 16, pady = 5, font = ('OpenSansCondensed', 16), width = 10, text = "Return", command = self.return_book)
		returnBtn.grid(row = 6, column = 3)

		self.root.mainloop()	

	def login(self):
		self.window1 = Tk(className = "LOGIN")
		self.window1.title("PASSWORD")
		self.window1.geometry("400x70")
		self.window1.attributes("-topmost", True)
		
		F0 = Frame(self.window1, relief = SUNKEN)
		F0.pack(side = LEFT)

		password_id1 = Label(F0, font = ('OpenSansCondensed', 12), text = "ENTER THE PASSWORD:", width = 35, anchor = "w")
		password_id1.grid(row = 0, column = 0)
		password_idEntry1 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = "", insertwidth = 4, justify = 'right', show = '*')
		password_idEntry1.grid(row = 0, column = 1)

		submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "LOGIN", command = lambda: [f for f in [self.login1(password_idEntry1.get())]])
		submitBtn.grid(row = 4, column = 0)

		self.window1.mainloop()

	def login1(self, password):
		password_for_admin = self.get_password()
		password_enterred_admin = password
		if(password_enterred_admin == password_for_admin):
			self.window1.destroy()
			self.root.destroy()
			Admin()
		else:
			messagebox.showwarning("ERROR", "Wrong password")

	def get_password(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				sql = "SELECT * FROM ADMIN"
				cursor.execute(sql)
				results = cursor.fetchall()
				db.commit()
				db.close()
				return results[0][0]
		except Error as e:
			print(e)
			db.rollback()
			db.close()
	
	def showImg(self):
		img = "image/" + self.usnEntry.get().upper() + ".png"
		load = Image.open(img)
		render = ImageTk.PhotoImage(load)

		self.img = Label(image = render)
		self.img.image = render
		self.img.place(x = 1600, y = 150)

	def clear_Label(self):
		self.img.config(image = "")

	def Submit(self):
		usn1 = self.usnEntry.get().upper()
		self.nameDisplay["text"] = ""
		self.branchDisplay["text"] = ""
		self.semDisplay["text"] = ""
		self.addressDisplay["text"] = ""
		self.phnoDisplay["text"] = ""
		self.proctorDisplay["text"] = ""
		self.clear_Label()

		for i  in range(1, 6):
			exec("self.slno%s[\"text\"] = \"\""%(i))
			exec("self.id%s[\"text\"] = \"\""%(i))
			exec("self.name%s[\"text\"] = \"\""%(i))
			exec("self.author%s[\"text\"] = \"\""%(i))
			exec("self.details%s[\"text\"] = \"\""%(i))
		
		self.nameDisplay["text"] = Information.get_name(usn1)
		self.branchDisplay["text"] = Information.get_branch(usn1)
		self.semDisplay["text"] = Information.get_sem(usn1)
		self.addressDisplay["text"] = Information.get_address(usn1)
		self.phnoDisplay["text"] = Information.get_phno(usn1)
		self.proctorDisplay["text"] = Information.get_proctor(usn1)
		Information.retrivePhoto(usn1)
		self.showImg()
		os.remove("image/" + usn1 + ".png")

		li0 = Information.infBook(usn1)
		for i in range(1, 6):
			if(len(li0) > (i-1)):
				exec("self.slno%s[\"text\"] = (%s)"%(i, i))
				exec("self.id%s[\"text\"] = li0[%s][0]"%(i, i-1))
				exec("self.name%s[\"text\"] = li0[%s][1]"%(i, i-1))
				exec("self.author%s[\"text\"] = li0[%s][2]"%(i, i-1))
				exec("self.details%s[\"text\"] = li0[%s][3]"%(i, i-1))

	def borrow_book(self):
		usn1 = self.usnEntry.get().upper()
		if(len(Information.infBook(usn1)) < 5):	
			window1 = Tk(className = "BORROW BOOK")
			window1.geometry("400x70")
			window1.title("BORROW A BOOK")
			window1.attributes("-topmost", True)

			F0 = Frame(window1, relief = SUNKEN)
			F0.pack(side = LEFT)

			book_id1 = Label(F0, font = ('OpenSansCondensed', 12), text = "  ENTER THE BOOK ID:", width = 35, anchor = "w")
			book_id1.grid(row = 0, column = 0)
			self.book_idEntry1 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = "", insertwidth = 4, justify = 'right')
			self.book_idEntry1.grid(row = 0, column = 1)

			submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "BORROW", command = lambda: [f() for f in [self.borrowBookDb, self.Submit, window1.destroy]])
			submitBtn.grid(row = 4, column = 0)
			window1.mainloop()
		else:
			messagebox.showwarning("CAN'T BORROW A BOOK", "Only 5 books are given for a Student")

	def borrowBookDb(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				usn1 = self.usnEntry.get().upper()
				sql = "INSERT INTO %s(BOOK_ID)\
					 VALUES('%s')"%\
					 (usn1, self.book_idEntry1.get())
				cursor.execute(sql)
				db.commit()
				messagebox.showinfo("BORROW A BOOK", "THE BOOK WAS BORROWED SUCCESSFULLY")
		except Error as e:
			messagebox.showwarning("CAN'T BORROW A BOOK1", "There is some error in the information provided")
			db.rollback()
		finally:
			db.close()

	def return_book(self):
		usn1 = self.usnEntry.get().upper()
		if(len(Information.infBook(usn1)) > 0):	
			window1 = Tk(className = "RETURN BOOK")
			window1.geometry("400x70")
			window1.title("RETURN THE BOOK")
			window1.attributes("-topmost", True)
			
			F0 = Frame(window1, relief = SUNKEN)
			F0.pack(side = LEFT)

			book_id1 = Label(F0, font = ('OpenSansCondensed', 12), text = "ENTER THE BOOK ID:", width = 35, anchor = "w")
			book_id1.grid(row = 0, column = 0)
			self.book_idEntry1 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = "", insertwidth = 4, justify = 'right')
			self.book_idEntry1.grid(row = 0, column = 1)

			submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "RETURN", command = lambda: [f() for f in [self.returnBookDb, self.Submit, window1.destroy]])
			submitBtn.grid(row = 4, column = 0)

			window1.mainloop()
		else:
			messagebox.showwarning("CAN'T RETURN A BOOK", "Student hasn't taken any book to return")

	def returnBookDb(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				usn1 = self.usnEntry.get().upper()
				sql = "DELETE FROM %s WHERE BOOK_ID = '%s'"%(usn1, self.book_idEntry1.get())
				cursor.execute(sql)
				db.commit()
				messagebox.showinfo("DELETE A BOOK", "THE BOOK WAS DELETED SUCCESSFULLY")
		except Error as e:
			messagebox.showwarning("CAN'T DELETE A BOOK", "THE BOOK ID DOESN'T EXIST")
			db.rollback()
		finally:
			db.close()


class Admin:
	def __init__(self):
		root = Tk(className = "Digital Library")
		root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file = 'image/SIT.png'))
		root.title("Digital Library")
		s = findSize() 
		root.geometry(s)

		menubar = Menu(root)
		root.config(menu = menubar)
		
		studentOperationMenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Student Operation", menu = studentOperationMenu)
		studentOperationMenu.add_command(label = "Add a Student", command = self.add)
		studentOperationMenu.add_command(label = "Change a Student Information", command = self.change)
		studentOperationMenu.add_command(label = "Delete a Student", command = self.delete)

		databaseMenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Table", menu = databaseMenu)
		databaseMenu.add_command(label = "Create the Table(It will delete if it already exists)", command = checkDb.createDb)
		databaseMenu.add_command(label = "Delete the Table", command = self.deleteDb)

		bookMenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Book", menu = bookMenu)
		bookMenu.add_command(label = "Add a Book", command = self.add_book)
		bookMenu.add_command(label = "Delete a Book", command = self.delete_book)

		displayMenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Table", menu = displayMenu)
		displayMenu.add_command(label = "Show all students", command = self.show_students)
		displayMenu.add_command(label = "Show all books", command = self.show_books)

		helpMenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Help", menu = helpMenu)
		helpMenu.add_command(label = "Developer", command = developer)

		exitMenu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Exit", menu = exitMenu)
		exitMenu.add_command(label = "Quit", command = root.destroy)
		exitMenu.add_command(label = "Log out as Admin", command = lambda: [f() for f in [root.destroy, BookBank]])

		Heading = Frame(root, width = 100, height = 100, relief = SUNKEN)
		Heading.pack(side = TOP)

		label1 = Label(Heading, font = ('OpenSansCondensed', 30, 'bold'), text = "SIDDAGANGA INSTITUTE OF TECHNOLOGY")
		label1.grid(row = 0, column = 0)

		label2 = Label(Heading, font = ('OpenSansCondensed', 16, 'bold'), text = "B H Road, Tumakuru-572103. Karnataka")
		label2.grid(row = 1, column = 0)

		collegeImage = PhotoImage(file = "image/SIT.png")

		canvas = Canvas()
		canvas.create_image(101, 101, image = collegeImage)
		canvas["width"] = 200
		canvas["height"] = 200
		canvas.pack()
 
		frame0 = Frame(root)
		frame0.pack(side = LEFT)

		usn = Label(frame0, font = ('OpenSansCondensed', 20), text = "  USN", width = 15, anchor = "w")
		usn.grid(row = 0, column = 0)

		self.usnEntry = Entry(frame0, font = ('OpenSansCondensed', 20), textvariable = "", insertwidth = 4, justify = 'right')
		self.usnEntry.grid(row = 0, column = 1)

		submitBtn = Button(frame0, padx = 16, pady = 5, font = ('OpenSansCondensed', 16), width = 8, text = "Submit", command = self.Submit)
		submitBtn.grid(row = 0, column = 2)

		l1 = ["name", "branch", "sem", "address", "phno", "proctor"]
		l2 = ["Name", "Branch", "Sem", "Address", "Phone Number", "Proctor Name"]
		
		for i in range(len(l1)):
			exec("%s = Label(frame0, font = ('OpenSansCondensed', 20), text = \"  %s\", width = 15, anchor = \"w\")"%(l1[i], l2[i]))
			exec("%s.grid(row = %s, column = 0)"%(l1[i], i+1))
			exec("self.%sDisplay = Label(frame0, font = ('OpenSansCondensed', 20), text = \"\", anchor = \"w\")"%(l1[i]))
			exec("self.%sDisplay.grid(row = %s, column = 1)"%(l1[i], i+1))
	
		self.img = Label(image = "")
		self.img.place(x = 1600, y = 150)

		frame1 = Frame(root, width = 800, height = 700, relief = SUNKEN)
		frame1.pack(side = RIGHT)

		slno0 = Label(frame1, font = ('OpenSansCondensed', 16), text = "Sl.No", width = 10)
		slno0.grid(row = 0, column = 0)
		id0 = Label(frame1, font = ('OpenSansCondensed', 16), text = "ID", width = 10)
		id0.grid(row = 0, column = 1)
		name0 = Label(frame1, font = ('OpenSansCondensed', 16), text = "BOOK NAME", width = 30)
		name0.grid(row = 0, column = 2)
		author0 = Label(frame1, font = ('OpenSansCondensed', 16), text = "BOOK AUTHOR", width = 20)
		author0.grid(row = 0, column = 3)
		details0 = Label(frame1, font = ('OpenSansCondensed', 16), text = "BOOK DETAILS", width = 30)
		details0.grid(row = 0, column = 4)
		
		for i in range(1, 6):
			exec("self.slno%s = Label(frame1, font = ('OpenSansCondensed', 16), text = \"\", width = 10)"%(i))
			exec("self.slno%s.grid(row = %s, column = 0)"%(i, i))
			exec("self.id%s = Label(frame1, font = ('OpenSansCondensed', 16), text = \"\", width = 10)"%(i))
			exec("self.id%s.grid(row = %s, column = 1)"%(i, i))
			exec("self.name%s = Label(frame1, font = ('OpenSansCondensed', 16), text = \"\", width = 30)"%(i))
			exec("self.name%s.grid(row = %s, column = 2)"%(i, i))
			exec("self.author%s = Label(frame1, font = ('OpenSansCondensed', 16), text = \"\", width = 20)"%(i))
			exec("self.author%s.grid(row = %s, column = 3)"%(i, i))
			exec("self.details%s = Label(frame1, font = ('OpenSansCondensed', 16), text = \"\", width = 30)"%(i))
			exec("self.details%s.grid(row = %s, column = 4)"%(i, i))
		
		borrowBtn = Button(frame1, padx = 16, pady = 5, font = ('OpenSansCondensed', 16), width = 8, text = "Borrow", command = lambda: [self.borrow_book()])
		borrowBtn.grid(row = 6, column = 1)

		returnBtn = Button(frame1, padx = 16, pady = 5, font = ('OpenSansCondensed', 16), width = 10, text = "Return", command = lambda: [self.return_book()])
		returnBtn.grid(row = 6, column = 3)

		root.mainloop()	

	def addDb(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				usn2 = self.usnEntry1.get().upper()
				sql = "INSERT INTO STUDENT_INFORMATION(USN, NAME, BRANCH, SEM, ADDRESS, PH_NO, PROCTOR)\
					   VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')"%\
					   (usn2, self.nameEntry1.get(), self.branchEntry1.get(), self.semEntry1.get(), self.addressEntry1.get(), self.phnoEntry1.get(), self.proctorEntry1.get())
				cursor.execute(sql)
				cursor1 = db.cursor(prepared = True)
				sql_insert_blob_query = """INSERT INTO PHOTO(USN, PHOTO)\
										VALUES(%s, %s)"""
				Picture = convertToBinaryData(self.photoEntry1.get())
				# Convert data into tuple format
				insert_blob_tuple = (usn2, Picture)
				cursor1.execute(sql_insert_blob_query, insert_blob_tuple)
				sql = "CREATE TABLE %s(BOOK_ID CHAR(10) NOT NULL)"%(usn2)
				cursor.execute(sql)
				db.commit()
				messagebox.showinfo("ADD A STUDENT", "STUDENT BIODATA WAS ADDED SUCCESSFULLY")
		except Error as e:
			print(e)
			messagebox.showwarning("CAN'T ADD A STUDENT", "THERE IS SOME ERROR IN THE INFORMATION PROVIDED")
			db.rollback()
		finally:
			db.close()

	def set_text1(self, text):
		self.photoEntry1.delete(0, END)
		self.photoEntry1.insert(0, text)
		return

	def add(self):
		window1 = Tk(className = "ADD A STUDENT")
		window1.geometry("530x300+0+0")
		window1.title("ADD A STUDENT")
		window1.attributes("-topmost", True)
		
		F0 = Frame(window1, relief = SUNKEN)
		F0.pack(side = LEFT)

		l1 = ["usn", "name", "branch", "sem", "address", "phno", "proctor"]
		l2 = ["USN", "NAME", "BRANCH", "SEM", "ADDRESS", "PHONE NUMBER", "PROCTOR NAME"]
		
		for i in range(len(l1)):
			exec("%s1 = Label(F0, font = ('OpenSansCondensed', 12), text = \"  ENTER THE %s:\", width = 30, anchor = \"w\")"%(l1[i], l2[i]))
			exec("%s1.grid(row = %s, column = 0)"%(l1[i], i))
			exec("self.%sEntry1 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = \"\", width = 30, justify = 'right')"%(l1[i]))
			exec("self.%sEntry1.grid(row = %s, column = 1)"%(l1[i], i))

		photo1 = Label(F0, font = ('OpenSansCondensed', 12), text = "  ENTER THE PHOTO LOCATION:", width = 30, anchor = "w")
		photo1.grid(row = 7, column = 0)
		self.photoEntry1 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = "", width = 30, justify = 'right')
		self.photoEntry1.grid(row = 7, column = 1)
		
		searchPhotoBtn1 = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "Search", command = lambda: self.set_text1(filedialog.askopenfilename(filetypes = (("Photo Files", "*.png"), ("All Files", "*.*")))))
		searchPhotoBtn1.grid(row = 7, column = 2)

		submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "ADD", command = lambda: [f() for f in [self.addDb, window1.destroy]])
		submitBtn.grid(row = 8, column = 0)
		window1.mainloop()

	def changeDb(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				usn3 = self.usnEntry2.get().upper()
				l1 = ["NAME", "BRANCH", "SEM", "ADDRESS", "PH_NO", "PROCTOR"]
				l2 = [self.nameEntry2.get(), self.branchEntry2.get(), self.semEntry2.get(), self.addressEntry2.get(), self.phnoEntry2.get(), self.proctorEntry2.get()]
				for i in range(len(l1)):
					exec("cursor.execute(\"UPDATE STUDENT_INFORMATION SET %s = '%s' WHERE USN = '%s'\")"%(l1[i], l2[i], usn3))
				sql = "DELETE FROM PHOTO WHERE USN = '%s'"%(usn3)
				cursor.execute(sql)
				db.commit()
		except Error as e:
			messagebox.showwarning("CAN'T CHANGE THE STUDENT INFORMATION", "THE USN ISN'T CORRECT")
			db.rollback()
			db.close()
			return
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor1 = db.cursor(prepared = True)
				sql_insert_blob_query = """INSERT INTO PHOTO(USN, PHOTO)\
										VALUES(%s, %s)"""
				Picture = convertToBinaryData(self.photoEntry2.get())
				# Convert data into tuple format
				insert_blob_tuple = (usn3, Picture)
				cursor1.execute(sql_insert_blob_query, insert_blob_tuple)
				db.commit()
				messagebox.showinfo("CHANGE THE INFORMATION", "STUDENT BIODATA WAS CHANGED SUCCESSFULLY")
		except Error as e:
			messagebox.showwarning("CAN'T CHANGE THE STUDENT INFORMATION", "THERE IS SOME ERROR IN THE PHOTO")
			db.rollback()
		finally:
			db.close()

	def set_text2(self, text):
		self.photoEntry2.delete(0, END)
		self.photoEntry2.insert(0, text)
		return

	def change(self):
		window1 = Tk(className = "CHANGE STUDENT PROFILE")
		window1.geometry("530x300")
		window1.title("CHANGE STUDENT PROFILE")
		window1.attributes("-topmost", True)
		
		F0 = Frame(window1, relief = SUNKEN)
		F0.pack(side = LEFT)

		l1 = ["usn", "name", "branch", "sem", "address", "phno", "proctor"]
		l2 = ["USN", "NAME", "BRANCH", "SEM", "ADDRESS", "PHONE NUMBER", "PROCTOR NAME"]
		
		for i in range(len(l1)):
			exec("%s2 = Label(F0, font = ('OpenSansCondensed', 12), text = \"  ENTER THE %s:\", width = 30, anchor = \"w\")"%(l1[i], l2[i]))
			exec("%s2.grid(row = %s, column = 0)"%(l1[i], i))
			exec("self.%sEntry2 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = \"\", width = 30, justify = 'right')"%(l1[i]))
			exec("self.%sEntry2.grid(row = %s, column = 1)"%(l1[i], i))

		photo2 = Label(F0, font = ('OpenSansCondensed', 12), text = "  ENTER THE PHOTO LOCATION:", width = 30, anchor = "w")
		photo2.grid(row = 7, column = 0)
		self.photoEntry2 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = "", width = 30, justify = 'right')
		self.photoEntry2.grid(row = 7, column = 1)
		
		searchPhotoBtn2 = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "Search", command = lambda: self.set_text2(filedialog.askopenfilename(filetypes = (("Photo Files", "*.png"), ("All Files", "*.*")))))
		searchPhotoBtn2.grid(row = 7, column = 2)

		submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "CHANGE", command = lambda: [f() for f in [self.changeDb, window1.destroy]])
		submitBtn.grid(row = 8, column = 0)

		window1.mainloop()

	def deleteDb1(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				usn4 = self.usnEntry3.get().upper()
				sql = "DELETE FROM STUDENT_INFORMATION WHERE USN = '%s'"%(usn4)
				cursor.execute(sql)
				sql = "DROP TABLE %s"%(usn4)
				cursor.execute(sql)
				cursor1 = db.cursor(prepared = True)
				sql = "DELETE FROM PHOTO WHERE USN = '%s'"%(usn4)
				cursor1.execute(sql)
				db.commit()
				messagebox.showinfo("DELETE A STUDENT", "STUDENT BIODATA WAS DELETED SUCCESSFULLY")
		except Error as e:
			messagebox.showwarning("CAN'T DELETE THE STUDENT INFORMATION", "THE USN DOESN'T EXIST")
			db.rollback()
		finally:
			db.close()

	def delete(self):
		window1 = Tk(className = "DELETE STUDENT PROFILE")
		window1.geometry("350x70")
		window1.title("DELETE STUDENT PROFILE")
		window1.attributes("-topmost", True)
		
		F0 = Frame(window1, relief = SUNKEN)
		F0.pack(side = LEFT)

		usn3 = Label(F0, font = ('OpenSansCondensed', 12), text = "  ENTER THE USN:", width = 25, anchor = "w")
		usn3.grid(row = 0, column = 0)
		self.usnEntry3 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = "", insertwidth = 4, justify = 'right')
		self.usnEntry3.grid(row = 0, column = 1)

		submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "DELETE", command = lambda: [f() for f in [self.deleteDb1, window1.destroy]])
		submitBtn.grid(row = 4, column = 0)

		window1.mainloop()

	def deleteDb(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				sql = "SELECT USN FROM STUDENT_INFORMATION"
				cursor.execute(sql)
				results = cursor.fetchall()
				for i in range(len(results)):
					sql = "DROP TABLE IF EXISTS %s"%(results[i][0])
					cursor.execute(sql)
				sql = "DROP TABLE IF EXISTS STUDENT_INFORMATION"
				cursor.execute(sql)
				sql = "DROP TABLE IF EXISTS PHOTO"
				cursor.execute(sql)
				sql = "DROP TABLE IF EXISTS BOOK"
				cursor.execute(sql)
				db.commit()
				messagebox.showinfo("DELETE TABLE", "Table was deleted successfully")
		except Error as e:
			messagebox.showwarning("CAN'T DELETE TABLE", "Table won't deleted due to the error")
			db.rollback()
		finally:
			db.close()

	def addBookDb(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				sql = "INSERT INTO BOOK(BOOK_ID, BOOK_NAME, BOOK_AUTHOR, BOOK_DETAILS) \
					 VALUES('%s', '%s', '%s', '%s')"%\
					 (self.book_idEntry1.get(), self.book_nameEntry1.get(), self.book_authorEntry1.get(), self.book_detailsEntry1.get())
				cursor.execute(sql)
				db.commit()
				messagebox.showinfo("ADD A BOOK", "THE BOOK WAS ADDED SUCCESSFULLY")
		except Error as e:
			messagebox.showwarning("CAN'T ADD A BOOK", "THERE IS SOME ERROR IN THE INFORMATION PROVIDED")
			db.rollback()
		finally:
			db.close()

	def add_book(self):
		window1 = Tk(className = "ADD BOOK")
		window1.geometry("400x160")
		window1.title("ADD A BOOK")
		window1.attributes("-topmost", True)

		F0 = Frame(window1, relief = SUNKEN)
		F0.pack(side = LEFT)

		l1 = ["book_id", "book_name", "book_author", "book_details"]
		l2 = ["BOOK ID", "BOOK NAME", "AUTHOR OF THE BOOK", "BOOK DETAILS"]
		
		for i in range(len(l1)):
			exec("%s1 = Label(F0, font = ('OpenSansCondensed', 12), text = \"  ENTER THE %s:\", width = 35, anchor = \"w\")"%(l1[i], l2[i]))
			exec("%s1.grid(row = %s, column = 0)"%(l1[i], i))
			exec("self.%sEntry1 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = \"\", insertwidth = 4, justify = 'right')"%(l1[i]))
			exec("self.%sEntry1.grid(row = %s, column = 1)"%(l1[i], i))

		submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "ADD", command = lambda: [f() for f in [self.addBookDb, window1.destroy]])
		submitBtn.grid(row = 4, column = 0)
		window1.mainloop()

	def deleteBookDb(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				sql = "SELECT * FROM BOOK WHERE BOOK_ID = '%s'"%(self.book_idEntry1.get())
				cursor.execute(sql)
				sql = "DELETE FROM BOOK WHERE BOOK_ID = '%s'"%(self.book_idEntry1.get())
				cursor.execute(sql)
				db.commit()
				messagebox.showinfo("DELETE A BOOK", "THE BOOK WAS DELETED SUCCESSFULLY")
		except Error as e:
			messagebox.showwarning("CAN'T DELETE A BOOK", "THE BOOK ID DOESN'T EXIST")
			db.rollback()
		finally:
			db.close()

	def delete_book(self):
		window1 = Tk(className = "REMOVE BOOK")
		window1.geometry("400x70")
		window1.title("REMOVE BOOK")
		window1.attributes("-topmost", True)
		
		F0 = Frame(window1, relief = SUNKEN)
		F0.pack(side = LEFT)

		book_id1 = Label(F0, font = ('OpenSansCondensed', 12), text = "ENTER THE BOOK ID:", width = 35, anchor = "w")
		book_id1.grid(row = 0, column = 0)
		self.book_idEntry1 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = "", insertwidth = 4, justify = 'right')
		self.book_idEntry1.grid(row = 0, column = 1)

		submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "DELETE", command = lambda: [f() for f in [self.deleteBookDb, window1.destroy]])
		submitBtn.grid(row = 4, column = 0)

		window1.mainloop()

	def get_students(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				sql = "SELECT * FROM STUDENT_INFORMATION"
				cursor.execute(sql)
				result = cursor.fetchall()
				db.commit()
				db.close()
				return result
		except Error as e:
			print(e)
			db.rollback()
			db.close()
		
	def show_students(self):
		window2 = Tk(className = "STUDENT LIST")
		window2.title("STUDENT LIST")
		window2.attributes("-topmost", True)
		s = findSize() 
		window2.geometry(s)
		
		scroll = Scrollbar(window2)
		scroll.pack(side = RIGHT, fill = Y)
		mylist = Listbox(window2, yscrollcommand = scroll.set, font = ('Courier', 20))
		heading  = "USN".center(10)
		heading += "NAME".center(20)
		heading += "BRANCH".center(8)
		heading += "SEM".center(10)
		heading += "ADDRESS".center(35)
		heading += "PHONE NUMBER".center(15)
		heading += "PROCTOR NAME".center(20)
		mylist.insert(END, heading)
		heading = ""
		mylist.insert(END, heading)
		li = self.get_students()
		for i in range(len(li)):
			st  = li[i][0].center(10)
			st += li[i][1].center(20)
			st += li[i][2].center(8)
			st += li[i][3].center(10)
			st += li[i][4].center(35)
			st += li[i][5].center(15)
			st += li[i][6].center(20)
			mylist.insert(END, st)
		mylist.pack(expand = True, fill = BOTH)
		scroll.config(command = mylist.yview)

		window2.mainloop()

	def get_books(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				sql = "SELECT * FROM BOOK"
				cursor.execute(sql)
				result = cursor.fetchall()
				db.commit()
				db.close()
				return result
		except Error as e:
			print(e)
			db.rollback()
			db.close()
		
	def show_books(self):
		window2 = Tk(className = "BOOK LIST")
		window2.title("BOOKS LIST")
		window2.attributes("-topmost", True)
		s = findSize() 
		window2.geometry(s)
		
		scroll = Scrollbar(window2)
		scroll.pack(side = RIGHT, fill = Y)
		mylist = Listbox(window2, yscrollcommand = scroll.set, font = ('Courier', 20))
		heading  = "BOOK ID".center(15)
		heading += "BOOK NAME".center(25)
		heading += "BOOK AUTHOR".center(25)
		heading += "BOOK DETAILS".center(45)
		mylist.insert(END, heading)
		heading = ""
		mylist.insert(END, heading)
		li = self.get_books()
		for i in range(len(li)):
			st  = li[i][0].center(15)
			st += li[i][1].center(25)
			st += li[i][2].center(25)
			st += li[i][3].center(45)
			mylist.insert(END, st)
		mylist.pack(expand = True, fill = BOTH)
		scroll.config(command = mylist.yview)

		window2.mainloop()

	def showImg(self):
		img = "image/" + self.usnEntry.get().upper() + ".png"
		load = Image.open(img)
		render = ImageTk.PhotoImage(load)

		self.img = Label(image = render)
		self.img.image = render
		self.img.place(x = 1600, y = 150)

	def clear_Label(self):
		self.img.config(image = "")

	def Submit(self):
		usn1 = self.usnEntry.get().upper()
		self.nameDisplay["text"] = ""
		self.branchDisplay["text"] = ""
		self.semDisplay["text"] = ""
		self.addressDisplay["text"] = ""
		self.phnoDisplay["text"] = ""
		self.proctorDisplay["text"] = ""
		self.clear_Label()

		for i  in range(1, 6):
			exec("self.slno%s[\"text\"] = \"\""%(i))
			exec("self.id%s[\"text\"] = \"\""%(i))
			exec("self.name%s[\"text\"] = \"\""%(i))
			exec("self.author%s[\"text\"] = \"\""%(i))
			exec("self.details%s[\"text\"] = \"\""%(i))
		
		self.nameDisplay["text"] = Information.get_name(usn1)
		self.branchDisplay["text"] = Information.get_branch(usn1)
		self.semDisplay["text"] = Information.get_sem(usn1)
		self.addressDisplay["text"] = Information.get_address(usn1)
		self.phnoDisplay["text"] = Information.get_phno(usn1)
		self.proctorDisplay["text"] = Information.get_proctor(usn1)
		Information.retrivePhoto(usn1)
		self.showImg()
		os.remove("image/" + usn1 + ".png")

		li0 = Information.infBook(usn1)
		for i in range(1, 6):
			if(len(li0) > (i-1)):
				exec("self.slno%s[\"text\"] = (%s)"%(i, i))
				exec("self.id%s[\"text\"] = li0[%s][0]"%(i, i-1))
				exec("self.name%s[\"text\"] = li0[%s][1]"%(i, i-1))
				exec("self.author%s[\"text\"] = li0[%s][2]"%(i, i-1))
				exec("self.details%s[\"text\"] = li0[%s][3]"%(i, i-1))
	
	def borrow_book(self):
		usn1 = self.usnEntry.get().upper()
		if(len(Information.infBook(usn1)) < 5):	
			window1 = Tk(className = "BORROW BOOK")
			window1.geometry("400x70")
			window1.title("BORROW A BOOK")
			window1.attributes("-topmost", True)

			F0 = Frame(window1, relief = SUNKEN)
			F0.pack(side = LEFT)

			book_id1 = Label(F0, font = ('OpenSansCondensed', 12), text = "  ENTER THE BOOK ID:", width = 35, anchor = "w")
			book_id1.grid(row = 0, column = 0)
			self.book_idEntry1 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = "", insertwidth = 4, justify = 'right')
			self.book_idEntry1.grid(row = 0, column = 1)

			submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "BORROW", command = lambda: [f() for f in [self.borrowBookDb, self.Submit, window1.destroy]])
			submitBtn.grid(row = 4, column = 0)
			window1.mainloop()
		else:
			messagebox.showwarning("CAN'T BORROW A BOOK", "Only 5 books are given for a Student")

	def borrowBookDb(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				usn1 = self.usnEntry.get().upper()
				sql = "INSERT INTO %s(BOOK_ID)\
					 VALUES('%s')"%\
					 (usn1, self.book_idEntry1.get())
				cursor.execute(sql)
				db.commit()
				messagebox.showinfo("BORROW A BOOK", "THE BOOK WAS BORROWED SUCCESSFULLY")
		except Error as e:
			messagebox.showwarning("CAN'T BORROW A BOOK1", "There is some error in the information provided")
			db.rollback()
		finally:
			db.close()

	def return_book(self):
		usn1 = self.usnEntry.get().upper()
		if(len(Information.infBook(usn1)) > 0):	
			window1 = Tk(className = "RETURN BOOK")
			window1.geometry("400x70")
			window1.title("RETURN THE BOOK")
			window1.attributes("-topmost", True)
			
			F0 = Frame(window1, relief = SUNKEN)
			F0.pack(side = LEFT)

			book_id1 = Label(F0, font = ('OpenSansCondensed', 12), text = "ENTER THE BOOK ID:", width = 35, anchor = "w")
			book_id1.grid(row = 0, column = 0)
			self.book_idEntry1 = Entry(F0, font = ('OpenSansCondensed', 12), textvariable = "", insertwidth = 4, justify = 'right')
			self.book_idEntry1.grid(row = 0, column = 1)

			submitBtn = Button(F0, padx = 16, pady = 5, font = ('OpenSansCondensed', 10), width = 8, text = "RETURN", command = lambda: [f() for f in [self.returnBookDb, self.Submit, window1.destroy]])
			submitBtn.grid(row = 4, column = 0)

			window1.mainloop()
		else:
			messagebox.showwarning("CAN'T RETURN A BOOK", "Student hasn't taken any book to return")

	def returnBookDb(self):
		try:
			db = mysqCon.connect(host = host1, database = database1, user = user1, password = password1)
			if db.is_connected():
				cursor = db.cursor()
				usn1 = self.usnEntry.get().upper()
				sql = "DELETE FROM %s WHERE BOOK_ID = '%s'"%(usn1, self.book_idEntry1.get())
				cursor.execute(sql)
				db.commit()
				messagebox.showinfo("DELETE A BOOK", "THE BOOK WAS DELETED SUCCESSFULLY")
		except Error as e:
			messagebox.showwarning("CAN'T DELETE A BOOK", "THE BOOK ID DOESN'T EXIST")
			db.rollback()
		finally:
			db.close()

ask_for_Db()
check()
checkDb.checkDb()
admin.admin()
BookBank()
