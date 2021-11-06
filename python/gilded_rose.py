# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

        self.update_functions  = {
            "Sulfuras, Hand of Ragnaros": self.update_sulfuras,
            "Aged Brie": self.update_aged_brie,
            "Backstage passes to a TAFKAL80ETC concert": self.update_backstage_pass,
            "Conjured Mana Cake": self.update_conjured,
        }

    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)

    def update_item_quality(self, item):
        updater = self.update_functions.get(item.name, self.update_normal_item)
        updater(item)

    def update_normal_item(self, item):
        self.decrement_quality(item)
        if item.sell_in <= 0:
            self.decrement_quality(item)

        self.decrement_sell_in(item)

    def update_backstage_pass(self, item):
        if  item.sell_in > 10:
            self.increment_quality(item)
        elif 5 < item.sell_in <= 10:
            self.increment_quality(item, 2)
        elif 0 < item.sell_in <= 5:
            self.increment_quality(item, 3)
        else:
            item.quality = 0

        self.decrement_sell_in(item)

    def update_aged_brie(self, item):
        self.increment_quality(item)

        if item.sell_in <= 0:
             self.increment_quality(item)

        self.decrement_sell_in(item)

    def update_sulfuras(self, item):
        item.quality = 80

    def update_conjured(self, item):
        self.decrement_quality(item, 2)
        if item.sell_in <= 0:
            self.decrement_quality(item, 2)

        self.decrement_sell_in(item)

    def decrement_sell_in(self, item):
        item.sell_in = item.sell_in - 1

    def increment_quality(self, item, amount_to_increase=1):
        item.quality = min(50, item.quality + amount_to_increase)

    def decrement_quality(self, item, amount_to_decrease=1):
        item.quality = max(0, item.quality - amount_to_decrease)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

