from ninja import NinjaAPI
from django.http import JsonResponse

from .models import Profile
from .schema import ProfileSchema, NotFoundSchema

api = NinjaAPI()

@api.get("/profiles/{profile_id_int}", response={200: ProfileSchema, 404: NotFoundSchema}) 
def profile(request, profile_id_int: int):
    try:
        profile = Profile.objects.get(profile_id_int=profile_id_int)
        return JsonResponse(ProfileSchema.from_orm(profile).dict(), status=200)

    except Profile.DoesNotExist:
        return 404, {"message": "Profile not found"}
