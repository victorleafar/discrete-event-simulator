# File: /discrete-event-simulator/discrete-event-simulator/src/main.py

from simulator.core import Simulator
from ui.simple_ui import SimpleUI

def main():
    ui = SimpleUI()
    ui.display_welcome_message()
    
    simulator = Simulator()
    
    while True:
        user_input = ui.get_user_input()
        if user_input.lower() == 'exit':
            break
        simulator.add_task(user_input)
        simulator.run()

    ui.display_goodbye_message()

if __name__ == "__main__":
    main()