from django.db import models


class ArticleType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=100, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    fichier = models.FileField(upload_to='media/fichier/', blank=True)
    image = models.ImageField(upload_to='media/article_photos/')
    link = models.URLField(max_length=200, blank=True)
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Slide(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_validite = models.IntegerField()
    active = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.article)


class Photo(models.Model):
    photo = models.ImageField(upload_to='media/gallerie/')


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
