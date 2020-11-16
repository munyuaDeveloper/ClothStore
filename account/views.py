
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
    paginator = Paginator(customer_orders, 5)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'customer_orders': paginated_queryset,
        'page_request_var': page_request_var,
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
