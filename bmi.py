# Body Mass Index

name = 'Bruno'
height = 1.90
weight = 90
bmi = weight / (height * height)

message = '{name} is {height:.2f} meters tall, weighs {weight} kilograms, and has a BMI of {bmi:.2f}'
formatted_message = message.format(
    name=name, 
    height=height, 
    weight=weight, 
    bmi=bmi
)

print(formatted_message)