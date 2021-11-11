# -*- coding: utf-8 -*-
import item_updater

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.__item_updater = item_updater.ItemUpdater()


    def update_quality(self):
        for item in self.items:
            self.__item_updater.update_item_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

