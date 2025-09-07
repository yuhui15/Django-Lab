from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Page, Like
from django.urls import reverse

def index(request):
    pages = []

    page_objects = Page.objects.all()
    for page in page_objects:
        pages.append({
            "title": page.title,
            "url": reverse("view", kwargs={ "id": page.id })
        })
    return render(request, "index.html", { "pages": pages })

def editor(request):
    return render(request, "editor.html")

def view_page(request, id):
    page = get_object_or_404(Page, pk=id)
    like_count = Like.objects.filter(page=page).count()
    return render(request, "page.html", { "title": page.title, "content": page.content, "id": id ,
        "like_count": like_count})

def save_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        page = Page(title=title, content=content)
        
        page.save()

        return redirect('/wiki/')
    return redirect('/wiki/')

def add_like(request, id):
    if request.method == 'POST':
        page = get_object_or_404(Page, pk=id)
        like = Like(page=page)
        
        like.save()

        return redirect(f'/wiki/page/{id}/')
    return redirect(f'/wiki/')

def view_likes(request, id):
    page = get_object_or_404(Page, pk=id)
    likes = Like.objects.filter(page=page)

    like_dates = [str(like.created_at) for like in likes]
    return render(request, "likes.html", { "id": page.id, "title": page.title, "likes": like_dates })

