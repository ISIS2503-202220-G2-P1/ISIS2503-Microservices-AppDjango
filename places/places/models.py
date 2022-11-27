from django.db import models

class Place(models.Model):
    measurements = models.ManyToOneRel(null=False, default=None)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)