from django.db import models
from userprofile.models import UserProfile


def item_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'item_{0}/{1}'.format(instance.id, filename)


class ItemCategory(models.Model):
    name = models.CharField('Name', max_length=256, null=False)
    desc = models.CharField('Description', max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField('Name', max_length=256, null=False)
    desc = models.CharField('Description', max_length=1024, null=True)
    datasheet = models.CharField('Datasheet', max_length=2048, null=True)
    code = models.CharField('Code', max_length=256, null=True)
    price = models.DecimalField('Price', max_digits=16, null=False, decimal_places=2, default=0)
    stock = models.IntegerField('Stock', null=False, default=0)
    dt_created = models.DateField('Creation date', auto_now_add=True)
    dt_modif = models.DateField('Change date', auto_now=True)
    category = models.ManyToManyField(ItemCategory, related_name='items')

    def __str__(self):
        return self.name


class ItemPhoto(models.Model):
    file_img = models.ImageField(upload_to=item_directory_path, default='notfound.png')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.file_img


class ItemRating(models.Model):
    value = models.IntegerField('Rating', null=False, default=1)
    comment = models.CharField('Comment', max_length=512, null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='ratings')
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return '{} stars to item {} from user {}'.format(self.value, self.item.name, self.userprofile.name)
