from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
from users import models as userModels


class Topic(models.Model):

    topic = models.CharField(max_length=255)

    def __str__(self):
        return self.topic


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=4000, blank=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    user = models.ForeignKey(userModels.User, on_delete=models.CASCADE)
    is_anonymous = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    topics = models.ManyToManyField(Topic)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)
        print(self.slug)

    def __str__(self):
        return self.title


class Answer(models.Model):
    class Meta:
        ordering = ["-updated_date"]

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.TextField(max_length=4000)
    user = models.ForeignKey(userModels.User, on_delete=models.CASCADE)
    is_anonymous = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} on {self.created_date}"
