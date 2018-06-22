import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn import model_selection
import seaborn as sns
from sklearn.linear_model import LinearRegression
# import statsmodels.api as sm

sns.set_style("whitegrid")
sns.set_context("poster")

# special matplotlib argument for improved plots
from sklearn.datasets import load_boston
boston = load_boston()
print("*************** Keys *****************")
print(boston.keys())
print("*************** Shape ****************")
print(boston.data.shape)
print("************* Features ***************")
print(boston.feature_names)
print("************* Description ************")
print(boston.DESCR)
bos = pd.DataFrame(boston.data)
print("************* HEAD *******************")
print(bos.head())
print("************Columns ******************")
bos.columns = boston.feature_names
print(bos.head())
print(boston.target.shape)
bos['PRICE'] = boston.target
print(bos.head())
print(bos.describe())
X = bos.drop('PRICE', axis = 1)
Y = bos['PRICE']

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size = 0.33, random_state = 5)
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)


lm = LinearRegression()
lm.fit(X_train, Y_train)

Y_pred = lm.predict(X_test)
plt.plot(Y_test, 'ro')
plt.plot(Y_pred, 'bo')
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices: $Y_i$ vs $\hat{Y}_i$")
plt.show()
