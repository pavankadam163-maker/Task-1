def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def convert_temperature():
    print("\n🌡️  Temperature Converter")
    print("==========================")
    print("1. Celsius → Fahrenheit")
    print("2. Celsius → Kelvin")
    print("3. Fahrenheit → Celsius")
    print("4. Fahrenheit → Kelvin")
    print("5. Kelvin → Celsius")
    print("6. Kelvin → Fahrenheit")

    choice = input("\nChoose a conversion (1–6): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        temp = float(input("Enter the temperature value: "))

        if choice == '1':
            print(f"\n✅ {temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
        elif choice == '2':
            print(f"\n✅ {temp}°C = {celsius_to_kelvin(temp):.2f} K")
        elif choice == '3':
            print(f"\n✅ {temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
        elif choice == '4':
            print(f"\n✅ {temp}°F = {fahrenheit_to_kelvin(temp):.2f} K")
        elif choice == '5':
            print(f"\n✅ {temp} K = {kelvin_to_celsius(temp):.2f}°C")
        elif choice == '6':
            print(f"\n✅ {temp} K = {kelvin_to_fahrenheit(temp):.2f}°F")
    else:
        print("\n❌ Invalid choice! Please select a number between 1 and 6.")

# Run the converter
convert_temperature()
