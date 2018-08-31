from django.db import models


# Create your models here.
class House(models.Model):
    area_unit = models.CharField(max_length=5)
    num_bathrooms = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    num_bedrooms = models.IntegerField(default=0)
    home_size = models.IntegerField(default=0)
    home_type = models.CharField(max_length=25)
    last_sold_date = models.CharField(max_length=10)
    last_sold_price = models.IntegerField(default=0)
    link = models.CharField(max_length=200)
    price = models.CharField(max_length=5)
    property_size = models.IntegerField(default=0)
    rent_price = models.CharField(max_length=5)
    rentzestimate_amount = models.IntegerField(default=0)
    rentzestimate_last_updated = models.CharField(max_length=10)
    tax_value = models.DecimalField(default=0.0, decimal_places=1, max_digits=10)
    tax_year = models.IntegerField(default=0)
    year_built = models.IntegerField(default=0)
    zestimate_amount = models.IntegerField(default=0)
    zestimate_last_updated = models.CharField(max_length=10)
    zillow_id = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    @classmethod
    def create(cls, values):
        h = cls()
        h.area_unit = values[0]
        if values[1] != '':
            h.num_bathrooms = float(values[1])
        if values[2] != '':
            h.num_bedrooms = int(values[2])
        if values[3] != '':
            h.home_size = int(values[3])
        h.home_type = values[4]
        h.last_sold_date = values[5]
        if values[6] != '':
            h.last_sold_price = int(values[6])
        h.link = values[7]
        h.price = values[8]
        if values[9] != '':
            h.property_size = int(values[9])
        h.rent_price = values[10]
        if values[11] != '':
            h.rentzestimate_amount = int(values[11])
        h.rentzestimate_last_updated = values[12]
        if values[13] != '':
            h.tax_value = float(values[13])
        if values[14] != '':
            h.tax_year = int(values[14])
        if values[15] != '':
            h.year_built = int(values[15])
        if values[16] != '':
            h.zestimate_amount = int(values[16])
        h.zestimate_last_updated = values[17]
        if values[18] != '':
            h.zillow_id = int(values[18])
        h.address = values[19]
        h.city = values[20]
        h.state = values[21]
        h.zipcode = values[22]
        return h

    def __str__(self):
        return self.link

