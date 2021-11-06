# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_sell_in_decrements_1_per_update(self):
        items = [Item(name="foo", sell_in=5, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_quality_decrements_1_per_update(self):
        items = [Item(name="foo", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    def test_quality_decrements_2_per_update_when_sell_by_passes(self):
        items = [Item(name="foo", sell_in=1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(7, items[0].quality)

    def test_quality_is_never_negative(self):
        items = [Item(name="foo", sell_in=1, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_brie_quality_increments_1_per_update(self):
        items = [Item(name="Aged Brie", sell_in=20, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)


    # It's not clear that Brie's double increment upon expiration
    # is this desired behavior,
    # but I'll document this behavior in a test so
    # that I know if the behavior changes.
    def test_brie_quality_increments_2_per_update_when_sell_by_passes(self):
        items = [Item(name="Aged Brie", sell_in=1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)

    def test_brie_quality_is_never_more_than_50(self):
        items = [Item(name="Aged Brie", sell_in=20, quality=49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_backstage_pass_quality_is_never_more_than_50(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=46)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(48, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=47)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_quality_never_decreases(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=3, quality=49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(49, items[0].quality)

    def test_backstage_pass_quality_increase_more_than_10_days(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=12, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)

    def test_backstage_pass_quality_increase_by_2_when_6_to_10_days_left(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        self.assertEqual(9, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].quality)
        self.assertEqual(8, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)
        self.assertEqual(7, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)
        self.assertEqual(6, items[0].sell_in)

    def test_backstage_pass_quality_increase_by_3_when_1_to_5_days_left(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)
        self.assertEqual(4, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)
        self.assertEqual(3, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)
        self.assertEqual(2, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

    # I'm interpretting "after the concert" to mean "sell_by=0"
    def test_backstage_pass_quality_is_0_after_sell_by(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
