def convert_temperature(value, scale):
    scale = scale.lower()

    if scale == "c": 
        fahrenheit = (value * 9/5) + 32
        kelvin = value + 273.15
        return f"Fahrenheit: {fahrenheit}", f"Kelvin: {kelvin}"

    elif scale == "f": 
        celsius = (value - 32) * 5/9
        kelvin = celsius + 273.15
        return f"Celsius: {celsius}", f"Kelvin: {kelvin}"

    elif scale == "k":  
        celsius = value - 273.15
        fahrenheit = (celsius * 9/5) + 32
        return f"Celsius: {celsius}", f"Fahrenheit: {fahrenheit}"

    else:
        return ["Invalid scale!"]


print("Temperature Converter")
value = float(input("Enter temperature value: "))
scale = input("Enter scale (C/F/K): ")

result = convert_temperature(value, scale)

print("Converted values:")
for r in result:
    print(r)
