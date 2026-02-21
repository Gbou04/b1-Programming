score = int(input("Enter your score (0-100): "))
if score >= 90:
    letter = "A"
elif score >= 80:
    letter = "B"
elif score >= 70:
    letter = "C"
elif score >= 60:
    letter = "D"
else:
    letter = "F"
print(f"your grade is {letter}")

# Encouragement for  an A
if letter == "A":
    print("Amazing job!")

# Comment for anyone with a B
elif letter == "B":
    print("Satisfactory work.")

# Comment for anything else
elif letter == "C" or letter == "D" or letter == "F":
    print("Do better.")