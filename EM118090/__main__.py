import time
from EM118090.EM118090 import EM18090
from EM118090 import parameters
from colorama import init, Fore, Style
import argparse

init(autoreset=True)  # Initialize colorama


def display_meter_data(meter):
    try:
        print(f"{Fore.YELLOW}{Style.BRIGHT}EM118090 Power Meter Test{Style.RESET_ALL}")
        print("\nLoading...", end="", flush=True)

        while True:
            voltage = meter.get_value(1, parameters.InstantaneousParameters.voltage)
            current = meter.get_value(1, parameters.InstantaneousParameters.current)
            frequency = meter.get_value(1, parameters.InstantaneousParameters.frequency)
            power = meter.get_value(1, parameters.PowerParameters.active_total_power)
            print("\033[H\033[J", end="")  # Clear the terminal screen (works on Windows with colorama)

            print(f"{Fore.YELLOW}{Style.BRIGHT}EM118090 Power Meter Test{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Voltage:{Style.RESET_ALL} {voltage} V")
            print(f"{Fore.BLUE}Current:{Style.RESET_ALL} {current} A")
            print(f"{Fore.CYAN}Frequency:{Style.RESET_ALL} {frequency} Hz")
            print(f"{Fore.MAGENTA}Power:{Style.RESET_ALL} {power} kWh")
            print(f"\n{Fore.WHITE}Press 'Ctrl+C' to exit{Style.RESET_ALL}")

    except KeyboardInterrupt:
        print("\033[H\033[J", end="")  # Clear the terminal screen (works on Windows with colorama)
        print(f"{Fore.RED}{Style.BRIGHT}Exiting...{Style.RESET_ALL}")
        time.sleep(1)
        print("\033[H\033[J", end="")  # Clear the terminal screen (works on Windows with colorama)
        exit()

    except:
        print("\033[H\033[J", end="")  # Clear the terminal screen (works on Windows with colorama)
        print(f"{Fore.RED}{Style.BRIGHT}Somethig went wrong.{Style.RESET_ALL}")
        print(f"{Fore.RED}{Style.BRIGHT}Exiting...{Style.RESET_ALL}")
        time.sleep(1)  # Simulate an exit animation
        print("\033[H\033[J", end="")  # Clear the terminal screen (works on Windows with colorama)
        exit()

def main():
    parser = argparse.ArgumentParser(description='Simple command line tool to test EM118090')
    parser.add_argument('--port', type=str, help='Port to communicate to the device', required=True)
    args = parser.parse_args()

    meter = EM18090(port=args.port)
    display_meter_data(meter)

if __name__ == "__main__":
    main()
