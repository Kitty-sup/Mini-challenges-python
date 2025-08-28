#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


from abc import ABC, abstractmethod
class Pet(ABC):
    def __init__(self, name, hunger, happiness):
        self.name=name
        self.__hunger=hunger
        self.__happiness=happiness
    def get_status(self):
        print(f"{self.name} has rate or hunger and happiness as {self.__hunger} and {self.__happiness}")
    def feed(self, value):
        self.__hunger= self.__hunger-value
        return self.__hunger
    def adjust_happiness(self, value):
        self.__happiness+=value
        return self.__happiness
    @abstractmethod
    def speak(self):
        pass
    @abstractmethod
    def play(self):
        pass
class Dog(Pet):
    def speak(self):
        return f"{self.name} woof"
    def play(self):
        self.adjust_happiness(2)
        self.feed(-1)
        return f"{self.name} is playing with ball."
class Cat(Pet):
    def speak(self):
        return f"{self.name} Meow"
    def play(self):
        self.adjust_happiness(2)
        self.feed(-1)
        return f"{self.name} is playing with string."
class Bird(Pet):
    def speak(self):
        return f"{self.name} Chirp"
    def play(self):
        self.adjust_happiness(2)
        self.feed(-1)
        return f"{self.name} is happy by singing."
        


# In[6]:


##### print("A GREAT WELCOME TO VIRTUAL PET SIMULATOR")
print("Here we have a list of PET, You can Choose your PET and and give name to it")
print("DOG\nCAT\nBird")
pet = input("Enter your choice: ").lower()
pet_name = input(f"Enter {pet} name: ")
if pet == "dog":
    my_pet=Dog(pet_name,5,5)
elif pet == "cat":
    my_pet=Cat(pet_name,5,5)
elif pet == "bird":
    my_pet=Bird(pet_name,5,5)
else:
    print("Offo, You made invalid choice, sorry")

while True:
    print("++++++++++++++++++")
    print("What would you like to do?")
    print("1.Feed your pet.🍉🍉")
    print("2.Play with your pet⚽⚽")
    print("3.Make your pet speak🔉🔉")
    print("4.Check pet status📃📃")
    print("5.Quit")
    ch = int(input("Enter choice: "))
    if ch==1:
        value = int(input("How much food you want to feed to your pet[0,10]: "))        
        my_pet.feed(value)
        print( f"you fed {pet_name}. Hunger reduced!!")
    elif ch==2:
        print(my_pet.play()) 
    elif ch==3:
        print(my_pet.speak())
    elif ch==4:
        print(my_pet.get_status())
    elif ch==5:
        print("Thank you so much for visiting 😘😘😘\n BYEEEEEE")
        break
    else:
        print("Invalid Choice...")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




