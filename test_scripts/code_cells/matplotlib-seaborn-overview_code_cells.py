# checking python version
! python -V

# importing packages 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

%matplotlib inline
# plt.style.use('seaborn-whitegrid')
plt.style.use('seaborn-white')       

# displaying figure and axes
fig = plt.figure()
ax = plt.axes()

# another way to display them
fig, ax = plt.subplots()  

# defining x values
x = np.linspace(0, 10, 100)
x

# taking cosine and sine of x
y1, y2 = np.cos(x), np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y1)
ax.plot(x, y2)

# using "show" called on plt
y1, y2 = np.cos(x), np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y1)
ax.plot(x, y2)
plt.show()

# stacking graphs vertically (defining 2 rows for plot)
fig, axes = plt.subplots(2)
axes[0].plot(x, y1)
axes[1].plot(x, y2)
plt.show()

# stacking graphs horizontally (1 row, 2 columns, and change figure size)
fig, axes = plt.subplots(1,2, figsize=(22,4))
axes[0].plot(x, y1)
axes[1].plot(x, y2, color = 'orange')
plt.show()

# defining random values
x = np.random.rand(30)
y = np.random.rand(30)
x, y

# plotting a scatter plot
# "s" is marker size in points, "alpha" is intensity of the marker 0 for transparent and 1 for opaque
plt.scatter(x, y, marker='o', color = 'red', s = 200, alpha=.4)
plt.title("scatter plot")
plt.show()

# changin "s" and "alpha" values
plt.scatter(x, y, marker='o', color = 'red', s = 100, alpha=.2)
plt.title("scatter plot")
plt.show()

# reading iris data
iris_data = pd.read_csv("./data/iris.csv", 
                        names = ["sepal_l", "sepal_w", "petal_l", "petal_w", "class"])

# transforming categorical 'class' to integers
iris_data['class'] = iris_data['class'].map({"Iris-setosa":0, 
                                             'Iris-versicolor':1,
                                             'Iris-virginica': 2})
iris_data.head(2)

# plotting a scatter plot using cmap - Colormap magma
plt.scatter(iris_data['sepal_l'], 
            iris_data['sepal_w'], 
            alpha=0.8,
            s=200, 
            c=iris_data['class'], 
            cmap='magma')

plt.xlabel('sepal_l')
plt.ylabel("sepal_w")
plt.title("Sepal Length v/s Sepal Width")
plt.show()

# plotting another scatter plot
fig, ax = plt.subplots(figsize = (12, 8))
ax.scatter(iris_data['sepal_l'], 
           iris_data['sepal_w'], 
           alpha=.7,
           s = 200, 
           c = iris_data["class"],  
           cmap='cividis')

# using more convenient way of setting properties
ax.set(title="Iris Data", xlabel='sepal_l', ylabel="sepal_w")
plt.show()

# defining multiple scatter plots and provide legend
fig, ax = plt.subplots(figsize = (12, 8))
ax.scatter(iris_data.loc[:49, 'sepal_l'], 
           iris_data.loc[:49,'sepal_w'],
           s = 200, 
           c = 'r', 
           alpha=.5, 
           label='Iris-setosa')

ax.scatter(iris_data.loc[49:99, 'sepal_l'], 
           iris_data.loc[49:99,'sepal_w'], 
           s = 200, 
           c = 'blue', 
           alpha=.5, 
           label='Iris-versicolor')

ax.scatter(iris_data.loc[99:, 'sepal_l'], 
           iris_data.loc[99:,'sepal_w'],
           s = 200, 
           c = 'green', 
           alpha=.5, 
           label='Iris-virginica')

# setting properties
ax.set(title="Iris Data", xlabel='sepal_l', ylabel="sepal_w")
ax.legend()
plt.show()

# creating a histogram
fig, ax = plt.subplots()
ax.hist(iris_data['sepal_l'], color = 'lightgreen', edgecolor='black')
ax.set_title("Histogram of Sepal Length")
ax.set_xlabel("Length (cms)")
ax.set_ylabel("Count")
plt.show()

# checking columns
iris_data.columns

# plotting histogram for each column and provide legend
fig, ax = plt.subplots(figsize = ((12, 8)))
ax.hist(iris_data['sepal_l'], alpha=.5, edgecolor='black')
ax.hist(iris_data['sepal_w'], alpha=.5, edgecolor='black')
ax.hist(iris_data['petal_l'], alpha=.5, edgecolor='black')
ax.hist(iris_data['petal_w'], alpha=.5, edgecolor='black')
ax.legend(['sepal_l', 'sepal_w', 'petal_l', 'petal_w'])
ax.set_xlabel("Length (cms)")
ax.set_ylabel("Count")
plt.show()

# pair plotting
features = ["sepal_l", "sepal_w", "petal_l", "petal_w"]
pair_plot = pd.plotting.scatter_matrix(iris_data[features], figsize=(12, 8))

# using seaborn library
pair_plot = sns.pairplot(iris_data, hue='class')

# transform integers back to categorical, set the style to dark and change the diagonal plots
sns.set(style = "dark")
iris_data['class'] = iris_data['class'].map({0:"Iris-setosa", 
                                             1:'Iris-versicolor', 
                                             2:'Iris-virginica'})
pair_plot = sns.pairplot(iris_data, hue='class', diag_kind = 'hist')

# creating correlation
corr = iris_data.corr()
corr

# plotting correlation
f, ax = plt.subplots(figsize=(11, 9))
sns.heatmap(corr, annot=True)
plt.show()

# plotting correwlation 
sns.set(font_scale=1.4)
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, 
            cmap=cmap, 
            vmax=.3, 
            center=0,
            square=True, 
            linewidths=.5, 
            cbar_kws={"shrink": .5}, 
            annot = True)
plt.show()



