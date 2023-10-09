import time
from prettytable import PrettyTable
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def display_header():
    print(f"{Fore.CYAN}{'#' * 50}")
    print(f"{Fore.CYAN}{'#' * 12} Raspberry Pi LED Wizard {'#' * 12}")
    print(f"{Fore.CYAN}{'#' * 50}")

def display_wiring_guide():
    table = PrettyTable()
    table.field_names = ["LED Strip", "GPIO Pin", "Color"]
    table.add_row(["LED Strip 1", "GPIO 17", "Red"])
    table.add_row(["LED Strip 2", "GPIO 18", "Green"])
    table.add_row(["LED Strip 3", "GPIO 27", "Blue"])
    print(f"{Fore.YELLOW}Wiring Guide:")
    print(table)

def control_leds():
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        print(f"{Fore.RED}Error: RPi.GPIO library not found. Please install it before running the script.")
        return

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)

    print(f"{Fore.GREEN}LED control initialized. You can now control your LEDs.")

    while True:
        color = input(f"{Fore.YELLOW}Enter the color you want to display (Red, Green, Blue, Quit): ").lower()
        if color == 'red':
            GPIO.output(17, True)
        elif color == 'green':
            GPIO.output(18, True)
        elif color == 'blue':
            GPIO.output(27, True)
        elif color == 'quit':
            GPIO.cleanup()
            print(f"{Fore.GREEN}Exiting. Have a nice day!")
            break
        else:
            print(f"{Fore.RED}Invalid color. Please enter Red, Green, Blue, or Quit.")

        time.sleep(1)
        GPIO.output(17, False)
        GPIO.output(18, False)
        GPIO.output(27, False)

if __name__ == "__main__":
    display_header()
    display_wiring_guide()

    proceed = input(f"{Fore.YELLOW}Have you completed the wiring as per the guide above? (yes/no): ").lower()
    if proceed == 'yes':
        control_leds()
    else:
        print(f"{Fore.RED}Please complete the wiring and then run the script again.")
