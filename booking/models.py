from django.db import models

class Booking(models.Model):

    SERVIZI = [
        ("taglio", "Taglio"),
        ("barba", "Barba"),
        ("combo", "Taglio + Barba"),
    ]

    nome_cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    data = models.DateField()
    ora = models.TimeField()
    servizio = models.CharField(max_length=20, choices=SERVIZI)

    completata = models.BooleanField(default=False)  # 👈 NUOVO

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("data", "ora")