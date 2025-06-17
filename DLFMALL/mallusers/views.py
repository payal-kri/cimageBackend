from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import*
from .models import*

class userSignup(APIView):
    def post (self,request):
        serliazerData= userDetailsSerializer(data=request.data)
        if serliazerData.is_valid():
            userDetails.objects.create(**serliazerData.data)
            message={"message": "User Signup Successfully"}
            return JsonResponse(message)
        return JsonResponse(serliazerData.errors)

class userMembership(APIView):
    def get(selfself,request,email):
        result = list(membershipDetails.objects.filter(email=email).values())
        message = {"Membership Details": result}
        return JsonResponse(message, safe=False)

