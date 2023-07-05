# PaleoBudget Python Program
#### Video Demo:  <https://youtu.be/RsDpPFoXEK8>
#### Description:

This Python program allows users to create a personalized conscious meal plan based on their information and dietary preferences. The program calculates the Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE) of the user and suggests breakfast, lunch, and dinner options, on the near future offering this adjusted on users monthly budget.

## Program Features

- User input and information storage: The program collects the user's name, gender, age, weight, and height using the `User` class.
- Calculation of BMR and TDEE: The `User` class calculates the user's BMR and TDEE based on their input and Mifflin-St. Jeor equation simplified equations.
- Meal plan generation: The program generates breakfast, lunch, and dinner options for the user.
- Updating user information: Users can update their information such as name, gender, age, weight, and height using the `update()` method.

## Dependencies

- Python 3.x
- `re` module
- `time` module
- `random` module
- `collections` module
- `fpdf` library
- `pyfiglet` library

## Getting Started

1. Clone the repository or download the `main.py` file.
2. Make sure you have Python 3.x installed on your system.
3. Install the required dependencies using the following command:
    pip install fpdf pyfiglet; pip install fpdf2
4. Run the program using the following command:
    python main.py

## Usage

1. Run the program and follow the prompts to provide your name, gender, age, weight, and height.
2. The program will calculate your BMR and TDEE.
3. Select your activity level to determine your TDEE.
4. The program will generate breakfast, lunch, and dinner options within your budget.
5. You can update your information or exit the program when prompted.

