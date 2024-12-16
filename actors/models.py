from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('Brazil', 'Brasil'),
    ('France', 'França'),
    ('Germany', 'Alemanha'),
    ('Argentina', 'Argentina'),
)
class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
    )
    
    def __str__(self):
        return self.name