from django.contrib import admin
from wallet.models import Wallet

# Register your models here.


class WalletAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'address')


admin.site.register(Wallet, WalletAdmin)
