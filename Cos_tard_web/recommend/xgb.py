# import xgboost
# import warnings; warnings.filterwarnings('ignore')
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import numpy as np

# df = pd.read_csv('C:/Users/user/git/Cos_tard/Cos_tard_web/static/trainlabel_f.csv')
# y_label = df['label']
# train_columns = ['expertised', 'loyalty', 'impact', 'effect']

# x_train, x_test, y_train, y_test = train_test_split(df[train_columns], y_label, test_size=0.3, random_state=32)
# dtrain = xgboost.DMatrix(data = x_train, label=y_train)
# dtest = xgboost.DMatrix(data=x_test, label=y_test)

# params = {'eta':0.3, 'objective':'binary:logistic', 'eval_metric':'logloss', 'early_stoppings':100}

# xgb_model = xgboost.XGBClassifier(n_estimators=500, learning_rate=0.2, max_depth=4, random_state = 32)
# xgb_model.fit(x_train,y_train)

# def classifier(x_test):
#     preds = xgb_model.predict(x_test)
#     preds_probs = xgb_model.predict_proba(x_test)[:,0]

#     result = [preds, preds_probs]

#     acc = accuracy_score(preds, y_test)

#     return result
