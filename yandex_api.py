
import json
import requests
import response


TRANSLATOR_NAME = 'yandex'

_URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key={api_key}&lang={lang}'


def FromConfig(config):
    api_key = config.get('api_key')



class YandexTranslator(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def Translate(self, original_text, src, dest):
        lang_pair = '%s-%s' % (src, dest)
        full_url = _URL.format(api_key=self.api_key, lang=lang_pair)
        r = requests.post(full_url, data={'text': original_text})
        json_response = json.loads(r.text)
        lang_codes = json_response['lang'].split('-')

        rr = response.TranslationResponse(original_text, json_response['text'][0], lang_codes[0], lang_codes[1], TRANSLATOR_NAME, None)
        return rr



if __name__ == '__main__':
    api_key = ''
    t = YandexTranslator(api_key)
    r = t.Translate('This is a test sentence', 'en', 'ru')
    print(r)
    #print(dir(r))
    #print(r.text)
