from django.shortcuts import render
from django.http import HttpResponse
from .models import House


# Create your views here.
def index(request):
    all_vals = read_file("houses/Los_Angeles-2018-08-08_0845.csv")
    add_to_table(all_vals)
    return HttpResponse("This is the houses index.")


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


def get_from_table():
    # things
    minimum = 1
    maximum = 100000000
    baths = 0
    sqft = 0
    if minimum and maximum:
        vals = House.objects.filter(price__gte=minimum).filter(price__lte=maximum)
    elif not maximum:
        vals = House.objects.filter(price__gte=minimum)
    else:
        vals = House.objects.filter(price_lte=maximum)
    vals = House.objects.filter(num_bathrooms__gte=baths)
    vals = House.objects.filter(home_size__gte=sqft)
    return vals
