import tkinter as tk

class Example():
    def __init__(self):
        self.root = tk.Tk()
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.toolbar = tk.Frame(self.root)
        self.toggle = tk.Button(self.toolbar, text="Toggle the message",
                                command=self.toggle_message)
        self.toggle.pack(side="left")

        # simulate a typical app with a navigation area on the left and a main
        # working area on the right
        self.navpanel = tk.Frame(self.root, background="bisque", width=100, height=200)
        self.main = tk.Frame(self.root, background="white", width=300, height=200, bd=1, relief='sunken')
        self.message = tk.Label(self.root, text="Hello, world!")

        self.toolbar.grid(row=0, column=0, columnspan=2)
        self.message.grid(row=1, column=0, columnspan=2)
        self.navpanel.grid(row=2, column=0, sticky="nsew")
        self.main.grid(row=2, column=1, sticky="nsew")

    def start(self):
        self.root.mainloop()

    def toggle_message(self):
        if self.message.winfo_viewable():
            self.message.grid_remove()
        else:
            self.message.grid()

if __name__ == "__main__":
    Example().start()