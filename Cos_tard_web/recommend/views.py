from django.shortcuts import render
from django.http import HttpResponse
from media4.models import *
from recommend.models import *
from recommend.utils import *
from recommend.cloud import *
from recommend.xgb import *
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

    result=[]

    username = ["a_arang_", "doublesoup", "calarygirl_a", "yulri_0i", "yeondukong", "lamuqe_magicup", "fallininm", "im_jella_",
            "hamnihouse", "ssinnim", "yu__hyewon", "hyojinc_", "leojmakeup", "2__yun__2", "areumsongee", "makeup_maker_",
            "r_yuhyeju", "vivamoon", "risabae_art", "yujin_so", "kisy0729", "ponysmakeup"]
    
    for user in username:
        id_object = Users_fix.objects.filter(user_id=user).first()
        ig_ids = id_object.ig_id

        score = scoring(ig_ids, model_value, level=price_value, market_value=market_value, product_value=product_value)
        score['Username'] = user
        #pred = [score['expertised'], score['loyalty'], score['impact'], score['effect']]
        #preob = classifier(pred)
        result.append(score)
        #result.append(preob)

    result_df = pd.DataFrame(result)

    sorted_df = result_df.sort_values(by='Score', ascending=False)
    top5 = sorted_df.head(5)

    names = top5['Username'].tolist()
    ig_id5 = top5['id'].tolist()
    top_ig_id = ig_id5[0]
    followersnum = top5['followersnum'].tolist()
    # followers=top5['followerslev']
    engage=top5['engage']
    experts=top5['expertised']
    images=top5['image']
    impact=top5['impact']
    loyalty=top5['loyalty']
    effect=top5['effect']
    
    print(effect)

    # # followers=scale_list(followers, 1, 5)
    engage=scale_line(engage, 3, 5)
    s_experts=scale_list(experts, 0, 5)
    s_images=scale_list(images, 0, 5)
    s_impact=scale_list(impact, 0, 5)
    s_effect=scale_list(effect, 0, 5)
    s_loyalty=scale_list(loyalty, 0, 5)

    # print(s_effect)

    # # scaled by 0-5
    # s_experts = rescale_list(experts, old_max=16, new_max=5)
    # s_loyalty = rescale_list(loyalty, 13, 5)
    # s_impact = rescale_list(impact, 50, 5)
    # s_effect = rescale_list(effect, 50, 5)
    # s_images=scale_list(images, 0, 5)
    
    # print(s_impact)
    # print(s_loyalty)

    result1 = top5.to_dict(orient='records') # top5 score dict
    result2 = {'name':names, 'followersnum':followersnum , 'engage':engage, 'expert':s_experts, 'image':s_images, 'impact':s_impact, 'effect':s_effect, 'loyalty':s_loyalty} #top5 score detail

    brandlist = branding(top_ig_id)

    clouddata = wordreturn(names[0])

    context = { 'top_influencers': result1, 'chartdata':result2, 'top_ig_id':top_ig_id , 'brandlist': brandlist, 'clouddata':clouddata}

    return JsonResponse(context)


def error(request):
   return render(request,'recommend/error-404.html')

   