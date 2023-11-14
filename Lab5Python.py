#1
"""
Create a class hierarchy for shapes, starting with a base class Shape. 
Then, create subclasses like Circle, Rectangle, and Triangle. Implement methods to calculate area and perimeter for each shape.
"""
class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

#2
"""
Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount. Implement methods for deposit, withdrawal, and interest calculation.
"""
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, balance, transaction_fee):
        super().__init__(balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        if amount + self.transaction_fee <= self.balance:
            self.balance -= amount + self.transaction_fee
        else:
            print("Insufficient funds")
#3
"""
Create a base class Vehicle with attributes like make, model, and year, and then create subclasses for specific types of vehicles like Car, Motorcycle, and Truck.
 Add methods to calculate mileage or towing capacity based on the vehicle type.
"""
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def calculate_mileage(self, miles, gas_used):
        return miles / gas_used

class Motorcycle(Vehicle):
    def calculate_mileage(self, miles, gas_used):
        return miles / gas_used

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def calculate_towing_capacity(self):
        return self.towing_capacity

#4
"""
Build an employee hierarchy with a base class Employee. 
Create subclasses for different types of employees like Manager, Engineer, and Salesperson. Each subclass should have attributes like salary and methods related to their roles.
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_information(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_department(self):
        print(f"Manager of the {self.department} department")

class Engineer(Employee):
    def __init__(self, name, salary, specialty):
        super().__init__(name, salary)
        self.specialty = specialty

    def display_specialty(self):
        print(f"Specialty: {self.specialty}")

class Salesperson(Employee):
    def __init__(self, name, salary, region):
        super().__init__(name, salary)
        self.region = region

    def display_region(self):
        print(f"Sales region: {self.region}")

#5
"""
Create a class hierarchy for animals, starting with a base class Animal.
 Then, create subclasses like Mammal, Bird, and Fish. Add properties and methods to represent characteristics unique to each animal group.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Mammal(Animal):
    def breathe(self):
        print("Breathing air")

    def make_sound(self):
        print("Mammal sound")

class Bird(Animal):
    def fly(self):
        print("Flying")

    def make_sound(self):
        print("Bird chirping")

class Fish(Animal):
    def swim(self):
        print("Swimming")

    def make_sound(self):
        print("Fish sound")
#6
"""Design a library catalog system with a base class LibraryItem and subclasses for different types of items like Book, DVD, and Magazine.
 Include methods to check out, return, and display information about each item.
"""
class LibraryItem:
    def __init__(self, title, author, publication_date):
        self.title = title
        self.author = author
        self.publication_date = publication_date

    def check_out(self):
        pass

    def return_item(self):
        pass

class Book(LibraryItem):
    def display_information(self):
        print(f"Book: {self.title} by {self.author}")

class DVD(LibraryItem):
    def display_information(self):
        print(f"DVD: {self.title}, released {self.publication_date}")

class Magazine(LibraryItem):
    def display_information(self):
          print(f"Magazine: {self.title}, released {self.publication_date}")