from django.shortcuts import render

posts = [
    {
        'author': 'Mark',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 6, 2019'
    },
    {
        'author': 'Joe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 6, 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
