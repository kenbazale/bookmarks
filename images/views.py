from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            form.cleaned_data
            new_item = form.save(commit=False)
            '# assign current user to the item'
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'image added successfully')
            '# redirtect to new created item detail view'
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    contects = {
           'form': form,
    }
    return render(request, 'images/image/create.html', contects)


def Image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    contects = {
        'image': image
    }
    return render(request, 'images/image/detail.html', contects)


@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ko'})
