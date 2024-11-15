import tkinter as tk
from tkinter import messagebox
from src.database import add_expense, add_income
from src.charts import show_expense_chart
from src.exports import export_to_excel

def create_gui():
    root = tk.Tk()
    root.title('Калькулятор расходов')

    #expenses
    tk.Label(root, text="Дата (YYYY-MM-DD):").grid(row=0, column=0)
    entry_date = tk.Entry(root)
    entry_date.grid(row=0, column=1)

    tk.Label(root, text="Категория:").grid(row=1, column=0)
    entry_category = tk.Entry(root)
    entry_category.grid(row=1, column=1)

    tk.Label(root, text="Сумма:").grid(row=2, column=0)
    entry_amount = tk.Entry(root)
    entry_amount.grid(row=2, column=1)

    tk.Label(root, text="описание:").grid(row=3, column=0)
    entry_description = tk.Entry(root)
    entry_description.grid(row=3, column=1)

    def on_add_expense():
        date = entry_date.get()
        category = entry_category.get()
        amount = entry_amount.get()
        description = entry_description.get()

        if date and category and amount:
            add_expense(date, category, amount, description)
            messagebox.showinfo('Успех', "Расход добавлен")
        else:
            messagebox.showerror("Ошибка", "Заполните все поля!")
    
    tk.Button(root, text='Добавить расход', command=on_add_expense).grid(row=4, column=0, columnspan=2)

    # Доходы
    tk.Label(root, text="Источник дохода:").grid(row=5, column=0)
    entry_source = tk.Entry(root)
    entry_source.grid(row=5, column=1)

    def on_add_income():
        date = entry_date.get()
        source = entry_source.get()
        amount = entry_amount.get()
        description = entry_description.get()
        
        if date and source and amount:
            add_income(date, source, amount, description)
            messagebox.showinfo("Успех", "Доход добавлен!")
        else:
            messagebox.showerror("Ошибка", "Заполните все поля!")

    tk.Button(root, text="Добавить доход", command=on_add_income).grid(row=6, column=0, columnspan=2)

    tk.Button(root, text="Показать график расходов", command=show_expense_chart).grid(row=8, column=0, columnspan=2)

    tk.Button(root, text="Экспорт в Excel", command=export_to_excel).grid(row=9, column=0, columnspan=2)

    root.mainloop()
