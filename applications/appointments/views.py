from django.shortcuts import render, get_object_or_404, redirect
from applications.appointments.models import RendezVous 
from .forms import RendezVousForm  
from django.utils.timezone import now

def liste_rendezvous(request):
    rdvs = RendezVous.objects.order_by('-date', 'heure')
    return render(request, 'rendezvous/liste.html', {'rdvs': rdvs})

def detail_rendezvous(request, pk):
    rdv = get_object_or_404(RendezVous, pk=pk)
    return render(request, 'rendezvous/detail.html', {'rdv': rdv})

def creer_rendezvous(request):
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_rendezvous')
    else:
        form = RendezVousForm()
    return render(request, 'rendezvous/form.html', {'form': form})

def modifier_rendezvous(request, pk):
    rdv = get_object_or_404(RendezVous, pk=pk)
    if request.method == 'POST':
        form = RendezVousForm(request.POST, instance=rdv)
        if form.is_valid():
            form.save()
            return redirect('liste_rendezvous')
    else:
        form = RendezVousForm(instance=rdv)
    return render(request, 'rendezvous/form.html', {'form': form})

def supprimer_rendezvous(request, pk):
    rdv = get_object_or_404(RendezVous, pk=pk)
    if request.method == 'POST':
        rdv.delete()
        return redirect('liste_rendezvous')
    return render(request, 'rendezvous/confirm_delete.html', {'rdv': rdv})