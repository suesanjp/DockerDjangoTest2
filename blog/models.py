from django.db import models


class Blog(models.Model):

    text = models.CharField(max_length=140)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class META:
        ordering = ["-poosted_date"]
