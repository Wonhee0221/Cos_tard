import requests
import unicodedata
import pandas as pd

"""user_id테이블"""

def crawl_users(admin_id, token, username):
    import requests
    url = f'https://graph.facebook.com/v17.0/{admin_id}?fields=business_discovery.username({username})%7Bbiography%2Cname%2Cusername%2Cfollows_count%2Cprofile_picture_url%2Cwebsite%2Cig_id%2Cfollowers_count%2Cmedia_count%2Cmedia.limit(5)%7Bcaption%2Ccomments_count%2Cid%2Cchildren%7Bmedia_url%2Cmedia_type%7D%2Clike_count%2Cmedia_product_type%2Cmedia_type%2Cmedia_url%2Cowner%2Cpermalink%2Ctimestamp%2Cusername%7D%7D&access_token={token}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # 4xx 또는 5xx 상태 코드에 대해 예외 발생
        data = response.json()
        user_info = data.get('business_discovery')

        if user_info:
            users_data = [
                user_info.get('ig_id'),
                user_info.get('name'),
                user_info.get('username'),
                user_info.get('biography'),
                user_info.get('website'),
            ]
            return users_data

    except requests.exceptions.RequestException as e:
        print(f"에러: {e}")
        return None, None


if __name__ == "__main__":
    admin_id = 17841402050732962
    token = "EAAIvJjhX7PgBO9abNiUoqdZBEc9cSUjW1J9Up1ZCMXiBlJNrmYL4rEiZAjPXHKpZCuZAzE9okSwYUgyTAOYKcdI5iTNv0nD7vq5jVXEIO37dtm0YccPtlGdIozP7A0VeVQ6FZCjysZCdETKBqVVqLP0fiLqzpFthXauUsMj8bgJZBTSdG0BDjTLIBW3BToEwbkwZD"

    # 예시: 특정 사용자명에 대한 사용자 정보 크롤링
    username = 'makeup_maker_'
    users = crawl_users(admin_id, token, username)

    # 이제 필요한대로 사용자 정보(사용자_정보)를 활용하면 됩니다.

#users

"""user_info"""

def crawl_user_info(admin_id, token, username):
    import requests
    from datetime import datetime
    url = f'https://graph.facebook.com/v17.0/{admin_id}?fields=business_discovery.username({username})%7Bbiography%2Cname%2Cusername%2Cfollows_count%2Cprofile_picture_url%2Cwebsite%2Cig_id%2Cfollowers_count%2Cmedia_count%2Cmedia.limit(5)%7Bcaption%2Ccomments_count%2Cid%2Cchildren%7Bmedia_url%2Cmedia_type%7D%2Clike_count%2Cmedia_product_type%2Cmedia_type%2Cmedia_url%2Cowner%2Cpermalink%2Ctimestamp%2Cusername%7D%7D&access_token={token}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # 4xx 또는 5xx 상태 코드에 대해 예외 발생
        data = response.json()
        user_info = data.get('business_discovery')
        now = datetime.now().date()
        formatted_date = now.strftime('%Y-%m-%d')

        if user_info:
            user_data = [
                user_info.get('ig_id'),
                formatted_date,
                user_info.get('follows_count'),
                user_info.get('followers_count'),
                user_info.get('media_count')
            ]
            return user_data

    except requests.exceptions.RequestException as e:
        print(f"에러: {e}")
        return None, None


if __name__ == "__main__":
    admin_id = 17841402050732962
    token = "EAAIvJjhX7PgBO9abNiUoqdZBEc9cSUjW1J9Up1ZCMXiBlJNrmYL4rEiZAjPXHKpZCuZAzE9okSwYUgyTAOYKcdI5iTNv0nD7vq5jVXEIO37dtm0YccPtlGdIozP7A0VeVQ6FZCjysZCdETKBqVVqLP0fiLqzpFthXauUsMj8bgJZBTSdG0BDjTLIBW3BToEwbkwZD"
    # 예시: 특정 사용자명에 대한 사용자 정보 크롤링
    username = 'makeup_maker_'
    user_info = crawl_user_info(admin_id, token, username)

    # 이제 필요한대로 사용자 정보(user_info)를 활용하면 됩니다.

#user_info

"""media_fix"""

def crawl_media_fix(admin_id, token, username):
    import requests
    from datetime import datetime
    url = f'https://graph.facebook.com/v17.0/{admin_id}?fields=business_discovery.username({username})%7Bbiography%2Cname%2Cusername%2Cfollows_count%2Cprofile_picture_url%2Cwebsite%2Cig_id%2Cfollowers_count%2Cmedia_count%2Cmedia.limit(5)%7Bcaption%2Ccomments_count%2Cid%2Cchildren%7Bmedia_url%2Cmedia_type%7D%2Clike_count%2Cmedia_product_type%2Cmedia_type%2Cmedia_url%2Cowner%2Cpermalink%2Ctimestamp%2Cusername%7D%7D&access_token={token}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # 4xx 또는 5xx 상태 코드에 대해 예외 발생
        data = response.json()
        user_info = data.get('business_discovery')

        media_list = []
        ig_id = user_info.get('ig_id')
        media_data = user_info.get('media').get('data')
        for media in media_data:
            caption = media.get('caption')
            media_id = media.get('id')
            media_url = media.get('media_url')
            permalink = media.get('permalink')
            timestamp = media.get('timestamp')
            dt_object = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z')
            # Extract the date and time in the desired format (combined)
            formatted_datetime = dt_object.strftime('%Y-%m-%d %H:%M:%S')

            media_list.append([
                ig_id,
                caption,
                media_id,
                media_url,
                permalink,
                formatted_datetime,
            ])
        return media_list

    except requests.exceptions.RequestException as e:
        print(f"에러: {e}")
        return None, None


if __name__ == "__main__":
    admin_id = 17841402050732962
    token = "EAAIvJjhX7PgBO9abNiUoqdZBEc9cSUjW1J9Up1ZCMXiBlJNrmYL4rEiZAjPXHKpZCuZAzE9okSwYUgyTAOYKcdI5iTNv0nD7vq5jVXEIO37dtm0YccPtlGdIozP7A0VeVQ6FZCjysZCdETKBqVVqLP0fiLqzpFthXauUsMj8bgJZBTSdG0BDjTLIBW3BToEwbkwZD"

    # 예시: 특정 사용자명에 대한 사용자 정보 크롤링
    username = 'makeup_maker_'
    media = crawl_user_info(admin_id, token, username)

    # 이제 필요한대로 사용자 정보(media)를 활용하면 됩니다.

"""media_info"""

def crawl_media_info(admin_id, token, username):
    import requests
    from datetime import datetime
    url = f'https://graph.facebook.com/v17.0/{admin_id}?fields=business_discovery.username({username})%7Bbiography%2Cname%2Cusername%2Cfollows_count%2Cprofile_picture_url%2Cwebsite%2Cig_id%2Cfollowers_count%2Cmedia_count%2Cmedia.limit(5)%7Bcaption%2Ccomments_count%2Cid%2Cchildren%7Bmedia_url%2Cmedia_type%7D%2Clike_count%2Cmedia_product_type%2Cmedia_type%2Cmedia_url%2Cowner%2Cpermalink%2Ctimestamp%2Cusername%7D%7D&access_token={token}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # 4xx 또는 5xx 상태 코드에 대해 예외 발생
        data = response.json()
        user_info = data.get('business_discovery')
        now = datetime.now().date()
        formatted_date = now.strftime('%Y-%m-%d')

        media_list = []
        ig_id = user_info.get('ig_id')
        media_data = user_info.get('media').get('data')
        for media in media_data:
            comments_count = media.get('comments_count')
            media_id = media.get('id')
            like_count = media.get('like_count')

            media_list.append([
                media_id,
                like_count,
                comments_count,
                formatted_date
            ])
        return media_list

    except requests.exceptions.RequestException as e:
        print(f"에러: {e}")
        return None, None

if __name__ == "__main__":
    admin_id = 17841402050732962
    token = "EAAIvJjhX7PgBO9abNiUoqdZBEc9cSUjW1J9Up1ZCMXiBlJNrmYL4rEiZAjPXHKpZCuZAzE9okSwYUgyTAOYKcdI5iTNv0nD7vq5jVXEIO37dtm0YccPtlGdIozP7A0VeVQ6FZCjysZCdETKBqVVqLP0fiLqzpFthXauUsMj8bgJZBTSdG0BDjTLIBW3BToEwbkwZD"

    # 예시: 특정 사용자명에 대한 사용자 정보 크롤링
    username = 'makeup_maker_'
    media_info = crawl_user_info(admin_id, token, username)

    # 이제 필요한대로 사용자 정보(media_info)를 활용하면 됩니다.