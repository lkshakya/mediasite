from haystack import indexes
from article.models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    created = indexes.DateTimeField(model_attr='created')

    def get_model(self):
        return Post

    def index_queryset(self,using=None):
        return self.get_model().objects.all()  
