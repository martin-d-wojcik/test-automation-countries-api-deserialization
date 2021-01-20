import json
from requests import Response


class ResponseHelper:
    @staticmethod
    # parameter: response_json is of type: Response
    # parameter: key is of type: string
    # return type is: string
    def get_value_from_response(response_json: Response, key: str) -> str:
        # convert response to a dict
        response_dict = json.loads(response_json.text)

        # get the capitol
        value = response_dict[0][key]

        return value
