import pandas as pd
from src.database import get_expenses_data, get_income_data

def export_to_excel():
    expenses_data = get_expenses_data()
    income_data = get_income_data()

    expenses_df = pd.DataFrame(expenses_data, columns=['id', 'date', 'category', 'amount', 'description'])
    income_df = pd.DataFrame(income_data, columns=['id', 'date', 'source', 'amount', 'description'])

    with pd.ExcelWriter('data/finance_data.xlsx') as writer:
        expenses_df.to_excel(writer, sheet_name='Расходы', index=False)
        income_df.to_excel(writer, sheet_name='Доходы', index=False)

    print("Данные экспортированы в data/finance_data.xlsx")
