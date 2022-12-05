import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import neighbors
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

option = 2
data_csv = 'inputs/data.csv' if option == 1 else 'inputs/data-2.csv'

df = pd.read_csv(data_csv)
features_np = df.columns.values
print(features_np)
features_np = np.delete(features_np, -1)
print(features_np)

y = df['Label']                   # 變出 y 資料
x = df.drop(['Label'], axis=1)
print(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# algorithm{‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}, default=’auto’
model = neighbors.KNeighborsClassifier(n_neighbors=5, algorithm='kd_tree')
model.fit(x_train, y_train)

print(model.score(x_test, y_test))
print(model.classes_)

y_prediction = model.predict(x_test)
print(classification_report(y_test, y_prediction))

confmat = confusion_matrix(y_true=y_test, y_pred=y_prediction)
fig, ax = plt.subplots(figsize=(2.5, 2.5))
ax.matshow(confmat, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confmat.shape[0]):
    for j in range(confmat.shape[1]):
        ax.text(x=j, y=i, s=confmat[i, j], va='center', ha='center')
plt.xlabel('predicted label')
plt.ylabel('true label')
plt.show()
