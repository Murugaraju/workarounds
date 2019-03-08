
from django.utils.functional import SimpleLazyObject
from datetime import datetime
from rest_framework.authtoken.models import Token
from .models import Expiry
import pytz
utc=pytz.UTC
class MuruganMiddleWare():
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self,request):
        
        print("printing request user object ", request.user, type(request.user))
        tokenkey=request.environ.get('HTTP_AUTHORIZATION',None)
        if tokenkey !=None:
            tokenkey=tokenkey.split(' ')[1]
            print("asdfasdfasdfsadfwsaedf",tokenkey)
            tkobj=Token.objects.get(key=tokenkey)
            time=tkobj.created
            expiry=Expiry.objects.get(user=tkobj.user).expirytime
            print(type(expiry))
            # print("SADsaedWAER",type(datetime.now()), expiry<datetime.now())
            # expiry=utc.localize(expiry)
            now=utc.localize(datetime.now())
            if expiry<now:
                print(" I am came")
                tkobj.delete()



        
           
            # if request.user.expiry_monitor.expirytime<datetime.now():
            #     request.user.auth_token.delete()


        


        response=self.get_response(request)
        print("printing request user object ", request.user, type(request.user))

        print("I m printing response",response, type(response))
        return response