import json
from abc import ABC

import requests

from api.data.ApiMethod import ApiMethod


class ApiClientAbs(ABC):
    BASE_URL = 'https://127.0.0.1:8080/bot/api/'
    session = requests.Session()

    def __init__(self):
        pass

    def method(self, api_method: ApiMethod):
        # self.session.request(
        #     method=api_method.type.value[0],
        #     url=f"{self.BASE_URL}{api_method.method}",
        #     json=json.dumps(api_method.params)
        # )

        method = api_method.type.value[0],
        url = f"{self.BASE_URL}{api_method.method}",
        json_values = json.dumps(api_method.params)

        print(
            method, url, json_values
        )
