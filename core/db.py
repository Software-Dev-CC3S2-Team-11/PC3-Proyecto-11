from datetime import datetime, timedelta
from typing import Dict, List, Optional


class URLData:
    """
    Representa una URL acortada con sus metadatos.
    Esta clase está diseñada para almacenar información sobre una URL acortada,
    incluyendo la URL original, un slug único, el propietario de la URL,
    la hora de creación, la hora de expiración y el número de visitas.
    """
    def __init__(self, original: str, slug: str, owner: str,
                 lifespan_days: int = 2):
        """
        Inicia una instancia de URLData.
        :param original: La URL original que se acortará.
        :param slug: El slug único para la URL acortada.
        :param owner: El propietario de la URL acortada.
        :param lifespan_days: El número de días que la URL acortada será válida.
        """
        self.original_url = original
        self.slug = slug
        self.owner = owner
        self.created_at = datetime.datetime.now()
        self.expires_at = self.created_at + timedelta(days=lifespan_days)
        self.visits = 0

    def increment_visits(self):
        """
        Incrementa el contador de visitas para la URL acortada.
        Este método se utiliza para rastrear cuántas veces se ha accedido a la URL acortada.
        """
        self.visits += 1 


class URLDatabase:
    """
    Una base de datos en memoria para almacenar objetos URLData.
    Esta clase proporciona métodos para añadir, recuperar y filtrar URLs
    basados en su propietario.
    Esta clase está diseñada como una base de datos en memoria para fines de demostración.
    """
    instance = None
    _urls: Dict[str, URLData] = {}

    def __new__(cls, *args, **kwargs):
        """
        Asegura que una instancia de URLData exista a la vez (Patrón Singleton).
        :return: La instancia Singleton de URLDatabase.
        """
        if not isinstance(cls._instance, cls):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def add(self, item: URLData):
        """
        Añade un elemento URLData a la base de datos en memoria.
        :param item: La instancia de URLData para ser añadido.
        """
        self._urls[item.slug] = item

    def get(self, slug: str) -> Optional[URLData]:
        """
        Recuperar una instancia de URLData por su slug.
        :param slug: La parte única de la URL acortada.
        :return: La instancia de URLData si se encuentra, de lo contrario None.
        """
        if not slug:
            return None
        return self._urls.get(slug)

    def by_owner(self, owner: str) -> List[URLData]:
        """
        Recupera todos los elementos URLData que pertenecen a un propietario específico.
        :param owner: El propietario de las URL acortadas.
        :return: Una lista de instancias URLData que pertenecen al propietario especificado.
        """
        if not owner:
            return []
        return [u for u in self._urls.values() if u.owner == owner]