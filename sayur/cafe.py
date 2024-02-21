data = {'vadai':30,'soda':20,'sandwich':100}
for i in data:
    print(f'the cost of {i} is {data[i]}')
ip =[int(input('How many vadai you want ?:')),int(input('How Many soda you want ? :')),int(input("How many sandwich you want ? :"))]
total = float(data['vadai']*ip[0]+data['soda']*ip[1]+data['sandwich']*ip[2])
print('your bill :',total)
cash = float(input('your payment :'))
if total-cash == 0:
    print('Thank you visit again')
elif total-cash < 0:
    print("Your change is :" ,cash - total)
else:
    print('you need to give :', total- cash)
    
