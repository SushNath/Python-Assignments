#!/usr/bin/env python
# coding: utf-8

# ## Write a program to check if a number is even or odd

# In[1]:


a=int(input("Enter a number "))
if(a%2==0):
    print("Even")
else:
    print("Odd")


# ## Write a program to check whether an alphabet is vowel or consonant

# In[3]:


a=str(input("Enter an alphabet "))
if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
    print("Vowel")
else:
    print("Consonant")


# ## Write a program to check if a person is eligible to vote or not

# In[5]:


a=int(input("Enter the age "))
if(a>=18):
    print("Eligible")
else:
    print("Not Eligible")


# ## Write a program to check if a number is positive, negative or zero

# In[2]:


a=int(input("Enter a number "))
if(a>0):
    print("Positive")
if(a<0):
    print("Negative")
if(a==0):
    print("Zero")


# ## Write a program to check if a given year is leap year or not

# In[4]:


a=int(input("Enter year "))
if(a%4==0):
    print("Leap Year")
else:
    print("Non leap year")


# ## Write a program to check if a triangle is equilateral, isosceles or scalene

# In[2]:


a=int(input("Enter 1st side "))
b=int(input("Enter 2nd side "))
c=int(input("Enter 3rd side "))
if(a==b==c):
    print("Equilateral Triangle")
if(a==b!=c or a!=b==c or a==c!=b):
    print("Isosceles Triangle")
if(a!=b!=c or a!=b!=c or a!=c!=b):
    print("Scalene Triangle")


# ## Write a program to check whether after selling a product there is profit or loss

# In[5]:


CP=int(input("Enter the cost price "))
SP=int(input("Enter the Selling price "))
if(SP>CP):
    print("Profit=",SP-CP)
if(SP<CP):
    print("Loss=",CP-SP)
if(SP==CP):
    print("No profit no loss")


# ## Write a program to enter two numbers and print the greater number.

# In[9]:


a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))
if(a>b):
    print("greater number is",a)
else:
    print("greater number is",b)
        


# ## Write a program to enter two numbers and print the smaller number.

# In[10]:


a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))
if(a<b):
    print("smaller number is ",a)
else:
    print("smaller number is ",b)


# ## Write a program to enter three numbers and print the greatest number.

# In[11]:


a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))
c=int(input("Enter 3rd no. "))
if(a>b and a>c):
    print("greatest number is ",a)
elif(b>a and b>c):
    print("greatest number is ",b)
else:
    print("greatest number is ",c)
    


# ## Write a program to enter three numbers and print the smallest number.

# In[12]:


a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))
c=int(input("Enter 3rd no. "))
if(a<b and a<c):
    print("smallest number is ",a)
elif(b<a and b<c):
    print("smallest number is ",b)
else:
    print("smallest number is ",c)


# ## Write a program to calculate roots of quadratic equation

# In[20]:


a=int(input("Enter 1st no. "))
b=int(input("Enter 2nd no. "))
c=int(input("Enter 3rd no. "))
x1=(-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2=(-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print("1st Root is",x1)
print("2nd root is",x2)


# ## Write a program to enter no. from 1-7 and print the respective day of the week.

# ### Using if- else

# In[28]:


num=int(input("Enter a number from 1-7 "))
if(num==1):
    print("Sunday")
elif(num==2):
    print("Monday")
elif(num==3):
    print("Tuesday")
elif(num==4):
    print("Wednesday")
elif(num==5):
    print("Thursday")
elif(num==6):
    print("Friday")
elif(num==7):
    print("Saturday")
else:
    print("Please enter a valid number")


# ### Using key and value

# In[27]:


a=int(input("Enter a no. "))
day={1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
day[a]


# ### Write a program to enter a number from 1-12 and display the respective month

# In[1]:


num=int(input("Enter a number from 1-12 "))
if(num==1):
    print("Jan")
elif(num==2):
    print("Feb")
elif(num==3):
    print("Mar")
elif(num==4):
    print("Apr")
elif(num==5):
    print("May")
elif(num==6):
    print("June")
elif(num==7):
    print("July")
elif(num==8):
    print("Aug")    
elif(num==9):
    print("Sept")    
elif(num==10):
    print("Oct")
elif(num==11):
    print("Nov")
elif(num==12):
    print("Dec")
else:
    print("Please enter a valid number")


# ## Write a program to enter a number from 1-4 and perform the operations(Addition,Subtraction, Multiplication, Division)

# In[3]:


num=int(input("Enter a number from 1-4 "))
a=int(input("Enter 1st number "))
b=int(input("Enter 2nd number "))
if(num==1):
    print("Sum is ",a+b)
if(num==2):
    print("Difference is ",a-b)
if(num==3):
    print("Product is ", a*b)
if(num==4):
    print("Division is ",a/b)


# ### Write a program to convert temp. to and from celsius, fahrenheit

# In[13]:


temp=input("Enter a temperature in C or F ")
deg=int(temp[:-1])
if(temp[-1]=='C'):
    fah=((deg*9)/5)+32
    print("Temp in F is ", fah)
elif(temp[-1]=='F'):
    cel=((deg-32)*5)/9
    print("Temp in C is ",cel)
else:
    print("Please enter a valid value")
   
     


# In[ ]:




