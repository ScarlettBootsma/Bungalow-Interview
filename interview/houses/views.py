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
