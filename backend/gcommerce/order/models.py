from django.db import models
from userprofile.models import UserProfile, Address
from item.models import Item


class Cart(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='carts')

    def __str__(self):
        return '{} cart'.format(self.userprofile)


class ItemOrder(models.Model):
    quantity = models.IntegerField('Quantity', null=False, default=0)
    discount = models.DecimalField('Discount', max_digits=16, null=False, decimal_places=2, default=0)
    item_price = models.DecimalField('Item price', max_digits=16, null=False, decimal_places=2, default=0)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_orders')
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, related_name='item_orders')

    def __str__(self):
        return '{} / qtd: {}'.format(self.item.name, self.quantity)


class Order(models.Model):
    dt_created = models.DateField('Creation date', auto_now_add=True)
    paid = models.DecimalField('Paid value', max_digits=16, null=False, decimal_places=2, default=0)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, related_name='orders')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, related_name='orders')
    items = models.ManyToManyField(ItemOrder, related_name='orders')

    def __str__(self):
        return str(self.id)
