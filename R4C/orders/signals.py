from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from customers.models import Customer
from robots.models import Robot
from django.core.mail import send_mail

@receiver(post_save, sender=Order)
def notify_customer_on_availability(sender, instance, created, **kwargs):
    if created:
        robot = instance.robot_serial
        customer = instance.customer
        model = robot.model
        version = robot.version

        subject = f'Робот {model}, версии {version} теперь в наличии'
        message = (
            f'Добрый день!\n'
            f'Недавно вы интересовались нашим роботом модели {model}, версии {version}.\n'
            f'Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.'
        )
        from_email = 'kiselevkirill258@outlook.com'
        recipient_list = [customer.email]

        send_mail(subject, message, from_email, recipient_list)
