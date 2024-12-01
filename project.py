import tkinter as tk
from tkinter import ttk

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())
        
        simple_interest = (principal * time * rate) / 100
        compound_interest = principal * (1 + rate / 100) ** time - principal
        
        result_label.config(text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

root = tk.Tk()
root.geometry("400x400")
root.title("Interest Calculator App")

ttk.Label(root, text="Principal:").grid(row=0, column=0, padx=10, pady=10)
principal_entry = ttk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Time (years):").grid(row=1, column=0, padx=10, pady=10)
time_entry = ttk.Entry(root)
time_entry.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(root, text="Rate of Interest (%):").grid(row=2, column=0, padx=10, pady=10)
rate_entry = ttk.Entry(root)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = ttk.Button(root, text="Calculate Interest", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
