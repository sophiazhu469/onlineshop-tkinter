
from atexit import register
from itertools import product
from re import A, L
from tabnanny import check
import tkinter as tk
from tkinter import StringVar, ttk,Toplevel
from functools import partial
from tkinter.messagebox import showinfo
from typing_extensions import IntVar
from venv import create
from onlineshop import OnlineShop
from model.badRequestError import BadRequestError
from datetime import date

aShop=OnlineShop()




  
# # create root window
# root = tk.Tk()
# root.geometry('800x800')
# root.title('Lincoln Online Shop')

# Login window
login_window = tk.Tk()

login_window.resizable(False, False)
# sets the title of the
login_window.title("Log In")

# sets the geometry of toplevel
login_window.geometry("600x400")

tk.Label(login_window,text ="Please enter your user name and password to login").grid(row=0,column=1,pady=40)

#username label and text entry box
usernameLabel = tk.Label(login_window, text="User Name").grid(row=2, column=0)
username = tk.StringVar()
usernameEntry = tk.Entry(login_window, textvariable=username).grid(row=2, column=1,columnspan=2)  

#password label and password entry box
passwordLabel = tk.Label(login_window,text="Password").grid(row=3, column=0)  
password = tk.StringVar()
passwordEntry = tk.Entry(login_window, textvariable=password, show='*').grid(row=3, column=1,columnspan=2,pady=40)  



def member_page():
    memberName=username.get()
    print(username.get())
    print(password.get())
    aMember=aShop.memberLogIn(username.get(),password.get())
    if aMember:
        memberName=username.get()
        print(memberName)
        login_window.destroy()
        member_window = tk.Tk()
        member_window.title('Member Page')
        member_window.geometry("800x1200")
        
        def search_prod_by_name():
            prod.set(aShop.searchProductByName2(search_prod_entry.get().lower()))


        def search_prod_by_category():
            try:
                prod.set(aShop.searchProductByCategory(search_prod_entry.get().lower()))
            except Exception as ex1:   
                showinfo(title='error',message=ex1)

            

        def show_prod_detail():
            selected_prod_indics=prod_listbox.curselection()
            selected_prod=prod_listbox.get(selected_prod_indics)
            prod__detail_label2.config(text=aShop.viewProductDetails(selected_prod))


        def add_to_cart():
            selected_prod_indics=prod_listbox.curselection()
            selected_prod=prod_listbox.get(selected_prod_indics)
            print('86'+memberName)
            aShop.addItem(memberName,selected_prod)
            cart_list=aShop.viewCart(memberName)
            cart_treeview.delete(*cart_treeview.get_children())
            for content in cart_list:
                cart_treeview.insert('',tk.END,values=content)
            sub_total_value_label.config(text=aShop.getSubTotal(memberName))



        def remove_item():
            selected_item=cart_treeview.selection()[0]
            pname=cart_treeview.item(selected_item)['values'][0]
            aShop.removeItem(memberName,pname)
            cart_treeview.delete(selected_item)
            print(len(aShop.viewCart(memberName)))
            sub_total_value_label.config(text=aShop.getSubTotal(memberName))



        def empty_cart():
            cart_treeview.delete(*cart_treeview.get_children())
            aShop.emptyCart(memberName)
            print(len(aShop.viewCart(memberName)))
            sub_total_value_label.config(text=aShop.getSubTotal(memberName))

        def checkout():
            # member_window.destroy()
            checkout_window = tk.Tk()
            checkout_window.title('Checkout Page')
            checkout_window.geometry("800x1200")

            def create_order():
                checkout_window.destroy()
                address_window=tk.Tk()
                address_window.title('Shipping Address')
                address_window.geometry('500x800')
                orderDetails=aShop.placeOrder(date.today(),memberName)
                aOrder=orderDetails[0]
                orderAmount=orderDetails[1]
                orderID=orderDetails[2]
                print(aOrder)
                print("orderAmount:{}".format(orderAmount))

                # address frame
                address_frame=tk.Frame(address_window,width=400,height=600)
                address_frame.grid(column=3,row=0)
                # enter address label
                address_label=tk.Label(address_frame,text='Please enter delivery Address')
                address_label.grid(column=0,row=0,columnspan=4)

                # street label
                street_label=tk.Label(address_frame,text='Street').grid(column=2,row=1)
                street_input=tk.StringVar()
                # street entry
                street_entry=tk.Entry(address_frame,textvariable=street_input).grid(column=0,row=2,columnspan=4)
                # suburb labels
                suburb_label=tk.Label(address_frame,text='Suburb').grid(column=2,row=3)
                # suburb entry
                suburb_input=tk.StringVar()
                suburb_entry=tk.Entry(address_frame,textvariable=suburb_input).grid(column=0,row=4,columnspan=4)
                # city labels
                city_label=tk.Label(address_frame,text='City').grid(column=2,row=5)
                # city entry
                city_input=tk.StringVar()
                city_entry=tk.Entry(address_frame,textvariable=city_input).grid(column=0,row=6,columnspan=4)
                # city labels
                postcode_label=tk.Label(address_frame,text='Postcode').grid(column=2,row=7)
                # city entry
                postcode_input=tk.StringVar()
                postcode_entry=tk.Entry(address_frame,textvariable=postcode_input).grid(column=0,row=8,columnspan=4)

                def cc_payment():
                    print(postcode_input.get())
                    anAddress=aShop.updateDeliveryAddress(street_input.get(),suburb_input.get(),city_input.get(),postcode_input.get(),aOrder)
                    print(anAddress)
                    print(aOrder)
                    address_window.destroy()
                    cc_payment_window=tk.Tk()
                    cc_payment_window.title('Credit Card Payment')
                    cc_payment_window.geometry('400x400')
                    
                    def confirm_payment():
                        aShop.updateCCPayment(orderAmount,cc_number_input.get(),cc_expired_input.get(),cc_holder_input.get(),CVC_input.get(),aOrder)
                        showinfo(title='success',message='Thank you for your order,Your order number is {}'.format(orderID))
                        cc_payment_window.destroy()
                        member_page()
                        aShop.emptyCart(memberName)
                
                    #cc payment frame
                    cc_payment_frame=tk.Frame(cc_payment_window)
                    cc_payment_frame.grid(column=0,row=0,columnspan=3)

                    # cc payment amount label
                    cc_payment_label=tk.Label(cc_payment_frame,text='Payment Amount:{}'.format(orderAmount))
                    cc_payment_label.grid(column=1,row=1,columnspan=3)

                    # cc number label and entry
                    cc_number_label=tk.Label(cc_payment_frame,text='Card Number').grid(column=1,row=2)
                    cc_number_input=StringVar()
                    cc_number_entry=tk.Entry(cc_payment_frame,textvariable=cc_number_input).grid(column=1,row=3)

                    # cc expired date label and entry
                    cc_expired_label=tk.Label(cc_payment_frame,text='Expired Date').grid(column=1,row=4)
                    cc_expired_input=StringVar()
                    cc_expired_entry=tk.Entry(cc_payment_frame,textvariable=cc_expired_input).grid(column=1,row=5)

                    # cc holder label and entry
                    cc_holder_label=tk.Label(cc_payment_frame,text='Card Holder').grid(column=1,row=6)
                    cc_holder_input=tk.StringVar()
                    cc_holder_entry=tk.Entry(cc_payment_frame,textvariable=cc_holder_input).grid(column=1,row=7)

                    # CVC label and entry
                    CVC_label=tk.Label(cc_payment_frame,text="CVC").grid(column=1,row=8)
                    CVC_input=StringVar()
                    CVC_entry=tk.Entry(cc_payment_frame,textvariable=CVC_input).grid(column=1,row=9)

                    #confirm payment button
                    confirm_payment_button=tk.Button(cc_payment_frame,text='Confirm Payment',command=confirm_payment).grid(column=1,row=10)


                def bank_payment():
                    aShop.updateDeliveryAddress(street_input.get(),suburb_input.get(),city_input.get(),postcode_input.get(),aOrder)
                    address_window.destroy()
                    bank_payment_window=tk.Tk()
                    bank_payment_window.title('Bank Payment')
                    bank_payment_window.geometry('400x400')
                    
                    def confirm_payment():
                        aShop.updateBankPayment(orderAmount,bank_number_input.get(),bank_holder_input.get(),aOrder)
                        showinfo(title='success',message='Order has been created successfully,thank you for your order')
                        bank_payment_window.destroy()
                
                    # bank payment frame
                    bank_payment_frame=tk.Frame(bank_payment_window)
                    bank_payment_frame.grid(column=0,row=0,columnspan=3)

                    # bank  payment amount label
                    bank_payment_label=tk.Label(bank_payment_frame,text='Payment Amount:{}'.format(orderAmount))
                    bank_payment_label.grid(column=1,row=1,columnspan=3)

                    # cc number label and entry
                    bank_number_label=tk.Label(bank_payment_frame,text='Bank Account Number').grid(column=1,row=2)
                    bank_number_input=StringVar()
                    bank_number_entry=tk.Entry(bank_payment_frame,textvariable=bank_number_input).grid(column=1,row=3)

                    # bank holder label and entry
                    bank_holder_label=tk.Label(bank_payment_frame,text='Account Owner').grid(column=1,row=4)
                    bank_holder_input=tk.StringVar()
                    bank_holder_entry=tk.Entry(bank_payment_frame,textvariable=bank_holder_input).grid(column=1,row=5)



                    #confirm payment button
                    confirm_payment_button=tk.Button(bank_payment_frame,text='Confirm Payment',command=confirm_payment).grid(column=1,row=6)


                # Credit card payment button
                CCpayment_button=tk.Button(address_frame,text="Pay by Credit Card",command=cc_payment).grid(column=1,row=9,padx=20,pady=40)
                # Bank payment button
                bank_payment_button=tk.Button(address_frame,text='Pay by Bank Account',command=bank_payment).grid(column=3,row=9,padx=20,pady=40)
                


            #shopping cart frame
            cart_frame=tk.Frame(checkout_window)
            cart_frame.grid(column=0,row=1,columnspan=3,padx=20)

            #shopping cart treeview
            columns=('item_name','item_quantity','total_price')
            cart_treeview=ttk.Treeview (cart_frame,columns=columns,show='headings')
            cart_treeview.heading('item_name',text='Item Name')
            cart_treeview.heading('item_quantity',text='Quantity')
            cart_treeview.heading('total_price',text='Total Price')
            cart_treeview.grid(column=0,row=1,columnspan=3)
            cartlist=aShop.viewCart(memberName)
            for item in cartlist:
                cart_treeview.insert('',tk.END,values=item)

     

            #sub total label
            sub_total_label=tk.Label(cart_frame,text='Sub Total')
            sub_total_label.grid(column=0,row=2)

            #sub total value label
            sub_total_value_label=tk.Label(cart_frame,text='$0.00',bg='white')
            sub_total_value_label.grid(column=1,row=2)
            sub_total_value_label.config(text=aShop.getSubTotal(memberName))

                #delivery cost label
            delivery_cost_label=tk.Label(cart_frame,text='Delivery Cost').grid(column=0,row=3)

            #shipping cost value label
            ship_cost_label=tk.Label(cart_frame,text='$5.0').grid(column=1,row=3)

            # create order button
            create_order_button=tk.Button(cart_frame,text='Create Order',command=create_order)
            create_order_button.grid(column=2,row=3)
    
        def order_history():
            order_history_window = tk.Tk()
            order_history_window.title('Order History Page')
            order_history_window.geometry("800x1200")


            #order history frame
            order_frame=tk.Frame(order_history_window)
            order_frame.grid(column=0,row=1)

            #order history label
            order_history_label=tk.Label(order_frame,text='My Orders')
            order_history_label.grid(column=0,row=0)
                
            #Order Details treeview
            columns=('order_ID','order_date','order_status','amount')
            order_treeview=ttk.Treeview (order_frame,columns=columns,show='headings')
            order_treeview.heading('order_ID',text='Order ID')
            order_treeview.heading('order_date',text='Order Date')
            order_treeview.heading('order_status',text='Order Status')
            order_treeview.heading('amount',text='Amount')
            order_treeview.grid(column=0,row=1,columnspan=2)
            orderlist=aShop.memberViewAllOrders(memberName)
            for item in orderlist:
                order_treeview.insert('',tk.END,values=item)

            
            # def show_order_detail():
            #     pass
            
            def cancel_order():
                selected_order=order_treeview.selection()[0]
                orderID=order_treeview.item(selected_order)['values'][0]
                if not selected_order:
                    showinfo(title='Alert',message='Please select a Order')
                info=aShop.cancelOrder(orderID,memberName)
                showinfo(message=info)
     


            # # view order details button
            # view_order_details_button=tk.Button(order_frame,text='View Order',command=show_order_detail)
            # view_order_details_button.grid(column=0,row=2)

            #cancel order button
            cancel_order_button=tk.Button(order_frame,text='Cancel Order',command=cancel_order)
            cancel_order_button.grid(column=1,row=2)





        #app frame
        app_frame=tk.Frame(member_window,relief=tk.FLAT,borderwidth=3)
        app_frame.grid(column=0,row=0,columnspan=4)

        #app label
        app_label=tk.Label(app_frame,text='Welcome Back, {}'.format(memberName))
        app_label.grid(column=1, row=0, pady=10)

        # Order History button
        order_history_button=tk.Button(app_frame,text='Order History',command=order_history).grid(column=3,row=0,padx=10)

        #nav frame
        nav_frame=tk.Frame(member_window)
        nav_frame.grid(column=0,row=1,sticky=tk.N,columnspan=2)

        #view product button
        view_prod_button=tk.Button(nav_frame,text=' Search Product By Category',command=search_prod_by_category)
        view_prod_button.grid(column=0,row=1,padx=25)

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
        cart_frame.grid(column=0,row=3,columnspan=4,padx=20)

        # shopping cart label
        cart_label=tk.Label(cart_frame,text='Shopping Cart')
        cart_label.grid(column=2,row=0)

        #shopping cart treeview
        columns=('item_name','item_quantity','total_price')
        cart_treeview=ttk.Treeview (cart_frame,columns=columns,show='headings')
        cart_treeview.heading('item_name',text='Item Name')
        cart_treeview.heading('item_quantity',text='Quantity')
        cart_treeview.heading('total_price',text='Total Price')
        cart_treeview.grid(column=0,row=1,columnspan=3)
        cartlist=aShop.viewCart(memberName)
        for item in cartlist:
            cart_treeview.insert('',tk.END,values=item)


        # remove item button
        remove_button=tk.Button(cart_frame,text='Remove Item',command=remove_item)
        remove_button.grid(column=0,row=2)

        # empty cart button
        empty_cart_button=tk.Button(cart_frame,text='Empty Cart',command=empty_cart)
        empty_cart_button.grid(column=1,row=2)

        #checkout button
        checkout_button=tk.Button(cart_frame,text='Checkout',command=checkout)
        checkout_button.grid(column=2,row=2)

        
        #sub total label
        sub_total_label=tk.Label(cart_frame,text='Sub Total')
        sub_total_label.grid(column=1,row=3)

        #sub total value label
        sub_total_value_label=tk.Label(cart_frame,text='$0.00',bg='white')
        sub_total_value_label.grid(column=2,row=3)
        sub_total_value_label.config(text=aShop.getSubTotal(memberName))



def guest_page():
    login_window.destroy()
    guest_window=tk.Tk()
    guest_window.title('Lincoln Online Shop')
    guest_window.geometry("800x1000")


     
   
    def search_prod_by_name():
            prod.set(aShop.searchProductByName2(search_prod_entry.get().lower()))


    def search_prod_by_category():
        try:
            prod.set(aShop.searchProductByCategory(search_prod_entry.get().lower()))
        except Exception as ex1:   
            showinfo(title='error',message=ex1)

        

    def show_prod_detail():
        selected_prod_indics=prod_listbox.curselection()
        selected_prod=prod_listbox.get(selected_prod_indics)
        prod__detail_label2.config(text=aShop.viewProductDetails(selected_prod))


    def add_to_cart():
        # cart_treeview.delete(0.0,tk.END)
        selected_prod_indics=prod_listbox.curselection()
        selected_prod=prod_listbox.get(selected_prod_indics)
        print(selected_prod)
        aShop.addItem('guest',selected_prod)
        cart_list=aShop.viewCart('guest')
        cart_treeview.delete(*cart_treeview.get_children())
        for content in cart_list:
            cart_treeview.insert('',tk.END,values=content)
        sub_total_value_label.config(text=aShop.getSubTotal('guest'))


    def remove_item():
        selected_item=cart_treeview.selection()[0]
        pname=cart_treeview.item(selected_item)['values'][0]
        aShop.removeItem('guest',pname)
        cart_treeview.delete(selected_item)
        print(len(aShop.viewCart('guest')))
        sub_total_value_label.config(text=aShop.getSubTotal('guest'))



    def empty_cart():
        
        cart_treeview.delete(*cart_treeview.get_children())
        aShop.emptyCart('guest')
        print(len(aShop.viewCart('guest')))
        sub_total_value_label.config(text=aShop.getSubTotal('guest'))
    
    def checkout():
    ####To do: change to badrequestError to throw message from controller
        if aShop.viewCart('guest')==[]:
            showinfo(title='error',message='Cart is empty')
        else:    
            showinfo(title='error', message='Please Register first')
            guest_window.destroy()
            register_window=tk.Tk()
            register_window.title('Register Form')
            

            def register():
                aMember=aShop.guestGetRegistered(name_input.get(),phone_input.get(),email_input.get(),password_input.get())
                print('member lens:{}'.format(len(aShop.allMembers)))
                memberName=name_input.get()
                register_window.destroy()
                checkout_window = tk.Tk()
                checkout_window.title('Checkout Page')
                checkout_window.geometry("800x1200")

                def create_order():
                    checkout_window.destroy()
                    address_window=tk.Tk()
                    address_window.title('Shipping Address')
                    address_window.geometry('500x800')
                    print(memberName)
                    orderDetails=aShop.placeOrder(date.today(),memberName)
                    aOrder=orderDetails[0]
                    orderAmount=orderDetails[1]
                    orderID=orderDetails[2]
                    print(aOrder)
                    print(orderID)
                    print("orderAmount:{}".format(orderAmount))

                    # address frame
                    address_frame=tk.Frame(address_window,width=400,height=600)
                    address_frame.grid(column=3,row=0)
                    # enter address label
                    address_label=tk.Label(address_frame,text='Please enter delivery Address')
                    address_label.grid(column=0,row=0,columnspan=4)

                    # street label
                    street_label=tk.Label(address_frame,text='Street').grid(column=2,row=1)
                    street_input=tk.StringVar()
                    # street entry
                    street_entry=tk.Entry(address_frame,textvariable=street_input).grid(column=0,row=2,columnspan=4)
                    # suburb labels
                    suburb_label=tk.Label(address_frame,text='Suburb').grid(column=2,row=3)
                    # suburb entry
                    suburb_input=tk.StringVar()
                    suburb_entry=tk.Entry(address_frame,textvariable=suburb_input).grid(column=0,row=4,columnspan=4)
                    # city labels
                    city_label=tk.Label(address_frame,text='City').grid(column=2,row=5)
                    # city entry
                    city_input=tk.StringVar()
                    city_entry=tk.Entry(address_frame,textvariable=city_input).grid(column=0,row=6,columnspan=4)
                    # city labels
                    postcode_label=tk.Label(address_frame,text='Postcode').grid(column=2,row=7)
                    # city entry
                    postcode_input=tk.StringVar()
                    postcode_entry=tk.Entry(address_frame,textvariable=postcode_input).grid(column=0,row=8,columnspan=4)

                    def cc_payment():
                        print(postcode_input.get())
                        anAddress=aShop.updateDeliveryAddress(street_input.get(),suburb_input.get(),city_input.get(),postcode_input.get(),aOrder)
                        print(anAddress)
                        print(aOrder)
                        address_window.destroy()
                        cc_payment_window=tk.Tk()
                        cc_payment_window.title('Credit Card Payment')
                        cc_payment_window.geometry('400x400')
                        
                        def confirm_payment():
                            aCCPayment=aShop.updateCCPayment(orderAmount,cc_number_input.get(),cc_expired_input.get(),cc_holder_input.get(),CVC_input.get(),aOrder)
                            print(aCCPayment)
                            showinfo(title='success',message='Thank you for your order,Your order number is {}'.format(orderID))
                            cc_payment_window.destroy()

                        #cc payment frame
                        cc_payment_frame=tk.Frame(cc_payment_window)
                        cc_payment_frame.grid(column=0,row=0,columnspan=3)

                        # cc payment amount label
                        cc_payment_label=tk.Label(cc_payment_frame,text='Payment Amount:{}'.format(orderAmount))
                        cc_payment_label.grid(column=1,row=1,columnspan=3)

                        # cc number label and entry
                        cc_number_label=tk.Label(cc_payment_frame,text='Card Number').grid(column=1,row=2)
                        cc_number_input=StringVar()
                        cc_number_entry=tk.Entry(cc_payment_frame,textvariable=cc_number_input).grid(column=1,row=3)

                        # cc expired date label and entry
                        cc_expired_label=tk.Label(cc_payment_frame,text='Expired Date').grid(column=1,row=4)
                        cc_expired_input=StringVar()
                        cc_expired_entry=tk.Entry(cc_payment_frame,textvariable=cc_expired_input).grid(column=1,row=5)

                        # cc holder label and entry
                        cc_holder_label=tk.Label(cc_payment_frame,text='Card Holder').grid(column=1,row=6)
                        cc_holder_input=tk.StringVar()
                        cc_holder_entry=tk.Entry(cc_payment_frame,textvariable=cc_holder_input).grid(column=1,row=7)

                        # CVC label and entry
                        CVC_label=tk.Label(cc_payment_frame,text="CVC").grid(column=1,row=8)
                        CVC_input=StringVar()
                        CVC_entry=tk.Entry(cc_payment_frame,textvariable=CVC_input).grid(column=1,row=9)

                        #confirm payment button
                        confirm_payment_button=tk.Button(cc_payment_frame,text='Confirm Payment',command=confirm_payment).grid(column=1,row=10)


                    def bank_payment():
                        aShop.updateDeliveryAddress(street_input.get(),suburb_input.get(),city_input.get(),postcode_input.get(),aOrder)
                        address_window.destroy()
                        bank_payment_window=tk.Tk()
                        bank_payment_window.title('Bank Payment')
                        bank_payment_window.geometry('400x400')
                        
                        def confirm_payment():
                            aShop.updateBankPayment(orderAmount,bank_number_input.get(),bank_holder_input.get(),aOrder)
                            showinfo(title='success',message='Thank you for your order,Your order number is {}'.format(orderID))
                            bank_payment_window.destroy()
                    
                        # bank payment frame
                        bank_payment_frame=tk.Frame(bank_payment_window)
                        bank_payment_frame.grid(column=0,row=0,columnspan=3)

                        # bank  payment amount label
                        bank_payment_label=tk.Label(bank_payment_frame,text='Payment Amount:{}'.format(orderAmount))
                        bank_payment_label.grid(column=1,row=1,columnspan=3)

                        # cc number label and entry
                        bank_number_label=tk.Label(bank_payment_frame,text='Bank Account Number').grid(column=1,row=2)
                        bank_number_input=StringVar()
                        bank_number_entry=tk.Entry(bank_payment_frame,textvariable=bank_number_input).grid(column=1,row=3)

                        # bank holder label and entry
                        bank_holder_label=tk.Label(bank_payment_frame,text='Account Owner').grid(column=1,row=4)
                        bank_holder_input=tk.StringVar()
                        bank_holder_entry=tk.Entry(bank_payment_frame,textvariable=bank_holder_input).grid(column=1,row=5)



                        #confirm payment button
                        confirm_payment_button=tk.Button(bank_payment_frame,text='Confirm Payment',command=confirm_payment).grid(column=1,row=6)


                    # Credit card payment button
                    CCpayment_button=tk.Button(address_frame,text="Pay by Credit Card",command=cc_payment).grid(column=1,row=9,padx=20,pady=40)
                    # Bank payment button
                    bank_payment_button=tk.Button(address_frame,text='Pay by Bank Account',command=bank_payment).grid(column=3,row=9,padx=20,pady=40)
                    
            
                #shopping cart frame
                cart_frame=tk.Frame(checkout_window)
                cart_frame.grid(column=0,row=1,columnspan=3,padx=20)

                #shopping cart treeview
                columns=('item_name','item_quantity','total_price')
                cart_treeview=ttk.Treeview (cart_frame,columns=columns,show='headings')
                cart_treeview.heading('item_name',text='Item Name')
                cart_treeview.heading('item_quantity',text='Quantity')
                cart_treeview.heading('total_price',text='Total Price')
                cart_treeview.grid(column=0,row=1,columnspan=3)
                cartlist=aShop.viewCart(memberName)
                for item in cartlist:
                    cart_treeview.insert('',tk.END,values=item)

        
                #sub total label
                sub_total_label=tk.Label(cart_frame,text='Sub Total')
                sub_total_label.grid(column=0,row=2)

                #sub total value label
                sub_total_value_label=tk.Label(cart_frame,text='$0.00',bg='white')
                sub_total_value_label.grid(column=1,row=2)
                sub_total_value_label.config(text=aShop.getSubTotal(memberName))

                # create order button
                create_order_button=tk.Button(cart_frame,text='Create Order',command=create_order)
                create_order_button.grid(column=2,row=2)
        


            # register form frame
            register_frame=tk.Frame(register_window).grid(column=0,row=0)

            # member name label and entry
            member_name_label=tk.Label(register_frame,text='Please enter your name').grid(column=0,row=0)
            name_input=tk.StringVar()
            member_name_entry=tk.Entry(register_frame,textvariable=name_input).grid(column=0,row=1)

            # member phone label and entry
            member_phone_label=tk.Label(register_frame,text='Please enter your phone number').grid(column=0,row=2)
            phone_input=tk.StringVar()
            member_phone_entry=tk.Entry(register_frame,textvariable=phone_input).grid(column=0,row=3)

            # member email label and entry
            member_email_label=tk.Label(register_frame,text='Please enter your email').grid(column=0,row=4)
            email_input=tk.StringVar()
            member_email_entry=tk.Entry(register_frame,textvariable=email_input).grid(column=0,row=5)

            # member password label and entry
            password_label=tk.Label(register_frame,text='Please enter a password').grid(column=0,row=6)
            password_input=tk.StringVar()
            password_entry=tk.Entry(register_frame,textvariable=password_input).grid(column=0,row=7)

            # register button
            register_button=tk.Button(register_frame,text='Register',command=register).grid(column=1,row=8,pady=40)


    #app frame
    app_frame=tk.Frame(guest_window,relief=tk.FLAT,borderwidth=3)
    app_frame.grid(column=0,row=0,sticky=tk.N,padx=(100,0))

    #app label
    app_label=tk.Label(app_frame,text='Welcome to Lincoln Online Shop')
    app_label.grid(column=1, row=0, pady=10)

    #nav frame
    nav_frame=tk.Frame(guest_window)
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
    all_prod_frame=tk.Frame(guest_window)
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
    prod_detail_frame=tk.Frame(guest_window)
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
    cart_frame=tk.Frame(guest_window)
    cart_frame.grid(column=0,row=3,columnspan=4,padx=20)

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
    cartlist=aShop.viewCart('guest')
    for item in cartlist:
        cart_treeview.insert('',tk.END,values=item)


    # remove item button
    remove_button=tk.Button(cart_frame,text='Remove Item',command=remove_item)
    remove_button.grid(column=0,row=2)

    # empty cart button
    empty_cart_button=tk.Button(cart_frame,text='Empty Cart',command=empty_cart)
    empty_cart_button.grid(column=1,row=2)

    #checkout button
    checkout_button=tk.Button(cart_frame,text='Checkout',command=checkout)
    checkout_button.grid(column=2,row=2)

    #sub total label
    sub_total_label=tk.Label(cart_frame,text='Sub Total')
    sub_total_label.grid(column=1,row=3)

    #sub total value label
    sub_total_value_label=tk.Label(cart_frame,text='$0.00',bg='white')
    sub_total_value_label.grid(column=2,row=3)
    sub_total_value_label.config(text=aShop.getSubTotal('guest'))





def staff_page():
    aStaff=aShop.staffLogIn(username.get(),password.get())
    if aStaff:
        print(aStaff)
        staffName=username.get()
        login_window.destroy()
        staff_window = tk.Tk()
        staff_window.title('Staff Page')
        staff_window.geometry("600x1200")
        
        #Staff Page label
        staff_label=tk.Label(staff_window,text='Staff Management System').grid(column=0,row=1,columnspan=2,pady=20)

        #orders frame
        order_frame=tk.Frame(staff_window)
        order_frame.grid(column=0,row=2,columnspan=2,padx=20)

        #orders Label
        order_label=tk.Label(staff_window,text='All Orders')

        #Order Details treeview
        columns=('order_ID','member_name','order_date','order_status','amount')
        order_treeview=ttk.Treeview (order_frame,columns=columns,show='headings')
        order_treeview.heading('order_ID',text='Order ID')
        order_treeview.heading('member_name',text='Member Name')
        order_treeview.heading('order_date',text='Order Date')
        order_treeview.heading('order_status',text='Order Status')
        order_treeview.heading('amount',text='Amount')
        order_treeview.grid(column=0,row=1,columnspan=2)
        orderlist=aShop.staffViewOrders(staffName)
        for item in orderlist:
            order_treeview.insert('',tk.END,values=item)
        
        # Order Status options
        order_status_options=['processing', 'awaiting shipment', 'shipped', 'delivered','Cancelled']
        order_status=tk.StringVar()
        order_status.set('select new order status')
        status_option=tk.OptionMenu(order_frame,order_status,*order_status_options).grid(column=0,row=5)

        # Update Order Status button
        update_status_button=tk.Button(order_frame,text='Update Order Status').grid(column=1,row=5,pady=30)


        #report frame
        report_frame=tk.Frame(staff_window).grid(column=0,row=7,columnspan=2)

        # options month for report
        OPTIONS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
        report_month = StringVar()
        report_month.set(OPTIONS[0]) # default value

        select_month_option = tk.OptionMenu(report_frame, report_month, *OPTIONS).grid(column=0,row=10)


        #Order Details treeview
        columns=('order_ID','member_name','order_date','order_status','amount')
        order_treeview=ttk.Treeview (report_frame,columns=columns,show='headings')
        order_treeview.heading('order_ID',text='Order ID')
        order_treeview.heading('member_name',text='Member Name')
        order_treeview.heading('order_date',text='Order Date')
        order_treeview.heading('order_status',text='Order Status')
        order_treeview.heading('amount',text='Amount')
        order_treeview.grid(column=0,row=8,columnspan=2)
        orderlist=aShop.staffViewOrders(staffName)
        for item in orderlist:
            order_treeview.insert('',tk.END,values=item)


         # generate report button
        genreport_button=tk.Button(report_frame,text='Generate Report').grid(column=1,row=10)   




            










# Member login button
login_button = tk.Button(login_window, text="Member Login",command=member_page).grid(row=4, column=0,padx=5)   

#Staff login Button
staff_login_button=tk.Button(login_window,text='Staff Login',command=staff_page).grid(row=4,column=1)
# Guest view button
guest_view_button=tk.Button(login_window, text="Shop as a Guest",command=guest_page).grid(row=4, column=2)

 
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





 

if __name__ == "__main__": 
    login_window.mainloop()