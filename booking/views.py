from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, timedelta
from django.db import IntegrityError

from .models import Booking


# 🏠 HOME

def home(request):
    prenotazioni = Booking.objects.all().order_by("data", "ora")[:5]  # ultime 5

    return render(request, "home.html", {
        "prenotazioni": prenotazioni
    })

# ✂️ PRENOTA CLIENTE
def prenota(request):
    errore = None

    if request.method == "POST":
        try:
            Booking.objects.create(
                nome_cliente=request.POST.get("nome_cliente"),
                telefono=request.POST.get("telefono"),
                data=request.POST.get("data"),
                ora=request.POST.get("ora"),
                servizio=request.POST.get("servizio"),
            )
            return redirect("home")

        except IntegrityError:
            errore = "❌ Orario già occupato"

    return render(request, "create.html", {"errore": errore})


# 📋 DASHBOARD BARBIERE
def prenotazioni(request):

    filtro = request.GET.get("filtro")

    prenotazioni = Booking.objects.all().order_by("data", "ora")

    if filtro == "oggi":
        prenotazioni = prenotazioni.filter(data=date.today())

    elif filtro == "domani":
        prenotazioni = prenotazioni.filter(data=date.today() + timedelta(days=1))

    return render(request, "prenotazioni.html", {
        "prenotazioni": prenotazioni,
        "filtro": filtro
    })


# ❌ ELIMINA PRENOTAZIONE
def elimina_prenotazione(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.delete()
    return redirect("prenotazioni")


# ✔ COMPLETA PRENOTAZIONE
def completa_prenotazione(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.completata = True
    booking.save()
    return redirect("prenotazioni")