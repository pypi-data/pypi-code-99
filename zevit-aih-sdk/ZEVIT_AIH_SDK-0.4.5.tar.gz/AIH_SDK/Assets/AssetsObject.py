from AIH_SDK.v2Object import v2Object


class AssetsObject(v2Object):
    
    def __init__(self):
        super().__init__()
        self._api = 'assets'
        self._version = '1.2'

