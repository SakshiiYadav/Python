
# coding: utf-8

# In[ ]:


# To determine Pythagorean distance between three 


# In[ ]:


x,y,z = 2,3,4
w =(x**2 + y**2 + z**2)**0.5
print("Pythagorean distance between three points is",w)


# In[ ]:


# To find LCM of two divisors


# In[ ]:


# 1st method 
no_1 = int(input("Enter first number:"))
no_2 = int(input("Enter second number:"))

if (no_1>no_2):
    
    max = no_1
else:
    max = no_2
while(True):
    if((max % no_1 ==0) and (max % no_2 ==0)):
        print("Lcm is", max)
        break
    max +=1


# In[ ]:


# 2nd method
counting = True                    

print("Enter first divisor:")
first_divisor = int(input())

print("Enter second divisor:")
second_divisor = int(input())

i = 1

while counting:
    if i % first_divisor == 0 and i % second_divisor == 0:
        print("Least Common Multiple of ",first_divisor,"and ",second_divisor," is",i,".")
        break
    i += 1
       


# In[ ]:


# 3rd method using def function
def compute_lcm(x,y):
    
    if x > y:
        greater = x
    else:
        greater = y
        
    while(True):
        if((greater % x==0) and (greater % y ==0)):
            lcm = greater
            break
        greater +=1
    return lcm
print("Enter first number:")
num1 = int(input())
print("Enter second number:")
num2 = int(input())

print("The L.C.M. is", compute_lcm(num1,num2))


# In[ ]:





# In[ ]:


# Making a simple calculator


# In[ ]:


def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y
 
def divide(x,y):
    return x / y

print("Select operation")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

while (True):
    choice = int(input("Enter choice 1/2/3/4:"))
    if choice in (1,2,3,4):
        number_1 = float(input("Enter first number:"))
        number_2 = float(input("Enter second number"))
        
        if choice == 1:
            print(number_1,"+",number_2,"is",add(number_1,number_2))
        elif choice == 2:
            print(number_1,"-",number_2,"is",subtract(number_1,number_2))  
        elif choice == 3:
            print(number_1,"*",number_2,"is",multiply(number_1,number_2))
        elif choice == 4:
            print(number_1,"/",number_2,"is",divide(number_1,number_2))
            
        next_calculation = input("Want to try another operation? yes/no:")
        if next_calculation == "no":
            break
else:
    print("Invalid Input")
            


# In[ ]:





# In[ ]:


# To find largest of the three numbers


# In[ ]:


numb_1 = input("Enter first number: ")
numb_2 = input("Enter second number: ")
numb_3 = input("Enter third number: ")

if ((numb_1 >= numb_2) and (numb1 >= numb3)):
    largest = numb_1
elif((numb_2 >= numb_1) and (numb_2 >= numb_3)):
     largest = numb_2
else:
     largest = numb_3
print("The largest among the three numbers is",largest)


# In[ ]:


# To find area of a triangle


# In[ ]:


a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

s = (a+b+c) / 2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print("Area of a scalene triangle is %0.2f"%area)


# In[ ]:





# In[ ]:


# Degrees and Radians 


# In[ ]:


import math

print(math.degrees(math.pi/2))
print(math.radians(60))

