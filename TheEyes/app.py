import types
import threading
import time


class Wagon:
    def __init__(self):
        self.__dict__ = {}
        self.rail = []
        self.carriages = {}

    def append_rail(self, key, q):
        self.carriages[key] = q

    def move(self):
        pass


class Rails:
    def __init__(self):
        self.wagons = {}
        pass

    def rail(self, wagon, carriages):
        """A decorator that is used to register a view function for a
        given URL rule.  This does the same thing as :meth:`add_url_rule`
        but is intended for decorator usage::

            @app.route('/')
            def index():
                return 'Hello World'

        For more information refer to :ref:`url-route-registrations`.

        :param wagon: unique name of this wagon
        :param carriages: front carriages that it have to decide which
                        ones are correct to pass the msg to them
        :param options: the options to be forwarded to the underlying
                        :class:`~werkzeug.routing.Rule` object.  A change
                        to Werkzeug is handling of method options.  methods
                        is a list of methods this rule should be limited
                        to (``GET``, ``POST`` etc.).  By default a rule
                        just listens for ``GET`` (and implicitly ``HEAD``).
                        Starting with Flask 0.6, ``OPTIONS`` is implicitly
                        added and handled by the standard request handling.
        """
        def decorator(f):
            if wagon in self.wagons:
                raise Exception
            else:
                w = Wagon()
                w.move = types.MethodType(f, w)
                self.wagons[wagon] = (w, carriages)

        return decorator

    def configure(self):
        for key in self.wagons:
            wagon = self.wagons[key][0]
            for carriage_key in self.wagons[key][1]:
                if carriage_key not in self.wagons:
                    raise Exception
                else:
                    carriage = self.wagons[carriage_key]
                    if isinstance(carriage, tuple):
                        carriage = carriage[0]
                    wagon.append_rail(carriage_key, carriage.rail)
            self.wagons[key] = wagon

    def run(self, preworks=[]):
        self.configure()
        for work in preworks:
            work = threading.Thread(name=work.__name__, target=work)
            work.setDaemon(True)
            work.start()
        wagons = self.wagons.values()
        while True:
            most_busy_wagon = max(wagons, key=lambda wagon: len(wagon.rail))
            most_busy_wagon.move()

