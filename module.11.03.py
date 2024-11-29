import matplotlib.pyplot as plt

# Пример данных
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Создаем линейный график
plt.plot(x, y, marker='o')
plt.title('Пример линейного графика')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig('plot.png')  # Сохраняем график
plt.show()  # Отображаем график
