from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from m3_ext.ui import all_components as ext
from objectpack.ui import BaseEditWindow, make_combo_box

User = get_user_model()


class UserEditWindow(BaseEditWindow):
    """
    Окно добавления и редактирования записи модели пользователя
    """

    def _init_components(self):
        super(UserEditWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label='password',
            name='password',
            allow_blank=False,
            anchor='100%'
        )

        self.field__last_login = ext.ExtDateField(
            label='last login',
            name='last_login',
            anchor='100%',
            format='d.m.Y'
        )

        self.field__is_superuser = ext.ExtCheckBox(
            label='superuser status',
            name='is_superuser'
        )

        self.field__username = ext.ExtStringField(
            label='username',
            name='username',
            allow_blank=False,
            anchor='100%'
        )

        self.field__first_name = ext.ExtStringField(
            label='first name',
            name='first_name',
            anchor='100%'
        )

        self.field__last_name = ext.ExtStringField(
            label='last name',
            name='last_name',
            anchor='100%'
        )

        self.field__email = ext.ExtStringField(
            label='email address',
            name='email',
            regex=r'.+@.+\..+',
            regex_text='Введённый email некорректен',
            anchor='100%'
        )

        self.field__is_staff = ext.ExtCheckBox(
            label='staff status',
            name='is_staff'
        )

        self.field__is_active = ext.ExtCheckBox(
            label='active',
            name='is_active',
            checked=True
        )

        self.field__date_joined = ext.ExtDateField(
            label='date joined',
            name='date_joined',
            allow_blank=False,
            anchor='100%',
            value=datetime.now().date(),
            format='d.m.Y'
        )

    def _do_layout(self):
        super(UserEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__is_superuser,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__is_staff,
            self.field__is_active,
            self.field__date_joined,
        ))

    def set_params(self, params):
        super(UserEditWindow, self).set_params(params)
        self.height = 'auto'


class PermissionEditWindow(BaseEditWindow):
    """
    Окно добавления и редактирования записи модели прав пользователей
    """

    def _init_components(self):
        super(PermissionEditWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label='name',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__content_type_id = make_combo_box(
            label='content type',
            name='content_type_id',
            allow_blank=False,
            anchor='100%',
            data=[(i.id, i.name) for i in ContentType.objects.all()],
            display_field='name',
            value_field='id',
        )

        self.field__codename = ext.ExtStringField(
            label='codename',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super(PermissionEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type_id,
            self.field__codename,
        ))

    def set_params(self, params):
        super(PermissionEditWindow, self).set_params(params)
        self.height = 'auto'
