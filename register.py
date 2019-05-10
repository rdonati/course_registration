import time
from pynput.keyboard import Key, Controller
from tkinter import *

num_of_courses = 6

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

	keyboard.press(Key.cmd)
	keyboard.press(Key.tab)
	keyboard.release(Key.cmd)
	keyboard.release(Key.tab)

	time.sleep(1.5)

	for i in range(num_of_courses):
		keyboard.type(crns[i])
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)

def select_all(event):
	event.widget.selection_range(0, END)

w = Tk()
w.title("Course Registration Helper")
w.resizable(height = False, width = False)
#Creates labels
labels = []
for i in range(num_of_courses):
	labels.append(Label(w, text = "{}. ".format(i + 1)))

#Creates input
entries = []
for i in range(num_of_courses):
	entries.append(Entry(w))

submit = Button(w, text = "Submit", command = submit)

#Shows labels
for i, label in enumerate(labels):
	label.grid(row = i, column = 0)

#Shows input
for i, entry in enumerate(entries):
	entry.grid(row = i, column = 1)
	entry.insert(0, "CRN {}".format(i + 1))
	entry.bind("<FocusIn>", select_all)

submit.grid(row = num_of_courses, column = 0)

w.mainloop()