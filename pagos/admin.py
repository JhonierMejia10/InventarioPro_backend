from django.contrib import admin
from .models import MedioPago, PagoVenta, PagoCompra

admin.site.register(MedioPago)
admin.site.register(PagoVenta)
admin.site.register(PagoCompra)