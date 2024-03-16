# -*- coding: utf-8 -*-
"""dataset_loader

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GpP4wxPfIBx9d_Khkb9IQIwBTLM4iXH9
"""

# import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split

from ucimlrepo import fetch_ucirepo

import warnings
warnings.filterwarnings('ignore')

def load_dataset(name):

    list_of_names = ['Wine', 'Hayes_Roth', 'Contraceptive_Method_Choice',
                 'Pen-Based_Recognition_of_Handwritten_Digits',
                 'Vertebral_Column', 'Differentiated_Thyroid_Cancer_Recurrence',
                 'Dermatology', 'Balance_Scale', 'Glass_Identification',
                 'Heart_Disease', 'Car_Evaluation', 'Thyroid_Disease', 'Yeast',
                 'Page_Blocks_Classification', 'Statlog_Shuttle', 'Covertype',
                 ]
    if name not in list_of_names:
        raise ValueError("Dataset no found")

    print(f"Loading {name}")

    if name == 'Wine':
      data_set = fetch_ucirepo(id=109)

      X = data_set.data.features
      y = data_set.data.targets

    if name == 'Hayes_Roth':
      data_set = pd.read_csv("datasets/hayes_roth.data")
      data_set.columns = ["name", "hobby", "age", "educational",
                          "marital", "target"
                          ]
      # Split the data into independent & dependent variables
      X = data_set.drop(['target','name'], axis=1)
      X = pd.get_dummies(X, columns = ['hobby', 'age', 'educational',
                                       'marital'], drop_first = True)
      y = data_set['target']

    if name == 'Contraceptive_Method_Choice':
      data_set = fetch_ucirepo(id=30)

      X = data_set.data.features
      X = pd.get_dummies(X, columns = ['wife_edu', 'husband_edu',
                                        'husband_occupation',
                                        'standard_of_living_index'], drop_first = True)
      y = data_set.data.targets


    if name == 'Pen-Based_Recognition_of_Handwritten_Digits':
      data_set = fetch_ucirepo(id=81)

      X = data_set.data.features
      y = data_set.data.targets

    if name == 'Vertebral_Column':
      data_set = pd.read_csv("datasets/vertebral.dat", delim_whitespace=True, header=None)

      data_set.columns = ["pelvic_incidence", "pelvic_tilt", "lumbar_lordosis_angle",
                      "sacral_slope","pelvic_radius", "degree_spondylolisthesis", "target"
                      ]
      X = data_set.drop(['target'], axis=1)
      y = data_set['target']

    if name == 'Differentiated_Thyroid_Cancer_Recurrence':
      data_set = fetch_ucirepo(id=915)

      X = data_set.data.features
      X_cat = X.loc[:, X.columns !='Age']
      X = pd.get_dummies(X, columns = X_cat.columns, drop_first = True)
      y = data_set.data.targets

    if name == 'Dermatology':
      data_set = fetch_ucirepo(id=33)

      X = data_set.data.features
      # X[X.isnull().any(1)].index
      # Drop nan rows
      X = X.dropna()

      y = data_set.data.targets
      y = y.drop([33, 34, 35, 36, 262, 263, 264, 265])


    if name == 'Balance_Scale':
      data_set = fetch_ucirepo(id=12)

      X = data_set.data.features
      X = pd.get_dummies(X, columns = X.columns, drop_first = True)
      y = data_set.data.targets

    if name == 'Glass_Identification':
      data_set = fetch_ucirepo(id=42)

      X = data_set.data.features
      y = data_set.data.targets

    if name == 'Heart_Disease':
      data_set = fetch_ucirepo(id=45)

      X = data_set.data.features
      X[X.isnull().any(1)].index
      X = X.dropna()
      X_cat = ['cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']
      X = pd.get_dummies(X, columns = X_cat, drop_first = True)

      y = data_set.data.targets
      y = y.drop([87, 166, 192, 266, 287, 302])


    if name == 'Car_Evaluation':
      data_set = fetch_ucirepo(id=19)

      X = data_set.data.features
      X = pd.get_dummies(X,columns = X.columns, drop_first = True)

      y = data_set.data.targets

    if name == 'Thyroid_Disease':
      data_set = pd.read_csv("datasets/new-thyroid.data", delimiter=',', header=None)
      data_set.columns = ["target", "T3_resin", "thyroxin", "triiodothyronine",
            "thyroid_stimulating_hormone", "Maximal_absolute_difference_of_TSH"]
      X = data_set.drop(['target'], axis=1)
      y = data_set['target']

    if name == 'Yeast':
      data_set = fetch_ucirepo(id=110)

      X = data_set.data.features
      y = data_set.data.targets

    if name == 'Page_Blocks_Classification':
      data_set = pd.read_csv("datasets/page_blocks.data", delim_whitespace=True)
      data_set.columns = ["height", "lenght", "area", "eccen","p_black",
                          "p_and", "mean_tr", "blackpix", "blackand",
                          "wb_trans", "target"
                          ]
      X = data_set.drop('target', axis=1)
      y = data_set['target']

    if name == 'Statlog_Shuttle':
      data_set_train = pd.read_csv("datasets/shuttle.trn", delim_whitespace=True, header=None)
      data_set_test = pd.read_csv("datasets/shuttle.tst", delim_whitespace=True, header=None)

      data_set_train.columns = ["na", "na1", "Rad Flow", "Fpv Close", "Fpv Open",
                                "High","Bypass", "Bpv Close", "Bpv Open", "target"
                                ]
      X_train = data_set_train.drop(["na", "na1","target"], axis=1)
      y_train = data_set_train['target']

      data_set_test.columns = ["na", "na1", "Rad Flow", "Fpv Close", "Fpv Open",
                              "High","Bypass", "Bpv Close", "Bpv Open", "target"
                                ]
      X_test = data_set_test.drop(["na", "na1","target"], axis=1)
      y_test = data_set_test['target']

      X = pd.concat([X_train, X_test], ignore_index=True)
      y = pd.concat([y_train, y_test], ignore_index=True)

    if name == 'Covertype':
      data_set = fetch_ucirepo(id=31)

      X = data_set.data.features
      y = data_set.data.targets

    return X, y

def preprocessing(X, y, scaler=StandardScaler(), test_size=0.3, random_state=42):

    le = LabelEncoder()
    y = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size,
                                       random_state=random_state, stratify=y)

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test