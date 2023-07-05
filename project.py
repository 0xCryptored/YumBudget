import sys, re, time
import random
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
        self.breakfast = None
        self.lunch = None
        self.dinner = None
        
    
    def __str__(self):
        return f"Name: {self.name}\n Gender: {self.gender}\n current weight: {self.weight}Kg\n height:{self.height}\n BMR: {self.bmr}\n TDEE: {self.tdee}\n"
        
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
    
    
    def update(self):
        print("Which attribute would you like to update?\n")
        while True:
            print("[1] Name")
            print("[2] Gender")
            print("[3] Age")
            print("[4] Weight")
            print("[5] Height")
            print("[6] Back to menu\n")
            att = input("Type the number of your selection: ").strip().lower()
            matches = re.match(r"^(?:'name'|'gender'|'age'|'weight'|'height'|\d{1,6})$", att, re.IGNORECASE)
            if matches:
                try:
                    if att in ["1", "name"]:
                        print(f"Current name: '{self.name}'")
                        if new := input("Type new name: "):
                            self.name = new
                            print(f"Your name is now: '{self.name}'\n")
                        else:
                            raise ValueError("Input is empty")

                    elif att in ["2", "gender"]: 
                        print(f"Current gender: {self.gender}")
                        if new := input("Type new gender [Male, Female, None]: "):
                            self.gender = new
                            print(f"{self.name}'s gender is now: {self.gender}\n")
                        else:
                            raise ValueError("Input is empty")

                    elif att in ["3", "age"]: 
                        print(f"Current age: {self.age}") 
                        if new := int(input("Type new age: ")):
                            self.age = new
                            print(f"{self.name}'s age is now: {self.age}\n")
                        else:
                            raise ValueError("Input is empty")

                    elif att in ["4", "weight"]:
                        print(f"Current weight: {self.weight}")
                        if new := float(input("Type new weight: ")):
                            self.weight = new
                            print(f"{self.name}'s weight is now: {self.weight}")
                        else:
                            raise ValueError("Input is empty")

                    elif att in ["5", "height"]:
                        print(f"Current height: {self.height}")
                        if new := float(input("Type new height: ")):
                            self.height = new
                            print(f"{self.name}'s height is now: {self.height}")
                        else:
                            raise ValueError("Input is empty")
                        
                    else:
                        options_menu(self)
                    
                        
                except ValueError as e:
                    print("An error has ocurred: ", e)
                    options_menu(self)
                    
    
    
    def calc_bmr(self):
        print_delay(".. Alright! lets get your Basal Metabolic Rate (BMR)...\n", 0.15)
        print_delay(disclaimers["info_bmr"], 0.1)
        if self.gender == 'M':
            value = (10 * self.weight) + (6.25 * (self.height * 100)) - (5 * self.age) + 5
        else:
            value = (10 * self.weight) + (6.25 * (self.height * 100)) - (5 * self.age) -161
        print(f"Your BMR is: {value}\n")
        time.sleep(3)
        return value


    def calc_tdee(self):
        print_delay("...Almost done! now, lets get your Total Daily Energy Expenditure (TDEE) \n", 0.1)
        print_delay(disclaimers["info_tdee"], 0.1)
        try:
            print("[1] Sedentary (little to no exercise).")
            print("[2] Lightly active (light exercise/sports 1-3 days/week).")
            print("[3] Moderately active (moderate exercise/sports 3-5 days/week).")
            print("[4] Very active (hard exercise/sports 6-7 days/week).")
            print("[5] Extra active (very hard exercise/sports and a physical job).\n")
            tdee_option = input("Select the number of the described activity level that fits you best: ").strip()
            if tdee_option not in ["1","2","3","4","5"]:
                raise ValueError("Error en calc tdee: no en lista.")
            else:
                match tdee_option:
                    case "1":
                        value = self.bmr * 1.2
                    case "2":
                        value = self.bmr * 1.375
                    case "3":
                        value = self.bmr * 1.55
                    case "4":
                        value = self.bmr * 1.725
                    case "5":
                        value = self.bmr * 1.9
                print(f"Your TDEE is: {value}\n")
                time.sleep(3)
                return value
        except ValueError as e:
            sys.exit("Exiting PaleoBudget")
    
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not re.match(r'^[A-Za-z]+$', name):
            raise ValueError("Invalid name. Name is required and must be a string")
        self._name = name
        
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, gender):
        if not re.match(r"^(M(?:ale)?|F(?:emale)?|N(?:one)?)$", gender):
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
    
    
# Notes to self, I will inclue the current object recepits as an attribute within
def main():
    print(banner("PaleoBudget"))
    print("================================================================================================================================================================")
    print(disclaimers["disc"])
    print("================================================================================================================================================================")
    chapi = User.get()
    buffer = options_menu(chapi)
            
            
def options_menu(chapi):
    options = ["1", "2", "3", "4"]
    while True:
        print(banner("menu", True))
        print("[1] Create: This will gen a diet based on your profile")
        print("[2] Update: This allows you to update your info.")
        print("[3] Print: This will gen a PDF file containing your diet plan")
        print("[4] Exit: This will exit the program\n")
        option = input("Type the number of your selection: ").strip().lower()
        if option in options:
            match option:
                case "1":
                    return create(chapi)
                case "2":
                    chapi.update()
                case "3":
                    return gen(chapi)
                case "4":
                    print(banner("Cya!", True))
                    sys.exit("..Closing program")
        else:
            print("Only valid options are numbers: Create [1], Update [2], Print [3], Exit[4]\n")
    
    
def create(chapi):
    # Dict Groups 1:Protein; 2:Oils; 3:Additionals; 4:Beverages; 5:Spices;
    def gen_breakfast(chapi):
        # Calories percentage: 25%
        ingredients = [{"salmon":120, "boiled-egg":140, "fried-egg":196, "bacon":42}, {"coconut-oil":117, "olive-oil":119}, {"cashews":55, "hazelnuts":62, "blueberries":57,"strawberries":32, "raspberries":53, "blackberries":43, "banana":96, "apple":52, "orange":43, "lemon":29, "sweet-potato":70, "avocado":160}, {"coconut-water":45, "almond-milk":40, "water":0, "coffe-latte":12}, {"coconut-butter":50, "honey":64, "maple-syrup":26, "cinnamon":3, "chia-seeds":48}]
        max_calories = round(chapi.tdee * 0.25) # 587 Calories
        calories = 0
        breakfast_ingredients = []
        while calories <= max_calories:
            for i in range(len(ingredients)):
                buff = random.choice(list(ingredients[i].keys()))
                breakfast_ingredients.append(buff)
                calories += ingredients[i][buff]
            while calories <= max_calories:
                buff = random.choice(list(ingredients[2].keys()))
                breakfast_ingredients.append(buff)
                calories += ingredients[2][buff]
        return breakfast_ingredients, calories     
        
    # Dict Groups 1:Protein; 2:Oils; 3:Additionals; 4:Beverages; 5:Spices;
    def gen_lunch(chapi):
        # Calories percentage: 40%
        ingredients = [{"salmon":104, "beef":125, "chicken":120, "pork":121, "turkey":95}, {"coconut-oil":117, "olive-oil":119}, {"kale": 49, "broccoli":34, "cauliflower":25, "spinach":23, "carrots":41, "avocado":80, "cilantro":23, "balsamic vinegar":88, "red wine vinegar":17, "arrowroot":35, "sweet potato":70, "zucchini":17, "cucumber":15, "bell-pepper":31, "tomato":18, "lettuce":5, "onion":40, "ginger":30, "celery":16}, {"water":0, "soft-drink":41, "apple-juice":46}, {"garlic":14, "paprika":10, "black-pepper":15, "oregano":10, "basil":22, "fish sauce":29,  "rosemary":13, "parsley":36, "nutmeg":11}]
        max_calories = round(chapi.tdee * 0.35) # 823
        calories = 0
        lunch_ingredients = []
        while calories <= max_calories:
            for i in range(len(ingredients)):
                buff = random.choice(list(ingredients[i].keys()))
                lunch_ingredients.append(buff)
                calories += ingredients[i][buff]
            while calories <= max_calories:
                buff = random.choice(list(ingredients[2].keys()))
                lunch_ingredients.append(buff)
                calories += ingredients[2][buff]
        return lunch_ingredients, calories    
        
    # Dict Groups 1:Protein; 2:Oils; 3:Additionals; 4:Beverages; 5:Spices;   
    def gen_dinner(chapi):
        # Calories percentage: 35%
        ingredients = [{"salmon":281, "chicken":200, "turkey":95, "shrimp":143}, {"olive oil":119, "coconut-oil": 117},{"avocado":120, "bell-pepper":15, "zucchini":13, "broccoli":26, "cauliflower":20, "snap-peas":29, "sweet-potato":112}, {"lemon-juice":4, "water":0, }, {"rosemary":4, "thyme":5, "basil":1, "garlic":5, "paprika":14, "dill":2}]
        max_calories = round(chapi.tdee * 0.30) # 705
        calories = 0
        dinner_ingredients = []
        while calories <= max_calories:
            for i in range(len(ingredients)):
                buff = random.choice(list(ingredients[i].keys()))
                dinner_ingredients.append(buff)
                calories += ingredients[i][buff]
            while calories <= max_calories:
                buff = random.choice(list(ingredients[2].keys()))
                dinner_ingredients.append(buff)
                calories += ingredients[2][buff]
        return dinner_ingredients, calories
    
    # 100 grams Sources include: FoodData Central  ,USDA
    chapi.bmr = chapi.calc_bmr() 
    chapi.tdee = chapi.calc_tdee()
    
    breakfast, breakfast_calories = gen_breakfast(chapi)
    lunch, lunch_calories = gen_lunch(chapi)
    dinner, dinner_calories = gen_dinner(chapi)
    
    rcpt_breakfast = [breakfast, breakfast_calories]
    rcpt_lunch = [lunch, lunch_calories]
    rcpt_dinner = [dinner, dinner_calories]
    
    return rcpt_breakfast, rcpt_lunch, rcpt_dinner    


def gen():
    ...


def print_delay(message, delay):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)

def banner(text, sub=None):
    figlet = Figlet()
    if sub:
        figlet.setFont(font="small")
    else:
        figlet.setFont(font="standard")
    return figlet.renderText(text)

disclaimers={"disc": "DISCLAIMER: Please note that these equations (Mifflin-St. Jeor equation) provide estimates, and individual variations and considerations should be taken into account.\nConsulting a healthcare professional or a registered dietitian is recommended to get personalized and accurate advice on calorie intake and dietary needs.", "info_bmr": "This measures the calories needed to perform your body's most basic (basal) functions while at rest, like breathing, circulation, and cell production.\nIt represents the minimum energy expenditure required to sustain life.\n\n", "info_tdee": "Is the total number of calories your body needs in a day, taking into account your BMR and the energy expended through physical activity and digestion.\nTDEE considers the calories burned through daily activities, exercise, and the thermic effect of food.\n\n"}


if __name__ == "__main__":
    main()

    