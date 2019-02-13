from django.shortcuts import render
from df_user.models import *
from .models import *



def order(request):
    user_id=request.session['user_id']
    user=UserInfo.objects.get(id=user_id)
    cart_ids=request.GET.getlist('cart_id')


    return render(request,'df_order/place_order.html.html')

def order_handle(request):
    pass
