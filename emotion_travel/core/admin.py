from django.contrib import admin
from core.models import Place , Image , Category , Emotion
# Register your models here.

admin.site.register(Emotion)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Image)
