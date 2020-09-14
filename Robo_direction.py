import math

up=input("input UP along with the number : \n")
list=up.split(" ")
tuple1=tuple(list)
print(tuple1[1])

down=input("input DOWN along with the number : \n")
list=down.split(" ")
tuple2=tuple(list)
print(tuple2[1])

left=input("input LEFT along with the number : \n")
list=left.split(" ")
tuple3=tuple(list)
print(tuple3[1])

right=input("input RIGHT along with the number : \n")
list=right.split(" ")
tuple4=tuple(list)
print(tuple4[1])

x=int(tuple1[1])-int(tuple2[1])
y=int(tuple3[1])-int(tuple4[1])
print("the Final Position is:")
print(x,y)
print("The distance the final point and origin is: ")
print(round(math.sqrt(x**2+y**2)))
