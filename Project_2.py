#This is a program that calculates the surface area of a cone
#SAMPLE INPUT:
#Radius: 3
#Slant Height: 5
#Expected Answer: 75.398

#Importing math
import math

print("👋")
print("I'm a cone caluculator.")
print("Give me the radius and the slant height of a cone and I will give you its surface area.")

#Asking user to input values for the radius and length
radius_text = input("Radius: ")
slant_height_text = input("Slant Height: ")

#Converting radius and length values to floats
r = float(radius_text)
l = float(slant_height_text)

#Calculating surface area
SA = (math.pi * (r * r)) + (math.pi * r * l)

#Rounding surface area to 3 decimal places
SA = (round(SA, 3))

#Printing surface area
print("The surface area of the cone is " + str(SA))
print("👍😎")