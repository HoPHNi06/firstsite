from django.db.models import OneToOneField, ImageField, DateField, PositiveSmallIntegerField, CharField, CASCADE, Model, DateTimeField
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.templatetags.static import static



class Profile(Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]

    user = OneToOneField(User, related_name="profile", on_delete=CASCADE)
    avatar = ImageField('Аватар:', upload_to="user/profiles/avatars/", null=True, blank=True)
    birthday = DateField(null=True, blank=True)
    gender = PositiveSmallIntegerField('Пол:', choices=GENDER_CHOICES, null=True, blank=True)
    phone = CharField('Номер телефона:', max_length=32, null=True, blank=True)
    address = CharField('Адрес:', max_length=255, null=True, blank=True)
    number = CharField('Номер дома:', max_length=32, null=True, blank=True)
    city = CharField('Город:', max_length=50, null=True, blank=True)

    created_at = DateTimeField('Дата создания:', auto_now_add=True)
    updated_at = DateTimeField('Изменён:', auto_now=True)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('user/img/profile-pic/default-profile-picture.png')
