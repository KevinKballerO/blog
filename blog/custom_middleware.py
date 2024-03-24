from django.http import HttpResponse
import time

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response #llama al siguiente middleware

    def __call__(self, request): #realiza las operaciones antes de que se porcese la solicita
        start_time = time.time()  # Inicio del tiempo de procesamiento
        response = self.get_response(request)  # Procesa la solicitud y obtiene la respuesta
        end_time = time.time()  # Fin del tiempo de procesamiento
        response["X-Processing-Time"] = str(end_time - start_time) # Añadir el tiempo de procesamiento como un encabezado personalizado
        response['X-Custom-Header'] = 'Tiempo de procesamiento: ' + str(end_time - start_time)
         # Añade el encabezado personalizado a traves de X-Custom-Header incluyendo el tiempo de procesamientoa de la solicitud
        return response
