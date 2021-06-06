from django.db import models

# Create your models here.
class Poll(models.Model):
    STATUS = (
        (0, "Unpublished"),
        (1, "Published"),
    )

    title = models.CharField(max_length=200)
    question = models.CharField(max_length=200)
    active_until = models.DateTimeField(null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

class Option(models.Model):
    title = models.CharField(max_length=200)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)

class Response(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    response_time = models.DateTimeField(auto_now_add=True)
    options = models.ForeignKey('Option', on_delete=models.CASCADE)