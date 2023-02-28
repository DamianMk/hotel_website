from django.db import models
from django.core.validators import MinValueValidator


class RoomStandard(models.Model):
    standard_name = models.CharField(max_length=50)
    price = models.SmallIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(max_length=300, default='')

    def __str__(self):
        return f'{self.standard_name}'


class Room(models.Model):
    room_number = models.SmallIntegerField(validators=[MinValueValidator(0)])
    room_area = models.SmallIntegerField(validators=[MinValueValidator(0)])
    room_standard_id = models.ForeignKey(
        RoomStandard, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f'{self.room_number}'


class Facility(models.Model):
    facility_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.facility_name}'


class RoomFacility(models.Model):
    room_id = models.ForeignKey(
        Room, on_delete=models.SET_NULL, null=True
    )
    facility_id = models.ForeignKey(
        Facility, on_delete=models.SET_NULL, null=True
    )


class HotelGuest(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Reservation(models.Model):
    reservation_number = models.CharField(max_length=100)
    booking_date = models.DateField(auto_now_add=True, editable=False)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.SmallIntegerField()
    hotel_guest_id = models.ForeignKey(
        HotelGuest, on_delete=models.SET_NULL, null=True
    )
    room_id = models.ForeignKey(
        Room, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f'{self.reservation_number}'


class Extras(models.Model):
    extras_name = models.CharField(max_length=50)
    price = models.SmallIntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.extras_name}'


class ReservationExtras(models.Model):
    reservation_id = models.ForeignKey(
        Reservation, on_delete=models.SET_NULL, null=True
    )
    extras_id = models.ForeignKey(
        Extras, on_delete=models.SET_NULL, null=True
    )






