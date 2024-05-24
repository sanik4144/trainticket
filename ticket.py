import random

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
        ch = input("1. A\n2. B\n3. C\n4. D\nChoose which train you want to travel: ")
        if ch == "1" or ch == "a" or ch == "A":
            coach = "A"
            break
        elif ch == "2" or ch == "b" or ch == "B":
            coach = "B"
            break
        elif ch == "3" or ch == "c" or ch == "C":
            coach = "C"
            break
        elif ch == "4" or ch == "d" or ch == "D":
            coach = "D"
            break
        else:
            print("Wrong Input. Try Again") 
    
    return coach


seat_list = []
def bookSeat(caoch):
    available_seat = random.randint(5, 9)
    print("Available Seat: ", available_seat)
    numberOfSeat = int(input("Enter how many seats you want to book(1 - 4): "))
    while numberOfSeat > 4 or numberOfSeat < 1:
        print("You cannot book more than 4 or less than 1 seats")
        numberOfSeat = int(input("Enter how many seats you want to book(1 - 4): "))

    if available_seat >= numberOfSeat:
        print("Seat Booked: ", end="")
        for i in range(1, numberOfSeat+1):
            print(f"{caoch+str(i)}",end=" ")
            seat_list.append(caoch+str(i))
    else:
        print(f"{numberOfSeat} seats not available in this coach")
    
    return seat_list



def display():
    train = bookTrain()
    coach = bookCoach()
    seat_list = bookSeat(coach)
    print("\n\n")
    print("Train: ", train)
    print("Coach: ", coach)
    print("Booked Seats: ", seat_list)

display()