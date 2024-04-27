from collections import deque

def parse_input(user_input):
    return user_input.strip().lower()

def check_palindrome(user_input):
    d = deque(user_input)
    reversed_d = deque(reversed(user_input))
    if d == reversed_d:
        print("Palindrome")
    else:
        print("Not a palindrome")
      

def main():
    print("Welcome!")
    while True:
        user_input = parse_input(input("Please enter your word to check (press Enter to exit): "))
        if len(user_input) > 0:
            if user_input.isalpha():
                check_palindrome(user_input)
            else:
                print("Please enter only letters.")
        else:
            print("Exiting the program. Good luck")
            break     

if __name__ == "__main__":
    main()