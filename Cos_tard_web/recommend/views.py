from django.shortcuts import render
from django.http import HttpResponse
from media4.models import *
from recommend.models import *
from recommend.utils import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd


def index(request): 
    
 return render(request,'recommend/table.html')

@csrf_exempt
def recommend(request):
    if request.method == 'POST':
        price_value = int(request.POST.get('price'))
        market_value = int(request.POST.get('market'))
        model_value = int(request.POST.get('model'))
        product_value = int(request.POST.get('product'))

    print(Activity.objects.filter(ig_id=336104951).values('imgcmt','infocmt','channelsize','contentpower','adratio','lifefeed', 'brandnum','reactfeed','followerfeed').first())
    
    result=[]

    username = ["a_arang_", "doublesoup", "calarygirl_a", "yulri_0i", "yeondukong", "lamuqe_magicup", "fallininm", "im_jella_",
            "hamnihouse", "ssinnim", "yu__hyewon", "hyojinc_", "leojmakeup", "2__yun__2", "areumsongee", "makeup_maker_",
            "r_yuhyeju", "vivamoon", "risabae_art", "yujin_so", "kisy0729", "ponysmakeup"]
    
    for user in username:
        id_object = Users_fix.objects.filter(user_id=user).first()
        ig_ids = id_object.ig_id
        score = scoring(ig_ids, model_value, level=price_value, market_value=market_value, product_value=product_value)
        score['Username'] = user
        result.append(score)

    result_df = pd.DataFrame(result)

    sorted_df = result_df.sort_values(by='Score', ascending=False)
    top5 = sorted_df.head(5)

    names = top5['Username'].tolist()
    ig_id5 = top5['id'].tolist()
    top_ig_id = ig_id5[0]
    followers=top5['followerslev']
    engage=top5['engage']
    experts=top5['expertised']
    images=top5['image']
    impact=top5['impact']
    effect=top5['effect']
    
    followers=scale_list(followers, 1, 5)
    engage=scale_line(engage, 3, 5)
    experts=scale_list(experts, 1, 5)
    images=scale_list(images, 1, 5)
    impact=scale_list(impact, 1, 5)
    effect=scale_list(effect, 1, 5)

    result1 = top5.to_dict(orient='records')
    result2 = {'name':names, 'follower':followers, 'engage':engage, 'expert':experts, 'image':images, 'impact':impact, 'effect':effect}

    context = { 'top_influencers': result1, 'chartdata':result2, 'top_ig_id':top_ig_id}

    return JsonResponse(context)


def error(request):
   return render(request,'recommend/error-404.html')
