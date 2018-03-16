from django.db import models

class url(models.Model):
    long_url=models.CharField(max_length=9999)
    short_hash=models.CharField(max_length=9999)
    count=models.IntegerField()
    status=models.BooleanField()
    created_at=models.DateTimeField()


    def __str__(self):
        return self.short_hash