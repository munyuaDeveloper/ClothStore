from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from orders.models import Order, OrderItem
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


def MyAccount(request):
    customer_orders = Order.objects.filter(user=request.user)

    context = {
        'customer_orders': customer_orders
    }
    return render(request,
                  'customer-orders.html', context
                  )


def OrderDetails(request, id):
    order_details = Order.objects.filter(id=id)
    order_items = OrderItem.objects.filter(order=id)
    context = {
        'order': order_details,
        'order_items': order_items
    }
    return render(request,
                  'customer-order.html', context
                  )
