unit = input("Enter your unit of temperature (C/F): ").lower()
temp = float(input("Enter the temperature: "))
if unit == "c":
    temp = (round((9*temp)/5 + 32,1))
    print(f"The temperature in Farhenheit is: {temp} deg F")
elif unit == "f":
    temp = (round((temp - 32)* 5/9,1))
    print(f"The temperature in celsius is: {temp} deg C")
else:
    print(f"{unit} is an invalid unit of measurement!")


# OUTPUT
Enter your unit of temperature (C/F): c
Enter the temperature: 29
The temperature in Farhenheit is: 84.2 deg F

Enter your unit of temperature (C/F): F
Enter the temperature: 34 
The temperature in celsius is: 1.1 deg C
