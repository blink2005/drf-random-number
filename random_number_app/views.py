import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions


class RandomNumber(APIView):
    """
    Выводит случайное число от X до Y
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request): # Возвращает случайное число от x до y
        x = request.GET.get('x')
        y = request.GET.get('y')

        if x and y and self.is_number(x, y):
            random_number = random.randint(int(x), int(y))
            return Response({'random_number': random_number})
        else:
            return Response({'error': 'missing number attributes \'x\' and \'y\''}, status=403)
    
    def is_number(self, x, y): # Проверка атрибутов на числа
        try:
            int(x)
            int(y)
            return True
        except:
            return False
