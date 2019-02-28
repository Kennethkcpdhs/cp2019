number = input("How many students do you have: ")
i=1
my_dict = dict()
while i<=number:
    student = raw_input('Enter than Student name: ')
    result = input("Enter the result: ")
    my_dict[result] = student
    i+=1  #to count and continue for number of students
studentresult=[]

for i in my_dict:      #change dictionary results to list for sorting
    studentresult.append(i)
studentresult.sort()

print(("Here is the highest result: "),my_dict.get(studentresult[-1]))   #using results to extract names
print(("Here is the 2nd highest result: "),my_dict.get(studentresult[-2]))


