from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'price','description')
@admin.register(Order)
class  OrderAdmin(admin.ModelAdmin):
    list_display = ('user','created_at','total_amount',)


@admin.register(OrderItem)
class OrderItemInline(admin.ModelAdmin):
    list_display = ('product','order','quantity','item_price')

@admin.register(SocialPlatform)
class SocialPlatFormAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','author','social_platform','created_at') 

@admin.register(ARContent)
class ARContentAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

@admin.register(ChatRoom)
class ChatroomAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Message)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('room','sender','content','timestamp')


