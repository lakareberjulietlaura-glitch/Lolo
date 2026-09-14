from stanfordkarel import *
print('karel library imported successfully!')

def climb_step():  
    move()  
    turn_left()
    move()
    turn_right()
    move()
    
def descend_step():
    move()
    turn_right()
    move()
    turn_left()

def climb_step():
    move()

def descend_step():
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()  

def main():       
    for i in range(3):
        climb_step()

    for i in range(3):
        descend_step()      

if __name__ == '__main__': 
     run_karel_program()        

