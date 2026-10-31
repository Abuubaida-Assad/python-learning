# f=open("sample.txt","w")
# str = "this is a sample txt file "
# f.write(str)
# print("file created sucess fully")

# example to handle file in append mode

f=open("sample.txt","a")
st="";
while st!="bye":
    st=input("enter the statment");
    if st == "bye":
        break
f.write(st);
f.close();
print("file is created sucessfully")


