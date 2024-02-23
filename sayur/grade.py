ds = float(input("Enter Your Datascience Marks outof 100 :"))
ml = float(input("Enter Your Machinelearning Marks outof 100:"))
ai = float(input("Enter Your Artificialintelligence Marks outof 100:"))
pr = float(input("Enter Your Probablity Marks outof 100:"))
dl = float(input("Enter your Deeplearning Marks outof 100:"))

average_marks = (ds+ml+ai+pr+dl)/5
print("Average Marks :" , average_marks )

if  average_marks >=90:
   print ("grade = o")
elif 80<= average_marks >=90 :
    print("grade = A+")
elif 70<= average_marks >=80:
    print("grade = A")
elif 60<= average_marks >=70:
    print("grade = B+")
elif 50<= average_marks >=60:
    print("grade=B")
else :
   print("grade = F")


        
