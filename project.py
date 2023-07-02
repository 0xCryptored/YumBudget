import re
import time
from pyfiglet import Figlet

class User:
    def __init__(self, name, gender, age, weight, height, duration, budget) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.duration = duration
        self.budget = budget
    
    def __str__(self):
        return f"{self.name} is on a journey of {self.duration} months with YumBudget! ${self.budget} to spend, current weight: {self.weight}Kg"
        
    @classmethod
    def get(cls):
        print_delay("... ", 0.8)
        print_delay("Hello There! ", 0.4)
        while True:
            try:
                name_input = input("What's your name?: ").strip().capitalize()
                if not re.match(r'^[A-Za-z]+$', name_input):
                    raise ValueError("Name is required and must be a string")
                
                gender_input = input("Gender (M, F, N): ").strip().capitalize()
                if not re.search(r"^(M|F|N|Male|Female|None)$", gender_input):
                    raise ValueError("Invalid gender input")
                
                age_input = int(input("Age: "))
                if age_input not in range(10, 116):
                    raise ValueError("Invalid age. Fact: Oldest person alive is 116 years old")
                
                weight_input = float(input("Weight (Kg): "))
                if weight_input < 10.0 or weight_input > 150.0:
                    raise ValueError("Invalid weight. Our test model is not designed yet for weight above 150Kg")
                
                height_input = float(input("Height (Meters): "))
                if height_input < 1.00 or height_input > 2.50:
                    raise ValueError("Height In Meters. (e.g) '1.75'")
                
                duration_input = int(input("Duration (In Months): "))
                if duration_input not in range(1, 30):
                    raise ValueError("For Duration greater than 12 months purchase our premium plan.. jk we just dont support that yet")
                
                budget_input = float(input("Budget (USD): "))
                if budget_input < 10.00 or budget_input > 3200.00:
                    raise ValueError("Budget Most be between 10 USD and 3200 USD")
                
                return cls(name_input, gender_input, age_input, weight_input, height_input, duration_input, budget_input)
            except ValueError as e:                
                print("Invalid input:", e)
                # Re-prompt the specific input // Not Working Idk why
                if "name" in str(e).lower():
                    continue
                elif "gender" in str(e).lower():
                    continue
                elif "age" in str(e).lower():
                    continue
                elif "weight" in str(e).lower():
                    continue
                elif "height" in str(e).lower():
                    continue
                elif "duration" in str(e).lower():
                    continue
                elif "budget" in str(e).lower():
                    continue
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name.")
        self._name = name
        
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, gender):
        if gender not in ["M", "F", "N", "Male", "Female", "None"]:
            raise ValueError("Invalid gender. M: Male; F: Female; N: None")
        self._gender = gender
        
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if age not in range(10, 116):
            raise ValueError("Invalid age. Fact: Oldest person alive is 116 years old")
        self._age = age
        
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, weight):
        if weight < 10.0 or weight > 150.0:
            raise ValueError("Invalid weight. Our test model is not designed yet for weight above 150Kg")
        self._weight = weight
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        if height < 1.00 or height > 2.50:
            raise ValueError("Invalid height (Meters). (e.g) '1.75'")
        self._height = height
    
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, duration):
        if duration not in range(1, 30):
            raise ValueError("Invalid duration. For more than 12 purchase our premium plan.. jk we just dont support that yet")
        self._duration = duration
    
    @property
    def budget(self):
        return self._budget
    @budget.setter
    def budget(self, budget):
        if budget < 10.00 or budget > 3200.00:
            raise ValueError("Invalid Budget. Most be between 10 USD and 3200 USD")
        self._budget = budget

def main():
    print(banner("YumBudget"))
    chapi = User.get()
    option = menu()
    match option:
        case "create":
            create()
        case "update":
            update()
        case "print":
            gen()
        case _:
            print("Invalid option: Case match")
            
            
def menu():
    options = ["create", "update", "print"]
    while True:
        # Fot the future: print graphical menu
        print(banner("Options", True))
        print("Create: This will gen a diet based on the chosen duration")
        print("Update: This allows you to update your info.")
        print("Print: This will gen a PDF file containing your diet plan")
        option = input("What you want to do? ").strip().lower()
        if option in options:
            return option
        else:
            print("Not a valid option: Menu function")
    
    
def create():
    ...

def update():
    ...
    
def gen():
    ...

def print_delay(message, delay):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)

def banner(text, sub=None):
    figlet = Figlet()
    if sub:
        figlet.setFont(font="digital")
    else:
        figlet.setFont(font="standard")
    return figlet.renderText(text)

if __name__ == "__main__":
    main()
    