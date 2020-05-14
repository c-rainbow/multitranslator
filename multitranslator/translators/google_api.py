
import json 

from google.cloud import translate
from google.oauth2 import service_account
from google.oauth2 import credentials

from multitranslator import response

TRANSLATOR_NAME = 'google'


def FromConfig(config):
    if 'api_key' in config:
        pass  # Create REST client for API key
    if 'service_account' in config:
        json_file = config['service_account']['content']
        with open(json_file, 'rb') as fp:
            data = fp.read()
        json.loads(data)
        project_id = data['project_id']
        return GoogleTranslator(json_file, project_id)


class GoogleTranslator(object):
    def __init__(self, credential_file, project_id):
        credentials = service_account.Credentials.from_service_account_file(credential_file)
        self.client = translate.TranslationServiceClient(credentials=credentials)
        self.parent = self.client.location_path(project_id, 'global')

    def Translate(self, original_text, src, dest):
        response = self.client.translate_text(
            parent=self.parent,
            contents=[original_text],
            mime_type='text/plain',
            source_language_code=src,
            target_language_code=dest,
        )
        return response

if __name__ == '__main__':
    t = GoogleTranslator(None)
    r = t.Translate('하나 둘', 'ko', 'en')
    print(r)