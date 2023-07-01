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
        print("Hello There!")
        name_input = input("What's your name?: ").capitalize()
        gender_input = input("Gender (M, F, N): ").upper()
        age_input = int(input("Age: "))
        weight_input = float(input("Weight (Kg): "))
        height_input = float(input("Height (Meters): "))
        duration_input = int(input("Duration (In Months): "))
        budget_input = float(input("Budget (USD): "))
        return cls(name_input, gender_input, age_input, weight_input, height_input, duration_input, budget_input)
        
        
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
        if gender not in ["M", "F", "N"]:
            raise ValueError("Invalid gender. M: Male; F: Female; N: Neutral")
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
    alan = User.get()
    print(alan)
    

if __name__ == "__main__":
    main()
    