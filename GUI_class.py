
from itertools import product
from re import L
from tabnanny import check
import tkinter as tk
from tkinter import ttk,Toplevel
from functools import partial
from tkinter.messagebox import showinfo
from onlineshop import OnlineShop

aShop=OnlineShop()




# class Customer_Window():
#     def __init__(self,master):
#         self.master=master

  
# create root window
root = tk.Tk()
root.geometry('800x800')
root.resizable(False, False)
root.title('Lincoln Online Shop')



def login_page():
     
    # Toplevel object which will
    # be treated as a new window
    login_window = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    login_window.title("Log In")
 
    # sets the geometry of toplevel
    login_window.geometry("600x600")
 
    tk.Label(login_window,text ="Please enter your user name and password to login").grid(row=0,column=1)

    #username label and text entry box
    usernameLabel = tk.Label(login_window, text="User Name").grid(row=2, column=0)
    username = tk.StringVar()
    usernameEntry = tk.Entry(login_window, textvariable=username).grid(row=2, column=1)  

    #password label and password entry box
    passwordLabel = tk.Label(login_window,text="Password").grid(row=3, column=0)  
    password = tk.StringVar()
    passwordEntry = tk.Entry(login_window, textvariable=password, show='*').grid(row=3, column=1)  


    def member_login():
        if aShop.memberLogIn(username.get(),password.get()):
            aMember=aShop.memberLogIn(username.get(),password.get())
            print(aMember)
            memberName=username.get()
            print(memberName)
            login_window.destroy()
            member_window = Toplevel(root)
            member_window.title('Member Page')
            member_window.geometry("800x1200")
            

            def search_prod_by_name():
                prod.set(aShop.searchProductByName(search_prod_entry.get().lower()))


            def search_prod_by_category():
                prod.set(aShop.searchProductByCategory(search_prod_entry.get().lower()))

                

            def show_prod_detail():
                selected_prod_indics=prod_listbox.curselection()
                selected_prod=prod_listbox.get(selected_prod_indics)
                prod__detail_label2.config(text=aShop.viewProductDetails(selected_prod))


            def add_to_cart():
                # cart_treeview.delete(0.0,tk.END)
                selected_prod_indics=prod_listbox.curselection()
                selected_prod=prod_listbox.get(selected_prod_indics)
                content=aShop.addItem(memberName,selected_prod)
    
                cart_treeview.insert('',tk.END,values=content)
                sub_total_value_label.config(text=aShop.getSubTotal(memberName))



            def remove_item():
                selected_item=cart_treeview.selection()[0]
                pname=cart_treeview.item(selected_item)['values'][0]
                aShop.removeItem(memberName,pname)
                cart_treeview.delete(selected_item)
                print(len(aShop.viewCart(memberName)))



            def empty_cart():
                
                cart_treeview.delete(*cart_treeview.get_children())
                aShop.emptyCart(memberName)
                print(len(aShop.viewCart(memberName)))


            #app frame
            app_frame=tk.Frame(member_window,relief=tk.FLAT,borderwidth=3)
            app_frame.grid(column=0,row=0,sticky=tk.N,padx=(100,0))

            #app label
            app_label=tk.Label(app_frame,text='Welcome Back, {}'.format(memberName))
            app_label.grid(column=1, row=0, pady=10)

            #nav frame
            nav_frame=tk.Frame(member_window)
            nav_frame.grid(column=0,row=1,sticky=tk.N,columnspan=2)

            #view product button
            view_prod_button=tk.Button(nav_frame,text=' Search Product By Category',command=search_prod_by_category)
            view_prod_button.grid(column=0,row=1,padx=20)

            #search product entry
            product_input=tk.StringVar()
            search_prod_entry=tk.Entry(nav_frame,textvariable=product_input)
            search_prod_entry.grid(column=1,row=1,padx=20)

            #search product button
            search_prod_button=tk.Button(nav_frame,text='Search Product By Name',command=search_prod_by_name)
            search_prod_button.grid(column=2,row=1,padx=20)


            # product frame
            all_prod_frame=tk.Frame(member_window)
            all_prod_frame.grid(column=0,row=2)

            # product Label
            all_prod_label = tk.Label(all_prod_frame,text='Product List')
            # all_prod_label.pack(side=tk.TOP)
            all_prod_label.grid(column=1,row=0)

            #Create a horizontal scrollbar
            prod_scrollbar = tk.Scrollbar(all_prod_frame, orient= 'vertical')
            # scrollbar2.pack(side= tk.RIGHT, fill='both')
            prod_scrollbar.grid(column=2,row=1)


            #product Listbox
            prod=tk.StringVar(value=aShop.viewAllProducts())

            prod_listbox=tk.Listbox(all_prod_frame,listvariable=prod,exportselection=False)
            # prod_listbox.place(x=320,y=60,width=210,height=160)
            # prod_listbox.pack(side=tk.BOTTOM,fill='both')
            prod_listbox.grid(column=1,row=1)
            prod_listbox.config(yscrollcommand= prod_scrollbar.set)
            prod_scrollbar.config(command= prod_listbox.yview)

            # view product details button
            view_details_button=tk.Button(all_prod_frame,text='View Details',command=show_prod_detail)
            view_details_button.grid(column=1,row=2)



            # product details frame
            prod_detail_frame=tk.Frame(member_window)
            prod_detail_frame.grid(column=1,row=2)

            # product detail Label
            prod_detail_label = tk.Label(prod_detail_frame,text='Product Detail')
            # all_prod_label.pack(side=tk.TOP)
            prod_detail_label.grid(column=1,row=0)


            #product detail display label
            prod__detail_label2=tk.Label(prod_detail_frame,text='Select a product to view\n')
            prod__detail_label2.grid(column=1,row=1)

            # view product details button
            add_to_cart_button=tk.Button(prod_detail_frame,text='Add To Cart', command=add_to_cart)
            add_to_cart_button.grid(column=1,row=2)


            #shopping cart frame
            cart_frame=tk.Frame(member_window)
            cart_frame.grid(column=0,row=3,columnspan=2)

            # shopping cart label
            cart_label=tk.Label(cart_frame,text='Shopping Cart')
            cart_label.grid(column=1,row=0)

            #shopping cart listbox
            columns=('item_name','item_quantity','total_price')
            cart_treeview=ttk.Treeview (cart_frame,columns=columns,show='headings')
            cart_treeview.heading('item_name',text='Item Name')
            cart_treeview.heading('item_quantity',text='Quantity')
            cart_treeview.heading('total_price',text='Total Price')
            cart_treeview.grid(column=0,row=1,columnspan=3)
            cartlist=aShop.viewCart(aShop.guest)
            for item in cartlist:
                cart_treeview.insert('',tk.END,values=item)


            # remove item button
            remove_button=tk.Button(cart_frame,text='Remove Item',command=remove_item)
            remove_button.grid(column=0,row=2)

            # empty cart button
            empty_cart_button=tk.Button(cart_frame,text='Empty Cart',command=empty_cart)
            empty_cart_button.grid(column=1,row=2)

            #sub total label
            sub_total_label=tk.Label(cart_frame,text='Sub Total')
            sub_total_label.grid(column=2,row=2)

            #sub total value label
            sub_total_value_label=tk.Label(cart_frame,text='$0.00',bg='white')
            sub_total_value_label.grid(column=3,row=2)
            sub_total_value_label.config(text=aShop.getSubTotal(memberName))



            #checkout button
            checkout_button=tk.Button(cart_frame,text='Checkout')
            checkout_button.grid(column=5,row=2)

            #order frame
            order_frame=tk.Frame(member_window)
            order_frame.grid(column=0,row=4)

            #order history label
            order_history_label=tk.Label(order_frame,text='Orders')
            order_history_label.grid(column=0,row=0)
            
             #Order Listbox
            order=tk.StringVar(value=aShop.memberViewAllOrders(memberName))

            order_listbox=tk.Listbox(order_frame,listvariable=order,exportselection=False)
            order_listbox.grid(column=0,row=1)

         
    

            # # view order details button
            # view_order_details_button=tk.Button(order_frame,text='View Order',command=show_order_detail)
            # view_order_details_button.grid(column=1,row=2)

            # Order details frame
            order_detail_frame=tk.Frame(member_window)
            order_detail_frame.grid(column=1,row=4)

            # Order detail Label
            order_detail_label = tk.Label(order_detail_frame,text='Order Detail')
            # all_prod_label.pack(side=tk.TOP)
            order_detail_label.grid(column=1,row=0)


            #order detail display label
            order__detail_label2=tk.Label(order_detail_frame,text='Select a order to view status\n')
            order__detail_label2.grid(column=1,row=1)



            #order buttons frame
            order_buttons_frame=tk.Frame(member_window)
            order_buttons_frame.grid(column=0,row=5,columnspan=2)

            #check order status button
            check_status_button=tk.Button(order_buttons_frame,text='Check Order Status')
            check_status_button.grid(column=0,row=0,padx=20)

            #cancel order button
            cancel_order_button=tk.Button(order_buttons_frame,text='Cancel Order')
            cancel_order_button.grid(column=2,row=0,padx=20)

            def show_order_detail():
                pass

       

     #login button
    loginButton = tk.Button(login_window, text="Login",command=member_login).grid(row=4, column=0)
 
    # def validation():
    # #getting form data
    #     uname=username.get()
    #     pwd=password.get()
    #     #applying empty validation
    #     if uname=='' or pwd=='':
    #         message.set("fill the empty field!!!")
    #     else:
    #         if uname=="abcd@gmail.com" and pwd=="abc123":
    #             message.set("Login success")
    #         else:
    #             message.set("Wrong username or password!!!")




def search_prod_by_name():
    prod.set(aShop.searchProductByName(search_prod_entry.get().lower()))


def search_prod_by_category():
    prod.set(aShop.searchProductByCategory(search_prod_entry.get().lower()))

    

def show_prod_detail():
    selected_prod_indics=prod_listbox.curselection()
    selected_prod=prod_listbox.get(selected_prod_indics)
    prod__detail_label2.config(text=aShop.viewProductDetails(selected_prod))


def add_to_cart():
    
    selected_prod_indics=prod_listbox.curselection()
    selected_prod=prod_listbox.get(selected_prod_indics)
    content=aShop.addItem('guest',selected_prod)
    cart_treeview.insert('',tk.END,values=content)
    print(len(aShop.viewCart(aShop.guest)))
    sub_total_value_label.config(text=aShop.getSubTotal('guest'))



def remove_item():
    selected_item=cart_treeview.selection()[0]
    pname=cart_treeview.item(selected_item)['values'][0]
    aShop.removeItem('guest',pname)
    cart_treeview.delete(selected_item)
    print(len(aShop.viewCart('guest')))



def empty_cart():
    
    cart_treeview.delete(*cart_treeview.get_children())
    aShop.emptyCart(aShop.guest)
    print(len(aShop.viewCart(aShop.guest)))

def checkout():

    ####To do: change to badrequestError to throw message from controller
    if aShop.viewCart('guest')==[]:
        showinfo(title='error',message='Cart is empty')
    else:    
        showinfo(title='error', message='Please log in first')


#app frame
app_frame=tk.Frame(root,relief=tk.FLAT,borderwidth=3)
app_frame.grid(column=0,row=0,sticky=tk.N,padx=(100,0))

#app label
app_label=tk.Label(app_frame,text='Welcome to Lincoln Online Shop')
app_label.grid(column=1, row=0, pady=10)

#nav frame
nav_frame=tk.Frame(root)
nav_frame.grid(column=0,row=1,sticky=tk.N,columnspan=2)

#view product button
view_prod_button=tk.Button(nav_frame,text=' Search Product By Category',command=search_prod_by_category)
view_prod_button.grid(column=0,row=1,padx=20)

#search product entry
product_input=tk.StringVar()
search_prod_entry=tk.Entry(nav_frame,textvariable=product_input)
search_prod_entry.grid(column=1,row=1,padx=20)

#search product button
search_prod_button=tk.Button(nav_frame,text='Search Product By Name',command=search_prod_by_name)
search_prod_button.grid(column=2,row=1,padx=20)


# Member login button
member_login_button=tk.Button(nav_frame,text='Member Log In',command=login_page)
member_login_button.grid(column=3,row=1,padx=20)


# staff login button
staff_login_button=tk.Button(nav_frame,text='Staff Log In',command=login_page)
staff_login_button.grid(column=4,row=1,padx=20)

# product frame
all_prod_frame=tk.Frame(root)
all_prod_frame.grid(column=0,row=2)

# product Label
all_prod_label = tk.Label(all_prod_frame,text='Product List')
# all_prod_label.pack(side=tk.TOP)
all_prod_label.grid(column=1,row=0)

#Create a horizontal scrollbar
prod_scrollbar = tk.Scrollbar(all_prod_frame, orient= 'vertical')
# scrollbar2.pack(side= tk.RIGHT, fill='both')
prod_scrollbar.grid(column=2,row=1)


#product Listbox
prod=tk.StringVar(value=aShop.viewAllProducts())

prod_listbox=tk.Listbox(all_prod_frame,listvariable=prod,exportselection=False)
# prod_listbox.place(x=320,y=60,width=210,height=160)
# prod_listbox.pack(side=tk.BOTTOM,fill='both')
prod_listbox.grid(column=1,row=1)
prod_listbox.config(yscrollcommand= prod_scrollbar.set)
prod_scrollbar.config(command= prod_listbox.yview)

# view product details button
view_details_button=tk.Button(all_prod_frame,text='View Details',command=show_prod_detail)
view_details_button.grid(column=1,row=2)



# product details frame
prod_detail_frame=tk.Frame(root)
prod_detail_frame.grid(column=1,row=2)

# product detail Label
prod_detail_label = tk.Label(prod_detail_frame,text='Product Detail')
# all_prod_label.pack(side=tk.TOP)
prod_detail_label.grid(column=1,row=0)


#product detail display label
prod__detail_label2=tk.Label(prod_detail_frame,text='Select a product to view\n')
prod__detail_label2.grid(column=1,row=1)

# view product details button
add_to_cart_button=tk.Button(prod_detail_frame,text='Add To Cart', command=add_to_cart)
add_to_cart_button.grid(column=1,row=2)


#shopping cart frame
cart_frame=tk.Frame(root)
cart_frame.grid(column=0,row=3,columnspan=2)

# shopping cart label
cart_label=tk.Label(cart_frame,text='Shopping Cart')
cart_label.grid(column=1,row=0)

#shopping cart listbox
columns=('item_name','item_quantity','total_price')
cart_treeview=ttk.Treeview (cart_frame,columns=columns,show='headings')
cart_treeview.heading('item_name',text='Item Name')
cart_treeview.heading('item_quantity',text='Quantity')
cart_treeview.heading('total_price',text='Total Price')
cart_treeview.grid(column=0,row=1,columnspan=3)

# remove item button
remove_button=tk.Button(cart_frame,text='Remove Item',command=remove_item)
remove_button.grid(column=0,row=2)

# empty cart button
empty_cart_button=tk.Button(cart_frame,text='Empty Cart',command=empty_cart)
empty_cart_button.grid(column=1,row=2)

#sub total label
sub_total_label=tk.Label(cart_frame,text='Sub Total')
sub_total_label.grid(column=2,row=2)

#sub total value label
sub_total_value_label=tk.Label(cart_frame,text='$0.00',bg='white')
sub_total_value_label.grid(column=3,row=2)



#checkout button
checkout_button=tk.Button(cart_frame,text='Checkout',command=checkout)
checkout_button.grid(column=5,row=2)





 

if __name__ == "__main__": 
    root.mainloop()