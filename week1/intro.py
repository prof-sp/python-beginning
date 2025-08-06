#print('hello')
#a = 'David'
#b = '20'
#print(f'{a} is {b} years old')
#print(a + ' is ' + b + ' years old')
#print('{} is {} years old'.format(a,b))
#print('David is 20 years old')
#b = 30
#print(b)

#pro_languages = ['python', 'java', 'dart', 25]
#print(pro_languages[3])

#capital_city = {"Kenya": "Nairobi", "Nigeria": "Lagos"}
#print(capital_city)

#a = input('enter your name:')
#b = input('what is your favorite colour:')

#print(f'Hello,{a} your favorite color is {b}')


'''
import random 
#  List of Python/programming jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "I told my Python code to sleep... now it won't wake up.",
    "Why did the developer go broke? Because he used up all his cache.",
    "What's a Python developer’s favorite snake? Monty Python 🐍",
    "How many programmers does it take to change a light bulb? None—it’s a hardware issue!",
    "Why can't Python programmers play hide and seek? Because they keep getting caught in exceptions!",
    "I tried writing a joke in Python, but it kept throwing syntax errors. Maybe humor is not defined."
]

#  Randomly select and display a joke
def tell_joke():
    joke = random.choice(jokes)
    print(f"\n🤖 Here's your joke:\n{joke}\n")

# Run the joke teller
if __name__ == "__main__":
    tell_joke()'''


a = float(input('enter a number:'))
b = input('enter an assignment operator ; +,-, *,/:')
c = float(input('enter a second number:'))

if b == '+':
    print(f'{a} + {c} = {a + c}')
elif b == '-': 
    print(f'{a} - {c} = {a - c}')
elif b == '*':          
    print(f'{a} * {c} = {a * c}')               
elif b == '/':
    if c != 0:
        print(f'{a} / {c} = {a / c}')
    else:
        print("Error: Division by zero is not allowed.")