# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    ############ Regular Item Tests ############
    def test_regular_item_before_sell_by(self):
        items = [Item("foo", 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual("foo", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_regular_item_after_sell_by(self):
        items = [Item("foo", 2, 10)]
        gilded_rose = GildedRose(items)

        for _ in range(5):
            gilded_rose.update_quality()

        self.assertEqual("foo", items[0].name)
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_regular_item_quality_minimum(self):
        items = [Item("foo", 2, 5)]
        gilded_rose = GildedRose(items)

        for _ in range(5):
            gilded_rose.update_quality()

        self.assertEqual("foo", items[0].name)
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    ############ Aged Brie Tests ############
    def test_aged_brie_before_sell_by(self):
        items = [Item("Aged Brie", 10, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_aged_brie_after_sell_by(self):
        items = [Item("Aged Brie", 2, 10)]
        gilded_rose = GildedRose(items)

        for _ in range(5):
            gilded_rose.update_quality()

        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(18, items[0].quality)

    def test_aged_brie_quality_maximum(self):
        items = [Item("Aged Brie", 2, 45)]
        gilded_rose = GildedRose(items)

        for _ in range(5):
            gilded_rose.update_quality()

        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
    
    ############ Sulfuras Tests ############
    def test_sulfuras_before_sell_by(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
     
    def test_sulfuras_after_sell_by(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        gilded_rose = GildedRose(items)

        for _ in range(5):
            gilded_rose.update_quality()

        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    ############ Backstage Passes Tests ############
    def test_backstage_passes_over_10_before_sell_by(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_passes_over_5_before_sell_by(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_passes_under_5_before_sell_by(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(13, items[0].quality)

    def test_backstage_passes_after_sell_by(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 10)]
        gilded_rose = GildedRose(items)

        for _ in range(5):
            gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_passes_quality_maximum(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 40)]
        gilded_rose = GildedRose(items)

        for _ in range(5):
            gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    
    ############ Multiple Items Tests ############
    def test_multiple_items(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49)]
        gilded_rose = GildedRose(items)

        for _ in range(3):
            gilded_rose.update_quality()

        repr(items) #Mostly to get the coverage up to 100%

        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(7, items[0].sell_in)
        self.assertEqual(17, items[0].quality)
        
        self.assertEqual("Aged Brie", items[1].name)
        self.assertEqual(-1, items[1].sell_in)
        self.assertEqual(4, items[1].quality)

        self.assertEqual("Elixir of the Mongoose", items[2].name)
        self.assertEqual(2, items[2].sell_in)
        self.assertEqual(4, items[2].quality)

        self.assertEqual("Sulfuras, Hand of Ragnaros", items[3].name)
        self.assertEqual(0, items[3].sell_in)
        self.assertEqual(80, items[3].quality)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[4].name)
        self.assertEqual(2, items[4].sell_in)
        self.assertEqual(50, items[4].quality)

        
if __name__ == '__main__':
    unittest.main()