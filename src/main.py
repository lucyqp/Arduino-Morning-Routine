from sunrise import sun_risen
from arduino import to_arduino
from arduino import buzzer_off
from music import play_music
from tasks import get_tasks

def main():
    """calls functions to perform morning routine
    """
    #before button pressed
    to_arduino("LCD: Good morning!\n")
    if sun_risen: #change this to a not IMPORTANT CHANGE
        to_arduino("LED: ON\n")

    #sets buzzer on 
    to_arduino("BUZZER: ON\n")

    #waits until buzzer is pressed before continuing
    buzzer_off()
    
 
    #after button pressed
    play_music()
    tasks = get_tasks()
    to_arduino(tasks)
    
main()    
    
    

