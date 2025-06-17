from datetime import datetime, timedelta


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