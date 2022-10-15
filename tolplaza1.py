print("WELCOME TO TOLPLAZA")

two_wheeler=0
four_wheeler=0
truck_bus=0

def total():
    a=0*two_wheeler
    print("money collected from two wheeler is :",a)
    m=four_wheeler*250
    print("money collected from four_wheeler is :",m)
    n=truck_bus*450
    print("money collected from four_wheeler is :",n)
    w=a+m+n
    print("total money collected is:",w)


name ="main"

vehicle_options={

    1:"TWO WHEELER",
    2:"FOUR_WHEELER",
    3:"TRUCK_BUS",
    4:"EXIT"
    
    }

print(vehicle_options)
print("\n")

def print_vehicle():
    for key in vehicle_options.keys():
      print(key,'--', vehicle_options[key])

def option1():
    print("type of vehicle passed : two wheeler  ")
    while(True):
        global two_wheeler
        two_wheeler+=1
        print("number of 2 wheeler passed:",two_wheeler)
        break

def option2():
    print("type of vehicle passed : four wheeler ")
    while(True):
        global four_wheeler
        four_wheeler+=1
        print("number of 4 wheeler passed:",four_wheeler)
        break

def option3():
    print("type of vehicle passes : truck or bus")
    global truck_bus
    truck_bus+=1
    while(True):
        print("number of truck or bus passed:",truck_bus)
        break   
    
if name=="main":
    while(True):
        print("\n")
        print_vehicle()
        option = " "
        try:
            option = int(input("Enter the type of vehicle passed: "))
        except:
            print("wrong input,Please enter a number....")
        if option == 1:
            option1()
            total()
            
        elif option == 2:
            option2()
            total()
            
        elif option ==3:
            option3()
            total()
            
            
        elif option ==4:
            print("thanks")
            exit()
        else:
            print("Invalid option...Please enter a number between 1 and 4")


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
carc=0
carf=0
busc=0
busf=0
bikec=0

win= Tk()# Create an instance of tkinter frame
win.geometry("700x350")# Set the size of the tkinter window
win.config(bg='red')

# Define a function to show the popup message
def show_msg():
   messagebox.showinfo("Message","Hey There! Happy Journey.")

def car():
        global carc
        global carf
        text_box = Text(win,height=5,width=80)
        text_box.pack(expand=True)
        text_box.config(state='normal')
        text_box.delete("1.0","end")
      
        carc=carc+1
        carf=carf+250
        print("pay 250")
        print("Total cars passed=",carc)
        print("Total car fee=", carf)
        """messagebox.showinfo("Message",carf)
        messagebox.showinfo("Message",carf)"""
        text_box.insert('end', "Total Cars Passed= ")
        text_box.insert('end', carc)
        text_box.insert('end', " Total money Collected=")
        text_box.insert('end', carf)
        
def bus():
        global busc
        global busf
        busc=busc+1
        busf=busf+250
        print("pay 450")
        print("Total bus passed=",busc)
        print("Total bus fee=", busf)

def bike():
        global bikec
        bikec=bikec+1
        print("pay 00")
        print("Total bikes passed=",bikec)

# Add an optional Label widget
Label(win, text= "Select your vehicle!", font= ('Aerial 17 bold italic')).pack(pady= 30)


# Create a Button to display the message
ttk.Button(win, text= "good bye", command=show_msg).pack(pady= 20)
ttk.Button(win, text= "Car", command=car).pack(pady= 10)
ttk.Button(win, text= "Bus", command=bus).pack(pady= 10)
ttk.Button(win, text= "Bike", command=bike).pack(pady= 10)
ttk.Button(win, text= "Exit", command=exit).pack(pady= 10)

#Button.pack()

win.mainloop()

        
        
