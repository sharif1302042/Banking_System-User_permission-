from django.contrib import admin

from USERs.models import Account, Topup, TranferBalance#, Payment

admin.site.register(Account)
admin.site.register(Topup)
admin.site.register(TranferBalance)
