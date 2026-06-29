import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url
        self._response = None

    def get_response_body(self):
        """
        Queries the targeted endpoint via an HTTP GET request
        and returns the raw BYTES data payload.
        """
        self._response = requests.get(self.url)
        return self._response.content

    def load_json(self):
        """
        Converts the response body directly into native Python structures.
        """
        if self._response is None:
            self.get_response_body()
            
        return self._response.json()