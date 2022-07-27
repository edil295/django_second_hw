from django.db import models


class Item(models.Model):
    name = models.CharField('Наименование товара', max_length=30)
    price = models.IntegerField('Цена товара')

    def __str__(self):
        return f'{self.name} - {self.price}'


class Purchase(models.Model):
    name = models.CharField('ФИО клиента', max_length=30)
    age = models.IntegerField('Возраст клиента')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateTimeField('Дата покупки')

    def __str__(self):
        return f'{self.name} - {self.age}'

