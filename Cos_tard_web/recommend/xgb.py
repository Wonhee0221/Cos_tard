# from xgboost import XGBClassifier
# import warnings; warnings.filterwarnings('ignore')
# import pandas as pd
# from sklearn.model_selection import train_test_split
# import numpy as np

# df = pd.read_csv('trainlabel_f.csv')
# y_label = df['label']
# train_columns = ['expertised', 'loyalty', 'impact', 'effect']

# x_train, x_test, y_train, y_test = train_test_split(df[train_columns], y_label, test_size=0.3, random_state=32)
# dtrain = xgb.DMatrix(data = x_train, label=y_train)
# dtest = xgb.DMatrix(data=x_test, label=y_test)

# params = {'eta':0.3, 'objective':'binary:logistic', 'eval_metric':'logloss', 'early_stoppings':100}

# xgb_model = XGBClassifier(params=params, dtrain=dtrain, num_boost_round=100, early_stoping_rounds=100,
#                       evals=[(dtrain, 'train'), (dtest, 'test')])

# def classifier(x_test):
#     preds = xgb_model.predict(x_test)
#     preds_probs = xgb_model.predict_proba(x_test)[:,0]

#     result = [preds, preds_probs]

#     return result