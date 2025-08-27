from django.db import models

# Create your models here.


class Article(models.Model):
    title=models.CharField(max_length=500)
    text=models.TextField()
    image=models.ImageField()
    posted_at=models.DateTimeField(auto_now_add=True)
    edited_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.title().strip(' *&^$#@')
        super().save(*args, **kwargs)

    class Meta:
        db_table='article'


