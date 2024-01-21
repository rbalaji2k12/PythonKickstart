import csv
 
with open('ind_nifty200Quality30_list.csv', mode ='r')as file:
   

  csvFile = csv.reader(file)
 
  for lines in csvFile:
    print(lines)