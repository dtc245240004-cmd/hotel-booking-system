from django.db import models


class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Phòng đơn'),
        ('double', 'Phòng đôi'),
        ('deluxe', 'Phòng Deluxe'),
        ('suite', 'Phòng Suite'),
    ]

    STATUS_CHOICES = [
        ('available', 'Còn trống'),
        ('maintenance', 'Bảo trì'),
    ]

    number = models.CharField(
        max_length=10,
        unique=True,
        verbose_name='Số phòng'
    )

    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPES,
        verbose_name='Loại phòng'
    )

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Giá mỗi đêm'
    )

    capacity = models.PositiveIntegerField(
        default=2,
        verbose_name='Sức chứa'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available',
        verbose_name='Trạng thái'
    )

    description = models.TextField(
        blank=True,
        verbose_name='Mô tả'
    )

    def __str__(self):
        return f'Phòng {self.number}'


class Customer(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name='Họ tên'
    )

    email = models.EmailField(
        unique=True,
        verbose_name='Email'
    )

    phone = models.CharField(
        max_length=20,
        verbose_name='Số điện thoại'
    )

    address = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Địa chỉ'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Chờ xác nhận'),
        ('confirmed', 'Đã xác nhận'),
        ('cancelled', 'Đã hủy'),
        ('completed', 'Đã hoàn thành'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name='Khách hàng'
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        related_name='bookings',
        verbose_name='Phòng'
    )

    check_in = models.DateField(
        verbose_name='Ngày nhận phòng'
    )

    check_out = models.DateField(
        verbose_name='Ngày trả phòng'
    )

    guests = models.PositiveIntegerField(
        default=1,
        verbose_name='Số khách'
    )

    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name='Tổng tiền'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Trạng thái'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f'{self.customer.full_name} - '
            f'Phòng {self.room.number}'
        )
