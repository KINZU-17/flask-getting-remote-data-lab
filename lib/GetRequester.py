import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url
        # Keep a private reference to the response object state
        self._response = None

    def get_response_body(self):
        """
        Queries the targeted endpoint via an HTTP GET request
        and returns the raw text data payload string.
        """
        # Execute the network GET request using the requests library
        self._response = requests.get(self.url)
        
        # Return the raw text body string representation
        return self._response.text

    def load_json(self):
        """
        Converts the text response body directly into native Python structures.
        """
        # If the request hasn't run yet, run it now to establish the response state
        if self._response is None:
            self.get_response_body()
            
        # Parse the response text using the json library (or native .json() method)
        return self._response.json()