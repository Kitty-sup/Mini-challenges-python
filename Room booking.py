#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
import random


# In[1]:


class Room:
    def __init__(self, room_no, ac, price, beds):
        self.room_no = room_no
        self.ac = ac
        self.price = price
        self.beds = beds
class Guest:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# In[38]:


class BookingSystem:
    def __init__(self):
        self.rooms=[]
        self.load_rooms()
        self.bookings = "bookings.txt"

    def load_rooms(self):
        self.rooms = [
            Room(101, "Yes", 999, 1),
            Room(102, "Yes", 1299, 2),
            Room(103, "No", 699, 1),
            Room(104, "No", 999, 2),
            Room(105, "Yes", 2999, 4),
            Room(201, "Yes", 999, 1),
            Room(202, "Yes", 1299, 2),
            Room(203, "No", 699, 1),
            Room(204, "No", 999, 2),
            Room(205, "Yes", 3199, 5),
        ]
    def view_rooms(self):
        print("Room details:")
        print(f"{'Room No':<9}{'AC Details':<15}{'Price':<10}{'Beds':<10}")
        for i in self.rooms:
            print(f"{i.room_no:<9}{i.ac:<15}{i.price:<10}{i.beds:<10}")
        print()
    def guest_id(self):
        return "ID"+str(random.randint(100,200))

    def booking(self):
        room_no = input("Enter room no to book: ")
        room = None
        for i in self.rooms:
            if str(i.room_no) == room_no:
                room = i
                break
        if not room:
            print("Sorry, you have entered wrong room number!\n")
            return
        name = input("Enter Guest name: ")
        age = input("Enter age: ")
        gender = input("Enter your gender: ")
        g_id = self.guest_id()
        guest = Guest(name, age, gender)
        booking = f"{g_id},{guest.name},{guest.age},{guest.gender},{room.room_no},{room.ac},{room.price},{room.beds}\n"
        with open(self.bookings, "a") as f:
            f.write(booking)
        print(f"\n Room booked!")
        print(f"Your Booking ID: {g_id}\n")

    def view_booking(self):
        if not os.path.exists(self.bookings):
            print("\n No booking has been done!\n")
            return
        print("\nBookings: ")
        print(f"{'ID':<9}{'Name':<15}{'Age':<5}{'Gender':<9}{'Room No':<9}{'AC Details':<15}{'Price':<10}{'Beds':<10}")
        with open(self.bookings, "r") as f:
            for i in f:
                data = i.strip().split(",")
                if len(data) == 8:
                    print("{:<9}{:<15}{:<5}{:<9}{:<9}{:<15}{:<10}{:<10}".format(*data))
        print()

    def cancel_booking(self):
        if not os.path.exists(self.bookings):
            print("\n No bookings found!\n")
            return
        g_id = input("Enter Booking id to cencal: ")
        found = False

        with open(self.bookings, "r") as f:
            lines = f.readlines()
        with open(self.bookings, "w") as f:
            for i in lines:
                if i.startswith(g_id):
                    found = True
                    continue
                f.write(i)
        if found:
            print(f"\n Booking with booking id : {g_id} cancelled successfully!\n")
        else:
            print("\n Booking id not found!\n")
            



# In[41]:


def main():
    system = BookingSystem()
    while True:
        print("======= Welcome to Hotel Bookig system ========")
        print("Choose according to your choice")
        print("1. View Rooms")
        print("2. Book a Room")
        print("3. View Booking")
        print("4. Cancel Booking")
        print("5. Exit")
        ch = input("Enter choice: ")
        if ch == "1":
            system.view_rooms()
        elif ch =="2":
            system.booking()
        elif ch == "3":
            system.view_booking()
        elif ch == '4':
            system.cancel_booking()
        elif ch == "5":
            break
        else:
            print("Wrong Choice!")
main()


# In[ ]:





# In[ ]:





# In[ ]:




