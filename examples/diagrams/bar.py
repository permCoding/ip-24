import matplotlib.pyplot as plt

categories = list('ABCDEF')
values = [2,4,5,8,4.1,5]

plt.figure(figsize=(8,6))
plt.bar(categories, values, color='purple', alpha=0.7)
plt.title('столбч диагр', fontsize=16)
plt.xlabel('категории', fontsize=14)
plt.ylabel('значения', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
