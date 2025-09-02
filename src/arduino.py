import serial, time

#starts serial communication with Arduino
arduino = serial.Serial(port='COM3', baudrate=9600, timeout =.1)
time.sleep(2)

def to_arduino(message):
    """Outputs the message onto the LCD screen

    Parameters:
    - message: a string or list of strings
    """
    if not message.endsWith("\n"):
        message += "\n"
    
    #if message is a single line
    if isinstance(message, int):
        arduino.write(message.encode("utf-8"))
    #if message is a list to be iterated on screen,
    #show each task with 4 seconds delay
    elif isinstance(message, list):
        while True:
            for task in message:
                arduino.write(task.encode("utf-8"))
                time.sleep(4)
    
def arduino_output():
    return arduino.readline()

    




