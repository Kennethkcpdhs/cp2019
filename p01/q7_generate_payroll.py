name = input("Enter your name: ")
hours_worked = eval(input("Enter hours worked weekly: "))
hour_pay = float(input("Enter hourly pay rate: "))

cpf_contribution = float(input("Enter CPF contribution rate(%): "))
gross_pay = hours_worked * hour_pay
CPF = float(gross_pay*(cpf_contribution/100))
Net_pay = gross_pay - CPF

print("\nPayroll statement for ",(name))
print("\nNumber of hours worked in week: {0} ".format(hours_worked))
print("\nHourly Pay rate: ${0:.2f}".format(hour_pay))
print("\nCPF contribution at {0}% = ${1:.2f} ".format(cpf_contribution,CPF))
print("\nNet pay = ${0:.2f}".format(Net_pay))
