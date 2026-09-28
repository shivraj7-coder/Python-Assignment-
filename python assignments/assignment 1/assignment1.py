{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 #creating a list\
students_list=["Aditi","Shaurya","Rishi","Sneha","Riya"]\
print("students list: ",students_list)\
students_list.append("Rohan")\
print(students_list)\
students_list.remove("Aditi")\
print(students_list)\
students_list=["Aditi","Shaurya","Rishi","Sneha","Riya"]\
students_list.pop(1)\
print(students_list)\
del students_list[3]\
print(students_list)\
students_list[2]="Shreya"\
print(students_list)\
#creating a tuple\
students_tuple=("Aditi","Shaurya","Rishi","Sneha","Riya")\
print("students tuple: ",students_tuple)\
y=list(students_tuple)\
y.append("rohan")\
y.append("Himesh")\
y.append("Karan")\
students_tuple=tuple(y)\
print(students_tuple)\
y=("Riley",)\
students_tuple += y\
print(students_tuple)\
y=list(students_tuple)\
y.remove("Aditi")\
y.remove("Riya")\
students_tuple=tuple(y)\
print(students_tuple)\
#creating a dictionary\
students_dict=\{1:"Aditi",2:"Shaurya",3:"Rishi",4:"Sneha",5:"Riya"\}\
print("students dictionary: ",students_dict)\
students_dict[6]="Rohan"\
print("After adding Rohan: ",students_dict)\
del students_dict[3]\
print("After deleting Rishi: ",students_dict)\
students_dict[2]="Shreya"\
print("After updating Shreya: ",students_dict)}