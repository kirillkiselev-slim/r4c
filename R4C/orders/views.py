from .models import Order
from robots.models import Robot
from customers.models import Customer
from django.shortcuts import render, redirect
from django.db.models import Count
from .forms import UserOrderForm
from django.contrib import messages


def check_availability(request):
    form = UserOrderForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            model = form.cleaned_data.get('model')
            version = form.cleaned_data.get('version')
            email = form.cleaned_data.get('email')
            robots = Robot.objects.filter(model=model, version=version)
            print(robots)
            available_robots_count = robots.count()
            print(available_robots_count)
            customer = Customer.objects.filter(email=email)

            if available_robots_count > 0 and robots.exists():
                robot = robots.first()

                print(customer)
                serial = robot.serial
                print(serial)
                order = Order(customer=customer, robot_serial=serial)
                order.save()
                robot.save()
                messages.success(request, "Order placed successfully.")

                return redirect('admin')

            else:
                messages.error(request, "The robot is not available at the moment. We will notify you")

        else:
            messages.error(request, "Enter a valid info")
    else:
        form = UserOrderForm()
    return render(request, 'orders/order.html', { form : 'form' })

