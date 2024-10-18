import os
class Car: 
    def __init__(car, make, model, color):
        car.make = make
        car.model = model
        car.color = color
    
    def view_cars(car):
        return f"{car.make} - {car.model} ({car.color})"  

    os.system("cls")
    while True:
        make = input("Skriv en bil: ")
        model = input("Vilken model: ")
        color = input("Vilken färg: ")
        done = input("Är du färdig: ")
        if (done == "ja"):
            break
        
    cars = []
    
    cars.append(car, make, model, color)

  
   


    for car in cars:
        print(car.view_cars())