from django.db import models

class Input(models.Model):
    input = models.CharField(max_length=200)
    output = models.CharField(max_length=200, blank = True)

    def __str__self():
        return (self.input, self.output)


