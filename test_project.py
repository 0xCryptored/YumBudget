import pytest
from project import User

def main():
    test_valid_user_input()
    test_update()
    test_calculate_bmr()

# Test for valid user input
def test_valid_user_input():
    user = User("John", "M", 25, 70.0, 1.8)
    assert user.name == "John"
    assert user.gender == "M"
    assert user.age == 25
    assert user.weight == 70.0
    assert user.height == 1.8

def test_update():
    user = User("John", "M", 25, 70.0, 1.8)
    user.name = "Pepe"
    user.age = 30
    user.height = 1.9
    assert user.name == "Pepe"
    assert user.age == 30
    assert user.height == 1.9

def test_calculate_bmr():
    user = User("John", "M", 25, 70.0, 1.8)
    bmr = user.calc_bmr()
    assert bmr == pytest.approx(1705.0, abs=0.5)
    
