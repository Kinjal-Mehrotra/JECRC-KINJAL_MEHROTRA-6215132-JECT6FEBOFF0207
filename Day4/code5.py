#Wap to eat all the fruits one by one , if there is a rotten fruit skip it and continue to the next one 

fruits=['apple','banana','rotten fruit','grapes']
for fruit in fruits:
    if 'rotten fruit'==fruit:
        print('skipping this fruit')
        continue

    print(f'Eating {fruit}')