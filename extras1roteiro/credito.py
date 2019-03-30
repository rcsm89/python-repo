sal = (int(input()))
comp = (int(input()))
pm = sal*0.3 - comp
if(comp > sal*0.3):
    pm = 0
print("%.2f"%pm)
