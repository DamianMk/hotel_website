from django.contrib import admin
from reservations.models import RoomStandard
from reservations.models import Room
from reservations.models import Facility
from reservations.models import RoomFacility
from reservations.models import HotelGuest
from reservations.models import Reservation
from reservations.models import Extras
from reservations.models import ReservationExtras


# Register your models here.


admin.site.register(RoomStandard)
admin.site.register(Room)
admin.site.register(Facility)
admin.site.register(RoomFacility)
admin.site.register(HotelGuest)
admin.site.register(Reservation)
admin.site.register(Extras)
admin.site.register(ReservationExtras)

