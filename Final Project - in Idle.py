# Import the tkinter library
from tkinter import *
from tkinter import PhotoImage
import random 
import time 


master = Tk() #instance of a GUI

master.geometry("800x800")
#master.resizable(width=True, height=True)

master.title("Calories Burned Calculator") #this names the program



#---------------- function for calorie  caclculation --------------- 

def cals_burned():
   #get the values 
   dropdown_selection = clicked.get()
   radio_selection = radio.get()
   entry_value = duration.get()

   #calculation based on values 
   if dropdown_selection == "Walking":
        option_value = 1
   elif dropdown_selection == "Jogging":
        option_value = 1.5
   elif dropdown_selection == "Running":
        option_value = 2
   else:
        option_value = 3    #this is for swimming
    
   if radio_selection == 1:
        radio_value = 1
   elif radio_selection == 2:
        radio_value = 2
   else:
        radio_value = 3   #this is for high intensity
    
   try:
        entry_value = float(entry_value)  # Convert duration entry value to float
   except ValueError:
        calBurn.insert("end", "Invalid input. Please enter a number.")
        return
   
   Final = option_value * radio_value * entry_value
   calBurn.delete(1.0, END)
   calBurn.insert(END, "Total calories burned: " + str(Final))

#Clear function
def clear_text():
   calBurn.delete("1.0", END)

Button(master,text="Clear", command=clear_text).grid(row=17, column = 0)

#-----------------------------------------------------------------------
# Buttons to Calculate the formula
calculation = Button(master, 
                  text = "Calculate the calories!", 
                 fg = "blue", 
                command = cals_burned)


calBurn = Text(master, height=2, width=20)
#calBurn.delete(1.0, END)
#   calBurn.insert(END, "Total calories burned: " + str(Final))

#---------------------  RadioButton for Intensity Choice

def selection():
   selected = "You selected option " + str(radio.get()) 
   labelIntensity.config(text=selected)

radio = IntVar()

# Define radiobutton for each options
r1 = Radiobutton(master, text="Low intensity", variable=radio, value=1, command=selection)

r2 = Radiobutton(master, text="Medium intensity", variable=radio, value=2, command=selection)

r3 = Radiobutton(master, text="High intensity", variable=radio, value=3, command=selection)

# Define a label widget
labelIntensity = Label(master, text = " ")


#-----------------   Dropdown box for Workout Choice
def show(): 
    labelWC.config( text = clicked.get() ) 

optionsWC = [ 
    "Walking", 
    "Jogging", 
    "Running", 
    "Swimming", 
]
  
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Walking" ) 
  
# Create Dropdown menu 
dropWC = OptionMenu( master , clicked , *optionsWC ) 

WCbutton = Button(master, 
                  text = "click Me" , 
                  command = show )
  
# Create Label 
labelWC = Label( master , text = " " ) 


#---------------------- Entry box for duration of workout

duration = Entry(master, width=10)
duration.insert(0, "0.0")

#-------------------------------  

#Create a randomized workout routine
# for loop for workout and duration
def RNDworkout1():
    for workout, duration in zip(workoutList, workoutDuration):
        random_workout1.insert( INSERT, f"{workout} for {duration} seconds.")

workoutList = ["Walk", 
               "Run", 
               "Jog", 
               "Rest",
               "Row", 
               "Burpees"
               ]

# Generate random durations for each item
workoutDuration = [random.randint(30, 120) 
                   for _ in range(len(workoutList))]  

Random1 = Button(master,
                 text = "Random workout: Do this for 5 rounds!",
                 command = RNDworkout1)


random_workout1 = Text(master, height=7, width=40)

#Clear function
def clear_text():
   random_workout1.delete("1.0", END)


#Button for clearing
Button(master,text="Clear", command=clear_text).grid(row=25, column = 0)

#---------------------------- Random workout for swimming

def RNDworkout2():
    swimList
    random.shuffle(swimList)
    random_workout2.insert(INSERT, swimList)

swimList = ["freestyle for 100 yards", 
               "rest for 1 minute", 
               "freestytle for 50 yards - sprint!", 
               "backstroke for 75 yards",
               "breaststroke for 100 yards",
               "rest for 1 minute",
               "kick for 50 yards",
               "pull for 50 yards",
               "tread water for 2 minutes",
               "rest for 1 minute"
               ]

Random2 = Button(master,
                 text = "Random workout: Do this for 4 sets!",
                 command = RNDworkout2)

random_workout2 = Text(master, height=7, width=40)

#clear function
def clear_text():
   random_workout2.delete("1.0", END)

#Button to clear the Entry Widget
Button(master,text="Clear", command=clear_text).grid(row=29, column = 0)


#-------------------------------------  function to open a new window 
# on a button click
def openNewWindow():
     
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel(master)
 
    # title
    newWindow.title("New Window")
    newWindow.geometry("800x800")
 
    # text
    Label(newWindow, 
          text ="Swimming became an Olympic sport in 1904.").grid(row= 0, column = 0)

    
    # Image location
    image_path = "C:/Users/Mac Hurt/Pictures/Pool_Tkinter.gif"
    photo = PhotoImage(file=image_path)

    #Label widget to display the image
    labelNW = Label(newWindow, image=photo)
    labelNW.grid(row = 3, column = 0)
  
    newWindow.mainloop()

# button to open the new window
newWindow = Button(master, 
             text ="Click to open a new window to learn a fun fact!", 
             command = openNewWindow)
newWindow.grid(row=1, column = 2)


#-------------------------------------  function to open a third window  
#for a second image
def openNewWindow2():
     
    # Toplevel object which will be treated as a new window
    newWindow2 = Toplevel(master)
 
    # title
    newWindow2.title("New Window # 2")
    newWindow2.geometry("800x800")
 
    # text
    Label(newWindow2, 
          text ="Walking and running outdoors is great for your physical and mental health!").grid(row= 0, column = 0)

    
    # Image location
    image_path = "C:/Users/Mac Hurt/Pictures/Walk_Outside.gif"
    photo = PhotoImage(file=image_path)

    #Label widget to display the image
    labelNW2 = Label(newWindow2, image=photo)
    labelNW2.grid(row = 2, column = 1)
  
    newWindow2.mainloop()

# button to open the new window
newWindow2 = Button(master, 
             text ="Click to open a new window to learn a fun fact!", 
             command = openNewWindow2)
newWindow2.grid(row=4, column = 2)

#---------------------------------------------

#-----------------------------------------------------------------------
# Display the objects and buttons
Label(master, text="What kind of workout are you going to do?").grid(row=0, column=0)

dropWC.grid(row=2, column=0) 
labelWC.grid(row=3, column=0) 
WCbutton.grid(row=4, column=0) 


Label(master, text="How intense will the workout be?").grid(row=6, column=0)

r1.grid(row=8, column=0)
r2.grid(row=9, column=0)
r3.grid(row=10, column=0)

labelIntensity.grid(row = 11, column = 0)

Label(master, text="How many minutes will the workout be?").grid(row=13, column=0)

duration.grid(row = 14, column = 0)
calculation.grid(row = 15, column = 0)
calBurn.grid(row = 16, column = 0)

Label(master, text="Let's make you a random workout!").grid(row = 20, column = 0)
Random1.grid(row = 22, column = 0)
Random2.grid(row = 27, column = 0)

random_workout1.grid(row = 24, column = 0)
random_workout2.grid(row = 28, column = 0)

#durationOutput.grid(row = 15, column =2)


# Function for closing window 
   
def Close(): 
    master.destroy() 
  
# Button for closing 
exit_button = Button(master, text="Exit", command=Close) 
exit_button.grid(row = 30, column = 1) 

