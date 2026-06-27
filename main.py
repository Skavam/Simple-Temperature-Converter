# Temperature converter program by @Skavam on GitHub

def main():

    print("Welcome to the Temperature Converter")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")
    print("3. Convert Celsius to Kelvin", end="\n\n")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = convert_to_kelvin(celsius)
        print(f"{celsius}°C is equal to {kelvin:.2f}K")

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
    
def convert_to_kelvin(celsius):
    return celsius + 273.15

if __name__ == "__main__":
    main()