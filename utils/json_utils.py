import json


class JsonUtils:
    @staticmethod
    def is_json(json_str: str) -> bool:
        try:
            json.loads(json_str)
        except json.decoder.JSONDecodeError:
            return False
        return True
