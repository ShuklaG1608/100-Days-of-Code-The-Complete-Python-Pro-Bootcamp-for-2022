print("Welcome to the tip calculator!")
bill = float((input("What was the total bill? $")))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
count = int(input("How many people to split the bill? "))
if tip == 10:
  total_bill = bill + bill * 0.10
elif tip == 12:
  total_bill = bill + bill * 0.12
elif tip == 15:
  total_bill = bill + bill * 0.15
pay = total_bill / count
final = round(pay,2)
print(f"Each person should pay: ${final}")
