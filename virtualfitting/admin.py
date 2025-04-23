from django.contrib import admin
from .models import  usregister,addproduct,Feedback,shopowner,Transaction,Addcart,Order


# Register your models here.

admin.site.register(usregister)
admin.site.register(shopowner)
admin.site.register(Feedback)
admin.site.register(addproduct)
admin.site.register(Addcart)
admin.site.register(Order)
admin.site.register(Transaction)