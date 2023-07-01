class User:
    def __init__(self, gender, age, weight, height, duration, budget) -> None:
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.duration = duration
        self.budget = budget
        
    @classmethod
    def get(cls):
        gender_input = input("Gender (M, F, N): ").upper()
        age_input = int(input("Age: "))
        weight_input = float(input("Weight (Kg): "))
        height_input = float(input("Height (Meters): "))
        duration_input = int(input("Duration (Months): "))
        budget_input = float(input("Budget (USD): "))
        return cls(gender_input, age_input, weight_input, height_input, duration_input, budget_input)
        
        
    @property
    def gender(self):
        return self._gender
    @gender.setter
    def gender(self, gender):
        if gender not in ["M", "F", "N"]:
            raise ValueError("M: Male; F: Female; N: Neutral")
        self._gender = gender
        
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        if age < 0 or age > 116:
            raise ValueError("Enter a valid age. Fact: Oldest person alive is 116 years old")
        self._age = age
        
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, weight):
        if weight < 10 or weight > 150:
            raise ValueError("Our test model is not designed yet for weight above 150Kg")
        self._weight = weight
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        self._height = height
    
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, duration):
        self._duration = duration
    
    @property
    def budget(self):
        return self._budget
    @budget.setter
    def budget(self, budget):
        self._budget = budget

def main():
    alan = User.get()
    print(alan.age)

if __name__ == "__main__":
    main()
    