import csv
from datetime import date
file=open('expense.csv','a+',newline='')
w=csv.writer(file)
w.writerow(['DATE','CATEGORY','AMOUNT']) #prefer to use writerow to provide column name
#writerows used for data 
w.writerows([
    [date.today(),'Travel',2000],
    [date.today(),'Food',1000],
    [date.today(),'Entertainment',1000]
])
file.seek(0)
r=csv.reader(file)
print(list(r))
file.close()
