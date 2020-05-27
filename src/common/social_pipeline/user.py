from django.contrib.auth import login


def social_user(backend, uid, user=None, *args, **kwargs):
    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)

    user = social.user if social else None

    return {'social': social, 'user': user, 'is_new': user is None, 'new_association': social is None}


def login_user(strategy, backend, user=None, *args, **kwargs):
    login(backend.strategy.request, user, backend='src.users.backends.EmailOrUsernameModelBackend')
