from .models import (
    BaseObjectPermission,
    BaseGenericObjectPermission,
    UserObjectPermissionBase,
    UserObjectPermissionAbstract,
    UserObjectPermission,
    GroupObjectPermissionBase,
    GroupObjectPermissionAbstract,
    GroupObjectPermission,
)
from ..utils import (
    get_group_model,
    get_permission_model
)

Group = get_group_model()
Permission = get_permission_model()

__all__ = [
    'BaseObjectPermission',
    'BaseGenericObjectPermission',
    'UserObjectPermissionBase',
    'UserObjectPermissionAbstract',
    'GroupObjectPermissionBase',
    'GroupObjectPermissionAbstract',
    'Permission',
    'Group',
    'UserObjectPermission',
    'GroupObjectPermission'
]
