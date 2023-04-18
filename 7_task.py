name=input("Enter your Name")
place = input("Enter your place")
fare = ('fare:10rs/KM')
print(fare)
km= float(input("Enter the number of KMs you need to travel \n "))
amount = km * 10
print("Amount:",amount)

tpa = amount * 0.10
print("GST AMount is 10%:",tpa)
print('Total payable amount:',amount + tpa)