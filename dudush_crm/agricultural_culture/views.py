import csv

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from .models import AgriculturalCulture
from .forms import AgriculturalCultureForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'agricultural_culture/culture_list.html')


@login_required
def agricultural_culture_list(request):
    cultures = AgriculturalCulture.objects.filter(user=request.user)
    context = {
        'cultures': cultures
    }
    return render(request, 'agricultural_culture/culture_list.html',
                  context)


@login_required
def delete_culture(request, culture_id):
    culture = get_object_or_404(AgriculturalCulture, id=culture_id)

    if culture.user != request.user:
        return HttpResponseForbidden("Ви не маєте права видаляти цю культуру.")

    if request.method == 'POST':
        culture.delete()
        return redirect('agricultural_culture_list')

    context = {
        'culture': culture
    }

    return render(request,
                  'agricultural_culture/culture_confirm_delete.html', context)


@login_required
def culture_edit(request, culture_id):
    culture = get_object_or_404(AgriculturalCulture, id=culture_id)

    if culture.user != request.user:
        return HttpResponseForbidden("Ви не маєте права редагувати цю культуру.")

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


@login_required
def culture_add(request):
    if request.method == 'POST':
        form = AgriculturalCultureForm(request.POST)
        if form.is_valid():
            culture = form.save(commit=False)
            culture.user = request.user
            culture.save()
            return redirect('agricultural_culture_list')
    else:
        form = AgriculturalCultureForm()
    context = {
        'form': form,
    }
    return render(request, 'agricultural_culture/culture_add.html', context)


@login_required
def export_cultures(request):
    cultures = AgriculturalCulture.objects.filter(user=request.user)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cultures.csv"'

    response.write('\ufeff')

    writer = csv.writer(response, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['ID', 'Title', 'Ripening Time', 'Planted Area', 'Planting Date', 'Field Number'])

    for culture in cultures:
        writer.writerow([
            culture.id,
            culture.title,
            culture.ripening_time,
            culture.planted_area,
            culture.planting_date,
            culture.field_number
        ])

    return response
