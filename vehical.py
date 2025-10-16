# Parent class 
class Vehical:
    def __init__(self,make,model,year) :
        self.make=make
        self.model=model
        self.year=year

    def start(self):
        print(f"{self.make} {self.model} Starting..")

    def stop(self):
        print(f"{self.make} {self.model} Stoping..")

#child class Car
class Car(Vehical) :
    def __init__(self,make,model,year,number_of_doors,trunk_size):
        super().__init__(make,model,year)
        self.number_of_doors=number_of_doors
        self.trunk_size=trunk_size

# child class Bicycle 
class Bicycle(Vehical):
    def __init__(self,make,model,year,gear_count,type_of_brakes):
        super().__init__(make,model,year)
        self.gear_count=gear_count
        self.types_of_brakes=type_of_brakes

# Usage

car=Car("Toyota","Camry",2020,4,"500L")
bicycle=Bicycle("Giant","Escape",2022,21,"Disc")
car.start()
print(f"Doors :{car.number_of_doors} , Trunk Size :{car.trunk_size}")
bicycle.start()
print(f"Gear count : {bicycle.gear_count} ,Brakes : {bicycle.types_of_brakes}")