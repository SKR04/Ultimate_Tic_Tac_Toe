import csv
with open("lag_detail.csv","w",newline="") as f:
    w = csv.writer(f)
    n = int(input("Enter no.of inputs: ")) #to be given 5
    ro = []
    for i in range(n):
        ro += [input("Enter the string: ").split(",")]
    for i in ro:
        if int(i[2]) < 75 or int(i[3]) < 75 or int(i[4]) < 75:
            w.writerow(ro)
with open("lag_detal.csv","r") as f:
    r = csv.reader(f)
    for i in r:
        print(i)

