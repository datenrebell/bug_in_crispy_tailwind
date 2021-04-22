from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(
            'Author',
            on_delete=models.CASCADE,
            # blank=True,
            null=True,
            related_name='Author'
    )
    publisher = models.ForeignKey(
            'Publisher',
            on_delete=models.CASCADE,
            # blank=True,
            null=True,
            related_name='Publisher'
    )

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
