#AGE CLASSIFIER
def classify_age(age):
    if age < 0:
        print("Age cannot be negative. Enter Again.")
    elif age <= 12:
        print("You are a child.")
    elif age <= 19:
        print("You are a Teenager.")
    elif age <= 64:
        print("You are an Adult.")
    else:
        print("You are a Senior.")