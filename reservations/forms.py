from django import forms
import datetime
from reservations.models import RoomStandard
from reservations.models import Room
from reservations.models import Facility
from reservations.models import RoomFacility
from reservations.models import HotelGuest
from reservations.models import Reservation
from reservations.models import Extras
from reservations.models import ReservationExtras


class RoomStandardForm(forms.ModelForm):
    class Meta:
        model = RoomStandard
        fields = '__all__'

    standard_name = forms.CharField(max_length=50)
    price = forms.IntegerField()
    description = forms.CharField(max_length=300)


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

    room_number = forms.IntegerField()
    room_area = forms.IntegerField()
    room_standard_id = forms.ModelChoiceField(
        queryset=RoomStandard.objects,
        required=True
    )


class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = '__all__'

    facility_name = forms.CharField(max_length=50)


class RoomFacilityForm(forms.ModelForm):
    class Meta:
        model = RoomFacility
        fields = '__all__'

    room_id = forms.ModelChoiceField(
        queryset=Room.objects,
        required=True
    )
    facility_id = forms.ModelChoiceField(
        queryset=Facility.objects,
        required=True
    )


class HotelGuestForm(forms.ModelForm):
    class Meta:
        model = HotelGuest
        fields = '__all__'

    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=15)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

    reservation_number = forms.CharField(max_length=100)

    today = datetime.date.today()
    check_in_date = forms.DateField(
        widget=forms.SelectDateWidget,
        initial=today,
    )
    check_out_date = forms.DateField(
        widget=forms.SelectDateWidget,
        initial=today+datetime.timedelta(days=1)
    )
    number_of_guests = forms.IntegerField()
    hotel_guest_id = forms.ModelChoiceField(
        queryset=HotelGuest,
        required=True,
    )
    room_id = forms.ModelChoiceField(
        queryset=Room,
        required=True,
    )


class ExtrasForm(forms.ModelForm):
    class Meta:
        model = Extras
        fields = '__all__'

    extras_name = forms.CharField(max_length=50)
    price = forms.IntegerField()


class ReservationExtrasForms(forms.ModelForm):
    class Meta:
        model = ReservationExtras
        fields = '__all__'

    reservation_id = forms.ModelChoiceField(
        queryset=Reservation,
        required=True,
    )
    extras_id = forms.ModelChoiceField(
        queryset=Extras,
        required=True,
    )








