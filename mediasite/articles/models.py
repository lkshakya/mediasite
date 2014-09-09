from django.db import models

# Create your models here.
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from sorl.thumbnail import ImageField
from suit_ckeditor.widgets import CKEditorWidget

class Author(models.Model):
    name = models.CharField(max_length=60,blank=True, null=True)
    image = ImageField(upload_to='author_post', blank=True, null=True)
    email = models.EmailField('Email/Username',unique='True')
    password=models.CharField('Password',max_length=30)
    dob = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name
    
    def update(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
        self.save()
        

class Category(models.Model):
    category_name = models.CharField(max_length=60)
    def __unicode__(self):
        return self.category_name

class Post(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True)
    author = models.ForeignKey(Author, blank=True, null=True)
    image = models.ImageField(upload_to='articleimage/',null=True,blank=True)
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __unicode__(self):
        return self.title

    def update(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
        self.save()
        
    def save(self, *args, **kwargs):
        try:
            this = Post.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass
        super(Post, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Post, self).delete(*args, **kwargs)

    def __init__(self, *args, **kargs):
        super(Post, self).__init__(*args, **kargs)
        self._meta.get_field_by_name("image")[0].directory = self.image

    
    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
                                                                    (self.image.name, self.image.name))
    thumbnail.allow_tags = True
    
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField("Name",max_length=60)
    email = models.EmailField('Email',unique='True')
    body = models.TextField()
    post = models.ForeignKey(Post)
    def __unicode__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))
 
class PostForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
            'body': CKEditorWidget(editor_options={'startupFocus': True})
        }
        fields = ['category','image','title','body']
        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)


class AuthorForm(ModelForm):
    class Meta:
         model = Author
         fields = ['name','image','email', 'password']


class PostAdmin(ModelAdmin):
    list_display = ["__unicode__",   "thumbnail"]
    list_filter = ["title"]
    list_per_page =10
    form = PostForm
    fieldsets = [
      ('Body', {'classes': ('full-width',), 'fields': ('category','author','image','title','body')})
    ]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body','post']
