# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == "Sulfuras, Hand of Ragnaros":
                self.update_sulfuras(item)

            elif item.name == "Aged Brie":
                self.update_aged_brie(item)

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_pass(item)

            else:
                self.update_normal_item(item)

    def update_normal_item(self, item):
        self.decrement_quality(item)
        if item.sell_in <= 0:
            self.decrement_quality(item)

        self.decrement_sell_in(item)

    def update_backstage_pass(self, item):
        self.increment_quality(item)
        if item.sell_in < 11 and item.sell_in > 0:
            self.increment_quality(item)
        if item.sell_in < 6 and item.sell_in > 0:
            self.increment_quality(item)
        if item.sell_in <= 0:
            item.quality = 0

        self.decrement_sell_in(item)

    def update_aged_brie(self, item):
        self.increment_quality(item)

        if item.sell_in <= 0:
             self.increment_quality(item)

        self.decrement_sell_in(item)

    def update_sulfuras(self, item):
        item.quality = 80

    def decrement_sell_in(self, item):
        item.sell_in = item.sell_in - 1


    def increment_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def decrement_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

