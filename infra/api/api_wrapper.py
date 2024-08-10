import requests
from infra.api import spotify_refresh_token
from infra.api.response_wrapper import ResponseWrapper


class APIWrapper:

    def __init__(self):
        self._request = None

    def make_request(self, method, url, params=None, body=None, headers=None, cookies=None, auth=None, json=None):
        try:
            # Make the HTTP request using the specified method
            response = requests.request(
                method,
                url,
                params=params,
                data=body,
                headers=headers,
                cookies=cookies,
                auth=auth,
                json=json
            )
            # Check if token is expired
            if response.status_code == 401:
                new_access_token = spotify_refresh_token.refresh_access_token()
                headers = headers or {}
                headers['Authorization'] = 'Bearer ' + new_access_token

                # Retry the request after refreshing the token
                response = requests.request(
                    method,
                    url,
                    params=params,
                    data=body,
                    headers=headers,
                    cookies=cookies,
                    auth=auth,
                    json=json
                )
            try:
                data = response.json()
            except ValueError:
                data = None
            # Raise an error for HTTP error responses
            response.raise_for_status()
            return ResponseWrapper(ok=response.ok, status=response.status_code, data=data)
        except requests.exceptions.HTTPError as e:
            print(f'HTTP error occurred: {e}')
            raise
        except Exception as e:
            print(f'Other error occurred: {e}')
            raise

    def get_request(self, url, params=None, body=None, headers=None, cookies=None, auth=None, json=None):
        return self.make_request('GET', url, params, body, headers, cookies, auth, json)

    def post_request(self, url, params=None, body=None, headers=None, cookies=None, auth=None, json=None):
        return self.make_request('POST', url, params, body, headers, cookies, auth, json)

    def delete_request(self, url, params=None, body=None, headers=None, cookies=None, auth=None, json=None):
        return self.make_request('DELETE', url, params, body, headers, cookies, auth, json)

    def put_request(self, url, params=None, body=None, headers=None, cookies=None, auth=None, json=None):
        return self.make_request('PUT', url, params, body, headers, cookies, auth, json)
