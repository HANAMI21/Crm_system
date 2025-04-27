from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import AgriculturalCulture
from .forms import AgriculturalCultureForm


# Create your views here.
def home(request):
    return render(request, 'agricultural_culture/culture_list.html')


def agricultural_culture_list(request):
    cultures = AgriculturalCulture.objects.all()
    return render(request, 'agricultural_culture/culture_list.html',
                  {'cultures': cultures})


def delete_culture(request, culture_id):
    culture = get_object_or_404(AgriculturalCulture, id=culture_id)

    if request.method == 'POST':
        culture.delete()
        return redirect('agricultural_culture_list')

    context = {
        'culture': culture
    }

    return render(request,
                  'agricultural_culture/culture_confirm_delete.html', context)


def culture_edit(request, culture_id):
    culture = get_object_or_404(AgriculturalCulture, id=culture_id)
    if request.method == 'POST':
        form = AgriculturalCultureForm(request.POST, instance=culture)
        if form.is_valid():
            form.save()
            return redirect('agricultural_culture_list')
    else:
        form = AgriculturalCultureForm(instance=culture)
    context = {
        'form': form,
    }
    return render(request, 'agricultural_culture/culture_edit.html', context)