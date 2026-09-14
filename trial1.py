from stanfordkarel import *
print('karel library imported successfully!')

def main():
    turn_left()
    move()
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()
    move()
    turn_right()
    move()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program()            
    
