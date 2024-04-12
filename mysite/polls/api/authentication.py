from polls.user import FFUser
from polls.apikey import ApiKey

def auth(obj):
        username = obj.session.get('username')
        api_key = obj.session.get('api_key')
        is_auth = True
        context = {}
        try:
            puser = PollUser.objects.get(user__username=username)
            apk = ApiKey.objects.get(user=puser, api_key=api_key)
        except PollUser.DoesNotExist:
            is_auth = False
            context = {'error': 'User not found with given username'}
        except ApiKey.DoesNotExist:
            is_auth = False
            context = {'error': 'ApiKey does not match'}
        else:
            context = {
                'name': "{} {}".format(puser.user.first_name, puser.user.last_name),
                'username': username,
                'user_id': puser.id
            }

        return is_auth, context
