from klab.members.models import Member


def member_for_user(request):
    context = dict(member_for_user=Member.member_for_user(request.user))
    return context