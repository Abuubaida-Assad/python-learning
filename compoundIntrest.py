price = int(input("enter the principle amount :"))
rate = int(input("enter the intrest rate :"))
dur=int(input("enter the duration: "))

amount = price * ((1 + rate / 100) ** dur)
print("principle",price);
print("intrest rate",rate);
print("duration",dur);
print("total amount",amount) 