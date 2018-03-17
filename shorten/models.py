from django.db import models

class url(models.Model):
    long_url=models.CharField(max_length=9999, null=True)
    short_hash=models.CharField(max_length=9999, null=True)
    count=models.IntegerField()
    status=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.short_hash