#ceaglebu@purdue.edu
#das185@purdue.edu
#knies2@purdue.edu 
#mgrassi@purdue.edu

N = int(input("How many terms do you want in your sequence?"))
num = [0, 1]
for i in range(2, N + 1):
    num.append(num[i-2]+num[i-1])

print(num)
