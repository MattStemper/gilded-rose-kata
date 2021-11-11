class ItemUpdater:

    def __init__(self):

        self.update_functions  = {
            "Sulfuras, Hand of Ragnaros": self.__update_sulfuras,
            "Aged Brie": self.__update_aged_brie,
            "Backstage passes to a TAFKAL80ETC concert": self.__update_backstage_pass,
            "Conjured Mana Cake": self.__update_conjured,
        }

    def update_item_quality(self, item):
        updater = self.update_functions.get(item.name, self.__update_normal_item)
        updater(item)

    def __update_normal_item(self, item):
        self.__decrement_quality(item)
        if item.sell_in <= 0:
            self.__decrement_quality(item)

        self.__decrement_sell_in(item)

    def __update_backstage_pass(self, item):
        if  item.sell_in > 10:
            self.__increment_quality(item)
        elif 5 < item.sell_in <= 10:
            self.__increment_quality(item, 2)
        elif 0 < item.sell_in <= 5:
            self.__increment_quality(item, 3)
        else:
            item.quality = 0

        self.__decrement_sell_in(item)

    def __update_aged_brie(self, item):
        self.__increment_quality(item)

        if item.sell_in <= 0:
            self.__increment_quality(item)

        self.__decrement_sell_in(item)

    def __update_sulfuras(self, item):
        item.quality = 80

    def __update_conjured(self, item):
        self.__decrement_quality(item, 2)
        if item.sell_in <= 0:
            self.__decrement_quality(item, 2)

        self.__decrement_sell_in(item)

    def __decrement_sell_in(self, item):
        item.sell_in = item.sell_in - 1

    def __increment_quality(self, item, amount_to_increase=1):
        item.quality = min(50, item.quality + amount_to_increase)

    def __decrement_quality(self, item, amount_to_decrease=1):
        item.quality = max(0, item.quality - amount_to_decrease)