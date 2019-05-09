import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

keyboard.press(Key.cmd)
keyboard.press(Key.tab)
keyboard.release(Key.cmd)
keyboard.release(Key.tab)


time.sleep(1.5)

keyboard.type("10200") #CS202
keyboard.press(Key.tab)
keyboard.release(Key.tab)

keyboard.type("10201") #CS203
keyboard.press(Key.tab)
keyboard.release(Key.tab)

keyboard.type("10203") #CS203L
keyboard.press(Key.tab)
keyboard.release(Key.tab) 
keyboard.type("10501") #MATH272 (Linear Algebra w/ Application)
keyboard.press(Key.tab)
keyboard.release(Key.tab)

keyboard.type("10298") #ENG247 (Nature Writing)
keyboard.press(Key.tab)
keyboard.release(Key.tab)

keyboard.press(Key.enter)
keyboard.release(Key.enter)