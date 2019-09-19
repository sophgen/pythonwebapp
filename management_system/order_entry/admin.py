from django.contrib import admin
from order_entry.models import order
from order_entry.models import item
from order_entry.models import item_price
from order_entry.models import payment_type

# Register your models here.
admin.site.register(order)
admin.site.register(item)
admin.site.register(item_price)
admin.site.register(payment_type)