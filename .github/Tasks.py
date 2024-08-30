#print(Calculate your age based on the current year and your birth year)
def Myage (birthyear:int, currentyear:int):
    age = birthyear - currentyear
    return age
result = Myage(2001,2024)
print (result)

#print(Write a program that calculates the area of a rectangle using length and width variables)
def Rectangle_area (length:int, width:int):
    area = length*width
    return area
result = Rectangle_area(8,5)
print (result)

#print(Write a program that calculates the area of a circle)
def circle_area (π:int, radius:int):
    area = π * radius ** 2 
    return area
result = circle_area(3.14,7)
print (result)

#print(Write a program that calculates the area of the cube.)
def cube_area (side:int):
    area = 6 * side ** 2
    return area
result = cube_area(4)
print (result)

#print(Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable)
def convert_temperature(fahrenheit:float):
    celsius = fahrenheit - 32 * 5 / 9
    return celsius
result = convert_temperature(98.6)
print (result)

def temperature_conversion(celsius:int):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit
result = temperature_conversion(37)
print (result)

#print(Convert a given number of seconds into minutes and seconds using variables)
def total_minutes(seconds: int):
    minutes = seconds // 60
    return minutes
result = total_minutes(500)
print(result)

def left_seconds(total_seconds: int):
    remaining_seconds = total_seconds % 60
    return remaining_seconds
result = left_seconds(500)
print(result)

#print(Write a program that calculates the percentage)
def calculate_percentage(obtained_marks: int, total_marks: int):
    percentage_value = (obtained_marks / total_marks) * 100
    return percentage_value
result = calculate_percentage(759, 1100)
print (result)

#print(Write a program that calculates the BMI using height and weight variables)
def MyBMI(weight:int, height:float):
    BMI = weight / height ** 2
    return BMI
result = MyBMI(64, 1.62)
print(result)

#print(Write a program that calculates the volume of a cylinder using the formula)
def cylinder_volume(π: float, radius1: int, height1: int):
    Volume = π * radius1 ** 2 * height1
    return Volume
result= cylinder_volume(3.14, 3, 5)
print (result)


