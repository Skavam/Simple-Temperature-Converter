# Temperature converter program by @Skavam on GitHub

from colorama import Fore

def main():

    print("Welcome to the Temperature Converter")
    print(f"\n{Fore.LIGHTBLUE_EX}--| Celsius |--{Fore.RESET}")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")

    print(f"\n{Fore.LIGHTBLUE_EX}--| Fahrenheit |--{Fore.RESET}")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")

    print(f"\n{Fore.LIGHTBLUE_EX}--| Kelvin |--{Fore.RESET}")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")

    choice = input("\nEnter your choice (1, 2, 3, 4, 5, or 6): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"\n{celsius}°C is equal to {Fore.GREEN}{fahrenheit}°F{Fore.RESET}")

    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"\n{celsius}°C is equal to {Fore.GREEN}{kelvin}K{Fore.RESET}")

    elif choice == '3':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"\n{fahrenheit}°F is equal to {Fore.GREEN}{celsius}°C{Fore.RESET}")

    elif choice == '4':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"\n{fahrenheit}°F is equal to {Fore.GREEN}{kelvin}K{Fore.RESET}")
    
    elif choice == '5':
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        print(f"\n{kelvin}K is equal to {Fore.GREEN}{celsius}°C{Fore.RESET}")

    elif choice == '6':
        kelvin = float(input("Enter temperature in Kelvin: "))
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"\n{kelvin}K is equal to {Fore.GREEN}{fahrenheit}°F{Fore.RESET}")

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print(f"{Fore.RED}Invalid choice.{Fore.RESET}")


# Celsius
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

# Kelvin
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

if __name__ == "__main__":
    main()
