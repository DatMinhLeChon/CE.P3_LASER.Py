import meta.external_var
import gc
import keyboard
import mouse
import time
import sys
from tkinter import Tk, messagebox
from template.login_frame import LoginFrame
from PIL import Image, ImageTk

sys.setrecursionlimit(1000000)

def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

def getTimeSinceLastMouseEvent():
    try:
        now = time.time()
        timestamp = mouse.get_last_mouse_event_timestamp()
        if timestamp is not None:
            return now - timestamp
        else:
            return None
    except: pass

def getTimeSinceLastKeyboardEvent():
    now = time.time()
    timestamp = keyboard.get_last_keyboard_event_timestamp()
    if timestamp is not None:
        return now - timestamp
    else:
        return None

def eventCheckLoginStatus():
    try:
        if meta.external_var.root is not None:
            if meta.external_var.login_status == False:
                meta.external_var.root.destroy()
                meta.external_var.root_temp.destroy()
                gc.collect()
            else: pass
            meta.external_var.root.after(1000,sequence(eventCheckLoginStatus()))
    except:
        pass
def eventCheckOut():
    try:
        if getTimeSinceLastKeyboardEvent >=100000 and getTimeSinceLastMouseEvent >= 100000:
            meta.external_var.login_status = False
            messagebox.showinfo(message= "System Log Out")
        meta.external_var.root.after(1000,sequence(eventCheckOut()))
    except:
        pass

def main():
    meta.external_var.root = Tk()
    meta.external_var.root.geometry('1200x1000+300+0') 
    meta.external_var.bg = ImageTk.PhotoImage(Image.open('data/images/FS_image1.png').resize((1920, 1080)))
    meta.external_var.logo = ImageTk.PhotoImage(Image.open('data/images/logo.png').resize((34, 30)))
    app_login = LoginFrame(meta.external_var.root)
    meta.external_var.root.mainloop()
    try:
        sequence(eventCheckLoginStatus(), eventCheckOut())
    except Exception as e :
        print(e)

if __name__ == "__main__" :
    main()