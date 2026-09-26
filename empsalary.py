eno= int(input("enter the employee id"))
ename= (input("enter the employee name"))
job=(input("domain"))
basic=int(input("enter the basic"))
hra=basic*14/100;
da= basic * 10/100;
ta = basic * 10 /100;
allowences = da + ta + da;

lic=basic * 12/100;
pf= basic * 8/100;
deductions = lic + pf;
gross = basic + allowences;
net = gross - deductions;
print("allowences:",allowences)
print("deductions",deductions)
print("gross",gross)
print("net",net)

