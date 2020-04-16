import time
from pynput.keyboard import Key, Controller
from tkinter import *

num_of_courses = 8

def print_data():

	crns = []
	for i in range(num_of_courses):
		crns.append(entries[i].get())

	for i in range(num_of_courses):
		print("{}: {}".format(i + 1, entries[i].get()))

def submit():

	crns = []
	for i in range(num_of_courses):
		crns.append(entries[i].get())

	keyboard = Controller()
	mouse = Controller()

	keyboard.press(Key.cmd)
	keyboard.press(Key.tab)
	keyboard.release(Key.cmd)
	keyboard.release(Key.tab)

	time.sleep(1)

	for i in range(num_of_courses):
		keyboard.type(crns[i])
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
		
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.press(Key.tab)
	keyboard.release(Key.tab)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)

w = Tk()
w.title("Course Registration Helper")
w.resizable(height = False, width = False)

crns = [
	30178,
	30184,
	30181,
	30599,
	30603,
	"",
	"",
	""
]

#Creates labels
labels = []
for i in range(num_of_courses):
	labels.append(Label(w, text = "{}. ".format(i + 1)))

#Creates input
entries = []
for i in range(num_of_courses):
	
	text = StringVar()
	e = Entry(w, textvariable = text)
	entries.append(e)
	text.set(crns[i])

submit = Button(w, text = "Submit", command = submit)

#Shows labels
for i, label in enumerate(labels):
	label.grid(row = i, column = 0)

#Shows input
for i, entry in enumerate(entries):
	entry.grid(row = i, column = 1)

submit.grid(row = num_of_courses, column = 0)

w.mainloop()