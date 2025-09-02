# Arduino-Morning-Routine
Arduino-Morning-Routine This repository is for a morning automation system that performs personalised tasks for the user, like playing recommended music and displaying tasks for the day.

# How It Works:
The Arduino main.ino program waits for a serial message from the python host program main.py, which sends commands. When a message is recieved, an alarm begins and once a button is pressed, Spotify API is used to open a random song from a specified playlist in the browser.
It uses the OpenWeatherAPI to automatically turn the LED on if the sun has not risen in the user's location yet, as well as the Google Tasks API to circulate through the first 5 tasks of the day on the LCD.


# Hardware:
- Arduino Uno
- 2x 220Ω resistor (for LCD and LED)
- LED
- 16x2 LCD display
- Buzzer

# Instructions:
1. Wire circuit with schematic
2. Clone this repository
3. Install dependencies ("pip install -r requirements.txt")
4. Copy .env.example to .env and fill in your own API credentials (Google Tasks API, Spotify API, OpenWeather API used)
5. Run with: "python src/main.py"


# Schematic Diagram
<img width="1254" height="749" alt="Screenshot 2025-09-02 012141" src="https://github.com/user-attachments/assets/8d47c98f-e25e-4e42-852b-8ae501b63c36" />

