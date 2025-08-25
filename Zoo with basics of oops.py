#!/usr/bin/env python
# coding: utf-8

# In[29]:


#polymorphism
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def show(self):
        print(self.real,"i + ",self.img,"j")
    #def add(self,num2):
        #n_real = self.real + num2.real
        #n_img = self.img + num2.img
        #return Complex(n_real,n_img)
    def __add__(self,num2):
        n_real = self.real + num2.real
        n_img = self.img + num2.img
        return Complex(n_real,n_img)
    def __sub__(self,num2):
        n_real = self.real - num2.real
        n_img = self.img - num2.img
        return Complex(n_real,n_img)
    def __mul__(self,num2):
        n_real = self.real * num2.real
        n_img = self.img * num2.img
        return Complex(n_real,n_img)
        
num1=Complex(3,4)
num1.show()

num2=Complex(2,1)
num2.show()

#num3= num1.add(num2)
#num3.show()

num3=num1+num2
num3.show()

num4=num1-num2
num4.show()

num5=num1*num2
num5.show()


# In[36]:


#simple Inheritance
class Emp:
    def __init__(self,name):
        self.name = name
    def salary(self):
        print(f"{self.name} got their salary")
class Emp_female(Emp):
    def salary(self): # overriding the method
        print(f"{self.name} got her salary")
class Emp_male(Emp):
    def salary(self):
        print(f"{self.name} got his salary")
emp1=Emp_female("Palak")
emp1.salary()
emp2=Emp_male("Kartik")
emp2.salary()

a = Emp("All Emp")
a.salary()


# In[47]:


'''Q3. Write Code
Create a BankAccount class:
Each account has name and balance.
Keep track of how many accounts are created (use classmethod).
Add a method is_valid_amount(amount) that checks if amount > 0 (use staticmethod).'''

class BankAccount:
    acc_count=0
    def __init__(self,name,bal):
        self.name = name
        self.bal = bal
        BankAccount.acc_count +=1
    @classmethod
    def no_of_acc(cls):
        print(f"Total no of accounts are {cls.acc_count}")
    @staticmethod
    def is_valid_amt(x):
        if x<0:
            print("Amount is not valid")
        else:
            print("Amount is valid")
a1=BankAccount("Kartik",1000)
a2=BankAccount("Palak",-23)
BankAccount.no_of_acc()
BankAccount.is_valid_amt(a2.bal)


# In[70]:


# ZOO MANAGEMENT SYSTEM
class Animal:
    total_animals = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Animal.total_animals+=1
    def speak(self):
        print(f"{self.name} speaks!!!")
    def feed(self):
        print(f"{self.name} eat food!!!!")
    @classmethod
    def get_total_animals(cls):
        print(f"Total animals are {cls.total_animals}")
    @staticmethod
    def is_valid_age(age):
        return age>=0
class Habitat:
    total_habitats=0
    def __init__(self,habitat_name):
        self.habitat_name = habitat_name
        self.animal_list = []
        Habitat.total_habitats+=1
    def add_animal(self,animal):
        self.animal_list.append(animal)
    def show_animals(self):
        for a in self.animal_list:
            print(a.name)
    @classmethod
    def total_habitat(cls):
        print(f"Total Habiats are {cls.total_habitats}")
class Lion(Animal):
    def speak(self):
        print(f"{self.name} says roars!!!")
    def feed(self):
        print(f"{self.name} eat meat")
class Parrot(Animal):
    def speak(self):
        print(f"{self.name} says helloo!!!")
    def feed(self):
        print(f"{self.name} eat chilli")
class Snake(Animal):
    def speak(self):
        print(f"{self.name} says hisses!!!")
    def feed(self):
        print(f"{self.name} eat rat")

a1 = Lion("sher",2)
a2 = Parrot("mithooo",1)
a3 = Snake("mues",1)

a1.speak()
a2.speak()
a3.speak()
a1.feed()
a2.feed()
a3.feed()
jungle = Habitat("jungle")
jungle.add_animal(a1)
jungle.add_animal(a2)
jungle.add_animal(a3)
jungle.show_animals()
Animal.get_total_animals()
print(a1.is_valid_age(a1.age))
print(a2.is_valid_age(a1.age))
print(a3.is_valid_age(a1.age))
Habitat.total_habitat()


# In[ ]:




