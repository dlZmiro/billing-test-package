import dtlpy as dl
import logging


class Runner(dl.BaseServiceRunner):
    def __init__(self):
        self.logger = logging.getLogger('Testing')

    @staticmethod
    def change_item_metadata(item: dl.Item):
        item.metadata['user'] = {'test': 'Hello Zmiro'}
        item.update()
