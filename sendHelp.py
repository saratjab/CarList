# 2 lists doubly and single with reading from file and saving 
class car_model:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price

    def __str__(self):
        return 'Name: ' + self.name + ' Year: ' + str(self.year) + ' Price: ' + str(self.price)

class NodeS:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class NodeD:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.pre = None
        self.list = Linked_list()

class Linked_list:
    def __init__(self):
        self.head = None

    def push_back(self, Model):
        new_Model = NodeS(Model)
        curr = self.head

        if self.search() == True:
            return
        
        if self.head == None:
            self.head = new_Model

        else:
            while curr != None:
                curr = curr.next
            curr.next = new_Model

    def remove(self, Model):
        curr = self.head
        if curr == None:
            return
        
        if curr.name == Model.name and curr.year == Model.year and  curr.price == Model.price:
            curr = curr.next
            return
        
        while curr.next != None:
            if curr.next.value.name == Model.name and curr.next.value.year == Model.year and curr.next.value.price == Model.price :
                B = curr.next
                curr.next = curr.next.next
                B.next = None
            curr = curr.next
        
    def search(self, Model):
        curr = self.head
        while curr != None:
            if curr.name == Model.name and curr.year == Model.year and  curr.price == Model.price:
                return True
            curr = curr.next
        return False

    def display(self):
        curr = self.head
        while curr != None:
            print(curr.value , end=' ')
        print()

class Doubly_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_back(self, Brand):
        new_Brand = NodeD(Brand)
        curr = self.head

        if self.search() == True:
            return

        if self.head == None:
            self.head = new_Brand
            self.tail = new_Brand
        else:
            new_Brand.pre = self.tail
            self.tail.next = new_Brand
            self.tail = new_Brand

    def pop_back(self): 
        if self.head == None:
            return 
        
        if self.head.next == None:
            self.head.list = None
            self.head = None
            self.tail = None
        else:
            B = self.tail.pre
            self.tail.pre = None
            self.tail.list = None 
            B.next = None
            self.tail = B
    
    def pop_front(self):
        if self.head == None:
            return
        
        if self.head.next == None:
            self.head.list = None
            self.head = None
            self.tail = None
        else:
            B = self.head.next
            self.head.next = None
            self.head.list = None
            B.pre = None
            self.head = B

    def remove(self, Brand): 
        curr = self.head
        if curr.value == Brand:
            self.pop_front()
            return
        if self.tail.value == Brand:
            self.pop_back()
            return
        while curr.next != None:
            if curr.value == Brand:
                B = curr.next
                curr.next = curr.next.next
                if curr.next  != None:
                    curr.next.pre = curr                    
                B.next = None
                B.pre = None
                B.List = None
                return
            curr = curr.next
        
    def push_back_model(self,Bradn, Model):
        curr = self.head
        while curr != None:
            if curr.value == Brand:
                curr.list.push_back(Model)
                return
            
    def remove_model(self, Brand, Model):
        curr = self.head
        while curr != None:
            if curr.value == Brand:
                curr.list.remove(Model)
                return
            
    def search_model(self, Brand, Model):
        curr = self.head
        while curr != None:
            if curr.value == Brand:
                curr.list.search(Model)
                return
            
    def display_model(self, Brand, Model):
        curr = self.head
        while curr != None:
            if curr.value == Brand:
                curr.list.display()
                return
            
    def search(self, Brand):
        curr = self.head
        while curr != None:
            if curr.value == Brand:
                return True
            curr = curr.next
        return False
    
    def display(self):
        curr = self.head
        while curr != None:
            print(curr.value, end =' ')
            curr = curr.next
        print()

    def display_all(self):
        curr = self.head
        while curr != None:
            print(f"Brand {curr.value}")
            self.display_model()

            curr = curr.next
        print()

def menu():
    print('--------------Div5 Cars---------------')
    print('1- Add Brand')
    print('2- Remove Brand')
    print('3- Add Models to a specific Brand')
    print('4- Remove a Model from a specific Brand')
    print('5- Search for a Brand')
    print('6- Search for a Models in a Brand')
    print('7- Display all Brands')
    print('8- Display all the Models of specific Brand')
    print('9- Disply all the Brands and their Models')
    print('10- Save to file')



X = Doubly_list() 
with open("cars.txt", "r") as file:
    for line in file:
        car = line.split()
        cnt = 0
        for e in car:
            if cnt == 0:
                X.push_back(e)
            else :
                X.push_back_model(e)
            cnt += 1


while True:
    menu()
    ch = int(input('Enter a number: '))

    if ch == 1:
        Brand = str(input('Enter a Brand: '))
        X.push_back(Brand)

    if ch == 2:
        Brand = str(input('Enter a Brand: '))
        X.remove(Brand)
    
    if ch == 3:
        Brand = str(input('Enter a Brand: '))
        name = str(input('Enter the model name: '))
        year = str(input('Enter the model year: '))
        price = float(input('Enter the model price: '))
        Model = car_model(name, year, price)
        X.push_back_model(Brand, Model)

    if ch == 4:
        Brand = str(input('Enter a Brand: '))
        name = str(input('Enter the model name: '))
        year = str(input('Enter the model year: '))
        price = float(input('Enter the model price: '))
        Model = car_model(name, year, price)   
        X.remove_model(Brand, Model)
    
    if ch == 5:
        Brand = str(input('Enter a Brand: '))
        X.search(Brand)

    if ch == 6:
        Brand = str(input('Enter a Brand: '))
        name = str(input('Enter the model name: '))
        year = str(input('Enter the model year: '))
        price = float(input('Enter the model price: '))
        Model = car_model(name, year, price)
        X.search_modle(Brand, Model)
    
    if ch == 7:
        X.display()

    if ch == 8:
        Brand = str(input('Enter a Brand: '))
        name = str(input('Enter the model name: '))
        year = str(input('Enter the model year: '))
        price = float(input('Enter the model price: '))
        Model = car_model(name, year, price)
        X.display_model(Brand, Model)

    if ch == 9:
        X.display_all()
    
    if ch == 10:
        with open("example.txt", "w") as file:
            curr = X.head
            while curr != None:
                coco = curr.list
                while coco != None:
                    name = coco.value.name
                    year = coco.value.year
                    price = coco.value.price
                    file.write(f"{curr.value} , {name}, {year}, {price}")
