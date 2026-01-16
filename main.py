print("Welcome to Study Load Optimizer")

name = input("What is your name? ")
print("Hello", name)

subjects = int(input("How many subjects do you have? "))

hours_per_day = float(input("How many hours do you need/intend to study in a day?? "))

days_left = int(input("Number of days left for the exam "))

total_hours = hours_per_day * days_left

print("\nSummary")
print("You have",subjects,"subjects" )
print("you need to study",round(total_hours,2),"hours" )
hours_per_subject = total_hours / subjects
print("\nOptimised plan")
print("the total hours per subject would be", round(hours_per_subject,2), "hours")

subject_names = []

for i in range(subjects):
    subject = input(f"Enter name of subject {i + 1}: ")
    subject_names.append(subject)

subject_weights = {}

print("\nNow assign importance (weightage) to each subject.")
print("Use numbers like 1 (low) to 5 (high).\n")

for subject in subject_names:
    weight = int(input(f"Enter importance for {subject} (1–5): "))
    subject_weights[subject] = weight
print("\nSubject weightages:")
print(subject_weights)
total_weight = sum(subject_weights.values())
print("/nFInal Optimised Study Plan")
for subjects, weight in subject_weights.items():
    fraction = weight / total_weight
    subject_hours = fraction * total_hours
    print(subjects, ":", round(subject_hours,2), "hours")
    
print("\nDAILY STUDY PLAN (PER DAY)\n")

daily_total = 0

for subject, weight in subject_weights.items():
    daily_hours = (weight / total_weight) * hours_per_day
    daily_hours = round(daily_hours, 2)
    daily_total += daily_hours
    print(subject, ":", daily_hours, "hours/day")

print("\nTotal study time per day:", round(daily_total, 2), "hours")
print("Study duration:", days_left, "days")