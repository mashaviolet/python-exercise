# The volume of a sphere with radius r is (4/3)*pie r**2.
# what is the volume of the sphere with radius 5.
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places

# solution
def volume_of_a_sphere():
    radius = int(input("Enter radius of a sphere :"))
    volume_of_a_sphere= (4/3)* (22/7)* (radius)**2
    print(f"The volume of a sphere of radius {radius} is :{volume_of_a_sphere:.2f} ")
volume_of_a_sphere()

# WITI has tasked me to automate a simple grading system.
# As as a python student, write a program used to display the grades that
# the student will be recieving marks based on the mark scored in a subject.
# the grade are:
# 90% - 100% Grade is A
# 80% - 89% Gade is B
# 70% - 79% Grade is C
# 60% - 69% Grade is D
# 50% - 59% Grade is E
# < 50% Fail

#solution
def calculation_of_grades():
    
    mark=int(input("Enter mark scored :\t"))
    if mark>=90 and mark<=100:
        print("Grade is A")
    elif mark>=80 and mark<89:
         print("Gade is B")
    elif mark>=70 and mark<=79:

         print("Grade is C")
    elif mark>=60 and mark<=69:
         print("Grade is D")
    elif mark>=50 and mark<=59:
         print("Grade is E")
    else:
         print("Fail")


calculation_of_grades()



#Create a program to calculate the area of a triangle(1/2*base * height). 
# Base and height should be entered using a keyboard.

#solution
def area_of_a_triangle():
      base=int(input("\t Enter the base of the triangle :"))
      height=int(input("\t Enter the height of a triangle :"))

      area=(1/2) * base * height
      print(f"The area of a triangle with base {base} and height {height} is {area:.2f}")

area_of_a_triangle()