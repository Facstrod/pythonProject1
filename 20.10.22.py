# Скрипт Class_kNN_make_blobs.py
# Классификация методом К ближайших соседей
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
import mglearn
from sklearn.datasets import make_blobs
plt.show()
# Генерация исходных данных: используется функция make_blobs
centers=4
X, y = make_blobs(n_samples=100,
 centers=centers,
 n_features=2,
 cluster_std=1.5,
 center_box=(-5.0, 10.0),
 random_state=10)
X1=X[:,0];
X2=X[:,1];
# Визуализация данных
# Массив паттернов
fig, ax0 = plt.subplots()
plt.title('Исходные данные')
ax0.scatter(X1, X2)
plt.xlabel("Первый признак")
plt.ylabel("Второй признак")
fig1, ax1 = plt.subplots()
plt.title('Классы')
plt.xlabel("Первый признак")
plt.ylabel("Второй признак")
mglearn.discrete_scatter(X1, X2, y)
plt.legend(["Класс 0", "Класс 1","Класс 2","Класс 3"], loc='best')
# разделим данные на обучающий и тестовый наборы
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=12)
from sklearn.neighbors import KNeighborsClassifier
random_state=0
clf=KNeighborsClassifier(algorithm='auto',
 # leaf_size=30,
 # metric='minkowski',
 # metric_params=None,
 # n_jobs=1,
 n_neighbors=4,
 # p=2,
 weights='uniform')
clf.fit(X_train, y_train)
# Правильность на обучающем наборе
print("Правильность на обучающем наборе: %.2f" % clf.score(X_train, y_train))
# Правильность на тестовом наборе
print("Правильность на тестовом наборе: {:.2f}".format(clf.score(X_test, y_test)))

# Граница класса
fig, axes1 = plt.subplots()
ax=axes1
mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.5)
mglearn.discrete_scatter(X1, X2, y, ax=axes1)
plt.xlabel("Признак 0")
plt.ylabel("Признак 1")
plt.legend(['0 класс', '1 класс','2 класс'])
ax.legend(loc='best')
plt.show()