print("Show total payable amount")
p1 = int (input("Enter the product 1 price"))
p2 = int (input("Enter the product 2 price"))
p3 = int (input("Enter the product 3 price"))

total = p1+p2+p3
print("Total product price is:",total)

gst=total*0.18

print("GST AMount is:",gst)

tpa=total+gst
print("Total payable amount is", tpa)