# Import tkinter

from tkinter import *

from tkinter import ttk, messagebox, Scrollbar, StringVar, IntVar,BooleanVar

from tkinter.ttk import Treeview


# Initialize lists for financial details
model = []
rents = []
days = []
ins_cost = []
tax_cost = []
total_cost_list = []
financial_treeview = None


# Create Window.

root = Tk()

# Set Window Size and Title.

root.geometry("1364x766")

root.title("TG Enterprises")

root.configure(background='#C673FF')

label1 = Label(root, text="Welcome to TG Enterprises.", font=("Arial",35), bg='#C673FF', fg='white')
label1.pack(fill = X)

# Set Icon

root.wm_iconbitmap("C:\\Users\\92321\\OneDrive\\Desktop\\Muneeb\\University Documents\\Semester 1\\Programming 1\\My Prrojects\\TG.ico")

global per,name,pn,add,idcard,car

# Creating Personal Information Window
def per_info():
    global per,name,pn,add,idcard,car

       
    per = Toplevel(root)
    per.title("TG Enterprises.(Personal Information)")
    per.geometry("600x400")
    per.configure(bg='#C673FF')
    per.wm_iconbitmap("C:\\Users\\92321\\OneDrive\\Desktop\\Muneeb\\University Documents\\Semester 1\\Programming 1\\My Prrojects\\TG.ico")
    #creating a label
    Label(per, text="Name:", font=('arial',15),bg='#C673FF',fg='white').place(x=60,y=50)
    #creating an entry box
    name = Entry(per, font=('arial',15))
    name.place(x=122,y=54, width=200, height=25)
    #creating a label
    Label(per, text="Phone Number:", font=('arial',15),bg='#C673FF',fg='white').place(x=60,y=100)
    #creating an entry box
    pn = Entry(per, font=('arial',15))
    pn.place(x=200,y=100, width=200, height=25)
    #creating a label
    Label(per, text="Address:", font=('arial',15),bg='#C673FF',fg='white').place(x=60,y=150)
    #creating an entry box
    add = Entry(per, font=('arial',15))
    add.place(x=144,y=150, width=200, height=25)
    #creating a label
    Label(per, text="Identity Number:", font=('arial',15),bg='#C673FF',fg='white').place(x=60,y=200)
    #creating an entry box
    idcard = Entry(per, font=('arial',15))
    idcard.place(x=211,y=200, width=200, height=25)
    #creating a label
    Label(per, text="Rent or Return:", font=('arial',15),bg='#C673FF',fg='white').place(x=60,y=250)
    #creating an entry box
    car = Entry(per, font=('arial',15))
    car.place(x=211,y=250, width=200, height=25)


    def destroyy():
        global per,name,pn,add,idcard,car
        with open("C:/Users/92321/OneDrive/Desktop/Programing/TG Enterprises Records.txt",'a') as f:
            n=name.get()
            ad=add.get()
            idcad=idcard.get()
            cars=car.get()
            f.write(f"{n,ad,idcad,cars}\n")
        per.destroy()
    #creating a button
    b11 = Button(per, text='Submit', font=('arial',15), bg='#7700C8',fg='white',command=destroyy).place(x=250,y=300)

#Create the frame 1.

f1 = Frame(root,width=374, height=766,bg='#C673FF')
f1.place(x=0, y=0)

f2 = Frame(root,width=4, height=600,bg='white')
f2.place(x=366, y=75)

model= []
rents= []
days= []
ins_cost= []
tax_cost= []
total_cost= []

# Function to add car

global Tr,no_list,car_models_list,available_list,rent_list,liability_list,comprehensive_list

no_list = [1,2,3,4,5,6]

car_models_list = ["Suzuki Alto", "Honda Civic", "Kia Sportage"," Toyota Yaris"," Hyundai Sonata"," Toyota Fortuner"]

available_list = [3,4,2,3,1,2]

rent_list = [3500,5000,6000,4000,5500,7000]

liability_list = [300,350,500,300,300,500]

comprehensive_list = [550,750,700,600,600,700]

def rent_car():

    global f3, no_list, car_models_list, available_list, rent_list, liability_list, comprehensive_list,table,Tr



    #creating the frame

    f3 = Frame(root,width=990,height=700 ,bg='#C673FF', bd=15)
    f3.place(x=374,y=58)

    #creating the label

    Label(f3, text="Please Select a Car:", font=('arial',20),bg='#C673FF',fg='white').place(x=5,y=40)

    #creating the table
    Tr = ttk.Treeview(f3, columns=(1,2,3,4,5,6), show='headings', height='8')

    style = ttk.Style()

    style.configure('Treeview',bd=10,bg='grey')

    Tr.place(x=5,y=100)

    #setting the table column width

    Tr.column(1,width=80)

    Tr.column(2,width=150)

    Tr.column(3,width=110)

    Tr.column(4,width=110)

    Tr.column(5,width=160)

    Tr.column(6,width=220)

    #setting the table headings


    Tr.heading(1, text="No.")

    Tr.heading(2, text="Car Models")

    Tr.heading(3, text="Available")

    Tr.heading(4, text="Rent/Day")

    Tr.heading(5, text="Liability Insurance/Day")

    Tr.heading(6, text="Comprehensive Insurance/Day")

    #filling the table with data
    for i in range(len(no_list)):

        Tr.insert('','end', values=(no_list[i],car_models_list[i],available_list[i],rent_list[i],liability_list[i],comprehensive_list[i]))

    #creating a scroll bar

    scroll_bar = ttk.Scrollbar(f3, orient="vertical", command=Tr.yview)

    scroll_bar.place(x=837, y=100, height='185')

    Tr.configure(yscrollcommand=scroll_bar.set)  

    #creating the label

    Label(f3, text="Enter the Number of Days:", font=('arial',15),bg='#C673FF',fg='white').place(x=5,y=300)

    #creating an entry box

    e2 = Entry(f3, font=('arial',15))

    e2.place(x=250,y=305, width=150, height=25)

    #creating a label

    Label(f3, text="Choose the Type of Insurance:", font=('arial',15),bg='#C673FF',fg='white').place(x=5,y=350)

    #creating radio buttons

    var1 = IntVar()

    r1 = Radiobutton(f3, text='Liability Insurance', font=('arial',15), bg='#C673FF',variable=var1, value=1).place(x=5,y=400)

    r2 = Radiobutton(f3, text='Comprehensive Insurance', font=('arial',15), bg='#C673FF',variable=var1, value=2).place(x=5,y=450)

    var2 = IntVar()

    c1 = Checkbutton(f3, text="Do you want a Driver (1000 Rs Per Day)", font=('arial',15), bg='#C673FF', variable=var2).place(x=5,y=500)

    def submit():
        global car_model, no_of_days, insurance_type, rent, liability_cost, comprehensive_cost, total_cost, ins
        no_of_days = e2.get()
        no_of_days = int(no_of_days)
        if no_of_days > 0:
            car_model = Tr.item(Tr.selection())['values'][1]
            rent = Tr.item(Tr.selection())['values'][3]
            liability_cost = Tr.item(Tr.selection())['values'][4]
            comprehensive_cost = Tr.item(Tr.selection())['values'][5]
            if var1.get() == 1:
                insurance_type = "Liability Insurance"
                ins = liability_cost
                if var2.get() == 0:
                    total_cost = (rent * no_of_days) + (liability_cost * no_of_days) + ((rent * no_of_days) * 0.05)
                else:
                    total_cost = (rent * no_of_days) + (liability_cost * no_of_days) + (
                                (rent * no_of_days) * 0.05) + (1000 * no_of_days)
            else:
                insurance_type = "Comprehensive Insurance"
                ins = comprehensive_cost
                if var2.get() == 0:
                    total_cost = (rent * no_of_days) + (comprehensive_cost * no_of_days) + ((rent * no_of_days) * 0.05)
                else:
                    total_cost = (rent * no_of_days) + (comprehensive_cost * no_of_days) + (
                                (rent * no_of_days) * 0.05) + (1000 * no_of_days)

            # Clear the lists before appending new values
            # model.clear()
            # rents.clear()
            # days.clear()
            # ins_cost.clear()
            # tax_cost.clear()
            # total_cost_list.clear()

            model.append(car_model)
            rents.append(rent)
            days.append(no_of_days)
            ins_cost.append(ins)
            tax_cost.append((rent * no_of_days) * 0.05)
            total_cost_list.append([total_cost])
            print(model)

            billing_summary()
        else:
            messagebox.showinfo("TG Enterprises", "Please enter a valid number of days")


    def add_car():
        global add_car_frame,e1,e2,e3,e4,e5

        add_car_frame = Toplevel(root)
        add_car_frame.title("TG Enterprises.(Add Car)")
        add_car_frame.geometry("600x400")
        add_car_frame.configure(bg='#C673FF')
        add_car_frame.wm_iconbitmap("C:\\Users\\92321\\OneDrive\\Desktop\\Muneeb\\University Documents\\Semester 1\\Programming 1\\My Prrojects\\TG.ico")
        #creating a label
        Label(add_car_frame, text="Car Model:", font=('arial',15),bg='#C673FF',fg='white').place(x=60,y=50)
        #creating an entry box
        e1 = Entry(add_car_frame, font=('arial',15))
        e1.place(x=160,y=50, width=200, height=25)
        #creating a label
        Label(add_car_frame, text="Available:", font=('arial',15),bg='#C673FF',fg='white').place(x=60,y=100)
        #creating an entry box
        e2 = Entry(add_car_frame, font=('arial',15))
        e2.place(x=150,y=100, width=200, height=25)
        #creating a label
        Label(add_car_frame, text="Rent/Day:", font=('arial',15),bg='#C673FF',fg='white').place(x=60,y=150)
        #creating an entry box
        e3 = Entry(add_car_frame, font=('arial',15))
        e3.place(x=155,y=150, width=200, height=25)
        #creating a label
        Label(add_car_frame, text="Liability Insurance/Day:", font=('arial',15),bg='#C673FF',fg='white').place(x=60,y=200)
        #creating an entry box
        e4 = Entry(add_car_frame, font=('arial',15))
        e4.place(x=270,y=200, width=200, height=25)
        #creating a label
        Label(add_car_frame, text="Comprehensive Insurance/Day:", font=('arial',15),bg='#C673FF',fg='white').place(x=60,y=250)
        #creating an entry box
        e5 = Entry(add_car_frame, font=('arial',15))
        e5.place(x=340,y=250, width=200, height=25)
        #creating a button
        b1 = Button(add_car_frame, text='Submit', font=('arial',15), bg='#7700C8',fg='white',command=submit_add_car).place(x=250,y=300)
    #creating the button
    b1 = Button(f3, text='Add Car', font=('arial',15), bg='#7700C8',fg='white',command=add_car,width=20).place(x=5,y=550)
    b2 = Button(f3, text='Submit', font=('arial',15), bg='#7700C8',fg='white',command=submit,width=20).place(x=299,y=550)


    def submit_add_car():
        global no_list, car_models_list, available_list, rent_list, liability_list, comprehensive_list,e1,e2,e3,e4,e5
        no_list.append(no_list[-1]+1)
        car_models_list.append(e1.get())
        available_list.append(int(e2.get()))
        rent_list.append(int(e3.get()))
        liability_list.append(int(e4.get()))
        comprehensive_list.append(int(e5.get()))
        table.insert('','end', values=(no_list[-1],car_models_list[-1],available_list[-1],rent_list[-1],liability_list[-1],comprehensive_list[-1]))
        add_car_frame.destroy()

    def billing_summary():
        global f4,ins,total_cost,rent,no_of_days,car_model,financial_data
        
    #Creating the frame for Bill
        f4 = Frame(root, width=990,height=700, bg='#C673FF', bd=15)
        f4.place(x=374,y=58)
        
    #Creating the label Billing Summary
        
        Label(f4, text="Billing Summary", font=('arial',27),bg='#C673FF',fg='white').place(x=300,y=0)
    #Creating a label Car Model
        
        Label(f4, text="Car Model:", font=('arial',20),bg='#C673FF',fg='white').place(x=220,y=120)

        Label(f4, text=car_model, font=('arial',20),bg='#C673FF',fg='white').place(x=470,y=120)
        
    #Creating a label Rent Cost
        
        Label(f4, text="Rent Cost:", font=('arial',20),bg='#C673FF',fg='white').place(x=220,y=180)

        Label(f4, text="Rs. "+str(rent*no_of_days), font=('arial',20),bg='#C673FF',fg='white').place(x=470,y=180)
        
    #Creating a label Number of Days
        
        Label(f4, text='Number of Days', font=('arial',20),bg='#C673FF',fg='white').place(x=220,y=240)

        Label(f4,text=str(no_of_days)+' Days', font=('arial',20),bg='#C673FF',fg='white').place(x=470,y=240)
        
    #Creating a label Insurance Cost
        
        Label(f4, text="Insurance Cost:", font=('arial',20),bg='#C673FF',fg='white').place(x=220,y=300)

        Label(f4, text="Rs. "+str(ins), font=('arial',20),bg='#C673FF',fg='white').place(x=470,y=300)
        
    #Creating a label Tax
        
        Label(f4, text="Tax:", font=('arial',20),bg='#C673FF',fg='white').place(x=220,y=360)

        Label(f4, text="Rs. "+str((rent*no_of_days)*0.05), font=('arial',20),bg='#C673FF',fg='white').place(x=470,y=360)
        
    #Creating a label Driver Cost
        
        Label(f4, text="Driver Cost:", font=('arial',20),bg='#C673FF',fg='white').place(x=220,y=420)

        Label(f4, text="Rs. "+str(1000 * no_of_days), font=('arial',20),bg='#C673FF',fg='white').place(x=470,y=420)
        
    #Creating a separator
        
        ttk.Separator(f4).place(x=222, y=44, width=377,height=3)
        ttk.Separator(f4).place(x=222, y=50, width=377,height=3)
        ttk.Separator(f4).place(x=90, y=469, width=599,height=3)
        ttk.Separator(f4).place(x=90, y=475, width=599,height=3)
        
    #Creating a label Tatol Cost
        
        Label(f4, text="Total Cost:", font=('arial',20),bg='#C673FF',fg='white').place(x=220,y=499)
        
        Label(f4, text="Rs. "+str(total_cost), font=('arial',20),bg='#C673FF',fg='white').place(x=470,y=499)


        def confirm_booking():
            global f4, available_list, ins, total_cost, rent, no_of_days, Tr, car_model
            selection = Tr.selection()
            if selection:
                index = int(Tr.item(selection[0])['values'][0])
                if available_list[no_list.index(index)] == 0:
                    messagebox.showinfo("TG Enterprises", "Sorry, this car is not available")
                    f4.destroy()
                else:
                    car_model = car_models_list[index - 1]  # Adjust index to match the list
                    available_list[index - 1] -= 1
                    update_treeview()
                    f4.destroy()
                    tax_0 = str((rent * no_of_days) * 0.05)
            else:
                messagebox.showinfo("TG Enterprises", "Please select a car to book")
                # Update the Treeview with the new available_list
            Tr.delete(*Tr.get_children())
            for j in range(len(no_list)):
                Tr.insert('', 'end', values=(no_list[j], car_models_list[j], available_list[j], rent_list[j], liability_list[j], comprehensive_list[j]))

        def update_treeview():
            global Tr
            Tr = ttk.Treeview(f3, columns=(1, 2, 3, 4, 5, 6), show='headings', height='8')
            Tr.delete(*Tr.get_children())
            for j in range(len(no_list)):
                Tr.insert('', 'end', values=(no_list[j], car_models_list[j], available_list[j], rent_list[j],
                                            liability_list[j], comprehensive_list[j]))

            
        def cancel_booking():
            global f4
            messagebox.showinfo("TG Enterprises","Your booking has successfully cancelled")
            f4.destroy()
    #creating the buttons
        b1 = Button(f4, text='Confirm', font=('arial',15), bg='#7700C8',fg='white',command=confirm_booking,width=20).place(x=180,y=550)
        b2 = Button(f4, text='Cancel', font=('arial',15), bg='#7700C8',fg='white',command=cancel_booking,width=20).place(x=430,y=550)  




def return_car():
    global f6,Label,car_models_list,available_list,Tr,car_select
    f6 = Frame(root, width=990,height=700, bg='#C673FF',bd=15)
    f6.place(x=374,y=58)
    Label00 = Label(f6, text="Please Select a Car:", font=('arial',20),bg='#C673FF',fg='white').place(x=277,y=40)
    #creating the dropdown menu
    car_select = ttk.Combobox(f6, value=car_models_list, font=('arial',15))
    car_select.place(x=277,y=111)
    #creating the submit button
    submit_button = Button(f6, text='Return',font=('arial',15), command=submit,width=22,bg='#C673FF',fg='white')
    submit_button.place(x=277,y=277)

def submit():
    global available_list,Tr,no_list
    car_model = car_select.get()
    for i in range(len(car_models_list)):
        if car_model == car_models_list[i]:
            available_list[i] += 1

            Tr = ttk.Treeview(f6, columns=(1,2,3,4,5,6), show='headings', height='8')
            Tr.delete(*Tr.get_children())
            
            for j in range(len(no_list)):
                Tr.insert('','end', values=(no_list[j],car_models_list[j],available_list[j],rent_list[j],liability_list[j],comprehensive_list[j]))
        # Update the Treeview with the new available_list
    Tr.delete(*Tr.get_children())
    for j in range(len(no_list)):
        Tr.insert('', 'end', values=(no_list[j], car_models_list[j], available_list[j], rent_list[j], liability_list[j], comprehensive_list[j]))

    messagebox.showinfo('Return Car', 'You have Successfully Returned a Car')
    f6.destroy()


# Updated financial function
def financial(root):
    global model, rents, days, ins_cost, tax_cost, total_cost_list
    
    f7 = Frame(root, width=990, height=700, bg='#C673FF')
    f7.place(x=374, y=58)

    # Label
    Label(f7, text='Financial Details:', bg='#C673FF', fg='white', font=('arial', 20)).place(x=5, y=40)

    # Table
    table = ttk.Treeview(f7, columns=['Car Model', 'Rent Cost', 'Number of Days', 'Insurance Cost', 'Tax', 'Total Cost'],
                         show='headings')
    table.place(x=5, y=100)

    # Table headings
    table.heading("Car Model", text="Car Model")
    table.heading("Rent Cost", text="Rent Cost")
    table.heading("Number of Days", text="Number of Days")
    table.heading("Insurance Cost", text="Insurance Cost")
    table.heading("Tax", text="Tax")
    table.heading("Total Cost", text="Total Cost")
    table.column(0, width=160)
    table.column(1, width=160)
    table.column(2, width=160)
    table.column(3, width=160)
    table.column(4, width=160)
    table.column(5, width=100)

    # Scrollbar
    ysb = ttk.Scrollbar(f7, orient=VERTICAL, command=table.yview)
    table.configure(yscrollcommand=ysb.set)
    ysb.place(x=907, y=100, height='224')
    table.place(x=5, y=100)

    # Populating table with all bookings
    for i in range(len(model)):
        table.insert('', 'end', values=(model[i], rents[i], days[i], ins_cost[i], tax_cost[i], total_cost_list[i][0]))

    # Total Income
    total_income = sum([item[0] for item in total_cost_list])  # Flatten the list before summing

    Label(f7, text="Total Income:", bg='#C673FF', font=('arial', 20), fg='white').place(x=5, y=350)
    Label(f7, text=total_income, bg='#C673FF', font=('arial', 20), fg='white').place(x=177, y=350)

    Label(f7, text="Total Insurance:", font=('arial', 20), bg='#C673FF', fg='white').place(x=5, y=420)
    Label(f7, text=sum(ins_cost), bg='#C673FF', font=('arial', 20), fg='white').place(x=211, y=420)

    Label(f7, text="Total Tax:", font=('arial', 20), bg='#C673FF', fg='white').place(x=5, y=490)
    Label(f7, text="Rs. " + str(sum(map(float, tax_cost))), font=('arial', 20), bg='#C673FF', fg='white').place(x=144,
                                                                                                                y=490)

    # OK Button
    Button(f7, text="OK", command=f7.destroy, font=('arial', 15), bg='#7700C8', fg='white', width=15).place(x=5, y=560)


# Label and Buttons in frame f1.

label2 = Label(f1, text="Please Select the Function:",font=("Arial",20),bg='#C673FF',fg='white')
label2.place(x=5, y=290)

label0 = Label(f1, text="Enter Your Information:",font=("Arial",20),bg='#C673FF',fg='white').place(x=5, y=180)

button0 = Button(f1, text="Personal Information",font=("Arial",15), width=18, command=per_info, bg='#7700C8', fg='white')
button0.place(x=15, y=240)

button1 = Button(f1, text="Car Rental",font=("Arial",15), width=18, command=rent_car, bg='#7700C8', fg='white')
button1.place(x=15, y=340)

button2 = Button(f1, text="Car Return",font=("Arial",15), width=18, command=return_car, bg='#7700C8', fg='white')
button2.place(x=15, y=390)

button3 = Button(f1, text="Total Financial Details",font=("Arial",15),width=18, command=lambda:financial(root), bg='#7700C8', fg='white')
button3.place(x=15, y=440)




root.mainloop()

#Coded By Muneeb Ali 

