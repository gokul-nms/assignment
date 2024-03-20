num = (int (input ("enter the values   :")))
val = str(num)
val2 = len(val)
armstrong = 0
for digit in val:
    armstrong += int(digit ) ** val2 
if armstrong == num:
    
    print( armstrong,"Its an Armstrong number")
else:
    print(armstrong ,"Its not an armstrong num")