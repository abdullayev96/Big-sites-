from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=260, unique=True, verbose_name="Url", db_index=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat  = models.ForeignKey("Category", on_delete=models.PROTECT)


    def __str__(self):
        return f"{self.title} || {self.content}"

    def get_absolute_url(self):
        return reverse('post', kwargs={"post_slug":self.slug})

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering =['time_create', 'title']



class Category(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(max_length=260, unique=True, verbose_name="Url", db_index=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"cat_id":self.pk})


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering =['id']

