from tkinter import *
from utils import calculate_grade
from pdf_generator import generate_pdf

def generate():
    try:
        name = entry_name.get()
        roll = entry_roll.get()
        sem = entry_sem.get()

        math = int(entry_math.get())
        science = int(entry_science.get())
        english = int(entry_english.get())

        total = math + science + english
        average = total / 3
        grade = calculate_grade(average)

        student = {
            "name": name,
            "roll": roll,
            "sem": sem,
            "math": math,
            "science": science,
            "english": english,
            "total": total,
            "average": average,
            "grade": grade
        }

        file = generate_pdf(student)
        result_label.config(text=f"Saved: {file}")

    except:
        result_label.config(text="Enter valid input!")

root = Tk()
root.title("PDF Report Generator")
root.geometry("350x400")

Label(root, text="Student Name").pack()
entry_name = Entry(root)
entry_name.pack()

Label(root, text="Roll No").pack()
entry_roll = Entry(root)
entry_roll.pack()

Label(root, text="Semester").pack()
entry_sem = Entry(root)
entry_sem.pack()

Label(root, text="Math Marks").pack()
entry_math = Entry(root)
entry_math.pack()

Label(root, text="Science Marks").pack()
entry_science = Entry(root)
entry_science.pack()

Label(root, text="English Marks").pack()
entry_english = Entry(root)
entry_english.pack()

Button(root, text="Generate PDF", command=generate).pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
