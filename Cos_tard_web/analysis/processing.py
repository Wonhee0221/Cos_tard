from media4.models import *
from analysis.models import Feed
from django.db.models import Case, When, Value, IntegerField, Count, Q

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

    if average > 0:
        positive = True
    else:
        positive = False

    diff = growth[len(growth)-1]
 
    if diff > 0:
        diff = "+" + str(diff)
    else:
        diff = str(diff)

    total_growth = sum (growth_rates)
    average_growth = total_growth / len(yData)

    max_growth = max (growth_rates)
    index = growth_rates.index(max_growth)
    max_growth_date = xData[index]

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
        'positive': positive,
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

def get_media_data(ig_id):
    media = list(Media_fix.objects.filter(owner_id=ig_id).order_by('-timestamp')[:1].values())[0]
    timestamp = media.get('timestamp')
    datePart = timestamp[:10]
    timePart = timestamp[11:16]
    timestamp = datePart + " " + timePart

    media_max = Media_info.objects.filter(owner_id=ig_id).order_by('-date').values()[:18]
    filtered_media_max = [row for row in media_max if row.get('like_count') is not None]
    if filtered_media_max:
        max_like_row = max(filtered_media_max, key=lambda x: x['like_count'])
    else:
        max_like_row = None  # Handle

    media_id = max_like_row['media_id']
    like_count = max_like_row['like_count']
    media_url=max_like_row['media_url']
    media_max_detail = Media_fix.objects.get(media_id=media_id)
    max_length = 100
    truncated_caption = truncate_string(media_max_detail.caption, max_length)

    media_data = {
                'timestamp': timestamp,
                'media_id': media_id,
                'like_count' : like_count,
                'caption': truncated_caption,
                'permalink' : media_max_detail.permalink,
                'date': media_max_detail.timestamp[:10],
                'media_url' : media_url,  
            }
    
    return media_data

def get_statistic(ig_id,follower):
    statistics = Feed.objects.filter(ig_id=ig_id).order_by('date_index').values('media','like_count', 'comments_count')
    statistics = list(statistics)
    media = [int(data['media']) for data in statistics]
    like = [data['like_count']/follower*1000 for data in statistics]
    comment = [data['comments_count']/follower*100000 for data in statistics]

    average_like = sum(like) / len(like)
    average_comment = sum(comment) / len(comment)
    engagement = (average_like + average_comment)

    statistics = {
        'media': media,
        'comment': comment,
        'like' : like,
        'average_like': average_like,
        'average_comment': average_comment,
        'engagement': engagement
    }
    return statistics

def get_ratio(ig_id):
    content = Media_fix.objects.filter(owner_id=ig_id) \
    .annotate(
        is_null=Case(
            When(media_url__isnull=True, then=Value(1)),
            default=Value(0),
            output_field=IntegerField()
        ),
        is_jpg=Case(
            When(media_url__icontains='.jpg', then=Value(1)),
            default=Value(0),
            output_field=IntegerField()
        ),
        is_mp4=Case(
            When(media_url__icontains='.mp4', then=Value(1)),
            default=Value(0),
            output_field=IntegerField()
        )
    ) \
    .aggregate(
        null_count=Count('is_null', filter=Q(is_null=1)),
        jpg_count=Count('is_jpg', filter=Q(is_jpg=1)),
        mp4_count=Count('is_mp4', filter=Q(is_mp4=1))
    )
    null_count = content['null_count']
    jpg_count = content['jpg_count']
    mp4_count = content['mp4_count']

    context = {
        'null_count': null_count,
        'jpg_count': jpg_count,
        'mp4_count': mp4_count,
    }
    return context