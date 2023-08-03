# from django.db import models
# #from . import Users_fix

# instar_data= [
#   "a_arang_",
#   "doublesoup",
#   "calarygirl_a",
#   "yulri_0i",
#   "yeondukong",
#   "lamuqe_magicup",
#   "fallininm",
#   "im_jella_",
#   "hamnihouse",
#   "ssinnim",
#   "yu__hyewon",
#   "hyojinc_",
#   "leojmakeup",
#   "2__yun__2",
#   "areumsongee",
#   "makeup_maker_",
#   "r_yuhyeju",
#   "vivamoon",
#   "risabae_art",
#   "yujin_so",
#   "kisy0729",
#   "ponysmakeup",
# ]
# user_columns= ['ig_id', 'username', 'name', 'website']
# #user_columns= ['biography', 'name', 'username', 'follows_count', 'profile_picture_url', 'website', 'ig_id', 'followers_count', 'media_count']

# import requests
# import unicodedata
# import pandas as pd

# def crawl_user_info(username,limit):
#     admin_id=17841402050732962
#     #17841460966522233
#     token = "EAAIvJjhX7PgBO9abNiUoqdZBEc9cSUjW1J9Up1ZCMXiBlJNrmYL4rEiZAjPXHKpZCuZAzE9okSwYUgyTAOYKcdI5iTNv0nD7vq5jVXEIO37dtm0YccPtlGdIozP7A0VeVQ6FZCjysZCdETKBqVVqLP0fiLqzpFthXauUsMj8bgJZBTSdG0BDjTLIBW3BToEwbkwZD"
#     #"EAALHVkEeHV8BO4wwsy6ZAwa8QYO0FT0MRrO8xxM9029LI5xJFs7iiNSZB3o4rBTnqwZCY1ww1utoRXLp0pqvtVlEXpyNFP0gZAmQExyGDMZC9Kji2obXLmp0O4l0Q98VQda3k3rcUIQCQojxZCbfOwunJD3bUeQjxzNezDY8vjLPOM3ZAVC4I0dsstXSC9PvMCf"
#     url = f'https://graph.facebook.com/v17.0/{admin_id}?fields=business_discovery.username({username})%7Bbiography%2Cname%2Cusername%2Cfollows_count%2Cprofile_picture_url%2Cwebsite%2Cig_id%2Cfollowers_count%2Cmedia_count%2Cmedia.limit({limit})%7Bcaption%2Ccomments_count%2Cid%2Cchildren%7Bmedia_url%2Cmedia_type%7D%2Clike_count%2Cmedia_product_type%2Cmedia_type%2Cmedia_url%2Cowner%2Cpermalink%2Ctimestamp%2Cusername%7D%7D&access_token={token}'


#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # 4xx 또는 5xx 상태 코드에 대해 예외 발생
#         data = response.json()

#         return data.get('business_discovery')

#         # user_data_list= []

#         # if user_info:
#         #   # 사용자 정보를 리스트에 저장
#         #   user_data = [
#         #           user_info.get('biography'),
#         #           user_info.get('name'),
#         #           user_info.get('username'),
#         #           user_info.get('follows_count'),
#         #           user_info.get('profile_picture_url'),
#         #           user_info.get('website'),
#         #           user_info.get('ig_id'),
#         #           user_info.get('followers_count'),
#         #           user_info.get('media_count')
#         #       ]

#         #   user_data_list.append(user_data)


#     except requests.exceptions.RequestException as e:
#         print(f"에러: {e}")
#         return None

# #user_data_list = []
# for i in range(len(instar_data)):
#   user_info = crawl_user_info(instar_data[i],1)
#   if user_info:
#       # 얻은 사용자 정보를 기반으로 미디어 콘텐츠 가져오기
#       user_data = [
#             #user_info.get('biography'),
#             user_info.get('name'),
#             user_info.get('username'),
#             #user_info.get('follows_count'),
#             #user_info.get('profile_picture_url'),
#             user_info.get('website'),
#             user_info.get('ig_id'),
#             #user_info.get('followers_count'),
#             #user_info.get('media_count')
#         ]
#       #user_data_list.append(user_data)
#       Users_fix.objects.create(user_id = user_data[3], ig_id =user_data[1], username =user_data[0], website=user_data[2])

#   else:
#       print("사용자 정보를 가져오는데 실패했습니다.")

# #user_df = pd.DataFrame(user_data_list,columns=user_columns )

# #print(user_df)
