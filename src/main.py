from sunrise import sun_risen
from arduino import to_arduino
from arduino import arduino_output
from music import play_music
from tasks import get_tasks

def main():
    """calls functions to perform morning routine
    """
    #before button pressed
    to_arduino("LCD: Good morning!")
    if not sun_risen:
        to_arduino("LED: ON")

    #sets buzzer on 
    to_arduino("BUZZER: ON")
    buzzerOn = True
    while buzzerOn:
        if arduino_output() == "BUZZER: OFF":
            buzzerOn = False

    #after button pressed
    play_music()
    
    tasks = get_tasks()
    to_arduino("LCD: " + tasks)
    
    
    
    

