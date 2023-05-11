from flask import Flask
import requests


class TMDB(object):
    def __init__(self, app=None, api_key=None):
        self.base_url = 'https://api.themoviedb.org/3'
        self.api_key = api_key
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        self.api_key = app.config.get('TMDB_APP_KEY', self.api_key)

        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["flask-tmdb"] = self

    def search_movies(self, params={}):
        """
        搜索电影
        详见: https://developers.themoviedb.org/3/search/search-movies
        """

        url = f'{self.base_url}/search/movie?'

        params['api_key'] = self.api_key

        response = requests.get(url, params=params, verify=False)

        return response.json()

    def get_movie_details(self, movie_id: int, params: dict = {}):
        """
        获取电影详情
        详见: https://developers.themoviedb.org/3/movies/get-movie-details
        """

        url = f'{self.base_url}/movie/{movie_id}'
        params['api_key'] = self.api_key
        response = requests.get(url, params=params, verify=False)

        return response.json()

    def get_movie_external_ids(self, movie_id: int):
        """
        获取电影外部 ID
        详见: https://developers.themoviedb.org/3/movies/get-movie-external-ids
        """

        url = f'{self.base_url}/movie/{movie_id}/external_ids'
        response = requests.get(url, params={"api_key": self.api_key}, verify=False)

        return response.json()

    def get_movie_credits(self, movie_id: int, params: dict = {}):
        """
        获取电影工作人员
        详见: https://developers.themoviedb.org/3/movies/get-movie-credits
        """
        url = f'{self.base_url}/movie/{movie_id}/credits'
        params['api_key'] = self.api_key
        response = requests.get(url, params=params, verify=False)

        return response.json()

    def get_collection_details(self, collection_id, params: dict = {}):
        """
        获取系列详情
        详见: https://developers.themoviedb.org/3/collections/get-collection-details
        """

        url = f'{self.base_url}/collection/{collection_id}'
        params['api_key'] = self.api_key
        response = requests.get(url, params=params, verify=False)

        return response.json()

    def search_multi(self, params: dict = {}):
        """
        多类型搜索
        详见: https://developers.themoviedb.org/3/search/multi-search
        """

        url = f'{self.base_url}/search/multi'
        params['api_key'] = self.api_key
        response = requests.get(url, params=params, verify=False)

        return response.json()

    def get_tv_genres(self, params: dict = {}):
        """
        获取剧集分类
        详见: https://developers.themoviedb.org/3/genres/get-tv-list
        """

        url = f'{self.base_url}/genre/tv/list'
        params['api_key'] = self.api_key
        response = requests.get(url, params=params, verify=False)

        return response.json()

    def get_en_poster(self, posters, default_poster):
        """
        优先获取英文海报
        """
        file_path = None
        for poster in posters:
            if poster['iso_639_1'] == 'en':
                file_path = poster['file_path']
                break

        return file_path or default_poster

    def get_logo_path(self, logos):
        file_path = None
        for logo in logos:
            if logo['iso_639_1'] == 'en':
                file_path = logo['file_path']
                break

        if len(logos) > 0 and file_path is None:
            file_path = logos[0]["file_path"]

        return file_path


    def get_tv_details(self, movie_id: int, params: dict = {}):
        """
        获取剧集详情
        详见: https://developers.themoviedb.org/3/tv/get-tv-details
        """

        url = f'{self.base_url}/tv/{movie_id}'
        params['api_key'] = self.api_key
        response = requests.get(url, params=params, verify=False)

        return response.json()

    def get_tv_external_ids(self, tv_id: int):
        """
        获取电影外部 ID
        详见: https://developers.themoviedb.org/3/tv/get-tv-external-ids
        """

        url = f'{self.base_url}/tv/{tv_id}/external_ids'
        response = requests.get(url, params={"api_key": self.api_key}, verify=False)

        return response.json()
