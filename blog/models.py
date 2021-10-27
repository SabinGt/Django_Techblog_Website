from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
def mycustomvalidator(value):
    if len(value) > 4:
        return True
    else:
        raise ValidationError("must have more than 5 characters")


def val2(value):
    if '@' in value:
        raise ValidationError("title can't have @ character")


class Category(models.Model):
    objects = None
    title = models.CharField(max_length=100, unique=True, validators=[mycustomvalidator, val2])

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    # publish_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "blog"
