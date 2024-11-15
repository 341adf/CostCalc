import matplotlib.pyplot as plt
from src.database import get_expenses_by_category

def show_expense_chart():
    data = get_expenses_by_category()

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(10, 5))
    plt.bar(categories, amounts)
    plt.xlabel('Категории')
    plt.ylabel('Сумма')
    plt.title('расходы по категориям')
    plt.show()