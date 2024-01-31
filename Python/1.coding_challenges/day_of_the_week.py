day = input("Enter the day of the week: ")
time = input("Enter the time of day right now:")
# print(day)
# if day == "Monday":

#     print("Make sure you write down your goals for the week")
# elif day == "Tuesday":
#     print("How's  your Tuesday going?")
# else:
#     print("Please input the day of the week.")

# print(day)
day = int(day)
time = int(time)
days = {
    "Monday" : 1,
    "Tuesday" : 2,
    "Wednesday" : 3,
    "Thursday" : 4,
    "Friday" : 5,
    "Saturday" : 6,
    "Sunday" : 7
}
if day >= 6:
    print("Non-working day")
elif day == 5:
    print("Almost the weekend")
else:
    print ("Working day")
print("Good morning!")