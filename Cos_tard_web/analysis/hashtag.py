from django.db import models
from media4.models import Hashtags
import pandas as pd
from collections import Counter
import numpy as np

def count_hashtags(ig_id):
    count_text_queryset = Hashtags.objects.filter(owner_id=ig_id).order_by('owner_id').values('tags')
    count_text_list = list(count_text_queryset)
    tags = [data['tags'] for data in count_text_list if 'tags' in data]
    dataframe = pd.DataFrame({'tags': tags})
    dataframe['tags'] = dataframe['tags'].str.replace(' ', '').str.strip()
    dataframe['tags'].replace('', np.nan, inplace=True)
    dataframe.dropna(subset=['tags'], inplace=True)
    
    tags_combined = ','.join(dataframe['tags'])
    tags_list = tags_combined.split(',')
    
    counter = Counter(tags_list)
    sorted_dict = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    
    keys_only = list(sorted_dict.keys())

    key_count = 5  # 원하는 상위 키의 개수
    count_text = {f'tags{i+1}': keys_only[i] for i in range(key_count)}

    return count_text
