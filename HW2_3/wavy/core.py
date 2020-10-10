class Application:

    def __init__(self, urlpatterns: dict, front_controllers: list):
        """
        :param urlpatterns: словарь связок url: view
        :param front_controllers: список front controllers
        """
        self.urlpatterns = urlpatterns
        self.front_controllers = front_controllers

    def __call__(self, env, start_response):
        # текущий url
        path = env['PATH_INFO']
        # получаем параметры запроса
        query_string = env['REQUEST_METHOD']
        request_params = None

        if method == 'GET':
            # превращаем параметры в словарь
            request_params = parse_input_data(query_string)
        elif method == 'POST':
            # получаем данные
            data = get_wsgi_input_data(env)
            # превращаем данные в словарь
            request_params = parse_wsgi_input_data(data)

        if path in self.urlpatterns:
            # получаем view по url
            view = self.urlpatterns[path]
            request = {}
            response = view(request, method, request_params)
            # добавляем в запрос данные из front controllers
            for controller in self.front_controllers:
                controller(request)
            # вызываем view, получаем результат
            code, text = view(request)
            # возвращаем заголовки
            start_response(code, [('Content-Type', 'text/html')])
            # возвращаем тело ответа
            return [text.encode('utf-8')]
        else:
            # Если url нет в urlpatterns - то страница не найдена
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Not Found"]

    def parse_input_data(self, data: str):
        result = {}
        if data:
            # делим параметры через &
            params = data.split('&')
            for item in params:
                # делим ключ и значение через =
                k, v = item.split('=')
                result[k] = v
        return result

    def get_wsgi_input_data(self, env) -> bytes:
        # получаем длину тела
        content_length_data = env.get('CONTENT_LENGTH')
        # приводим к int
        content_length = int(content_length_data) if content_length_data else 0
        # считываем данные если они есть
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            # декодируем данные
            data_str = data.decode(encoding='utf-8')
            # собираем их в словарь
            result = parse_input_data(data_str)
        return result