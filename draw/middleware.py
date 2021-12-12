from datetime import timedelta, datetime
from . import views

from countdown.models import Countdown


class DrawMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            self.countdown = Countdown.objects.first()

            # check if increase the day
            self.increase_day()
            self.check_if_draw(request)

        # "BEFORE VIEW"
        response = self.get_response(request)
        # "AFTER VIEW"

        return response

    def increase_day(self):
        now = datetime.now()
        today = str(now).split(' ')[0]
        current_date = str(self.countdown.current_date).split(' ')[0]

        if current_date < today:
            if self.countdown.day <= 10:
                self.countdown.day = self.countdown.day + 1
                self.countdown.current_date = now
                self.countdown.save()
    

    def check_if_draw(self, request):
        print(self.countdown.day)
        if self.countdown.day == 11 and self.countdown.done == False:
            views.create_draw(request)