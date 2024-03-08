from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=65)
    image = models.ImageField(upload_to='dogs/')

    def __str__(self):
        return self.name

    def delete(self):
        self.image.delete()
        super().delete()


class Bill(models.Model):
    name = models.CharField(max_length=65)
    image = models.ImageField(upload_to='bills/')

    def __str__(self):
        return self.name

    def delete(self):
        self.image.delete()
        super().delete()

class ApprovedEntry(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return f"{self.field1} - {self.field2}"  # Modify as per your fields

class PendingEntry(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return f"{self.field1} - {self.field2}"  # Modify as per your fields

class AcceptedItem(models.Model):
    feature = models.CharField(max_length=100)
    dog_view_url = models.URLField()
    bill_view_url = models.URLField()