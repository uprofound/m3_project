from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow

from .ui import PermissionEditWindow, UserEditWindow

User = get_user_model()


class UserPack(ObjectPack):
    """
    ObjectPack для модели пользователей
    """

    model = User

    add_to_desktop = True
    add_to_menu = True

    add_window = edit_window = UserEditWindow


class GroupPack(ObjectPack):
    """
    ObjectPack для модели групп пользователей
    """

    model = Group

    add_to_desktop = True
    add_to_menu = True

    add_window = edit_window = ModelEditWindow.fabricate(model)


class ContentTypePack(ObjectPack):
    """
    ObjectPack для модели типов содержимого
    """

    model = ContentType

    add_to_desktop = True
    add_to_menu = True

    add_window = edit_window = ModelEditWindow.fabricate(model)


class PermissionPack(ObjectPack):
    """
    ObjectPack для модели прав пользователей
    """

    model = Permission

    add_to_desktop = True
    add_to_menu = True

    add_window = edit_window = PermissionEditWindow
