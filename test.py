from pynput.keyboard import Key, Controller

keyboard = Controller()

keyboard.press(Key.ctrl)
keyboard.press(Key.tab)
keyboard.release(Key.ctrl)
keyboard.release(Key.tab)

