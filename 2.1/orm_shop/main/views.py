from django.http import Http404
from django.shortcuts import render, get_object_or_404

from main.models import Car, Sale

def cars_list_view(request):
    query = request.GET.get('q')  # получаем строку из формы
    if query:
        cars = Car.objects.filter(model__icontains=query)  # нечувствительно к регистру
    else:
        cars = Car.objects.all()  # Получаем все авто из базы
    template_name = 'main/list.html'
    context = {
        'cars': cars,
        'query': query
    }
    return render(request, template_name, context)


def car_details_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)  # Получаем авто или 404
    template_name = 'main/details.html'
    context = {
        'car': car
    }
    return render(request, template_name, context)


def sales_by_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    sales = Sale.objects.filter(car=car)
    template_name = 'main/sales.html'
    context = {
        'car': car,
        'sales': sales
    }
    return render(request, template_name, context)

