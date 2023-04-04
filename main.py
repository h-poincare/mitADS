
import tkinter as tk
import sys

class App:
    def __init__(self, master):
        self.master = master
        self.label1 = tk.Label(self.master, text="Input 1")
        self.label1.pack()
        self.entry1 = tk.Entry(self.master)
        self.entry1.pack()

        self.label2 = tk.Label(self.master, text="Input 2")
        self.label2.pack()
        self.entry2 = tk.Entry(self.master)
        self.entry2.pack()

        self.button = tk.Button(self.master, text="Run Script", command=self.get_inputs)
        self.button.pack()

        self.text = tk.Text(self.master)
        self.text.pack()

    def run_script(self, input1, input2):
        # your script code here
        output = f"Input 1: {input1}\nInput 2: {input2}"
        print("TESTING")
        return output

    def get_inputs(self):
        input1 = self.entry1.get()
        input2 = self.entry2.get()
        
        # redirect stdout to text widget
        sys.stdout = TextRedirector(self.text)

        output = self.run_script(input1, input2)

    # restore stdout when done
    sys.stdout = sys.__stdout__

class TextRedirector:
    def __init__(self, widget):
        self.widget = widget

    def write(self, string):
        self.widget.insert(tk.END, string)

root = tk.Tk()
app = App(root)
root.mainloop()
