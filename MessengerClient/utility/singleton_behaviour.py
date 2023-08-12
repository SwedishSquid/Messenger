class SingletonBehaviour:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(SingletonBehaviour, cls).__new__(cls)
        return cls.__instance

    @classmethod
    def get_instance(cls):
        return cls.__instance
