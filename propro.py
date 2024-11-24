# one list without read and save into file
class NodeD: # ?Node for the doubly 
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None
        self.single = None  #head for each single list of Brand

class NodeS: #? Node for the singly
    def __init__(self, value):
        self.value = value
        self.next = None
    
class car_model:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
    
    def __str__(self):
        return "Car: Name:-  " + self.name + " Year:- " + str(self.year) + " Price:- " + str(self.price)

class List_cars:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_back(self, Brand):
        new_Brand = NodeD(Brand)
        curr = self.head

        if self.serach_brand() == True:
            return

        if self.head == None:
            self.head = new_Brand
            self.tail = new_Brand
        else:
            new_Brand.pre = self.tail
            self.tail.next = new_Brand
            self.tail = new_Brand

    def push_front(self, Brand):
        new_Brand = NodeD(Brand)
        curr = self.head

        if self.serach_brand() == True:
            return

        if self.head == None:
            self.head = new_Brand
            self.tail = new_Brand
        else:
            new_Brand.next = self.head
            self.head.pre = new_Brand
            self.head = new_Brand
    
    def pop_back(self): 
        if self.head == None:
            return 
        
        if self.head.next == None:
            self.head.single = None
            self.head = None
            self.tail = None
        else:
            B = self.tail.pre
            self.tail.pre = None
            self.tail.single = None #*
            B.next = None
            self.tail = B
    
    def pop_front(self):
        if self.head == None:
            return
        
        if self.head.next == None:
            self.head.single = None
            self.head = None
            self.tail = None
        else:
            B = self.head.next
            self.head.next = None
            self.head.single = None
            B.pre = None
            self.head = B

    def remove_brand(self, Brand):
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
                B.single = None
                return
            curr = curr.next
        
    
    def display_brand(self):
        curr = self.head
        while curr != None:
            print(curr.value, end =' ')
            curr = curr.next
        print('')
    
    def serach_brand(self, Brand):
        curr = self.head
        while curr != None:
            if curr.value == Brand:
                return True
            curr = curr.next
        return False
    
    def push_back_model(self, Brand, Model):
        new_Model = NodeS(Model)

        if self.search_model(Brand) == True:
            return

        curr = self.head
        while curr != None:
            if curr.value == Brand:
                if curr.single == None:
                    curr.single = new_Model
                else :
                    coco = curr.single
                    while coco.next != None:
                        coco = coco.next
                    coco.next = new_Model
                return
            curr = curr.next
        print("The Brand Is Not Found")
    
    def remove_model(self, Brand, Model): 
        curr = self.head
        while curr != None:
            if curr.value == Brand:
                coco = curr.single
                if coco == None:
                    return
                if coco.value.name == Model.name and coco.value.year == Model.year and coco.value.price == Model.price :
                    curr.single = curr.single.next
                    return
                while coco.next != None:
                    if coco.value.name == Model.name and coco.value.year == Model.year and coco.value.price == Model.price :
                        if coco.next.next == None:
                            coco.next = None
                            return
                        else :
                            B = coco.next
                            coco.next = coco.next.next
                            B.next = None
                            return
                    coco = coco.next
            curr = curr.next
        
        
    def display_model(self, Brand):
        curr = self.head
        while curr != None:
            if curr.value == Brand:
                coco = curr.single
                if coco == None:
                    print("The Brand With No Model")
                    return
                while coco != None:
                    print(coco.value, end=' ')
                    coco = coco.next
                print('')
                return
            curr = curr.next
        print('The Brand Not Found')
    
    def search_model(self, Brand, Model):
        curr = self.head
        while curr != None:
            if curr.value == Brand:
                coco = curr.single
                while coco != None:
                    if coco.value.name == Model.name and coco.value.year == Model.year and coco.value.price == Model.price : 
                        print('The Model Is Found')
                        return
                    coco = coco.next
                print('The Model Is Not Found')
                return
            curr = curr.next
        print("The Brand Is Not Found")

    def display_brands_models(self):
        curr = self.head
        while curr != None:
            print(f"Brand : {curr.value}")
            coco = curr.single
            print("model(s): ")
            if coco == None:
                print('No Modles')
            while coco != None:
                print(coco.value , end = ' ')
                coco = coco.next
            print('')
            print('')
            curr = curr.next

def menu():
    print('--------------Div5 Cars---------------')
    print('1- Add Brand to the end of the list')
    print('2- Add Brand to the beginning')
    print('3- Remove Brand form the end of the list')
    print('4- Remove Brand from the beginning')
    print('5- Remove a specific Brand')
    print('6- Add Models to a specific Brand')
    print('7- Remove a Model from a specific Brand')
    print('8- Search for a Brand')
    print('9- Search for a Models in a Brand')
    print('10- Display all Brands')
    print('11- Display all the Models of specific Brand')
    print('12- Disply all the Brands and their Models')
    
while True:
    menu()
    X = List_cars()
    ch = int(input('Enter the number: '))
    if ch == 1:
        Brand = str(input('Enter a Brand: '))
        X.push_back(Brand)

    if ch == 2:
        Brand = str(input('Enter a Brand: '))
        X.push_front(Brand)
    
    if ch == 3:
        X.pop_back()
    
    if ch == 4:
        X.pop_front()
    
    if ch == 5:
        Brand = str(input('Enter a Brand: '))
        X.remove_brand(Brand)
    
    if ch == 6:
        Brand = str(input('Enter a Brand: '))
        name = str(input('Enter the model name: '))
        year = str(input('Enter the model year: '))
        price = float(input('Enter the model price: '))
        Model = car_model(name, year, price)
        X.push_back_model(Brand, Model)
    
    if ch == 7:
        Brand = str(input('Enter a Brand: '))
        name = str(input('Enter the model name: '))
        year = str(input('Enter the model year: '))
        price = float(input('Enter the model price: '))
        Model = car_model(name, year, price)
        X.remove_brand(Brand, Model)
    
    if ch == 8:
        Brand = str(input('Enter a Brand: '))
        X.search_Brand(Brand)
    
    if ch == 9:
        Brand = str(input('Enter a Brand: '))
        name = str(input('Enter the model name: '))
        year = str(input('Enter the model year: '))
        price = float(input('Enter the model price: '))
        Model = car_model(name, year, price)
        X.search_model(Brand, Model)
    
    if ch == 10:
        X.display_brand()
    
    if ch == 11:
        Brand = str(input('Enter a Brand: '))
        X.display_model(Brand)
    
    if ch == 12:
        X.display_brands_models()
    

# X = List_cars()
# X.push_back(7)
# X.push_back(8)
# X.push_front(9)
# X.push_front(1)
# X.display_brand()
# X.push_back_model(1, 2)
# X.push_back_model(1, 3)
# X.push_back_model(1, 3)
# X.push_back_model(1, 7)
# X.push_back_model(9,3)
# X.remove_model(1, 3)
# X.remove_model(1, 7)
# X.display_brands_models()
