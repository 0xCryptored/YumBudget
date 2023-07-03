import sys, re, time
from pyfiglet import Figlet

class User:
    def __init__(self, name, gender, age, weight, height) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.budget = None
        self.bmr = None
        self.tdee = None
    
    def __str__(self):
        return f"Name: {self.name}\n Gender: {self.gender}\n current weight: {self.weight}Kg\n height:{self.height}\n BMR: {self.bmr}\n TDEE: [Pending...]"
        
    @classmethod
    def get(cls):
        print_delay("... ", 0.8)
        print_delay("Hello There! ", 0.2)
        while True:
            try:
                name_input = input("What's your name?: ").strip().capitalize()
                if not re.match(r'^[A-Za-z]+$', name_input):
                    raise ValueError("Name is required and must be a string")
                
                gender_input = input("Gender (M, F, N): ").strip().capitalize()
                if not re.match(r"^(M(?:ale)?|F(?:emale)?|N(?:one)?)$", gender_input):
                    raise ValueError("Invalid gender input")
                if len(gender_input) > 1:
                    gender_input = gender_input[0]
                
                age_input = int(input("Age: "))
                if age_input not in range(10, 116):
                    raise ValueError("Invalid age. Fact: Oldest person alive is 116 years old")
                
                weight_input = float(input("Weight (Kg): "))
                if weight_input < 10.0 or weight_input > 150.0:
                    raise ValueError("Invalid weight. Our test model is not designed yet for weight above 150Kg")
                
                height_input = float(input("Height (Meters): "))
                if height_input < 1.00 or height_input > 2.50:
                    raise ValueError("Height In Meters. (e.g) '1.75'")
                
                return cls(name_input, gender_input, age_input, weight_input, height_input)
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
    
    
    def calc_bmr(self):
        print_delay(".. Alright! lets get your Basal metabolic rate (BMR)... ", 0.1)
        if self.gender == 'M':
            value = (10 * self.weight) + (6.25 * (self.height * 100)) - (5 * self.age) + 5
        else:
            value = (10 * self.weight) + (6.25 * (self.height * 100)) - (5 * self.age) -161
        print(f"Your BMR is: {value}")
        time.sleep(3)
        print("===============================================")
        print(disclaimers["bmr"])
        print("===============================================")
        return value
        
        
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
        else:
            if len(gender) > 1:
                gender = gender[0]
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
    def budget(self):
        return self._budget
    @budget.setter
    def budget(self, budget):
        if budget:
            if budget < 10.00 or budget > 3200.00:
                raise ValueError("Invalid Budget. Most be between 10 USD and 3200 USD")
        else:
            self._budget = budget

    @property
    def bmr(self):
        return self._bmr
    @bmr.setter
    def bmr(self, bmr):
        if not bmr:
            self._bmr = None
        else:
            self._bmr = bmr
            
        
    @property
    def tdee(self):
        return self._tdee
    @tdee.setter
    def tdee(self, tdee):
        if not tdee:
            self._tdee = None
        else:
            self._tdee = tdee
    
    
def main():
    print(banner("PaleoBudget"))
    chapi = User.get()
    option = menu()
    match option:
        case "create":
            create(chapi)
        case "update":
            update()
        case "print":
            gen()
        case _:
            print("Invalid option: That one is yet to come")
    print(chapi)
            
            
def menu():
    options = ["create", "update", "print"]
    while True:
        # Fot the future: print graphical menu
        print(banner("Options", True))
        print("Create: This will gen a diet based on your profile")
        print("Update: This allows you to update your info.")
        print("Print: This will gen a PDF file containing your diet plan")
        option = input("What you want to do? ").strip().lower()
        if option in options:
            return option
        else:
            print("Only valid options are: Create, Update, and Print.")
    
    
def create(chapi):
    # 100 grams Sources include: FoodData Central  ,USDA
    chapi.bmr = chapi.calc_bmr() 
    print(chapi)
    chapi.tdee = calc_tdee(chapi)
    print("So far so good (y)")
    snacks = {"orange": 50, "carrot": 50, "celeries": 50}
    breakfast = gen_breakfast()
    lunch = gen_lunch()
    dinner = gen_dinner() 

    def calc_tdee(chapi):
        print_delay("...loading", 0.15)
        try:
            print("1). Sedentary (little to no exercise).")
            print("2). Lightly active (light exercise/sports 1-3 days/week).")
            print("3.) Moderately active (moderate exercise/sports 3-5 days/week).")
            print("4). Very active (hard exercise/sports 6-7 days/week).")
            print("5). Extra active (very hard exercise/sports and a physical job).")
            tdee_option = input("Selec the number of the described activity level that fits you best.").strip()
            if tdee_option not in ["1","2","3","4","5"]:
                raise ValueError("Error en calc tdee: no en lista.")
            else:
                match tdee_option:
                    case "1":
                        value = chapi.bmr * 1.2
                    case "2":
                        value = chapi.bmr * 1.375
                    case "3":
                        value = chapi.bmr * 1.55
                    case "4":
                        value = chapi.bmr * 1.725
                    case "5":
                        value = chapi.bmr * 1.9
                return value
        except ValueError as e:
            sys.exit("Exiting PaleoBudget")
        
    
    def gen_breakfast():
        break_ingredients = {"eggs": 155, "bacon": 42, "avocado": 160, "coconut oil": 862, "olive oil": 884, "cashews": 553, "hazelnuts": 628, "macadamia nuts": 718, "blueberries": 57,"strawberries": 32, "raspberries": 53, "blackberries": 43, "banana": 96, "apple": 52, "orange": 43, "lemon": 29, "lime": 30, "garlic": 149, "coconut milk": 230, "almond milk": 17, "coconut flour": 480, "almond flour": 576, "coconut butter": 717, "ghee": 900, "coconut aminos": 100, "honey": 304, "maple syrup": 260, "cinnamon": 247,}
        
    def gen_lunch():
        lunch_ingredients = {"salmon": 206, "beef": 250, "chicken": 165, "pork": 242, "turkey": 189, "kale": 49, "broccoli": 34, "cauliflower": 25, "spinach": 23, "carrots": 41, "avocado": 160, "cilantro": 23, "apple cider vinegar": 22, "olive oil": 884, "balsamic vinegar": 88, "red wine vinegar": 17, "arrowroot flour": 357, "sweet potato": 86, "black pepper": 251, "butternut squash": 45, "paprika": 282, "zucchini": 17, "cucumber": 15, "bell pepper": 31, "tomato": 18, "lettuce": 5, "onion": 40, "ginger": 80, "garlic": 149, "turmeric": 312, "celery": 16, "coconut flour": 480, "fish sauce": 29, "almond flour": 576, "coconut butter": 717, "oregano": 265, "basil": 22, "rosemary": 131, "parsley": 36, "nutmeg": 525,}
        ...
        
    def gen_dinner():
        dinner_ingredients = {"salmon": 206, "beef": 250, "chicken": 165, "pork": 242, "turkey": 189, "avocado": 160, "cilantro": 23, "almonds": 579, "walnuts": 654, "olive oil": 884, "butternut squash": 45,}
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


disclaimers={"bmr": "Disclaimer: please note that these equations provide estimates, and individual variations and considerations should be taken into account. Consulting a healthcare professional or a registered dietitian is recommended to get personalized and accurate advice on calorie intake and dietary needs. [Working on a BMR for 'gender = None']"}


if __name__ == "__main__":
    main()

    
def update():
    ...
    
def gen():
    ...