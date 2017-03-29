#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list1 = ['poi', 'salary', 'deferral_payments', 'total_payments', 'bonus', 'director_fees', 'other',
                 'deferred_income', 'total_stock_value', 'exercised_stock_options','restricted_stock_deferred',
                 'long_term_incentive', 'restricted_stock', 'director_fees', 'to_messages','from_messages', 
                 'from_poi_to_this_person', 'from_this_person_to_poi', 'shared_receipt_with_poi',
                 'total_salary_ratio', 'payments_plus_stock']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict1 = pickle.load(data_file)

### Task 2: Remove outliers
data_dict1.pop('TOTAL')
data_dict1.pop('THE TRAVEL AGENCY IN THE PARK')

### Task 3: Create new feature(s)

for name in data_dict1:
	# total_salary_ratio is ratio of total_payements which includes bonus, long term incentive, and other payments 
	# to employees salary
    if data_dict1[name]['total_payments'] != 'NaN' and data_dict1[name]['salary'] != 'NaN':
        data_dict1[name]['total_salary_ratio'] = (data_dict1[name]['total_payments']*1./data_dict1[name]['salary'])
    else:
        data_dict1[name]['total_salary_ratio'] = 'NaN'
    # payments_plus_stock is total_payments added to total_stock_value
    if data_dict1[name]['total_payments'] != 'NaN' and data_dict1[name]['total_stock_value'] != 'NaN':
        data_dict1[name]['payments_plus_stock'] = data_dict1[name]['total_payments'] \
        + data_dict1[name]['total_stock_value']
    else:
        data_dict1[name]['payments_plus_stock'] = 'NaN'
           
### Store to my_dataset for easy export below.
my_dataset = data_dict1

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list1, sort_keys = True)
labels, features = targetFeatureSplit(data)

from sklearn.cross_validation import train_test_split

features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0, random_state=42)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# set up various pipeline objects
from pprint import pprint
from sklearn.model_selection import GridSearchCV # updated based on scikit-learn 0.18.1
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn.preprocessing import Normalizer
from sklearn.decomposition import PCA
from datetime import datetime as dt
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.naive_bayes import GaussianNB

# set up various pipeline objects
kbest = SelectKBest(f_classif)
pca = PCA()
scaler = preprocessing.StandardScaler()
clf_GNB = GaussianNB()

pipe_nb = Pipeline(steps =[
    ('kbest', kbest),
    ('std_scale', scaler),    
    ('PCA', pca),   
    ('nb_clf', clf_GNB)    
    ])

parameters_nb = {"PCA__n_components":[2,4,6], "PCA__whiten": [True],
              "kbest__k":[6,8,10,12,'all']}



# use pipeline in GridSearchCV
    # initialize grid search
grid_search = GridSearchCV(pipe_nb, parameters_nb, n_jobs = 1, verbose = 1, scoring = "roc_auc")
print("\nPerforming grid search...")
print("pipeline:", [name for name, _ in pipe_nb.steps])
print("parameters:")
pprint(parameters_nb)
t0 = dt.now()
grid_search.fit(features_train, labels_train)
print("done in {}\n".format(dt.now() - t0))
print("\nBest score: {:0.3f}".format(grid_search.best_score_))
print("\nBest parameters set:")
best_parameters = grid_search.best_estimator_.get_params()
for param_name in sorted(parameters_nb.keys()):
    print("\t{}: {}".format(param_name, best_parameters[param_name]))

# get the best features that we will use in final classifier
features_selected_bool = grid_search.best_estimator_.named_steps['kbest'].get_support()
features_selected_list = [x for x, y in zip(features_list1[1:], features_selected_bool) if y]


### Extract features and labels from dataset for local testing (use features_selected_list)

# due to featureFormat() need to add 'poi' as first feature of the list
# https://discussions.udacity.com/t/valueerror-the-least-populated-class-in-y-has-only-1-member-which-is-too-few/44984/2
poi_first = ['poi']
features_selected_list = poi_first + features_selected_list
data1 = featureFormat(my_dataset, features_selected_list, sort_keys = True)
labels, features = targetFeatureSplit(data1)
pprint(features_selected_list)

from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0, random_state=42)


# fit the best classifer from GridSearchCV
best_clf = grid_search.best_estimator_.fit(features_train, labels_train)




### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(best_clf, my_dataset, features_selected_list)
