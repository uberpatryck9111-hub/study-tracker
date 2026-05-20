topic = input("What did you study today? ")
minutes = input("How many minutes? ")

with open("study_data.csv", "a") as file:
    file.write(f"{topic},{minutes}/n")

print("Saved!")