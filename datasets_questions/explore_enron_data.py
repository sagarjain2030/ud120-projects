#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

feature_Lay = enron_data['LAY KENNETH L']
print(feature_Lay)

feature_Lay = enron_data['LAY KENNETH L']['total_payments']
print(feature_Lay)

feature_Faston = enron_data['FASTOW ANDREW S']['total_payments']
print(feature_Faston)

feature_Ski = enron_data['SKILLING JEFFREY K']['total_payments']
print(feature_Ski)

temp = [s for s in enron_data.keys() if enron_data[s]['salary']=='NaN']
print(len(temp))

temp = [s for s in enron_data.keys() if enron_data[s]['email_address']=='NaN']
print(len(temp))

#f = open('../final_project/poi_names.txt','r')
#message = f.read()
#temp = message.split('\n')
#print(len(temp))

quantified_salary_count = 0
for k in enron_data:
    if enron_data[k]['salary'] != 'NaN':
        quantified_salary_count += 1
print "How many folks in this dataset have a quantified salary? ", \
        quantified_salary_count


email_address_count = 0
for k in enron_data:
    if enron_data[k]['email_address'] != 'NaN':
        email_address_count += 1
print "What about a known email address? ", email_address_count

nan_total_payments = 0
l = 0
for k in enron_data:
    l += 1
    if enron_data[k]['total_payments'] == 'NaN':
        nan_total_payments += 1

print ("Percent of nan in total payments ", (nan_total_payments/float(l))*100)

no_POI = 0
l = 0
for k in enron_data:
    l += 1
    if enron_data[k]['poi'] == True and enron_data[k]['total_payments'] == 'NaN':
        no_POI += 1

print (no_POI,  "  Percent of nan in total payments ", (no_POI / float(l)) * 100)

l = 0
for k in enron_data:
    if enron_data[k]['poi'] == True:
        l += 1

print(l)
