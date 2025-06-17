from datetime import datetime, timedelta
from typing import Dict, List, Optional

class URLData:
    """
    Represents a shortened URL with its metadata.
    This class is designed to store information about a shortened URL,
    including the original URL, a unique slug, the owner of the URL,
    the creation time, the expiration time, and the number of visits.
    """
    def __init__(self, original: str, slug: str, owner: str,
                 lifespan_days: int = 2):
        """
        Initializes a URLData instance.
        :param original: The original URL to be shortened.
        :param slug: The unique slug for the shortened URL.
        :param owner: The owner of the shortened URL.
        :param lifespan_days: The remaining time in which the shortened URL is valid.
        """
        self.original_url = original
        self.slug = slug
        self.owner = owner
        self.created_at = datetime.datetime.now()
        self.expires_at = self.created_at + timedelta(days=lifespan_days)
        self.visits = 0

    def increment_visits(self):
        """
        Increments the visit count for the shortened URL.
        This method is used to track how many times the shortened URL has been accessed.
        """
        self.visits += 1 


class URLDatabase:
    """
    A simple singleton in-memory database for storing URLData objects.
    This class provides methods to add, retrieve, and filter URLs based on their owner.
    This class is designed as a dummy in-memory database for demonstration purposes.

    """
    instance = None
    _urls: Dict[str, URLData] = {}

    def __new__(cls, *args, **kwargs):
        """
        Ensures that only one instance of URLDatabase is created (Singleton pattern).
        :return: The singleton instance of URLDatabase.
        """
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def add(self, item: URLData):
        """
        Adds a URLData item to the in-memory database.
        :param item: The URLData instance to be added.
        """
        self._urls[item.slug] = item

    def get(self, slug: str) -> Optional[URLData]:
        """
        Retrieves a URLData item by its slug.
        :param slug: The unique slug of the shortened URL.
        :return: The URLData instance if found, otherwise None.
        """
        return self._urls.get(slug)

    def by_owner(self, owner: str) -> List[URLData]:
        """
        Retrieves all URLData items owned by a specific owner.
        :param owner: The owner of the shortened URLs.
        :return: A list of URLData instances owned by the specified owner.
        """
        if not owner:
            return []
        return [u for u in self._urls.values() if u.owner == owner]