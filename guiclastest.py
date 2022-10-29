import tkinter as tk

root=tk.Tk()

class Loginframe():
    def __init__(self,root):
        self= tk.Frame(root)

        # # sets the title of the
        # self.title("Log In")

        # # sets the geometry of toplevel
        # self.geometry("600x600")

        tk.Label(self,text ="Please enter your user name and password to login").grid(row=0,column=1)

        #username label and text entry box
        usernameLabel = tk.Label(self, text="User Name").grid(row=2, column=0)
        username = tk.StringVar()
        usernameEntry = tk.Entry(self, textvariable=username).grid(row=2, column=1)  

        #password label and password entry box
        passwordLabel = tk.Label(self,text="Password").grid(row=3, column=0)  
        password = tk.StringVar()
        passwordEntry = tk.Entry(self, textvariable=password, show='*').grid(row=3, column=1)  



class MemberFrame():
    def __init__(self,root):
        #app frame
        app_frame=tk.Frame(root,relief=tk.FLAT,borderwidth=3)
        app_frame.grid(column=0,row=0,sticky=tk.N,padx=(100,0))

        #app label
        app_label=tk.Label(app_frame,text='Welcome to lincoln Shop')
        app_label.grid(column=1, row=0, pady=10)

        #nav frame
        nav_frame=tk.Frame(root)
        nav_frame.grid(column=0,row=1,sticky=tk.N,columnspan=2)

        #view product button
        view_prod_button=tk.Button(nav_frame,text=' Search Product By Category')
        view_prod_button.grid(column=0,row=1,padx=20)


class OrderFrame():
    def __init__(self,root):


        #shopping cart frame
        cart_frame=tk.Frame(root)
        cart_frame.grid(column=0,row=3,columnspan=2)

        # shopping cart label
        cart_label=tk.Label(cart_frame,text='Shopping Cart')
        cart_label.grid(column=1,row=0)
               # remove item button
        remove_button=tk.Button(cart_frame,text='Remove Item')
        remove_button.grid(column=0,row=2)

        # empty cart button
        empty_cart_button=tk.Button(cart_frame,text='Empty Cart')
        empty_cart_button.grid(column=1,row=2)

        #sub total label
        sub_total_label=tk.Label(cart_frame,text='Sub Total')
        sub_total_label.grid(column=2,row=2)

memberPage=ShoppingFrame()
