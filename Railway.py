#!/usr/bin/env python
# coding: utf-8

# In[28]:


import random
import os


# In[1]:


class Train: 
    def __init__(self, train_no, name, source, destination, seats):
        self.train_no = train_no
        self.name = name
        self.source = source
        self.destination = destination
        self.seats = seats
        


# In[3]:


class Passenger:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# In[32]:


class BookingSystem:
    def __init__(self):
        self.trains = []
        self.load_train()
        self.booking_file = "booking.txt"
        
    def load_train(self):
        self.trains = [
            Train("1001","Rajdhani Express", "Delhi", "Mumbai", 120),
            Train("1002", "Shatabdi Express", "Delhi", "Mumbai", 120),
            Train("1003", "Garib Rath", "Kolkata", "Patna", 90),
            Train("1004", "Vande Bharat Express", "Varanasi", "Delhi", 190),
            Train("1005", "Tejas Express", "Delhi", "Kerala", 130),
        ]
    def view_trains(self):
        print("Available Trains:")
        print(f"{'Train NO':<10}{'Train Name':<20}{'Source':<15}{'Destination':<15}{'Seats':<10}")
        for i in self.trains:
            print(f"{i.train_no:<10}{i.name:<20}{i.source:<15}{i.destination:<15}{i.seats:<10}")
        print()
        
    def pnr(self):
        return "PNR" + str(random.randint(10000, 99999))

    def book_ticket(self):
        train_no = input("Enter Train no to book: ")
        train = None
        for i in self.trains:
            if i.train_no == train_no:
                train = i
                break
        if not train:
            print("Invalid Train number!\n")
            return
        name = input("Enter your name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender : ")
        pnr = self.pnr()
        passenger = Passenger(name, age, gender)

        booking = f"{pnr},{passenger.name},{passenger.age},{passenger.gender},{train.train_no},{train.name},{train.source},{train.destination}\n"
        with open(self.booking_file, "a") as f:
            f.write(booking)
        print(f"\n Ticket booked!!!!!!")
        print(f"Your PNR: {pnr}\n")
    def view_booking(self):
        if not os.path.exists(self.booking_file):
            print("\n No bookings yet! \n")
            return
        print("\nBookings: ")
        print(f"{"PNR":<10} {"Name":<15} {"Age":<5} {"Gender":<8} {"Train no":<10} {"Train name":<20} {"Source": <15} {"Destination":<15}")

        with open(self.booking_file, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 8:
                    print("{:<10} {:<15} {:<5} {:<8}{:<10} {:<20} {:<15} {:<15}".format(*data))
        print()
    def cancel_ticket(self):
        if not os.path.exists(self.booking_file):
            print("\n No Bookings found!\n")
            return
        pnr = input("Enter PNR to cancel: ")
        found = False

        with open(self.booking_file, "r") as f:
            lines = f.readlines()

        with open(self.booking_file, "w") as f:
            for line in lines:
                if line.startswith(pnr):
                    found = True
                    continue
                f.write(line)

        if found:
            print(f"\n Ticket with PNR {pnr} cancelled successfully!\n")
        else: 
            print("\nPNR not found!\n")


# In[33]:


def main():
    system = BookingSystem()
    while True:
        print("++ Railway Ticket boooking system ++")
        print("1. view trains")
        print("2. Book Ticket")
        print("3. view Bookings")
        print("4. Cancel Ticket")
        print("5. Exit")
        ch = input("Enter your choice: ")

        if ch == "1":
            system.view_trains()
        elif ch == "2":
            system.book_ticket()
        elif ch == "3":
            system.view_booking()
        elif ch == "4":
            system.cancel_ticket()
        elif ch == "5":
            print("Thank you")
            break
        else:
            print("Invalid Choice! Try again.\n")

if __name__ == "__main__":
    main()


# In[ ]:




