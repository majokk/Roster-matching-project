import re

def month_generator():
    # creates a dict with dates (represented as strings) as key and [None] as value
    month={}
    for number in xrange(01,32):
        month[(str(number).zfill(2)+"1015")] = [None]
    return month       

def parser(input_file):
    # finds DO dates for a particular employee and returns a list with said dates
    with open(input_file, "r+") as myfile:
        b = []
        for line in myfile:
            a = re.split(r'\t+', line)
            if a[0].isdigit() and a[1] == ("DO" or "WDO"):
                b.append(a[0])
    return b
        

def append_monthly_dict(input_list_of_DOs, database, employee):
    # takes output of parser and adds employee id to database(matches date and id)
    # database is a dictionary from month_generator()
    # input_list_of_DOs is the list returned by parser
    # employee is employee id
    for item in input_list_of_DOs:
        # append the list which makes up dict item
        database[item].append(employee)
    return database

def output_formatting(input_dict):
    # makes the output of append_monthly_dict() look neater
    for k in sorted(input_dict):
        print k, input_dict[k]

output_formatting(append_monthly_dict(parser("sample_roster.txt"),month_generator(),"employee id"))
