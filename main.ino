#include <LiquidCrystal.h>

/*
  Main 

  This program takes a string command from a python host program via serial,
  then produces the correct output.
  It can display a message on the LCD, turn the LED on, or begin an alarm with
  a buzzer depending on the command.

  Wiring:
    - LED to pin 7
    - buzzer to pin 13
    - button to pin A0
    - LCD to pins 12,11,5,4,3,2
*/

//initalise LED, LCD, buzzer and button to pins
#define WHITE 7
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
int buzzer = 13;
int button = A0;

void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);
  pinMode(WHITE, OUTPUT) //led
  pinMode(buzzer, OUTPUT) //buzzer
  pinMode(button, INPUT_PULLUP) //button
}

void loop() {
  while (!Serial.available()); 
  //get message sent through serial communication
  String command = Serial.readStringUntil('\n');

  switch(command.trim()) {
    case "LCD:":
      //displays new message on LCD
      String msg = command.substring(4);
      lcd.clear();
      lcd.print(msg);
    case "LED:":
      //turn LED on full brightness
      analogWrite(WHITE, 255)
    case "BUZZER:"
      //turn buzzer on and off until button is pressed
      while (digitalRead(button) == HIGH) {
        tone(buzzerPin, 1000); //buzzer set to a tone of 1000 Hz
        delay(1000); 
        noTone(buzzerPin); //stops buzzer
        delay(1000);
      }
      //button pressed, alarm turns off 
      digitalWrite(buzzer, LOW)
      //communicate to python that button is pressed
      Serial.println("BUZZER: OFF")
    }

      

}
