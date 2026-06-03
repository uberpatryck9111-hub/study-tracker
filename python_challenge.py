students = {
    "Alice":   [92, 88, 95, 91],
    "Bob":     [72, 65, 70, 68],
    "Carlos":  [55, 60, 58, 52],
    "Diana":   [88, 91, 85, 90],
    "Eve":     [40, 55, 48, 60],
}

def get_average(scores):
    return sum(scores) / len(scores)

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def print_report():
    for name, scores in students.items():
        avg = get_average(scores)
        grade = get_grade(avg)
        print(name + " | Average: " + str(round(avg, 2)) + " | Grade: " + grade)

def top_student():
    best_name = ""
    best_avg = 0
    for name, scores in students.items():
        avg = get_average(scores)
        if avg > best_avg:
            best_avg = avg
            best_name = name
    print("Top student: " + best_name + " with " + str(round(best_avg, 2)))

def count_passed():
    count = 0
    for name, scores in students.items():
        if get_average(scores) >= 60:
            count = count + 1
    print("Students passed: " + str(count))

if __name__ == "__main__":
    print_report()
    print()
    top_student()
    count_passed()