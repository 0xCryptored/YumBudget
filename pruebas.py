import re

def main():
    s = input("gender? ")
    match = re.match(r"^(M(?:ale)?|F(?:emale)?|N(?:one)?)$", s)
    print(match)
    
main()