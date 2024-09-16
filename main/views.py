from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def main(request):
    context_d = {
            'title': 'main',
            'orders' : [
                {'name':'Двигатель бензиновый DLE30', 'price': '42000 ₽', 'img':'<img class="img_goods" src="http://127.0.0.1:9000/mysite2/1.jpg">'  ,'id': 1},
                {'name':'Сервопривод EMAX ES08MDII', 'price': '1620 ₽', 'img': '<img class="img_goods" src="http://127.0.0.1:9000/mysite2/2.jpg">', 'id': 2},
                {'name':'Двигатель T-Motor AT4120', 'price': '11980 ₽', 'img': '<img class="img_goods" src="http://127.0.0.1:9000/mysite2/3.jpg">', 'id': 3},
                {'name':'Адаптер для пропеллера', 'price': '42770 ₽', 'img': '<img class="img_goods" src="http://127.0.0.1:9000/mysite2/4.jpg">', 'id': 4},
                {'name':'Двигатель бензиновый DLE60', 'price': '152380 ₽', 'img': '<img class="img_goods" src="http://127.0.0.1:9000/mysite2/5.jpg">', 'id': 5},
                {'name':'Модуль для программ регуляторов', 'price': '4540 ₽', 'img': '<img class="img_goods" src="http://127.0.0.1:9000/mysite2/6.jpg">', 'id': 6},
            ],
            'value':'',
    }

    if request.method == 'GET':

        return render(request, 'main.html', context_d)
    
    else:

        #print(request.POST.get('text'))
        context_d['value'] = str(request.POST.get('text')).lower().capitalize()

        goods = {
            'title':'main',
            'orders':[

            ],
            'value':str(request.POST.get('text')).lower().capitalize(),
        }

        for var in context_d['orders']:
            if context_d['value'] in var['name']:
                goods['orders'].append(var)

        # for i in goods['orders']:
        #     print(i['name'])


        return render(request, 'main.html', goods)


def info(request, id):
    context_d ={
        'title':'info',
        'desc' : [
            {'name':'Двигатель бензиновый DLE30', 'price': '42000 ₽', 'desc':'Бензиновый двигатель от известного производителя моторов DLE, рекомендованный для использования на небольших самолётах.', 'img':'<img class="picG" src="http://127.0.0.1:9000/mysite2/1.jpg">'  ,'id': 1},
            {'name':'Сервопривод EMAX ES08MDII', 'price': '1620 ₽', 'desc':'Небольшой по размерам и по мощности сервопривод, Futaba/JR-совместимый.', 'img': '<img class="picG" src="http://127.0.0.1:9000/mysite2/2.jpg">', 'id': 2},
            {'name':'Двигатель T-Motor AT4120', 'price': '11980 ₽', 'desc':'Бесколлекторный высокоэффективный двигатель, рекомендуемый к использованию с пропеллерами 15"-16".', 'img': '<img class="picG" src="http://127.0.0.1:9000/mysite2/3.jpg">', 'id': 3},
            {'name':'Адаптер для пропеллера', 'price': '42770 ₽', 'desc':'Алюминиевый адаптер для тянущих пропеллеров. Устанавливается на вал диаметром 5мм. Используется для лопастей с осевым отверстием 3 мм.', 'img': '<img class="picG" src="http://127.0.0.1:9000/mysite2/4.jpg">', 'id': 4},
            {'name':'Двигатель бензиновый DLE60', 'price': '152380 ₽', 'desc':'Бензиновый двигатель от известного производителя моторов DLE, рекомендованный для использования на больших самолётах, таких как VolJet VT10 и VolJet VT20.', 'img': '<img class="picG" src="http://127.0.0.1:9000/mysite2/5.jpg">', 'id': 5},
            {'name':'Модуль для программ регуляторов', 'price': '4540 ₽', 'desc':'Модуль Hobbywing Program Card предназначен для программирования бесколлекторных регуляторов HobbyWing. Дружественный интерфейс делает программирование ESC простым и быстрым.', 'img': '<img class="picG" src="http://127.0.0.1:9000/mysite2/6.jpg">', 'id': 6},
        ]
    }

    con_ready = {
        'title':'info',
        'desc': context_d['desc'][id-1]
    }

    return render(request, 'info.html', con_ready)

def bucket(request):

    context_d = {
        'title':'bucket',
        'orders' : [
            {'name':'Двигатель бензиновый DLE30', 'price': '42000 ₽', 'img':'<img class="imgor" src="http://127.0.0.1:9000/mysite2/1.jpg">'  ,'id': 1},
            {'name':'Сервопривод EMAX ES08MDII', 'price': '1620 ₽', 'img': '<img class="imgor" src="http://127.0.0.1:9000/mysite2/2.jpg">', 'id': 2},
            {'name':'Двигатель T-Motor AT4120', 'price': '11980 ₽', 'img': '<img class="imgor" src="http://127.0.0.1:9000/mysite2/3.jpg">', 'id': 3},
        ]

    }

    return render(request, 'bucket.html', context_d)

