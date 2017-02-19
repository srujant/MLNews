import csv   

import os

file_name = './data/fake.csv'
stories = './data/stories/'
type = 'real'




with open(file_name, 'a') as f:
    writer = csv.writer(f)
    for filename in os.listdir(stories):
    	text = open (stories + filename,"r") 
    	row = [" "] * 20	    
        row[5] = text.read() 
        row[19] = type
        writer.writerow(row)
		



