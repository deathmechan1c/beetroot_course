import csv
my_file = open('test.csv', 'w')
my_list = ['apple', 'pineapple', 'melon', 'watermelon']
my_file.write (str(my_list))
my_file.close()
#
with open('test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        print(', '.join(row))