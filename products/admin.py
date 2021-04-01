from django.contrib import admin

from .models.departments import Department
from .models.item import Item
from products.models.slider import Slider
from products.models.contact import Contact

admin.site.register(Department)
admin.site.register(Item)
admin.site.register(Slider)
admin.site.register(Contact)