N = int(input("Please Enter any Number: "))
Sum = 0

while(N > 0):
    Reminder = N % 10
    Sum = Sum + Reminder
    N = N //10

print("\n Sum of the digits of Given Number = %d" %Sum)
