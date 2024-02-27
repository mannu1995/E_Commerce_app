from django.shortcuts import render,redirect

# Create your views here.
from django.http import JsonResponse
from .models import Product,Order,OrderItem,Post,PostAnalytics,ARContent
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def view_cart(request):
    order = Order.objects.filter(user=request.user).last()
    return render(request, 'view_cart.html', {'order': order})


def social_media(request):
    posts = Post.objects.all()
    analytics = PostAnalytics.objects.all()
    return render(request, 'dashboard.html',{'posts': posts, 'analytics': analytics})
    

def ar_home(request):
    ar_content = ARContent.objects.all()
    return render(request, 'ar_view.html', {'ar_content': ar_content})



def chat_room(request, room_name):
    return render(request, 'chat_room.html', {
        'room_name': room_name
    })

