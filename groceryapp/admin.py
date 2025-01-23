from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Carousel)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(Booking)
admin.site.register(Feedback)
