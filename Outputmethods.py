name,age,salary ="Ramesh",50,5500.13
# method 1-printing the value of variable directly
print(name,age,salary)
# method 2-concadinate string with a value of variabel
print("Name is ",name)
print("Age is",age)
print("salary is",salary)
#method 3(using C language syntax)Data type is important
print("Name is %s Age is %d Salary is %g" %(name,age,salary))
#method 4-using format function value is important
print("Name is {} Age is {} salary is {}".format(name,age,salary))
#method 5 using format fuction value and index number are important
print("Name is {0} Age is {1} salary is {2}".format(name,age,salary))
