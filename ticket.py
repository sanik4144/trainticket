import random
from datetime import *

now = datetime.now()

current_date = date.today()
current_time = now.strftime("%H:%M:%S")
current_hr = now.strftime("%H")

class user:
    def __init__(self, name, mono) -> None:
        self.name = name
        self.mono = mono

def bookTrain():
    while True:
        tr = input("1. BANALATA\n2. PADMA\nChoose which train you want to travel: ")
        if tr == "1":
            train = "BANALATA"
            break
        elif tr == "2":
            train = "PADMA"
            break
        else:
            print("Wrong Input. Try Again")
        
    return train

def bookCoach():
    while True:
        ch = input("A B C D\nChoose which coach: ")
        if ch == "a" or ch == "A":
            coach = "A"
            break
        elif ch == "b" or ch == "B":
            coach = "B"
            break
        elif ch == "c" or ch == "C":
            coach = "C"
            break
        elif ch == "d" or ch == "D":
            coach = "D"
            break
        else:
            print("Wrong Input. Try Again") 
    
    return coach


seat_list = []
def bookSeat(caoch):
    available_seat = random.randint(0, 9)
    print("Available Seat: ", available_seat)
    numberOfSeat = int(input("Enter how many seats you want to book(1 - 4): "))
    while numberOfSeat > 4 or numberOfSeat < 1:
        print("You cannot book more than 4 or less than 1 seats")
        numberOfSeat = int(input("Enter how many seats you want to book(1 - 4): "))
    if available_seat == 0:
        print("No seat avalible in this coach.")
    elif available_seat >= numberOfSeat:
        print("Seat Booked: ", end="")
        for i in range(1, numberOfSeat+1):
            print(f"{caoch+str(i)}",end=" ")
            seat_list.append(caoch+str(i))
    else:
        print(f"{numberOfSeat} seats not available in this coach")
    
    return seat_list

name = input("Enter your name: ")
mono = input("Enter you mobile number: ")
usr = user(name, mono)

def display():
    print("Date: ", current_date)
    print("Time: ", current_time)
    current_hr_int = int(current_hr)
    if current_hr_int > 8 and current_hr_int < 23:
        train = bookTrain()
        coach = bookCoach()
        seat_list = bookSeat(coach)
        print("\n\n")

        if seat_list:
            print("Congratulations! Your ticket/s are booked successfully")
            print("Name: ", usr.name)
            print("Mobile Number: ",usr.mono)
            print("Train: ", train)
            print("Coach: ", coach)
            print("Booked Seats: ", seat_list)
        else:
            print("...Unsuccessful...")
    else:
        print("You can not book ticket at this time. Try again after 8:00 AM")


display()