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

clf = DecisionTreeClassifier(max_depth = 12,criterion='entropy',min_samples_leaf = 5)
clf = clf.fit(X_train,y_train)


y_pred = clf.predict(X_test)


def traverse (estimator = clf,feature_cols=feature_cols): 
    '''
    Decision tree traversal. Sklearn uses absolute paths to store nodes. For example 
    the numbers 0,1,2, ... , number of nodes -1 are all specific nodes. It's really 
    stupid, but all the code below is based on that. Node 0 is the root, and everything else isn't easy to identify.
    '''
    tree_ = estimator.tree_ # The actual tree structure.
    n_nodes = estimator.tree_.node_count # Child structure : leftchild[i] is the left child to node with absolute path i. etc.
    children_left = estimator.tree_.children_left
    children_right = estimator.tree_.children_right
    feature = estimator.tree_.feature # Features: Feature[i] returns the column number/feature on which node i is being split.
    threshold = estimator.tree_.threshold # Threshold: The value at which the split occurs.

    feature_names = [feature_cols[i] for i in feature]# Gives names to feature columns rather than numbers.

    leave_id = estimator.apply(X_test) #Identifies all the possible leaf nodes of the dataset. 

    def recurse(node):
        if node in leave_id: #Base case: Hitting a leaf
            return clf.classes_[np.argmax(tree_.value[node])]
        else:#User input.
            print('Is your' + str(feature_names[node]) + '<='+ str(threshold[node]))
            inp = input()
            if float(inp) <= threshold[node]:
                return recurse(node = children_left[node])
            else:
                return recurse(node = children_right[node])
    #prints this to the city
    print(recurse(0))
        

    # First let's retrieve the decision path of each sample. The decision_path
    # method allows to retrieve the node indicator functions. A non zero element of
    # indicator matrix at the position (i, j) indicates that the sample i goes
    # through the node j.

    node_indicator = estimator.decision_path(X_test)

    # Similarly, we can also have the leaves ids reached by each sample.