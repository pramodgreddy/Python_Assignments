import math



scores={}
for i in range(4):
	name=input("enter your name: ")
	marks=input("enter your marks in this order: Math, Physics,Chemistry,Biology,social-science: ")
	scores[name]=marks

print(scores)

# for j in range(4):
# 	if(j!="exit"):
# 		name_check=input("enter the name of student: ")
# 		sub=input("enter the subject you want to know the marks of: ")
# 	else:
# 		break


# name_check=""
# while (name_check!="exit"):
# 		name_check=input("enter the name of student: ")

	
def logic():

	name_check=""
	output=0
	sub=" "
	while (name_check!="exit"):

		name_check=input("enter the name of student: ")
		sub=input("enter the subject you want to know the marks of: ")

		for key,val in scores.items():
			if(name_check==key):
				if(sub=="Math"):
					output=val.split(",")
					print(f"{name_check} scored {output[0]} in {sub}")
				elif(sub=="Physics"):
					output=val.split(",")
					print(f"{name_check} scored {output[1]} in {sub}")
				elif(sub=="Chemistry"):
					output=val.split(",")
					pprint(f"{name_check} scored {output[2]} in {sub}")
				elif(sub=="Biology"):
					output=val.split(",")
					print(f"{name_check} scored {output[3]} in {sub}")
				elif(sub=="Social"):
					output=val.split(",")
					print(f"{name_check} scored {output[4]} in {sub}")


logic()
	

