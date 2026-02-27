from django.shortcuts import render, redirect
from .models import Adherent,Association
from .forms import AdherentForm
from django.contrib.auth.decorators import login_required

@login_required
def liste_adherents(request):
    adherents = Adherent.objects.all()
    form = AdherentForm()
    associations = Association.objects.all()
    association_id = request.GET.get('association')
    if association_id:
        adherents = adherents.filter(association__id=association_id)

    if request.method == 'POST':
        form = AdherentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_adherents')

    return render(request, 'adherents/liste.html', {
        'adherents': adherents,
        'form': form,
        'associations': associations,
    })

@login_required
def supprimer_adherent(request, id):
    adherent = Adherent.objects.get(id=id)
    adherent.delete()
    return redirect('liste_adherents')

@login_required
def modifier_adherent(request, id):
    adherent = Adherent.objects.get(id=id)
    form = AdherentForm(instance=adherent)

    if request.method == 'POST':
        form = AdherentForm(request.POST, instance=adherent)
        if form.is_valid():
            form.save()
            return redirect('liste_adherents')

    return render(request, 'adherents/modifier.html', {
        'form': form,
        'adherent': adherent
    })