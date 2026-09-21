from django.db import models


class Location(models.Model):
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Название", max_length=255)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField("Название", max_length=255, unique=True)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return self.name


class Model(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.PROTECT,
        verbose_name="Производитель",
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
        verbose_name="Категория",
    )
    name = models.CharField("Модель", max_length=255)

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return f"{self.vendor.name} {self.name}"