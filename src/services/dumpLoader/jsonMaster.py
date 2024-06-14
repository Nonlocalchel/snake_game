import json

from .fileMaster import FileMaster


class JsonMaster(FileMaster):
    suffix = '.json'

    @staticmethod
    def dump_data(data: any) -> any:
        return json.dumps(data, indent=4, ensure_ascii=False)

    @staticmethod
    def load_data(data: any) -> any:
        return json.loads(data.read())
