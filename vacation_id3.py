import pandas as pd 
import numpy as np 
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from scipy import sparse
import pydotplus

scores = pd.read_csv('full_country_score')
#scores.drop(['CASINOS'],axis= 1)
all_scores = pd.DataFrame().append([scores]*200)
feature_cols = scores.columns[1:] 
scores[feature_cols] = np.sqrt(scores[feature_cols])
#diff_scores = [scores]*100
#all_scores = scores.append(diff_scores)
variance = pd.DataFrame([scores.var(axis = 0)])
for columns in feature_cols:
	all_scores[columns] += np.random.normal(0,np.sqrt(variance[columns]/2),len(all_scores))


X = all_scores[feature_cols] 

y = all_scores['city']


X_train , X_test , y_train, y_test = train_test_split(X,y,test_size=0.3,random_state = 1)

clf = DecisionTreeClassifier(max_depth = 10,criterion='entropy',min_samples_leaf = 5)
clf = clf.fit(X_train,y_train)


y_pred = clf.predict(X_test)


print('Accuracy:' + str(metrics.accuracy_score(y_test,y_pred)))
print(clf.tree_.max_depth)

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=list(scores['city']))
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('vacations.png')
Image(graph.create_png())
