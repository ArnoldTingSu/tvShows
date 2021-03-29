from django.shortcuts import render, redirect
from django.contrib import messages


from .models import Show


def all_shows(request):
    context = {
        'shows':Show.objects.all()
    }
    return render(request, 'all_shows.html', context)

def new(request):
    return render(request, 'new_show.html')

def create(request):
    errors = Show.objects.input_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release=request.POST['release_date'],
        desc=request.POST['description']
    )
    url = (Show.objects.last().id)
    return redirect(f'/shows/{url}')

def show_details(request, show_id):
    context = {
        'details': Show.objects.get(id=show_id)
    }
    return render(request, 'show_details.html', context)

def edit(request, show_id):
    context = {
        'show':Show.objects.get(id=show_id)
    }
    return render(request,'edit_show.html', context)

def update(request, show_id):
    current_info = Show.objects.get(id=show_id)
    url = show_id
    errors = Show.objects.input_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{url}/edit')
    else:
        if current_info.title != request.POST['title']:
            current_info.title = request.POST['title']
            current_info.save()
        if current_info.network != request.POST['network']:
            current_info.network = request.POST['network']
            current_info.save()
        if current_info.release != request.POST['release_date']:
            current_info.release = request.POST['release_date']
            current_info.save()
        if current_info.desc != request.POST['description']:
            current_info.desc = request.POST['description']
            current_info.save()
    return redirect(f'/shows/{url}')

def delete(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/')
    