from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.URLField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)

    def lte(self):
        if self.lte_exists:
            return 'Есть'
        else:
            return 'Нет'



