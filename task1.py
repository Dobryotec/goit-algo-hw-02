from queue import Queue
from random import randint
import time

def parse_input(user_input):
    return user_input.strip().lower()

q = Queue()

def generate_request():
   number_client = randint(1,10)
   q.put(f'Client -- {number_client}')
   print(f'Congratulations!!! Client -- {number_client} was added')


def process_request():
   if not q.empty():
      request = q.get()
      print(f'Request processed: {request}')
   else:
      print("Queue is empty")   

def main():
   print('Welcome to the Service Center!')
   while True:
    user_input = input("Would you like to create a request? (yes/no) ")
    command = parse_input(user_input)
    if command == "yes":
      generate_request()
      time.sleep(2)
      process_request() 
    elif command == "no":
       print("Exiting the program. Good luck")
       break   
    else:
       print("Invalid command. Please enter 'yes' or 'no'.")
    


if __name__ == "__main__":
    main()
