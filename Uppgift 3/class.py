    import os

    class Car: 
        def __init__(self, make, model, color):
            self.make = make
            self.model = model
            self.color = color
        
        def view_car(self):
            return f"{self.make} - {self.model} ({self.color})"  

    def main():
        os.system("cls")
        
        cars = []

        while True:
            make = input("Skriv en bil: ")
            model = input("Vilken model: ")
            color = input("Vilken färg: ")
            done = input("Är du färdig: ")
            
            car = Car(make, model, color) 
            cars.append(car) 
            
            if done.lower() == "ja":
                break

        for car in cars:
            print(car.view_car()) 

    if __name__ == "__main__":
        main()
