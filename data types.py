first_name='Devi'
last_name='priya'
full_name='Devipriya'
is_married='True'
age=17
country='India'
city='Chennai'
year=2007
is_true='True'
first_name,last_name,full_name,is_married,age,country,city,year,is_true='Devi','priya','Devipriya','True',17,'India','Chennai',2007,'True'
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(is_married))
print(type(age))
print(type(country))
print(type(city))
print(type(year))
print(type(is_true))
print(len(first_name))
print(len(last_name))
a=len(first_name)
b=len(last_name)
if a>b:
 print('the lenth of first name is greater')
elif a<b:
 print('the lenth of last name is greater')
else:
 print('the lenth of the first and last name are equal')
num_1=5
num_2=4
total=num_1+num_2
diff=num_2-num_1
product=num_2*num_1
division=num_1/num_2
modulus=num_2%num_1
exp=num_1**num_2
floor_division=num_1//num_2
print(total,diff,product,division,modulus,exp,floor_division)
r,π=30,3.14
area_of_circle=π*r**2
circumference=2*π*r
print(area_of_circle,circumference)