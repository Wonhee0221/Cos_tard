from media4.models import *

def follower_graph(ig_id):
    follower_trend = Users_info.objects.filter(ig_id=ig_id).order_by('-date').values('followers_count', 'date')
    return (follower_trend)


