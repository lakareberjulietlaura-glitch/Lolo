from stanfordkarel import *
print('Karel library imported successfully!')

def main():
    turn_left()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    turn_right() 
    move()   
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    turn_right()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    turn_right()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    finish()

def turn_left():
      move()
      move()
          

def turn_right():
        turn_left()
        turn_left()
        turn_left()


def finish():
      move() 
                     
        
            

if __name__ == "__main__":
    run_karel_program()    
  





