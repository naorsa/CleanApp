from django import template
from django.template.defaultfilters import stringfilter
from ..models import UserProfile
register = template.Library()

@register.filter(name='check')
@stringfilter
def checkuser(user):
    userid = user.user.id
    data = UserProfile.objects.get(user_id=userid)
    data = data.admin
    return data