from stanfordkarel import *
print('karel library imported successfully!')

def main():
    fill_pothole()
    
def fill_pothole():
    turn_left()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()
    return()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left() 
      
        

if __name__ == "__main__":
    run_karel_program()
