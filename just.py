import sys

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def pda(string):


    E = '+-*/'
    s = Stack();	# Stack
    str_len = len(string)
    state = 1								# Initial state	
    accept_state = 6						# Accepting state
    print('Initial State q{}'.format(state)) # Current state q1

    for i in string:						# Iterate over string

        if i == '%' and state == 1:			# Check if string begins with % 
            s.push('%')						# If yes, then push % into the stack
            state = 2						# Move to state 2
            print('{}, Ɛ -> %: Current State q{}'.format(i,state)) # %, Ɛ -> % current state q2



        elif i.isdigit() and state == 2:	
            state = 3						# Move to state 3
            print('{}, Ɛ -> Ɛ: Current State q{}'.format(i,state)) # N, Ɛ -> Ɛ current state q3

        elif i == '(' and state == 2:
            s.push('(')
            state = 2						# Move to state 2
            print('{}, Ɛ -> (: Current State q{}'.format(i,state)) # (, Ɛ -> ( current state q2
    
        elif (i == '.') and state == 2:
            state = 4						# Move to state 4
            print('{}, Ɛ -> (: Current State q{}'.format(i,state)) # C, Ɛ -> Ɛ current state q4



        elif i.isdigit() and state == 3:
            state = 3						# Move to state 3
            print('{}, Ɛ -> Ɛ: Current State q{}'.format(i,state)) # N, Ɛ -> Ɛ current state q3

        elif (i == '.') and state == 3:
            state = 4						# Move to state 4
            print('{}, Ɛ -> (: Current State q{}'.format(i,state)) # C, Ɛ -> Ɛ current state q4

        elif i in E and state == 3:
            state = 2						# Move to state 2
            print('{}, Ɛ -> Ɛ: Current State q{}'.format(i,state)) # E, Ɛ -> Ɛ current state q2

        elif i == '%' and state == 3:
            if s.peek() == '%':
                s.pop()	
                state = accept_state		# Move to state 6
            else:
                break
            print('{}, % -> Ɛ: Current State q{}'.format(i,state)) # %, % .> Ɛ current state q6
        
        elif i == ')' and state == 3:
            if s.peek() == '(':
                s.pop()
                state = 5						# Move to state 5
            else:
                break
            print('{}, ( -> Ɛ: Current State q{}'.format(i,state)) # ), Ɛ -> ( current state q5



        elif (i.isdigit() or i == '.') and state == 4:
            state = 4						# Move to state 4
            print('{}, Ɛ -> Ɛ: Current State q{}'.format(i,state)) # NC_, Ɛ -> Ɛ current state q4

        elif i in E and state == 4:
            state = 2						# Move to state 2
            print('{}, Ɛ -> Ɛ: Current State q{}'.format(i,state)) # E, Ɛ -> Ɛ current state q2

        elif i == ')' and state == 4:
            if s.peek() == '(':
                s.pop()
                state = 5						# Move to state 5
            else:
                break
            print('{}, ( -> Ɛ: Current State q{}'.format(i,state)) # ), Ɛ -> ( current state q5

        elif i == '%' and state == 4:
            if s.peek() == '%':
                s.pop()	
                state = accept_state		# Move to state 6
            else:
                break
            print('{}, % -> Ɛ: Current State q{}'.format(i,state)) # %, % -> Ɛ current state q6


        elif i in E and state == 5:
            state = 2						# Move to state 2
            print('{}, Ɛ -> Ɛ: Current State q{}'.format(i,state)) # E, Ɛ -> Ɛ current state q2

        elif i == ')' and state == 5:
            if s.peek() == '(':
                s.pop()
                state = 5						# Move to state 5
            else:
                break
            print('{}, ( -> Ɛ: Current State q{}'.format(i,state)) # ), ( -> Ɛ current state q5

        elif i == '%' and state == 5:
            if s.peek() == '%':
                s.pop()	
                state = accept_state		# Move to state 6
            else:
                break
            print('{}, % -> Ɛ: Current State q{}'.format(i,state)) # %, % -> Ɛ current state q6

        else:
            print('Program crashed at state {} and symbol {}'.format(state,i))
            break							# If no, end the program

    if state == 6:
         print('Program accepted')
    else:
         print('Program rejected')
def main():
    while True:								# Keep running while response != n
        string = input("Would you like to enter string to check? (y/n)  ")
        if(string.lower() == 'n'):
            break
        else:								# Enter the string to check
            string = input("Enter the string: ")
            pda(string)						# Call PDA function

    #Used for testing
    for line in sys.stdin:
        if line.rstrip() == 'y':
            continue
        elif line.rstrip() == 'n':
            break
        else:
            pda(line.rstrip())
    


if __name__ == "__main__":
    main()