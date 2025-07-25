import os
import datetime
from django.http import JsonResponse
from django.shortcuts import render
from livekit import AccessToken, VideoGrant

from django.shortcuts import render

def video_call_view(request):
    return render(request, "videocall/video.html", {
        "livekit_url": "wss://videocall-d6wah1fm.livekit.cloud",  # Or from settings
    })


def get_token(request):
    identity = request.GET.get('identity', 'user1')
    room = request.GET.get('room', 'test-room')

    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")

    # Create the token
    token = AccessToken(api_key, api_secret, identity=identity, ttl=datetime.timedelta(hours=1))

    # Assign the grant directly (correct usage)
    token.grant = VideoGrant(room_join=True, room=room)

    # Return token as JWT
    return JsonResponse({'token': token.to_jwt(), 'room': room})


