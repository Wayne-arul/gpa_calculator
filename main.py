import tkinter as tk
from tkinter import ttk, messagebox


def calculate_credit_points(grade):
    if grade == "O":
        return 10
    elif grade == "A+":
        return 9
    elif grade == "A":
        return 8
    elif grade == "B+":
        return 7
    elif grade == "B":
        return 6
    else:
        return 0


def calculate_gpa():
    sum_credit_points = 0
    sum_credits = 0

    for i in range(num_subjects.get()):
        grade = grade_entries[i].get().upper()
        credits = float(credit_entries[i].get())

        credit_points = calculate_credit_points(grade)
        subject_credit_points = credit_points * credits

        sum_credit_points += subject_credit_points
        sum_credits += credits

    if sum_credits > 0:
        gpa = sum_credit_points / sum_credits
        result_label.config(text=f"\nTotal GPA: {gpa:.2f}")

        messagebox.showinfo("Total GPA", f"Total GPA: {gpa:.2f}")
    else:
        result_label.config(text="No credits entered. Cannot calculate GPA.")

        messagebox.showinfo("Total GPA", "No credits entered. Cannot calculate GPA.")

    total_gpa_label.grid(
        row=calculate_button.grid_info()["row"] + 1,
        column=calculate_button.grid_info()["column"],
    )

    for entry in grade_entries + credit_entries:
        entry.destroy()

    enter_button.grid_forget()


def create_subject_entries():
    num_subjects_value = num_subjects.get()

    for entry in grade_entries + credit_entries:
        entry.destroy()

    for i in range(num_subjects_value):
        ttk.Label(root, text=f"Subject {i+1} Grade:").grid(
            row=i + 1, column=0, padx=10, pady=5
        )
        grade_var = tk.StringVar()
        grade_entry = ttk.Entry(root, textvariable=grade_var)
        grade_entry.grid(row=i + 1, column=1, padx=10, pady=5)
        grade_entries.append(grade_var)

        ttk.Label(root, text=f"Subject {i+1} Credits:").grid(
            row=i + 1, column=2, padx=10, pady=5
        )
        credit_var = tk.StringVar()
        credit_entry = ttk.Entry(root, textvariable=credit_var)
        credit_entry.grid(row=i + 1, column=3, padx=10, pady=5)
        credit_entries.append(credit_var)


root = tk.Tk()
root.title("GPA Calculator by Wayne")

num_subjects_label = ttk.Label(root, text="Enter the number of subjects:")
num_subjects_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
num_subjects = tk.IntVar()
num_subjects_entry = ttk.Entry(root, textvariable=num_subjects)
num_subjects_entry.grid(row=0, column=2, padx=10, pady=10)

enter_button = ttk.Button(root, text="Enter", command=create_subject_entries)
enter_button.grid(row=0, column=3, padx=10, pady=10)

grade_entries = []
credit_entries = []

calculate_button = ttk.Button(root, text="Calculate GPA", command=calculate_gpa)
calculate_button.grid(row=0, column=4, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=1, column=0, columnspan=5, pady=10)

total_gpa_label = ttk.Label(root, text="Total GPA:")

root.mainloop()
