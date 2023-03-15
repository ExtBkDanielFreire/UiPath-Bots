import csv

with open(r"C:\Users\Daniel\Downloads\testUIPA.csv", 'w') as myfile:
    csv.writer(myfile, delimiter=';').writerow(['teste', 'amigo'])

def add(a,b):
    result = a+" "+b

    return result