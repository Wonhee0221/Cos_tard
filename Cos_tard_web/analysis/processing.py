from media4.models import *

def follower_graph(ig_id):

    ##검색한 인플루언서##
    follower_trend = Users_info.objects.filter(ig_id=ig_id).order_by('date').values('followers_count', 'date')
    follower_trend = list(follower_trend)
    xData = [data['date'] for data in follower_trend]
    yData = [data['followers_count'] for data in follower_trend]
   
    growth = []
    growth_rates = [0]

    for i in range(1, len(yData)):
        prev_value = yData[i - 1]
        current_value = yData[i]

        diff = current_value - prev_value
        growth_rate = ((current_value - prev_value) / prev_value) * 100
        growth.append(diff)
        growth_rates.append(growth_rate)

    total = sum (growth)
    average = total / len(growth)

    diff = growth[len(growth)-1]
       
    if diff > 0:
        diff = "+" + str(diff)
    else:
        diff = str(diff)

    total_growth = sum (growth_rates)
    average_growth = total_growth / len(yData)

    max_growth = max (growth_rates)
    index = growth_rates.index(max_growth)
    max_growth_date = xData[index-1]

    ##검색한 인플루언서 이외, 비교군##

    ##이상치
    exclude = "1579839464"

    all_users= Users_fix.objects.exclude(ig_id=ig_id).values('ig_id')
    all_users = [data['ig_id'] for data in all_users if data['ig_id'] != exclude]

    contrast = []
    
    for i in all_users:
        follower_other = Users_info.objects.filter(ig_id=i).order_by('date').values('followers_count','date')
        follower_other = list(follower_other)
        y = [data['followers_count'] for data in follower_other]
        growth_other = [0]

        for i in range(1, len(y)):
            prev_value = y[i - 1]
            current_value = y[i]
        
            growth_rate = ((current_value - prev_value) / prev_value) * 100
            growth_other.append(growth_rate)

        contrast.append(growth_other)

    contrast = list(zip(*contrast))
    growth_rate_average = [sum(data) / len(data) for data in contrast]

    total_growth_average = sum (growth_rate_average)
    average_average_growth = total_growth_average / len(y)

    if average_average_growth < average_growth:
        compare = "타 인플루언서들 보다 팔로워 증가율이 높습니다!"
    else:
        compare = "타 인플루언서들 보다 팔로워 증가율이 낮습니다"
    
    

    follower_trend = {

        'xData': xData,
        'yData': yData,
        'growth_rates' : growth_rates, #인플루언서 증가율
        'growth_rate_average': growth_rate_average, #비교군 증가율
        'average_growth' : str(round(average_growth, 5))+"%", #인플루언서 증가율 평균
        'average_average_growth' : average_average_growth, #비교군 증가율 평균
        'max_growth_date' : max_growth_date,
        'average' : round(average,2), #평균 증가량
        'diff' : diff,
        'compare' : compare
    }
    return (follower_trend)

def get_image(ig_id): 
    link = Media_info.objects.filter(owner_id=ig_id).order_by('-date').values('date', 'media_url')[:18]
    image_link = [link['media_url'] for link in link if link['media_url'] is not None and "_video_dashinit.mp4" not in link['media_url']]

    return image_link

def truncate_string(text, max_length, suffix="..."):
    if len(text) > max_length:
        truncated_text = text[:max_length - len(suffix)] + suffix
        return truncated_text
    return text

def get_media_data(date,ig_id):
    media = list(Media_fix.objects.filter(owner_id=ig_id).order_by('-timestamp')[:1].values())[0]
    timestamp = media.get('timestamp')
    datePart = timestamp[:10]
    timePart = timestamp[11:16]
    timestamp = datePart + " " + timePart

    media_max = Media_fix.objects.filter(owner_id=ig_id).order_by('-timestamp').values()[:50]
    media_data = {
                'timestamp': timestamp,
                'media_id': None,
                'caption': "해당 날짜에 게시물이 없습니다",
                'permalink' : None,
                'media_url' : None,  
            }
    try: 
        for x in media_max:
            if str(date) in x['timestamp']:
                media_id = x['media_id']
                max_media = Media_fix.objects.get(media_id=media_id)
                max_media_info = list(Media_info.objects.filter(media_id=media_id).order_by('-date')[:1].values())[0]
                max_length = 100
                truncated_caption = truncate_string(max_media.caption, max_length)

                media_data = {
                    'timestamp': timestamp,
                    'media_id': media_id,
                    'caption': truncated_caption,
                    'permalink' : max_media.permalink,
                    'media_url' : max_media_info.get('media_url'),  
                }
                break
    except: 
       pass

    return media_data


