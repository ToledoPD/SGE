from django.db.models.signals import post_save
from django.dispatch import receiver
from outflows.models import Outflow
from services.notify import Notify


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, **kwargs):
    if instance.quantity > 0:
        product = instance.product
        product.quantity -= instance.quantity
        product.save()


@receiver(post_save, sender=Outflow)
def send_outflow_event(sender, instance, created, **kwargs):
    try:
        if created:
            notify = Notify()

            data = {
                'event_type': 'create_outflow',
                'timestamp': str(instance.created_at),
                'product': instance.product.title,
                'product_selling_price': float(instance.product.selling_price),
                'product_cost_price': float(instance.product.cost_price),
                'quantity': instance.quantity,
                'descripition': instance.descripition,
            }

            notify.send_order_event(data)
    except:
        pass
