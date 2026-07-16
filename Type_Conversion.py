#type conversion #python itself does type coversion between float and integer but cannot do so betweern str and float
a= 3.6
b= 3
print(type(a))
print(type(b))
print(a+b)


c="2"
d=5
print (c+d)

#thus we need to forcefully change its type this is called type casting

e="2"
e=int(e)
f=5.1

print(type(e))
print(type(f))
print(e+f)

s=3.14
s=str(s)
print (type(s))