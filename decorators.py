from django.contrib.auth.decorators import user_passes_test, permission_required

def group_required(*group_names,login_url):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated :
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, login_url=login_url)

# @group_required(('HR_Group'),login_url='login/')