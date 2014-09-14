from django.shortcuts import render

# Create your views here.

from django import forms
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.mail import EmailMultiAlternatives
#from articles.models import Post,Category, Comment,Author
from articles.models import Post,PostForm,Category, Comment,CommentForm,Author,AuthorForm
#from haystack.forms import FacetedSearchForm,HighlightedSearchForm
#from haystack.query import SearchQuerySet
#from haystack.views import FacetedSearchView,SearchView,search_view_factory


def main(request):
    """Main listing."""
    categories = Category.objects.all().order_by("category_name")
    posts = Post.objects.all().order_by("-created")
    paginator = Paginator(categories, 100)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    try:
        categories = paginator.page(page)
    except (InvalidPage, EmptyPage):
        categories = paginator.page(paginator.num_pages)
    paginator = Paginator(posts, 12)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
       
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
    return render_to_response('articles/list.html', RequestContext(request, {'posts':posts,'categories':categories}))


def article_detail(request,article_id):
    """Main listing."""
    form = CommentForm(request.POST,None)
    if form.is_valid():
            cmodel = form.save()
            cmodel.save()
    comments = Comment.objects.filter(post_id=article_id).order_by("created")
    paginator = Paginator(comments, 100)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
    try:
        comments = paginator.page(page)
    except (InvalidPage, EmptyPage):
        comments = paginator.page(paginator.num_pages)
    categories = Category.objects.all().order_by("category_name")
    paginator = Paginator(categories, 100)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        categories = paginator.page(page)
    except (InvalidPage, EmptyPage):
        categories = paginator.page(paginator.num_pages)

    posts = Post.objects.filter(id=article_id) 
    paginator = Paginator(posts, 2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
    return render_to_response("articles/detail.html", RequestContext(request, {'posts':posts,'categories':categories,'comments':comments}))


def category_detail(request,cat_id):
    """Main listing."""
    form = CommentForm(request.POST,None)
    if form.is_valid():
        cmodel = form.save()
        cmodel.save()
    comments = Comment.objects.all().order_by("created")
    paginator = Paginator(comments, 100)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    try:
        comments = paginator.page(page)
    except (InvalidPage, EmptyPage):
        comments = paginator.page(paginator.num_pages)
    categories = Category.objects.all().order_by("category_name")
    paginator = Paginator(categories, 100)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
    try:
        categories = paginator.page(page)
    except (InvalidPage, EmptyPage):
        categories = paginator.page(paginator.num_pages)
    posts = Post.objects.filter(id=cat_id) 
    paginator = Paginator(posts, 2)

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1
    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
    return render_to_response("articles/list.html", RequestContext(request, {'posts':posts,'categories':categories,'comments':comments}))


def search_posts(request):
 
    categories = Category.objects.all().order_by("category_name")
    paginator = Paginator(categories, 100)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    try:
        categories = paginator.page(page)
    except (InvalidPage, EmptyPage):
        categories = paginator.page(paginator.num_pages)
    posts = Post.objects.all() 
    paginator = Paginator(posts, 2)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
 
    post_type = str(request.GET.get('q')).lower()
    sqs = SearchQuerySet().filter(text=post_type)
    clean_query = sqs.query.clean(post_type)
    result = sqs.filter(content=clean_query)
    #result=SearchQuerySet().all()
    #result = sqs.all()
    view = search_view_factory(
        view_class=SearchView,
        template='search/search.html',
        searchqueryset=result,
        form_class=HighlightedSearchForm
        )
    return view(request)


def comment_post(request,article_id):
    """Main listing."""
    form = CommentForm(request.POST,None)
    if form.is_valid():
            cmodel = form.save()
            cmodel.save()             
            #This is where you might chooose to do stuff.
            #cmodel.name = 'test1'
    categories = Category.objects.all().order_by("category_name")
    paginator = Paginator(categories, 100)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        categories = paginator.page(page)
    except (InvalidPage, EmptyPage):
        categories = paginator.page(paginator.num_pages)
    posts = Post.objects.filter(id=article_id)
    paginator = Paginator(posts, 2)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
    return render_to_response("articles/detail.html", RequestContext(request, {'posts':posts,'categories':categories}))


def authors(request):
    author = get_object_or_404(Author, pk=request.session['author_id'])
    form = AuthorForm(None,instance=author)
    return render_to_response('articles/author_edit.html',
                              {'author_form': form,
                               'author_id': request.session['author_id']},
                              context_instance=RequestContext(request))


def file_view(request):
    posts = Post.objects.filter(author_id=request.session['author_id'])
    paginator = Paginator(posts, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)
    return render_to_response("articles/myarticle.html", RequestContext(request, {'posts':posts}))


def upload_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            cmodel = form.save()
            cmodel.save()

    post = Post()
    form = PostForm(None,instance=post)
    return render_to_response('articles/writearticle.html',
                              {'post_form': form,
                               'author_id': request.session['author_id']},
                              context_instance=RequestContext(request))


def author_add(request):
        form = AuthorForm(request.POST,None)
        if form.is_valid():
            cmodel = form.save()
            #This is where you might chooose to do stuff.
            #cmodel.name = 'test1'
            request.session['author_id'] = cmodel.id
            cmodel.save()
            subject, from_email, to = 'hello', 'from@example.com', 'opposite800@gmail.com'
            text_content = 'This is an important message. New Author get registered'
            html_content = '<p>This is an <strong>important</strong> message.</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            #msg.send()
            request.session['author_id'] = cmodel.id
            return redirect(authors)
        return render_to_response('articles/author_add.html',
                                  {'author_form': form},
                                  context_instance=RequestContext(request))


def author_edit(request):
    if request.method == 'POST':
        Author.objects.get(pk=request.session['author_id']).update(name=request.POST['name'],image=request.FILES.get('image'),email=request.POST['email'])
    author = get_object_or_404(Author, pk=request.session['author_id'])
    form = AuthorForm(None,instance=author)
    return render_to_response('articles/author_edit.html',
                              {'author_form': form,
                               'author_id': request.session['author_id']},
                              context_instance=RequestContext(request))


def login(request):
    c = {}
    msg = "Invlaid Username or Password!"
    c.update(csrf(request))
    if request.method != 'POST':
        return render_to_response('articles/login.html', RequestContext(request, {}))
    try:
        m = Author.objects.get(email=request.POST['email'])
        if m.password == request.POST['password']:
            request.session['author_id'] = m.id
            return redirect(authors)
    except Author.DoesNotExist:
        #return render_to_response('student/login.html', {'message': message, 'dt': dt})
        return render_to_response('articles/login.html', RequestContext(request, {'messages':msg}))
     
    return render_to_response('articles/login.html', RequestContext(request, {}))


def logout(request):
    try:
        del request.session['author_id']
    except KeyError:
        pass
    return redirect(login)

