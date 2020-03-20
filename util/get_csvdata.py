import csv

def get_csv_data(file_name):
    rows=[]
    with open(file_name,'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        for row in reader:
            rows.append(row)
        return rows


# print(get_csv_data("/Users/lindafang/PycharmProjects/selenium3forpython2020/thirdday/test_data.csv"))