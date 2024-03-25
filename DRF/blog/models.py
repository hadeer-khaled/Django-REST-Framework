from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Post(models.Model):
    class PostObjects(models.Manager):
        """
        Usage:
            By defining this custom manager, any queries performed using Post.objects
            (the default manager) will retrieve all posts, regardless of their status.
            However, if you use Post.postobjects, it will only retrieve
            posts with a status of "published" due to the custom queryset filtering.
        """
        def get_queryset(self):
            return super().get_queryset().filter(status="published")
        
    objects = models.Manager()  # Default manager
    postobjects = PostObjects()  # Custom manager
    options = (('draft', 'Draft'), ('published', "Published"))

    # --------------------- Table Fields ---------------------

    # PROTECT prevents deletion of the referenced Category as long as there are still Post objects in it. 
    category_name = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=100, unique_for_date="published")
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=100, choices=options, default="published")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-published",)  # Note the comma after "-published"
