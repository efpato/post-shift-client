# -*- coding: utf-8 -*-

import requests


__all__ = ['PostShiftClient', 'PostShiftClientException']


class PostShiftClientException(Exception):
    pass


class PostShiftClient:
    URL = 'https://post-shift.ru/api.php'

    def __init__(self, name='', domain=''):
        url = '{}?action=new&type=json'.format(PostShiftClient.URL)
        if name:
            url += '&name={}'.format(name)
        if domain:
            url += '&domain={}'.format(domain)

        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            raise PostShiftClientException(data['error'])

        self.__email = data['email']
        self.__key = data['key']

    @property
    def email(self):
        return self.__email

    @property
    def key(self):
        return self.__key

    def get_list(self):
        response = requests.get('{}?action=getlist&type=json&key={}'.format(
            PostShiftClient.URL, self.key))
        data = response.json()

        if 'error' not in data:
            return data

        if data['error'] == 'the_list_is_empty':
            return []

        raise PostShiftClientException(data['error'])

    def get_mail(self, id_, forced=1):
        response = requests.get(
            '{}?action=getmail&type=json&key={}&id={}&forced={}'.format(
                PostShiftClient.URL, self.key, id_, forced))
        data = response.json()

        if 'error' in data:
            raise PostShiftClientException(data['error'])

        return data['message']

    def livetime(self):
        response = requests.get('{}?action=livetime&type=json&key={}'.format(
            PostShiftClient.URL, self.key))
        data = response.json()

        if 'error' in data:
            raise PostShiftClientException(data['error'])

        return int(data['livetime'])

    def update(self):
        response = requests.get('{}?action=update&type=json&key={}'.format(
            PostShiftClient.URL, self.key))
        data = response.json()

        if 'error' in data:
            raise PostShiftClientException(data['error'])

        return int(data['livetime'])

    def clear(self):
        response = requests.get('{}?action=clear&type=json&key={}'.format(
            PostShiftClient.URL, self.key))
        data = response.json()

        if 'error' in data:
            raise PostShiftClientException(data['error'])

        return data['clear'] == 'ok'

    def delete(self):
        response = requests.get('{}?action=delete&type=json&key={}'.format(
            PostShiftClient.URL, self.key))
        data = response.json()

        if 'error' in data:
            raise PostShiftClientException(data['error'])

        return data['delete'] == 'ok'
