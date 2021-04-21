from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限只容许对象的所有者编辑他
    """
    def has_object_permission(self, request, view, obj):
        # 读取权限容许任何请求
        # 所以我们总是允许GET, HEAD, OPTIONS请求
        if request.method in permissions.SAFE_METHODS:
            return  True

        # 只有该snippet的所有者才允许写权限
        return obj.owner == request.user

