from django.shortcuts import render, redirect, get_object_or_404
from kegs.forms import BeerForm, KegForm
from kegs.models import Beer, Keg

# Create your views here.
def keg_detail(request, pk):
    beer_obj = Beer.objects.get(pk=pk)
    keg_objs = Keg.objects.filter(beer_id=beer_obj.id)
    context = {
        'kegs': keg_objs,
        'beers': beer_obj,
    }
    return render(request, 'keg_detail.html', context)

def beer_list(request, template_name='beer_list.html'):
    beer = Beer.objects.all()
    data = {}
    data['object_list'] = beer
    return render(request, template_name, data)

def keg_list(request, template_name='keg_list.html'):
    keg = Keg.objects.all()
    data = {}
    data['object_list'] = keg
    return render(request, template_name, data)

def beer_create(request, template_name='beer_form.html'):
    form = BeerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('kegs:beer_list')
    return render(request, template_name, {'form':form})

def keg_create(request, template_name='keg_form.html'):
    form = KegForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('kegs:keg_list')
    return render(request, template_name, {'form':form})

def beer_update(request, pk, template_name='beer_form.html'):
    beer = get_object_or_404(Beer, pk=pk)
    form = BeerForm(request.POST or None, instance=beer)
    if form.is_valid():
        form.save()
        return redirect('kegs:beer_list')
    return render(request, template_name, {'form':form})

def keg_update(request, pk, template_name='keg_form.html'):
    keg = get_object_or_404(Keg, pk=pk)
    form = KegForm(request.POST or None, instance=keg)
    if form.is_valid():
        form.save()
        return redirect('kegs:keg_list')
    return render(request, template_name, {'form':form})

def beer_delete(request, pk, template_name='beer_confirm_delete.html'):
    beer = get_object_or_404(Beer, pk=pk)
    if request.method=='POST':
        beer.delete()
        return redirect('kegs:beer_list')
    return render(request, template_name, {'object':beer})

def keg_delete(request, pk, template_name='keg_confirm_delete.html'):
    keg = get_object_or_404(Keg, pk=pk)
    if request.method=='POST':
        keg.delete()
        return redirect('kegs:keg_list')
    return render(request, template_name, {'object':keg})