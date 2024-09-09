from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    result = None
    if request.method == "POST":
        num1 = request.POST.get('input1')
        num2 = request.POST.get('input2')
        operation = request.POST.get('operations')

        num1 = float(num1)
        num2 = float(num2)

        if operation == 'add':
            result = num1 + num2

        elif operation == 'subtract':
            result = num1 - num2

        elif operation == 'multiply':
            result = num1 * num2

        elif operation == 'divide':
            result = num1 / num2

    return render(request, 'calculator/index.html', {
        'result': result
    })