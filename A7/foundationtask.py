def temp(far):
    cel=(far-32)*5/9
    return f"{far}°F is {cel:.2f}°C"

far=int(input("Enter temperature in Farenheit:"))
print(temp(far))
