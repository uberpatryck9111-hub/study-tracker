topic = input("What did you study today? ")
minutes = input("How many minutes? ")
energy = input("Energy level (1-5)? ")

with open("study_data.csv", "a") as file:
    file.write(f"{topic},{minutes},{energy}/n")

print("Saved!")