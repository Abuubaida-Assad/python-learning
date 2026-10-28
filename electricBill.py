cno = int(input("enter the customer number"))
cname= input("enter the customer name")
pmr= int(input("enter the privious reading"))
cmr=int(input("enter the current reading"))

if cmr>pmr:
    units = cmr - pmr;
    
    if units <= 200:
        amount = units *1;
    elif units < 300:
        amount = (200 * 1) + (units - 200) * 1.25;
    elif units < 400:
        amount = (200 * 1) + (100 * 1.25) + (units - 200) * 1.5;
    elif units <= 500:
        amount = (200 * 1) + (100 * 1.25) +(100 * 1.5) + (units - 300) * 1.75;
    else :
        amount = (200 * 1) + (100 * 1.25) + (100 * 1.5) + (100 * 1.75) + (units - 400) * 2;
else:
    print("current reading is less than privious reading")

    surcharge = amount + 10 /100;
    totalAmount = amount + surcharge;
    print("charged unit", units);
    print("charged amount", amount);
    print("surcharge amount", surcharge)
    print("total amount",totalAmount);
    




