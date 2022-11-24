import stripe
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from Rishat import settings
from my.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyItemView(View):
    def get(self, request, *args, **kwargs):
        product_id = self.kwargs["id"]
        product = Item.objects.get(id=product_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                            'description': product.description,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class ItemView(TemplateView):
    template_name = 'item.html'

    def get_context_data(self, **kwargs):
        product = Item.objects.get(id=self.kwargs['id'])
        context = super(ItemView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context
