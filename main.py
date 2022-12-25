import tkinter as tk
from generator import generate

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x250')
        self.root.title('Password generator')
        self.root.resizable(None, None)

        self.load()

    def load(self):
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.pack()

        self.let = tk.BooleanVar()
        self.let.set(1)
        self.num = tk.BooleanVar()
        self.num.set(1)
        self.symb = tk.BooleanVar()
        self.symb.set(1)

        self.lenght = tk.Label(self.mainFrame, text='Password lenght (default 8)').pack()
        self.lenghtEntry = tk.Entry(self.mainFrame)
        self.lenghtEntry.pack()
        
        self.letCheck = tk.Checkbutton(self.mainFrame, text='Letters', variable=self.let, onvalue=1, offvalue=0)
        self.letCheck.pack()
        self.numCheck = tk.Checkbutton(self.mainFrame, text='Numbers', variable=self.num, onvalue=1, offvalue=0)
        self.numCheck.pack()
        self.symbCheck = tk.Checkbutton(self.mainFrame, text='Symbols', variable=self.symb, onvalue=1, offvalue=0)
        self.symbCheck.pack()

        self.genButton = tk.Button(self.mainFrame, text='Generate', command=self.gen)
        self.genButton.pack()

        self.password = tk.Label(self.mainFrame, text='Password').pack()
        self.passwordEntry = tk.Entry(self.mainFrame, state='disabled')
        self.passwordEntry.pack()

        self.copyButton = tk.Button(self.mainFrame, text='Copy', command=self.copy)
        self.copyButton.pack()

    def gen(self):
        try:
            lenght = int(self.lenghtEntry.get())
        except ValueError as e:
            lenght = 8

        let = self.let.get()
        print(let)
        num = self.num.get()
        print(num)
        symb = self.symb.get()
        print(symb)

        if let == False and num == False and symb == False:
            a = generate()
        else:
            a = generate(int(lenght), let, num, symb)

        self.passwordEntry.configure(state=tk.NORMAL)
        self.passwordEntry.delete(0, tk.END)
        self.passwordEntry.insert(0, str(a))
        self.passwordEntry.configure(state=tk.DISABLED)
    
    def copy(self):
        self.passwordEntry.configure(state=tk.NORMAL)
        data = self.passwordEntry.get()
        self.passwordEntry.configure(state=tk.DISABLED)
        self.root.clipboard_clear()
        self.root.clipboard_append(data)

    def start(self):
        self.root.protocol("WM_DELETE_WINDOW", self.__exit)
        self.root.mainloop()
    def __exit(self):
        self.root.destroy()
    

if __name__ == '__main__':
    gui = GUI()
    gui.start()