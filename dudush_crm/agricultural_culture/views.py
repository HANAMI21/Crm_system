import csv

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import AgriculturalCulture
from .forms import AgriculturalCultureForm


# Create your views here.
def home(request):
    return render(request, 'agricultural_culture/culture_list.html')


def agricultural_culture_list(request):
    cultures = AgriculturalCulture.objects.all()
    context = {
        'cultures': cultures
    }
    return render(request, 'agricultural_culture/culture_list.html',
                  context)


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


def culture_add(request):
    if request.method == 'POST':
        form = AgriculturalCultureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agricultural_culture_list')
    else:
        form = AgriculturalCultureForm()
    context = {
        'form': form,
    }
    return render(request, 'agricultural_culture/culture_add.html', context)


def export_cultures(request):
    cultures = AgriculturalCulture.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cultures.csv"'

    # Добавляем BOM для корректного распознавания в Excel
    response.write('\ufeff')

    writer = csv.writer(response, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['ID', 'Title', 'Ripening Time', 'Planted Area', 'Planting Date', 'Field Number'])

    for culture in cultures:
        writer.writerow([culture.id, culture.title, culture.ripening_time, culture.planted_area, culture.planting_date,
                         culture.field_number])

    return response
