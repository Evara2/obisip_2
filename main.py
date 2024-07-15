import datetime
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Age and BMI Calculator")
window.geometry("600x400")
window.resizable(False, False)  # Disable window resizing
window.configure(bg='#f0f0f0')  # Set the background color to a light gray

# Add some styling
style = ttk.Style()
style.theme_use('clam')  # Set the theme to 'clam'
style.configure('TNotebook.Tab', background='#4285F4', foreground='white')  # Set the tab color to blue
style.map('TNotebook.Tab', background=[('selected', '#2F6FED')])  # Set the selected tab color to a darker blue
style.configure('TEntry', fieldbackground='#E8F0FE')  # Set the form field background color to a light blue

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True)

# Create the Age Calculator tab
age_tab = ttk.Frame(notebook)
notebook.add(age_tab, text='Age Calculator')

name_label = ttk.Label(age_tab, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
name_entry = ttk.Entry(age_tab)
name_entry.grid(row=0, column=1, padx=10, pady=5)

year_label = ttk.Label(age_tab, text="Year:")
year_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
year_entry = ttk.Entry(age_tab)
year_entry.grid(row=1, column=1, padx=10, pady=5)

month_label = ttk.Label(age_tab, text="Month:")
month_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
month_entry = ttk.Entry(age_tab)
month_entry.grid(row=2, column=1, padx=10, pady=5)

date_label = ttk.Label(age_tab, text="Day:")
date_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
date_entry = ttk.Entry(age_tab)
date_entry.grid(row=3, column=1, padx=10, pady=5)

age_result_text = tk.Text(age_tab, height=5, width=40)
age_result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def get_age():
    name = name_entry.get()
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())
        day = int(date_entry.get())
        birthdate = datetime.date(year, month, day)
        today = datetime.date.today()
        age = today.year - birthdate.year
        if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
            age -= 1
        age_result_text.delete('1.0', tk.END)
        answer = f"Hey {name}, you are {age} years old!"
        age_result_text.insert(tk.END, answer)
    except ValueError as e:
        age_result_text.delete('1.0', tk.END)
        age_result_text.insert(tk.END, f"Invalid input: {str(e)}. Please try again.")
    except Exception as e:
        age_result_text.delete('1.0', tk.END)
        age_result_text.insert(tk.END, f"An error occurred: {str(e)}. Please try again.")

calculate_age_button = ttk.Button(age_tab, text="Calculate Age", command=get_age)
calculate_age_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Create the BMI Calculator tab
bmi_tab = ttk.Frame(notebook)
notebook.add(bmi_tab, text='BMI Calculator')

name_label = ttk.Label(bmi_tab, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
name_entry = ttk.Entry(bmi_tab)
name_entry.grid(row=0, column=1, padx=10, pady=5)

gender_label = ttk.Label(bmi_tab, text="Gender:")
gender_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')
gender_entry = ttk.Combobox(bmi_tab, values=['Male', 'Female'])
gender_entry.grid(row=1, column=1, padx=10, pady=5)

height_label = ttk.Label(bmi_tab, text="Height (cm):")
height_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
height_entry = ttk.Entry(bmi_tab)
height_entry.grid(row=2, column=1, padx=10, pady=5)

weight_label = ttk.Label(bmi_tab, text="Weight (kg):")
weight_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')
weight_entry = ttk.Entry(bmi_tab)
weight_entry.grid(row=3, column=1, padx=10, pady=5)

bmi_result_text = tk.Text(bmi_tab, height=5, width=40)
bmi_result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def get_bmi():
    name = name_entry.get()
    height = height_entry.get()
    weight = weight_entry.get()
    gender = gender_entry.get().lower()

    if not height or not weight:
        bmi_result_text.delete('1.0', tk.END)
        bmi_result_text.insert(tk.END, "Please enter height and weight.")
        return

    try:
        height = float(height)
        weight = float(weight)
    except ValueError:
        bmi_result_text.delete('1.0', tk.END)
        bmi_result_text.insert(tk.END, "Invalid height or weight entered. Please try again.")
        return

    if gender == "male":
        bmi_long = weight / (height / 100) ** 2
    elif gender == "female":
        bmi_long = weight / (height / 100) ** 2 * 0.9
    else:
        bmi_result_text.delete('1.0', tk.END)
        bmi_result_text.insert(tk.END, "Please select a valid gender.")
        return

    bmi_short = round(bmi_long, 2)
    bmi_result_text.delete('1.0', tk.END)

    if bmi_short < 18.5:
        message = "You are underweight."
    elif bmi_short >= 18.5 and bmi_short < 25:
        message = "Your weight is normal."
    elif bmi_short >= 25 and bmi_short < 30:
        message = "You are overweight."
    else:
        if gender == "male":
            message = "You are obese."
        else:
            message = "You are obese." if bmi_short >= 30 else "You are overweight."

    ANSWER = f"Hey {name}, your Body Mass Index value is {bmi_short}. {message}"
    bmi_result_text.insert(tk.END, ANSWER)

calculate_bmi_button = ttk.Button(bmi_tab, text="Calculate BMI", command=get_bmi)
calculate_bmi_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()