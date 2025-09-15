class NSQLMockHelper:
    def __init__(self):
        self.client = {
            "db": {
                "collections": {
                    "users": dict(),
                    "profiles": dict(),
                    "pending_users": dict(),
                    "discussion_posts": dict(),
                    "request_headers": dict(),
                    "cookies": dict(),
                }
            }
        }

    def get_collection(self, collection_name):
        if self.client is None:
            return None
        # Handle case where collection_name is passed as dict
        if isinstance(collection_name, dict):
            return None
        collection = self.client["db"]["collections"].get(collection_name)
        return collection

    def upsert(self, collection_name, key, value):
        collection = self.get_collection(collection_name)
        if collection is None:
            return None
        collection[key] = value
        return collection[key]


DB_INSTANCE = NSQLMockHelper()
