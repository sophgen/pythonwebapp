from django.db import models

class item(models.Model):
    code = models.CharField(max_length=5)
    description = models.CharField(max_length=200)
    def __str__(self):
        return f"({self.code}) - ({self.description})"
    class Meta:
        db_table = 'order_entry_item'

class item_price(models.Model):
    price_item = models.ForeignKey(item, on_delete=models.CASCADE)
    price = models.FloatField()
    price_effective_from = models.DateField()
    price_effective_to = models.DateField()
    def __str__(self):
        return f"[{self.price_item}] - [{self.price}] - [{self.price_effective_from}] - [{self.price_effective_to}]"
    class Meta:
        db_table = 'order_entry_item_price'

class payment_type(models.Model):
    code = models.CharField(max_length=5)
    type = models.CharField(max_length=200)
    def __str__(self):
        return f"[{self.code}] - [{self.type}]"
    class Meta:
        db_table = 'order_entry_payment_type'


class order(models.Model):
    order_desc = models.CharField(max_length=255)
    order_date = models.DateField(auto_now=False)
    order_item = models.ForeignKey(item, on_delete=models.PROTECT, related_name="item")
    order_payment_type = models.ForeignKey(payment_type, on_delete=models.PROTECT, related_name="payment")
    order_qty = models.IntegerField()
    order_amount = models.FloatField()
    order_created_date = models.DateTimeField(auto_now=True)
    order_notes = models.CharField(max_length=1000)
    def __str__(self):
        return f"[{self.order_date}] - [{self.order_item}] - [{self.order_payment_type}] - [{self.order_amount}] - [{self.order_notes}]"

    class Meta:
        db_table = 'order_entry_order'

