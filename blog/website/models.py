from django.db import models

class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    GR = 'GR', 'Geral'

class Contact(models.Model):
    name= models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )
    approved = models.BooleanField(default=True)

    imagem = models.ImageField(upload_to='posts')

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.subtitle

    def get_category_label(self):
        return self.get_categories_display()

    full_name.admin_order_field = 'title'