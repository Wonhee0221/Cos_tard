from django.shortcuts import render
from django.http import HttpResponse
from media4.models import *
from recommend.models import *
from recommend.utils import *
#from .models import Users

# followers = Users_info.objects.order_by('date').values('followers_count')[0]
    # print(11111)
    # testrow=Comment.objects.values('totalcomment')
    # print(Users_fix.objects.filter(user_id='hamnihouse').first())
    # print(Users_info.objects.filter(ig_id=1579839464).order_by('date').values_list('followers_count').first()[0])
    # print(Comment.objects.filter(ig_id=1579839464).values_list('domain').first()[0])
    # print(Media_fix.objects.filter(owner_id=1579839464).values_list('media_id', flat=True))
    # print(Media_info.objects.filter(media_id='17982565250118885').values_list('comments_count', flat=True))
    # print(list(Media_fix.objects.filter(owner_id=1579839464).values_list('media_id', flat=True)))
    # print(cal_engagement(ig_id=1579839464))

    # firstdata = testrow[0]
    # context = {'followers' : firstdata}


# Create your views here.
def index(request): 
    scores = {}
    username = ["a_arang_", "doublesoup", "calarygirl_a", "yulri_0i", "yeondukong", "lamuqe_magicup", "fallininm", "im_jella_",
            "hamnihouse", "ssinnim", "yu__hyewon", "hyojinc_", "leojmakeup", "2__yun__2", "areumsongee", "makeup_maker_",
            "r_yuhyeju", "vivamoon", "risabae_art", "yujin_so", "kisy0729", "ponysmakeup"]

    for user in username:
        id_object = Users_fix.objects.filter(user_id=user).first()
        ig_ids = id_object.ig_id
        score = scoring(ig_ids)
        scores[user] = score  # Store score in the dictionary with the username as the key

    print(score)

    sorted_data = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    context = {'sorted_data': sorted_data}
    
    return render(request,'recommend/recommend.html', context)

