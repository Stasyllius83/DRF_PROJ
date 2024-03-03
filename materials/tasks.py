
from materials.models import Subscription
from celery import shared_task


@shared_task
def check_subscribe_course(pk, model):
    users_subscribe= Subscription.objects.get(pk=pk)

    for user in users_subscribe:
        if user.status_subscrip:
            pass
