from django.contrib import admin
from mayflower.models import admindb, catdb, icedb
# Register your models here.
admin.site.register(admindb)
admin.site.register(catdb)
admin.site.register(icedb)