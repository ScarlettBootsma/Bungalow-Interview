#!/usr/bin/python

def read_file(file_name):
    fp = open(file_name, "r")
    arr = []

    for line in fp:
        line = line.rstrip('\n')
        to_add = []
        for val in line.split(","):
            to_add.append(val)
        arr.append(to_add)

    return arr


def add_to_table(all_vals):
    for val in all_vals:
        if val == all_vals[0]:
            continue

        h = House.create(val)
        h.save()

import os, sys
if __name__ == '__main__':
    # Setup environ
    sys.path.append(os.getcwd())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "interview.settings")

    # Setup django
    import django
    django.setup()
    from houses.models import House

    House.objects.all().delete()

    all_vals = read_file("Los_Angeles-2018-08-08_0845.csv")
    add_to_table(all_vals)

    #get user input here
    while True:

        value = input("retrieve based on (1)price, (2)number of bathrooms, (3)size, (4)exit: ")

        if value == "1":
            #prices
            try:
                minimum = int(float(input("Minimum price: ")))
            except ValueError:
                minimum = 0

            try:
                maximum = int(float(input("Maximum price: ")))
            except ValueError:
                maximum = 0

            print(minimum)
            print(maximum)

            if minimum > 0 and maximum > 0:
                print("both")
                vals = House.objects.filter(last_sold_price__range=(minimum, maximum))# price__gte=minimum, price__lte=maximum)
            elif maximum == 0 and minimum == 0:
                print("none")
                vals = House.objects.all()
            elif minimum == 0:
                print("only max")
                vals = House.objects.filter(last_sold_price__lte=maximum)
            else:
                print(minimum)
                print("only min")
                vals = House.objects.filter(last_sold_price__gte=minimum)

            print(vals)

        elif value == "2":
            #bathrooms
            try:
                baths = float(input("Minimum number of bathrooms: "))
            except ValueError:
                baths = 0

            vals = House.objects.filter(num_bathrooms__gte=baths)

            print(vals)

        elif value == "3":
            #size
            try:
                sqft = float(input("Minimum square footage: "))
            except ValueError:
                sqft = 0

            vals = House.objects.filter(home_size__gte=sqft)

            print(vals)

        elif value == "4":
            break

