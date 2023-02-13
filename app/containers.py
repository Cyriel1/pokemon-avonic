from dependency_injector import containers, providers

from .model.containers import Models
from .view.containers import Views
from .controller.containers import Controllers


class Application(containers.DeclarativeContainer):
    models = providers.Container(Models)
    views = providers.Container(Views)
    controllers = providers.Container(Controllers)
