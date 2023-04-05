import tkinter as tk
import sys
import subprocess
import threading 
import time
# --- functions ---

def run():
    threading.Thread(target=test).start()

def test():
    print("Hello World")
    time.sleep(1)
    print("Hello World")
    


    print("Finished")
             
# --- classes ---

class Redirect():

    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert('end', text)
        #self.widget.see('end') # autoscroll

    #def flush(self):
    #    pass

# --- main ---    

root = tk.Tk()

text = tk.Text(root)
text.pack()

button = tk.Button(root, text='TEST', command=run)
button.pack()

old_stdout = sys.stdout    
sys.stdout = Redirect(text)

root.mainloop()

sys.stdout = old_stdout