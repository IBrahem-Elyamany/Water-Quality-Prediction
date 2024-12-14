## import library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import sklearn
from scipy import stats
from matplotlib.patches import Rectangle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import RandomOverSampler
from collections import Counter
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import sklearn.model_selection as model_selection
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

ds=pd.read_excel('water_potability.xlsx')

##1) Data Preprocessing

ds['ph']=ds['ph'].fillna(ds.groupby(['Potability'])['ph'].transform('mean'))
ds['Sulfate']=ds['Sulfate'].fillna(ds.groupby(['Potability'])['Sulfate'].transform('mean'))
ds['Trihalomethanes']=ds['Trihalomethanes'].fillna(ds.groupby(['Potability'])['Trihalomethanes'].transform('mean'))

num_col = (ds.columns).to_list()
num_col = num_col[0:]
def outliers(ds, column):
  Q1 = ds[column].quantile(0.25)
  Q3 = ds[column].quantile(0.75)
  IQR = Q3-Q1
  lower_bound = Q1-1.5*IQR
  upper_bound = Q3+1.5*IQR

  for i in range(len(ds)):
     if ds[column].iloc[i] > upper_bound:
        ds[column].iloc[i] = upper_bound
     if ds[column].iloc[i] < lower_bound:
          ds[column].iloc[i] = lower_bound

for feature in num_col:
    outliers(ds, feature)





y = ds['Potability']
X = ds.drop(['Potability'], axis=1)

rus =RandomOverSampler(sampling_strategy=1)
x_res, y_res = rus.fit_resample(X,y)


"""###13. Split data"""

X_train,X_test, y_train, y_test = train_test_split(x_res,y_res, test_size=0.07, random_state=10)

standard_scaler = StandardScaler()
X_train = standard_scaler.fit_transform(X_train)
X_test = standard_scaler.transform(X_test)


lr_model = LogisticRegression (solver= 'liblinear')
lr_model.fit(X_train, y_train)
y_pred_logistic = lr_model.predict (X_test)
report_logistic = classification_report (y_test,y_pred_logistic)
print('report:',report_logistic,sep='\n')
accuracy_logistic = accuracy_score(y_test, y_pred_logistic)
print("Accuracy of LogisticRegression:", accuracy_logistic)


svm_model = SVC(kernel="rbf",C=17) #c= 45 oversampling + scale
svm_model.fit(X_train, y_train)
y_pred_svm=svm_model.predict(X_test)
report_svm = classification_report (y_test, y_pred_svm)
print('report:',report_svm,sep='\n')
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print("Accuracy of SVM:", accuracy_svm)


dt_model = DecisionTreeClassifier(max_depth=4)
dt_model.fit(X_train, y_train)
y_pred_DecisionTree = dt_model.predict(X_test)
report_DecisionTree = classification_report (y_test,y_pred_DecisionTree)
print('report:',report_DecisionTree,sep='\n')
accuracy_DecisionTree = accuracy_score(y_test, y_pred_DecisionTree)
print("Accuracy of DecisionTree:", accuracy_DecisionTree)


knn_model=KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train,y_train)
y_pred_knn=knn_model.predict(X_test)
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print("Accuracy of Knn:", accuracy_knn)
report_knn=classification_report(y_test, y_pred_knn)
print(report_knn)


rf_model = RandomForestClassifier(n_estimators=100)#345 in oversampling without scale
rf_model.fit(X_train, y_train)
y_pred_RandomForest = rf_model.predict(X_test)
accuracy_RandomForest = accuracy_score(y_test, y_pred_RandomForest)
print("Accuracy of RandomForest:", accuracy_RandomForest)
report_RandomForest = classification_report (y_test,y_pred_RandomForest)
print('report:',report_RandomForest,sep='\n')

from xgboost import XGBClassifier
xgb_model = XGBClassifier(learning_rate=0.5,colsample_bytree=0.8)
xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict(X_test)
accuracy_xgb = accuracy_score(y_test, y_pred_xgb)
print("Accuracy of XGBoost:", accuracy_xgb)
report_xgb = classification_report (y_test,y_pred_xgb)
print('report:',report_RandomForest,sep='\n')

def predictModels(ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity,model):
    data=np.array([ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]).reshape(1,-1)
    data=standard_scaler.transform(data)
    if(model=="Logistic_Regression"):
        return lr_model.predict(data)
    elif(model=="SVM"):
        return svm_model.predict(data)
    elif(model=="Decision_Tree"):
        return dt_model.predict(data)
    elif(model=="Knn"):
        return knn_model.predict(data)
    elif(model== "Random_Forest"):
        return rf_model.predict(data)
    elif(model== "xgb"):
        return xgb_model.predict(data)


def accuracyModels(model):
    if (model == "Logistic_Regression"):
        return accuracy_logistic
    elif (model == "SVM"):
        return accuracy_svm
    elif (model == "Decision_Tree"):
        return accuracy_DecisionTree
    elif (model == "Knn"):
        return accuracy_knn
    elif (model == "Random_Forest"):
        return accuracy_RandomForest
    elif (model == "xgb"):
        return accuracy_xgb

def reportModels(model):
    if (model == "Logistic_Regression"):
        return report_logistic
    elif (model == "SVM"):
        return report_svm
    elif (model == "Decision_Tree"):
        return report_DecisionTree
    elif (model == "Knn"):
        return report_knn
    elif (model == "Random_Forest"):
        return report_RandomForest
    elif (model == "xgb"):
        return report_xgb