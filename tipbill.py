print("Welcome to Tip Calculator")

total_bill= float(input("What is your total bill: "))
total_member=input("How many people are there: ")
tip=int(input("How much % would you tip 10, 12 or 15: "))

tip_bill= float(tip/100*total_bill+total_bill)
split_bill=tip_bill/int(total_member)
final_bill=round(split_bill, 2)
print((f"Your total bill per person is {final_bill}"))

