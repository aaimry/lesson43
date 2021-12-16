from django.shortcuts import render

# Create your views here.


def calculator_view(request):
    if request.method == 'GET':
        return render(request, 'calculator.html')
    elif request.method == 'POST':
        context = {
            'first_num': request.POST.get('first_num'),
            'second_num': request.POST.get('second_num'),
            'action': request.POST.get('action'),
            'result': None
        }
        if context['action'] == 'add':
            context['action'] = '+'
            context['result'] = float(context['first_num']) + float(context['second_num'])
        elif context['action'] == 'subtract':
            context['action'] = '-'
            context['result'] = float(context['first_num']) - float(context['second_num'])
        elif context['action'] == 'multiply':
            context['action'] = '*'
            context['result'] = float(context['first_num']) * float(context['second_num'])
        elif context['action'] == 'divide':
            context['action'] = '/'
            context['result'] = float(context['first_num']) / float(context['second_num'])

        return render(request, 'calculator.html', context)
