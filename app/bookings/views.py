from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404

from .models import Room, Customer, Booking


def home(request):
    rooms = Room.objects.filter(
        status='available'
    ).order_by('number')

    return render(
        request,
        'bookings/home.html',
        {
            'rooms': rooms
        }
    )


def booking(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        guests = request.POST.get('guests')

        if not all([
            full_name,
            email,
            phone,
            check_in,
            check_out,
            guests
        ]):
            return render(
                request,
                'bookings/booking.html',
                {
                    'room': room,
                    'error': 'Vui lòng nhập đầy đủ thông tin.'
                }
            )

        try:
            check_in_date = datetime.strptime(
                check_in,
                '%Y-%m-%d'
            ).date()

            check_out_date = datetime.strptime(
                check_out,
                '%Y-%m-%d'
            ).date()

            guests = int(guests)

        except (ValueError, TypeError):
            return render(
                request,
                'bookings/booking.html',
                {
                    'room': room,
                    'error': 'Thông tin đặt phòng không hợp lệ.'
                }
            )

        if check_out_date <= check_in_date:
            return render(
                request,
                'bookings/booking.html',
                {
                    'room': room,
                    'error': 'Ngày trả phòng phải sau ngày nhận phòng.'
                }
            )

        if guests <= 0:
            return render(
                request,
                'bookings/booking.html',
                {
                    'room': room,
                    'error': 'Số khách phải lớn hơn 0.'
                }
            )

        if guests > room.capacity:
            return render(
                request,
                'bookings/booking.html',
                {
                    'room': room,
                    'error': (
                        f'Phòng này chỉ dành cho tối đa '
                        f'{room.capacity} khách.'
                    )
                }
            )

        overlapping_booking = Booking.objects.filter(
            room=room,
            status__in=['pending', 'confirmed'],
            check_in__lt=check_out_date,
            check_out__gt=check_in_date,
        ).exists()

        if overlapping_booking:
            return render(
                request,
                'bookings/booking.html',
                {
                    'room': room,
                    'error': (
                        'Phòng đã được đặt trong khoảng thời gian này.'
                    )
                }
            )

        customer, created = Customer.objects.get_or_create(
            email=email,
            defaults={
                'full_name': full_name,
                'phone': phone,
                'address': address,
            }
        )

        if not created:
            customer.full_name = full_name
            customer.phone = phone
            customer.address = address
            customer.save()

        number_of_nights = (
            check_out_date - check_in_date
        ).days

        total_price = room.price * number_of_nights

        Booking.objects.create(
            customer=customer,
            room=room,
            check_in=check_in_date,
            check_out=check_out_date,
            guests=guests,
            total_price=total_price,
            status='pending',
        )

        return redirect('home')

    return render(
        request,
        'bookings/booking.html',
        {
            'room': room
        }
    )
