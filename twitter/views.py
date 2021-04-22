from django.http import JsonResponse
import requests
import json
import environ

env = environ.Env()
env.read_env()
def daftar_follower(request, nama=""):
    cursor = -1
    pengikut=[]
    while(cursor !=0):
        follower = requests.get(url="https://api.twitter.com/1.1/followers/list.json?screen_name={}&&count=200&&cursor={}".format(nama, cursor) , headers={"Authorization": f"Bearer {env('BEARER_TOKEN')}"})
        data = follower.json()
        for x in data['users']:
            pengikut.append({x["name"]:x["screen_name"]})
        cursor=data["next_cursor"]
    return(JsonResponse({"data":pengikut}, safe=True))
def daftar_following(request, nama=""):
    cursor = -1
    mengikuti=[]
    while(cursor !=0):
        follower = requests.get(url="https://api.twitter.com/1.1/friends/list.json?screen_name={}&&count=200&&cursor={}".format(nama, cursor) , headers={"Authorization": f"Bearer {env('BEARER_TOKEN')}"})
        data = follower.json()
        for x in data['users']:
            mengikuti.append({x["name"]:x["screen_name"]})
        cursor=data["next_cursor"]
    return(JsonResponse({"data":mengikuti}, safe=True))

def serialize_sets(obj):
    if isinstance(obj, set):
        return list(obj)
def daftar_following_not_followers(request, nama=""):
    pengikut=[]
    cursor = -1
    while(cursor !=0):
        follower = requests.get(url="https://api.twitter.com/1.1/followers/list.json?screen_name={}&&count=200&&cursor={}".format(nama, cursor) , headers={"Authorization": f"Bearer {env('BEARER_TOKEN')}"})
        data = follower.json()
        for x in data['users']:
            pengikut.append({x["name"]:x["screen_name"]})
        cursor=data["next_cursor"]
    mengikuti=[]
    cursor = -1
    while(cursor !=0):
        follower = requests.get(url="https://api.twitter.com/1.1/friends/list.json?screen_name={}&&count=200&&cursor={}".format(nama, cursor) , headers={"Authorization": f"Bearer {env('BEARER_TOKEN')}"})
        data = follower.json()
        for x in data['users']:
            mengikuti.append({x["name"]:x["screen_name"]})
        cursor=data["next_cursor"]
    # return JsonResponse(json.dumps((mengikuti-pengikut), default=serialize_sets), safe=False)
    return JsonResponse({"data":[x for x in mengikuti if x not in pengikut ]}, safe=True)
