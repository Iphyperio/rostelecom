from django.shortcuts import render, HttpResponse


class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def amount(self):
        return self.price*self.quantity



def index(request):
    phone = Product('Телефон',10_000,5)
    food = Product('Хлеб',50, 10)
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        item = Product(name,price,quantity)
        print(f'Создан товар { item.name }')
    context = {'phone': phone,
               'food': food,}
    return render(request,'main/content.html',context)

    # 'colors': colors
    # colors = ['red','blue','green','white']
def about(request):
    return render(request,'main/about.html')


def contacts(request):
    return render(request,'main/contacts.html')

def plus(request,a,b):
    return HttpResponse(f'Сумма {a}+{b} = {a+b}')

from django.shortcuts import redirect
def custom_404(request,exception):
    return redirect('home')

    return HttpResponse('<h1>Очень жаль,'
                        ' но страница не найдена</h1>')