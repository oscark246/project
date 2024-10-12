import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Expense:
    def __init__(self, description, category, amount):
        self.description = description
        self.category = category
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, category, amount):
        expense = Expense(description, category, amount)
        self.expenses.append(expense)

    def view_expenses(self):
        return self.expenses

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

class ExpenseTrackerApp:
    def __init__(self, root):
        self.tracker = ExpenseTracker()
        self.root = root
        self.root.title("Expense Tracker")

        # Description
        self.description_label = tk.Label(root, text="Description")
        self.description_label.grid(row=0, column=0)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=0, column=1)

        # Category
        self.category_label = tk.Label(root, text="Category")
        self.category_label.grid(row=1, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1)

        # Amount
        self.amount_label = tk.Label(root, text="Amount")
        self.amount_label.grid(row=2, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=2, column=1)

        # Add Button
        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=3, column=0, columnspan=2)

        # View Expenses Button
        self.view_button = tk.Button(root, text="View Expenses", command=self.view_expenses)
        self.view_button.grid(row=4, column=0, columnspan=2)

        # Total Expenses Button
        self.total_button = tk.Button(root, text="Total Expenses", command=self.show_total_expenses)
        self.total_button.grid(row=5, column=0, columnspan=2)

    def add_expense(self):
        description = self.description_entry.get()
        category = self.category_entry.get()
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number.")
            return
        self.tracker.add_expense(description, category, amount)
        messagebox.showinfo("Success", "Expense added successfully!")
        self.description_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def view_expenses(self):
        expenses = self.tracker.view_expenses()
        if not expenses:
            messagebox.showinfo("No Expenses", "No expenses to display.")
            return
        
        expenses_window = tk.Toplevel(self.root)
        expenses_window.title("Expenses")

        tree = ttk.Treeview(expenses_window, columns=("Description", "Category", "Amount"), show='headings')
        tree.heading("Description", text="Description")
        tree.heading("Category", text="Category")
        tree.heading("Amount", text="Amount")

        for expense in expenses:
            tree.insert("", tk.END, values=(expense.description, expense.category, expense.amount))

        tree.pack()

    def show_total_expenses(self):
        total = self.tracker.total_expenses()
        messagebox.showinfo("Total Expenses", f"Total expenses: {total}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
