import importlib
import logging
import os
import pathlib

logger = logging.getLogger(__name__)

BASE_PATH = pathlib.Path(__file__).parent.parent


def pre_load_all_models():
    """
    Import all models.py modules.
    SQLAlchemy may fire errors like:

    > sqlalchemy.exc.InvalidRequestError: When initializing mapper Mapper[Blog(blog_blog)],
    > expression 'BlogInvite' failed to locate a name ('BlogInvite'). If this is a class name,
    > consider adding this relationship() to the <class 'blogs.models.Blog'>
    > class after both dependent classes have been defined.

    if some model wasn't imported and another model refers it with "relationship".
    Looks like the solution is to import all modules in advance.
    Some details: stackoverflow.com/a/59241485
    """
    logger.info('Starting preloading models...')
    for folder in sorted(next(os.walk(BASE_PATH))[1]):
        if not folder.startswith('_') and not folder.startswith('.'):
            for module_path in [
                BASE_PATH / folder / 'models.py',
                BASE_PATH / folder / 'signal_handlers.py',
            ]:
                if os.path.exists(module_path):
                    module_name = f'{folder}.models'
                    logger.debug('Loading %s', module_name)
                    importlib.import_module(module_name)
    logger.info('Preloading models done successully')
