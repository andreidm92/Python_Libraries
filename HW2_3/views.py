from wavy import render


def main_view(request, method, request_params):
    secret = request.get('secret_key', None)
    # Используем шаблонизатор
    return '200 OK', render('index.html', secret=secret)


def about_view(request, method, request_params):
    # Просто возвращаем текст
    return '200 OK', "About"

def contact_view(request, method, request_params):
    if method == 'GET':
        data = request.datas.get('data', None)
        title = 'Контакты'
        content = f'это {method} запрос с параметрами = {request_params}'
        renders = render('templates/contact.html', object_list=[{'title': title}, {'content': content}, {'data': data}])
    else:
        data = request.datas.get('data', None)
        print('email', data)
    return Response(OK, [renders])