import json

from redis import Redis

from backend.config.settings import REDIS_HOST


class Cache(object):
    def __init__(self, host=REDIS_HOST, port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.cache = None
        self.prefix = ""

        self.connect()

    def connect(self):
        try:
            self.cache = Redis(host=self.host, port=self.port, db=self.db)
        except Exception as exc:
            print(f'There was a problem connecting to the cache {exc}')
            raise Exception

    def get_all_keys(self):
        """Get all the keys in the cache"""
        if self.cache and type(self.cache) == Redis:
            try:
                all_keys = self.cache.keys(f'*{self.prefix}*')
                return all_keys
            except Exception as exc:
                print(f'There was a problem getting all the keys from the cache, exception was {exc}')
                raise Exception

    def get_value_by_key(self, key):
        """Get a specific value in cache by its key"""
        if self.cache and type(self.cache) == Redis:
            try:
                value_json = self.cache.get(f'{self.prefix}__{key}')
                if value_json:
                    print('cache hit')
                    value = json.loads(value_json)
                    return value
                else:
                    return None
            except Exception as exc:
                print(f'There was a problem getting data from the cache, exception was {exc}')
                raise Exception

    def check_if_key_exists(self, key):
        """Check if a key exists in the cache"""
        if self.cache and type(self.cache) == Redis:
            try:
                return self.cache.exists(f'{self.prefix}__{key}')
            except Exception as exc:
                print(f'There was a problem getting data from the cache, exception was {exc}')
                raise Exception

    def set_value_by_key(self, key, value):
        """Create a value in the cache using its key"""
        if self.cache and type(self.cache) == Redis:
            try:
                value_json = json.dumps(value)
                self.cache.set(f'{self.prefix}__{key}', value_json)
            except Exception as exc:
                print(f'There was a problem setting data in the cache, exception was {exc}')
                raise Exception

    def set_value_by_key_with_expiry(self, key, value, expiry_time_sec):
        """Create a value in the cache using its key, with an attached expiry time"""
        if self.cache and type(self.cache) == Redis:
            try:
                value_json = json.dumps(value)
                self.cache.setex(f'{self.prefix}__{key}', expiry_time_sec, value_json)
            except Exception as exc:
                print(f'There was a problem setting expiry data in the cache, exception was {exc}')
                raise Exception

    def delete_value_by_key(self, key):
        """Delete all values in the cache with the specified key"""
        if self.cache and type(self.cache) == Redis:
            try:
                self.cache.delete(f'{self.prefix}__{key}')
            except Exception as exc:
                print(f'There was a problem deleting data from the cache, exception was {exc}')
                raise Exception

    def flush_cache(self):
        """Delete all values in the cach"""
        if self.cache and type(self.cache) == Redis:
            try:
                self.cache.flushall()
            except Exception as exc:
                print(f'There was a problem flushing the cache, exception was {exc}')
                raise Exception


class TestCache(Cache):
    """
    This is the cache used to store data returned when calls are made to an API
    """

    def __init__(self):
        super(TestCache, self).__init__()
        self.prefix = "test"

