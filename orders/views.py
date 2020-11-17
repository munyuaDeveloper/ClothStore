import requests
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem, Order


def order_create(request):
    cart = Cart(request)
    is_loading = False
    sent = False
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.pay = True
                order.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                order_items = OrderItem.objects.filter(order=order)
                # clear the cart
                cart.clear()
                # data = {
                #     "email": "munyuapeter07@gmail.com",
                #     "password": "SwordFish_123"
                # }
                # response = requests.post('https://uptechpay.com/api/getaccess', data)
                # access_details = response.json()
                # access_token = access_details.get('access_token')
                # headers = {
                #     'Authorization': 'Bearer ' + access_token
                # }
                # payload = {
                #     "user_phone": str(form.cleaned_data.get('phone')),
                #     "transaction_summary": str(order.id),
                #     "business_token": "bXVueXVhcGV0ZXIwN0BnbWFpbC5jb21LS1hwT3dpN1M0YlRlR2Q1Zkg5Nmk4OVhNdlFwUzFhVjAuMzQ3OTg4MDAgMTYwNTEwMDMzMw==",
                #     "amount": 1,
                #     "account_ref": "MCS"
                # }
                # print('payload', payload)
                # invoke_payment = requests.post('https://uptechpay.com/api/businesspay', headers=headers, data=payload)
                #
                # if invoke_payment:
                #     is_loading = False
                #     order = Order.objects.get(id=order.pk)
                #     order.paid = True
                #     order.save()

                # payment_response = invokeSTK.json()
                #  "amount": int(order.get_total_cost()),

                # Send Email Upon Success order placement
                # subject = f"Regarding an order you placed from MunyuaClothStore (#{order.pk})"
                # message = f"Your order has been received and is being prepared. We will contact you when it's ready for delivery \n\n " \
                #           f"Name: {order.first_name} {order.last_name}\n" \
                #           f"Phone number: {order.phone}\n" \
                #           f"Address: {order.address}\n" \
                #           f"Postal Code: {order.postal_code}\n" \
                #           f"Total Cost: # {order.get_total_cost() + 200}\n"
                #
                # send_mail(subject, message, 'munyuapeter07@gmail.com',
                #           [order.email])
                sent = True
                return render(request,
                              'customer-order.html',
                              {'order': order,
                               'order_items': order_items,
                               'email_sent': sent,
                               })
        else:
            form = OrderCreateForm()
            return render(request,
                          'checkout1.html',
                          {
                              'cart': cart,
                              'is_loading': is_loading,
                              'form': form
                          })
    else:
        return redirect('login')


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/order_details.html',
                  {'order': order})
