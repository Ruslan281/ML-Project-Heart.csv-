# -*- coding: utf-8 -*-
"""Heart(Ruslan Huseynov).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RZPIdZCDobRXXSOnMXYPMI4PzHHxDnbN

**Datanın sütunları haqqında məlumat**

1.   Age - yaş
2.   sex - cinsiyyət
3.   cp  - sinə ağrılarının növləri
4.   trestbps - qan təyziqi
5.   chol  - serum xolestrat
6.   fbs  - qan şəkərinin dəyəri
7.   restecg   - elektrokardioqrafik nəticələr
8.   thalach   - max ürək dərəcəsi
9.   exangh  - angina
10.  oldpeak   - depressiya
11.  slope  - məşq seqmentinin yamacı
12.  ca  - flourosopy ilə rənglənmiş damar sayı
12.  thal  - qüsur

# **Exploratory Data Analysis**
"""

import pandas as pd
data = pd.read_csv('/content/drive/MyDrive/Csv/heart.csv') # Pandasın read_csv funksiyası ilə datasetimizi import edirik

data.head() # head() funksiyası ilə Datanın ilk 5 sütununu görüntüləyirik (head() funksiyasına əlavə dəyər verərək istənilən sayda datanı çağıra bilərik)

data.tail()  # tail() funksiyası ilə Datanın son 5 sütununu görüntüləyirik (tail() funksiyasına əlavə dəyər verərək istənilən sayda sondan başa doğru datanı çağıra bilərik)

data.shape # Shape funksiyası ilə datamızın sətir və sütun sayı haqqında məlumat əldə edə bilərik  (datamızda 1025 sətir və 14 sütun vardır)

data.dtypes  # dtypes() funksiyası datamızın sütunlarının tipləri haqqında bizə məlumat verir
# Outputdan göründüyü kimi datamızı int64 və float64 data tipi əhatə edir

data.info()  # Info() funskiyası ilə datamızın yenə tipləri haqqında null dəyərlərin olub olmamağı haqqında,  datanın yaddaşı haqqında məlumat əldə edirik
# Data 112.2 kb həcm yer tutur
# int64 tipinə 13 ədəd , float64 tipinə isə 1 ədəd column aiddir
# Outputdan göründüyü kimi null dəyərlərimiz yoxdur

data.isna().sum()
# Hər ehtimala qarşı datamızda yenidən null dəyərləri kontrol etdik
# Outputdan görünürki datamızda null dəyər yoxdur

dataframe = pd.DataFrame(data)
duplicate = dataframe[dataframe.duplicated()]
duplicate
# Datada təkrarlanan dəyərlərin kontrol edilməsi
# Datada 723 sətrimiz təkrarlanır

data.describe()
# Describe() funksiyası ilə datanın statistik məlumatlarını əldə edirik
# Statistik məlumatlara datanın sayı,mean,std,IQR,MIN,MAX məlumatları daxildir

import matplotlib.pyplot as plt
f = plt.figure(figsize=(12, 10))
plt.matshow(data.corr(), fignum=f.number)
plt.xticks(range(data.select_dtypes(['number']).shape[1]), data.select_dtypes(['number']).columns, fontsize=14, rotation=45)
plt.yticks(range(data.select_dtypes(['number']).shape[1]), data.select_dtypes(['number']).columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=16);

# Datanın correlation münasibətlərinin vizuallaşdırılması

data.sex.value_counts()
# Datamızda cinsiyyət sütununda 1 rəqəmlərini kişi ilə 0 rəqəmləri isə qadınla əvəz etsək
# datamızda 713 kişi və 312 qadın vardır

import seaborn as sns   # Vizuallaşdırma kitabxanası
sns.barplot(x="sex", y="target", data=data[:50]); # Cinsiyyət (sex) sütununun Hədəf (target) sütunundan aslılıq qrafiki

for i, col in enumerate(data.columns):
  plt.figure(i)
  sns.kdeplot(data[col], shade=True); # Datanın sütunlarının saçılması(distribution) qrafiki

data.cp.value_counts()
# 4 növ sinə ağrısı tipi var
# 1-ci növ sinə ağrısı olan xəstələrin sayı - 497 eded
# 2-ci növ sinə ağrısı olan xəstələrin sayı - 167 eded
# 3-cü növ sinə ağrısı olan xəstələrin sayı - 284 eded
# 4-cü növ sinə ağrısı olan xəstələrin sayı - 77 eded

# Ayrıca olaraq sinə ağrılarının saçılma (distribution) qrafikini vizuallasdıraq
sns.kdeplot(data['cp'], shade=True);
# Vizuallaşdırmadan da görünür ki, 1ci növ sinə ağrılarının sayı digərlərindən daha çoxdur

sns.displot(data, x="cp",bins=10);
# Bu vizuallaşdırma ilə də görürüki 1ci növ sinə ağrılarının sayı digərlərindən çoxdur

# Datanın hədəf(target) sütununa görə sinə ağrılarının aslılıq qrafikini vizuallaşdıraq
sns.barplot(x="cp", y="target", data=data[:100]);  # data=data[:100] ifadəsi datadan 100 ədəd nümunə vizuallaşdırırıq

# Datanın hədəf(target) sütununa göre datanın qan şəkərinin(fbs) dəyərinin aslılıq qrafikini vizuallaşdıraq
sns.barplot(x="fbs", y="target", data=data[:100]);

# Datada qan təyziqinin(trestbps) saçılması(distribution) qrafikini vizuallaşdıraq
sns.kdeplot(data['trestbps'], shade=True);

sns.displot(data, x="trestbps",bins=10);  # Qan təyziqinin hər dəyərdən neçə ədəd olduğunu aydınlaşdırmaq üçün onun qrafikini vizuallaşdıraq

# Qan təyziqinin dəyərlərinin  Cinsiyyət sütunundan aslılıq qrafikini vuzallaşdıraq
sns.barplot(x="trestbps", y="sex", data=data[:15]);

# Datada xolestrat(chol) dəyərlərinin saçılması(distribution) qrafikini vizuallaşdıraq
sns.kdeplot(data['chol'], shade=True);

data['chol'].value_counts() # Xolestrat swtununda hansı dəyərlərin olduğunu kontrol edirik

sns.displot(data, x="age",bins=5);  # Yaş sütununda hər dəyərdən neçə ədəd olduğunu aydınlaşdırmaq üçün onun qrafikini vizuallaşdıraq

sns.set()
sns.pairplot(data[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target']])  # Datanın bütün sütunlarının pairplot qrafikini vizuallaşdıraq

# Sinə ağrılarının dərəcələrinə görə yaş qruplarının siyahılarının qrafikini vizuallaşdiraq
# 1-ci dərəcəli sinə ağrılarına görə yaş qruplarının siyahısı
plt.figure(figsize=(22, 10));
age_critical_cp=[];
index_critical_cp=[] ;
for i in range(len(data)-1):
    if data.cp[i]==0:
             index_critical_cp.append(i);
             age_critical_cp.append(data.age[i]);
sns.countplot(age_critical_cp);
plt.xlabel('Age');
plt.title('1-ci dərəcəli sinə ağrılarına görə yaş qruplarının siyahısı');

# 2-ci dərəcəli sinə ağrılarına görə yaş qruplarının siyahısı
plt.figure(figsize=(22, 10));
age_critical_cp=[];
index_critical_cp=[] ;
for i in range(len(data)-1):
    if data.cp[i]==1:
             index_critical_cp.append(i);
             age_critical_cp.append(data.age[i]);
sns.countplot(age_critical_cp);
plt.xlabel('Age');
plt.title('2-ci dərəcəli sinə ağrılarına görə yaş qruplarının siyahısı');

# 3-cü dərəcəli sinə ağrılarına görə yaş qruplarının siyahısı
plt.figure(figsize=(22, 10));
age_critical_cp=[];
index_critical_cp=[] ;
for i in range(len(data)-1):
    if data.cp[i]==2:
             index_critical_cp.append(i);
             age_critical_cp.append(data.age[i]);
sns.countplot(age_critical_cp);
plt.xlabel('Age');
plt.title('3-cü dərəcəli sinə ağrılarına görə yaş qruplarının siyahısı');

# 4-cü dərəcəli sinə ağrılarına görə yaş qruplarının siyahısı
plt.figure(figsize=(22, 10));
age_critical_cp=[];
index_critical_cp=[] ;
for i in range(len(data)-1):
    if data.cp[i]==3:
             index_critical_cp.append(i);
             age_critical_cp.append(data.age[i]);
sns.countplot(age_critical_cp);
plt.xlabel('Age');
plt.title('4-cü dərəcəli sinə ağrılarına görə yaş qruplarının siyahısı');

# Datamızda olan kənar göstəricilərin(outlayer) violinplot ilə vizuallaşdırılması
for i, num in enumerate(data.columns):
  plt.figure(i);
  plt.figure(figsize=(24,20));
  plt.subplot(4, 2, 2);
  sns.violinplot(data[num], orient='vertical', color='magenta');

# Datanın depressiya(oldpeak) sütununun yaş(age) sütunundan aslılıq qrafikini vizuallaşdıraq
sns.barplot(x="oldpeak", y="age", data=data[:15]);

data.head() # Dataya ümumi baxış keçirək

sns.distplot(data['target']);  # Hədəf(target) dəyişəninin yayılım qrafikinin vizuallaşdırılması
plt.show();

sns.lineplot(x='age',y = 'oldpeak',data = data[:1000]);
# Yaş aralığının depresiyyadan aslılıq qrafikini vizuallaşdıraq

sns.lineplot(x='age',y = 'cp',data = data[:50]);
# Yaş aralığının sinə ağrılarından aslılıq qrafiki

sns.relplot(x="age", y="trestbps",hue="age", data=data[:1000], kind="scatter");
# Qan təyziqi sütununun yaş sütununa görə saçılma qrafikini vizuallaşdıraq

sns.pairplot(data, hue='cp', height=2.5);

# Datamızda Feature Distribution - ların Normal Distribution - dan nə qədər uzaqlıqda və yaxınlıqda olduğunu qrafik olaraq vizuallaşdıraq (QQ plot)
import scipy.stats as stats
for i, feature in enumerate(data.columns):
  plt.figure(i)
  plt.figure(figsize=(24,20))
  plt.subplot(4, 2, 2)
  plt.title(feature)
  fig = stats.probplot(data[feature], dist="norm", plot=plt)

# Təkrarlanan dəyərləri cixaraq
duplicate = data[data.duplicated()]
duplicate.shape
# 14 Sütun üzrə 723 təkrarlanan dəyərin olduğunu görürük

# Datasetimizdə kənar göstəriciləri(outlayer) vizuallaşdıraraq kontrol edək
for i, outlayer in enumerate(data.columns):
  plt.figure(i)
  plt.figure(figsize=(24,20))
  plt.subplot(4, 2, 2)
  fig = data.boxplot(column=outlayer)
  fig.set_title('')
  fig.set_ylabel(outlayer)

# Vizuallaşdırmadan görürük ki, aşağıdakı sütunlarda outlayerlerimiz var
# 1) trestbps  - qan təyziqi
# 2) chol  - serum xolestrat
# 3) fbs - qan şəkərinin dəyəri
# 4) thalach - maksimum ürək döyüntüləri
# 5) oldpeak - depressiya
# 6) ca  - floursopy ilə rənglənmiş damar sayı
# 7) thal  - qüsur

# Outlayerlərimizin silinməsi
import numpy as np
Q1 = np.percentile(data['trestbps'], 25,
                   interpolation = 'midpoint')

Q3 = np.percentile(data['trestbps'], 75,
                   interpolation = 'midpoint')

IQR = Q3 - Q1
upper = np.where(data['trestbps'] >= (Q3+1.5*IQR))
lower = np.where(data['trestbps'] <= (Q1-1.5*IQR))
data.drop(upper[0], inplace = True)
data.drop(lower[0], inplace = True)

data.boxplot(column='trestbps')
# Vizuallaşdırma vasitəsiylə görürük ki, trestbps sütunuda outlayerlerimiz qalmayıb

# Chol sütunun outlayerlerinin təmizlənməsi
import numpy as np
for x in ['chol']:
    q75,q25 = np.percentile(data.loc[:,x],[75,25])
    intr_qr = q75-q25
 
    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)
 
    data.loc[data[x] < min,x] = np.nan
    data.loc[data[x] > max,x] = np.nan

data.boxplot(column='chol') # Vizuallaşdırmadan görürük ki, outlayer qalmayıb

data.isnull().sum() # Chol sütununda outlayer olan dəyərləri yuxarıdakı kod vaasitəsiylə null dəyərlərlə əvəz etdik

data = data.dropna(axis = 0) # Əvəz etdiyimiz null dəyərləri silirik

data.isnull().sum() # Yenidən kontrol etdikdə null dəyərlər təmizlənmişdir

import numpy as np
for x in ['fbs']:
    q75,q25 = np.percentile(data.loc[:,x],[75,25])
    intr_qr = q75-q25
 
    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)
 
    data.loc[data[x] < min,x] = np.nan
    data.loc[data[x] > max,x] = np.nan

  # Fbs sütununda outlayer olan dəyərləri yuxarıdakı kod vasitəsiylə null dəyərlərlə əvəz etdik

data = data.dropna(axis = 0)  # Əvəz etdiyimiz null dəyərləri silirik

data.boxplot(column='fbs') # Vizuallaşdıraraq görürük ki, outlayerlərimiz təmizlənmişdir

import numpy as np
for x in ['thalach']:
    q75,q25 = np.percentile(data.loc[:,x],[75,25])
    intr_qr = q75-q25
 
    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)
 
    data.loc[data[x] < min,x] = np.nan
    data.loc[data[x] > max,x] = np.nan

 # Thalach sütununda outlayer olan dəyərləri yuxarıdakı kod vasitəsiylə null dəyərlərlə əvəz etdik

data = data.dropna(axis = 0) # Əvəz etdiyimiz null dəyərləri silirik

data.boxplot(column='thalach') # Vizuallaşdıraraq görürük ki, outlayerlərimiz təmizlənmişdir

import numpy as np
for x in ['oldpeak']:
    q75,q25 = np.percentile(data.loc[:,x],[75,25])
    intr_qr = q75-q25
 
    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)
 
    data.loc[data[x] < min,x] = np.nan
    data.loc[data[x] > max,x] = np.nan

# Oldpeak sütununda outlayer olan dəyərləri yuxarıdakı kod vasitəsiylə null dəyərlərlə əvəz etdik

# Qeyd :  kod parçasını 2 dəfə işlətdikdən sonra outlayerlərimiz təmizlənir

data = data.dropna(axis = 0) # Əvəz etdiyimiz null dəyərləri silirik

data.boxplot(column='oldpeak') # Vizuallaşdıraraq görürük ki, outlayerlərimiz təmizlənmişdir

import numpy as np
for x in ['ca']:
    q75,q25 = np.percentile(data.loc[:,x],[75,25])
    intr_qr = q75-q25
 
    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)
 
    data.loc[data[x] < min,x] = np.nan
    data.loc[data[x] > max,x] = np.nan

# Ca sütununda outlayer olan dəyərləri yuxarıdakı kod vasitəsiylə null dəyərlərlə əvəz etdik

data = data.dropna(axis = 0)  # Əvəz etdiyimiz null dəyərləri silirik

data.boxplot(column='ca')   # Vizuallaşdıraraq görürük ki, outlayerlərimiz təmizlənmişdir

import numpy as np
for x in ['thal']:
    q75,q25 = np.percentile(data.loc[:,x],[75,25])
    intr_qr = q75-q25
 
    max = q75+(1.5*intr_qr)
    min = q25-(1.5*intr_qr)
 
    data.loc[data[x] < min,x] = np.nan
    data.loc[data[x] > max,x] = np.nan

# Thal sütununda outlayer olan dəyərləri yuxarıdakı kod vasitəsiylə null dəyərlərlə əvəz etdik

data = data.dropna(axis = 0) # Əvəz etdiyimiz null dəyərləri silirik

data.boxplot(column='thal') # Vizuallaşdıraraq görürük ki, outlayerlərimiz təmizlənmişdir

# Yenidən outlayer olan sütunlarımızı vizuallaşdıraraq kontrol edirik...
for i, outlayer in enumerate(data.columns):
  plt.figure(i)
  plt.figure(figsize=(24,20))
  plt.subplot(4, 2, 2)
  fig = data.boxplot(column=outlayer)
  fig.set_title('')
  fig.set_ylabel(outlayer)

# Vizuallaşdırmadan görünürki outlayerlərimizi uğurlu şəkildə kənarlaşdırmışıq

"""# **ML Modelinin Qurulması**"""

# Machine Learning modelimizin qurulması üçün lazım olan python paketlərini import edirik
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score, classification_report, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X = data.drop(['target'], axis=1) # Hədəf(target) sütunudan başqa digər sütunları X dəyişəninə mənimsədirik

X.shape # X dəyişəninə mənimsətdiyimiz datada 758 sətir 13 sütun vardır

X.head() # Dataya ümumi baxış keçirdirik

y = data['target'] # Datanın target sütununu y dəyişəninə mənimsədirik

y.shape # y dəyişəninə mənimsətdiyimiz datada 758 sətir 1 sütun vardır

y.head() # Dataya ümumi baxış keçirdirik

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
# X və y dəyərlərinə mənimsətdiyimiz datanı pythonun sklearn kitabxanasının  train_test_split() funksiyası vasitəsiylə train və test hissələrinə ayırırıq

X_train.shape # X_train üçün 606 sətir və 13 sütun vardır

X_test.shape  # X_test üçün 152 sətir və 13 sütun ayrılmışdır

"""# **Model Pipeline -nın  qurulması**"""

# 7 Model alqoritmasından istifadə edərək pipeline -nı qururuq
# Istifadə etdiyimiz  supervised learning modelləri aşağıdakılardır
 # LinearRegression()
 # DecisionTreeRegressor()
 # RandomForestRegressor()
 # KNeighborsRegressor()
 # XGBRegressor()
 # LogisticRegression()
 # SVM (Support Vector Machine)

 # Pipeline parametrlərində göstərdiyimiz StandardScaler() -in iş prinsipi:
 # StandardScaler() ortalama dəyərin (mean) 0,standart devision-nın 1 olduğu,datanın distributionunun normala yaxınlaşdığı bir metoddur
 # Yəni datanın ortalama dəyərini çıxarırıq,sonra isə varyans dəyərinə bölürük  (Standardize)
pipeline_linear_r=Pipeline([("scalar1",StandardScaler()),
                     ("lr_classifier",LinearRegression())])

pipeline_decision_t=Pipeline([("scalar2",StandardScaler()),
                     ("dt_classifier",DecisionTreeRegressor())])


pipeline_random_f=Pipeline([("scalar3",StandardScaler()),
                     ("rf_classifier",RandomForestRegressor())])


pipeline_kn=Pipeline([("scalar4",StandardScaler()),
                     ("rf_classifier",KNeighborsRegressor())])


pipeline_xgb=Pipeline([("scalar5",StandardScaler()),
                     ("rf_classifier",XGBRegressor())])

pipeline_logistic=Pipeline([("scalar5",StandardScaler()),
                     ("rf_classifier",LogisticRegression())])

pipeline_svm=Pipeline([("scalar5",StandardScaler()),
                     ("rf_classifier",SVC())])

pipelines = [pipeline_linear_r, pipeline_decision_t, pipeline_random_f, pipeline_kn, pipeline_xgb,pipeline_logistic,pipeline_svm]

pipe_dict = {0: "LinearRegression", 1: "DecisionTree", 2: "RandomForest",3: "KNeighbors", 4: "XGBRegressor",5 : "LogisticRegression",6 : "SCV"}

# Pipeline -a daxil etdiyimiz model növlərini döngü vasitəsiylə ardıcıl olaraq  fit edirik
for pipe in pipelines:
    pipe.fit(X_train, y_train)

# Hər bir modelin performans göstəricisini yazdıraq
cv_results_rms = []
for i, model in enumerate(pipelines):
    cv_score = cross_val_score(model, X_train,y_train,scoring="neg_root_mean_squared_error", cv=10)
    cv_results_rms.append(cv_score)
    print("%s: %f " % (pipe_dict[i], cv_score.mean()))
# Outputdan görürük ki, ən uyğun modelimiz DecisionTree() modelidir

# Nəticədəndə görünür ki, ən yaxşı öyrənmə Modeli DecisionTree modelidir

# Ardıcıl olaraq modelin R² , R2 score, Mean absolute error, Mean squared error,Root mean squared errorlarını hesasblayaq
pred = pipeline_decision_t.predict(X_test) 
print("R^2:",metrics.r2_score(y_test, pred))
print("Adjusted R^2:",1 - (1-metrics.r2_score(y_test, pred))*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1))
print("MAE:",metrics.mean_absolute_error(y_test, pred))
print("MSE:",metrics.mean_squared_error(y_test, pred))
print("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, pred)))

# Burada isə hər bir modelin predict faizini hesablayaq
pipelines = [pipeline_linear_r, pipeline_decision_t, pipeline_random_f, pipeline_kn, pipeline_xgb, pipeline_logistic, pipeline_svm]
for i in pipelines:
  print(i[1],"--  ",round(i.score(X_test, y_test),2)*100,"%")

pipeline_decision_t.score(X_test, y_test)

y_pred = pipeline_decision_t.predict(X_test)

accuracy_score(y_test,y_pred) # accuracy_score() funksiyası ilə Modelin dəqiqlik xalını hesabalayırıq

cf_matrix = confusion_matrix(y_test,y_pred)  # confusion_matrix() funksiyası ilə modelin qarisiqliq matrisini hesablayırıq

cf_matrix

# Confusion Matrixin qrafikinin vizuallaşdırılması
con = sns.heatmap(cf_matrix, annot=True, cmap='Blues')
con.set_title('Confusion Matrix - in vizuallasdirilmasi\n\n');
con.set_xlabel('\nPredicted Values')
con.set_ylabel('Actual Values ');
con.xaxis.set_ticklabels(['False','True'])
con.yaxis.set_ticklabels(['False','True'])
plt.show()

# Modelin AUC dəyərinin hesablanması
auc = roc_auc_score(y_test,y_pred)  # Bu onu göstərir ki, modelimiz yüksək performans əldə etmişdir
auc

# Modelin ROC (Receiver Operating Characteristic) əyrisinin qrafikini vizuallaşdıraq
fpr, tpr, thresholds = roc_curve(y_test,y_pred)
plt.plot(fpr , tpr , color='orange',label='ROC')
plt.plot([0,1],[0,1],color = 'darkblue',linestyle='--',label='ROC curve(area = %0.2f)'% auc)
plt.xlabel('false positive rate')
plt.ylabel('true positive rate')
plt.title('Modelimizin ROC eyrisi')
plt.legend()
plt.show()

f1_score(y_test,y_pred) # F1 scorun hesablanması

# classification_report() funksiyası vasitəsiylə Ümumi olaraq precision,recal ve f1-score dəyərlərinin hesablanması
print(classification_report(y_test,y_pred))

"""# **Model Saved**"""

# Modelimizi pythonun pickle kitabxanası vasitəsiylə save() edə bilərik
import pickle 
filename = 'final_model.sav' # Modelin adını təyin etdik
pickle.dump(model, open(filename, 'wb'))
# pickle kitabxanasının dump funsiyası ilə fit etdiyimiz model parametrlərini filename dəyişəninə təyin etdiyimiz 'final_model.sav' faylına yazdırırıq
# Bizim burada modelimiz DecisionTreeRegressor modelidir
# model = DecisionTreeRegressor()
# model.fit(X_train, y_train)
# pickle.dump(model, open(filename, 'wb')) kod sətrində 'model' parametrini yazdığımız kod parçasından aldığımızı fərz edin (bu yazdığınız koda əsasən dəyişə bilər)

"""# **Load the Model**"""

# Hazır modelin çağrılaraq istifadə edilməsi
import pickle
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result)