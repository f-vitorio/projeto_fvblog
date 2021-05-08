from django.shortcuts import render


posts= [
    { 
        'author': 'fvitorio',
        'title': 'Blog Post1',
        'content': 'primeiro conteudo',
        'date_posted': 'august 27,2021'
        },

  { 
        'author': 'vitorio',
        'title': 'Blog Post2',
        'content': ' conteudo',
        'date_posted': 'august 27,2031'
        },

   ]




def home(request):
    context = {
        'posts':posts
            }
    return render (request, 'blog/home.html',context)


def about(request):
    return render (request, 'blog/about.html')
