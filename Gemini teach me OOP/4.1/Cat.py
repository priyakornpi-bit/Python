class CatManager:
    def __init__(self,
                 date_in,
                 cat_type,
                 date_out,
                 owner_name,
                 age):  
        self.date_in = date_in
        self.date_out = date_out
        self.cat_type = cat_type
        self.ownner_name = owner_name
        self.age = age

    def show_detail(self):
        print("Date In:", self.date_in)
        print("Cat Type:", self.cat_type)   
        print("Date Out:", self.date_out)
        print("Owner Name:", self.ownner_name)
        print("Age:", self.age)

    def make_sound(self):
        print("Meow Meow")
    def eat(self):
        print("Cat is eating")
    def sleep(self):    
        print("Cat is sleeping")
    def play(self):
        print("Cat is playing")
    def scratch(self):
        print("Cat is scratching")
    def purr(self):  
        print("Cat is purring")
    def climb(self):    
        print("Cat is climbing")
    def hunt(self):         
        print("Cat is hunting")
    def groom(self):
        print("Cat is grooming itself")
    def jump(self):
        print("Cat is jumping")
        

c1 = CatManager("2023-01-01", "Siamese", "2023-01-10", "Alice", 2)
c1.show_detail()
c1.make_sound()
c1.eat()
c1.sleep()      
c1.play()