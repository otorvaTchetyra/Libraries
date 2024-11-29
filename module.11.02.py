import pandas as pd

# Считываем данные из CSV файла
df = pd.read_csv('D:\\PythonProjects\\libraries\\Libraries\\data.csv')

# Выводим первые 5 строк данных
print(df.head())

# Выполняем простой анализ: среднее значение по определенному столбцу
mean_value = df['column_name'].mean()
print(f'Среднее значение: {mean_value}')

# Фильтруем данные
filtered_df = df[df['column_name'] > 10]
print(filtered_df)
