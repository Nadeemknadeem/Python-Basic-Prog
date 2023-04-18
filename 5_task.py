print("Display avg marks of a student")
Name = input("Enter you Name")
Branch = input ("Enter your Branch")
USN = int(input("Enter your USN"))
T1 = float(input("Emter test 1 marks"))
T2 = float(input("Emter test 2 marks"))
T3= float(input("Emter test 3 marks"))
avg = (T1+T2+T3)/3
print("Mr/Ms.{0} From {1} with SID:{2} has scored {3} average marks in python".format(Name,Branch,USN,avg))