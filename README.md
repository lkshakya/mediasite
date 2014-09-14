=====
Articles
=====

Articles is a simple Django app to list Web-based News. For each
article  visitors can post the comments.


Quick start
-----------

1. Add "articles" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = ('your apps1',
    'articles',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^', include('articles.urls')),

3. Run `python manage.py migrate` to create the articles models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a articles, category (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/ to see the the article.

