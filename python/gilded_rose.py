# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name == "Aged Brie":
                self.increment_quality(item)

                if item.sell_in <= 0:
                     self.increment_quality(item)

                item.sell_in = item.sell_in - 1

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.increment_quality(item)
                if item.sell_in < 11 and item.sell_in > 0:
                    self.increment_quality(item)
                if item.sell_in < 6 and item.sell_in > 0:
                    self.increment_quality(item)
                if item.sell_in <= 0:
                    item.quality = 0

                item.sell_in = item.sell_in - 1

            else:
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                        if item.name == "Backstage passes to a TAFKAL80ETC concert":
                            if item.sell_in < 11:
                                if item.quality < 50:
                                    item.quality = item.quality + 1
                            if item.sell_in < 6:
                                if item.quality < 50:
                                    item.quality = item.quality + 1
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.sell_in = item.sell_in - 1
                if item.sell_in < 0:
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality


    def increment_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
