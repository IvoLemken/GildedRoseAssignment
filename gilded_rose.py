# -*- coding: utf-8 -*-
from ast import match_case
import re

###### Global Variables ######
MAX_ITEM_QUALITY = 50
##############################

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """
            Updates quality and sell_in values for all items
        """

        for item in self.items:
            match item.name :
                case item.name if re.search("aged brie",item.name,re.IGNORECASE) :
                    self.__update_quality_aged_brie(item)
                case item.name if re.search("backstage passes",item.name,re.IGNORECASE) :
                    self.__update_quality_backstage_passes(item)
                case item.name if re.search("sulfuras",item.name,re.IGNORECASE) :
                    continue
                case item.name if re.search("conjured",item.name,re.IGNORECASE) :
                    self.__update_quality_conjured(item)
                case _ :
                    self.__update_quality_regular(item)

    def __update_quality_regular(self, item):
        """ 
            Updates regular items:
            Quality decreases by 1 before, and by 2 after sell by date
        """

        if item.quality > 0:
            if item.sell_in > 0:
                item.quality -= 1
            else:
                item.quality = max(item.quality-2, 0)
        item.sell_in -= 1
        return item

    def __update_quality_aged_brie(self, item):
        """
            Updates Aged Brie: 
            Quality increases by 1 before, and by 2 after sell by date
        """

        if item.quality < MAX_ITEM_QUALITY:
            if item.sell_in > 0:
                item.quality += 1
            else:
                item.quality = min(item.quality+2, MAX_ITEM_QUALITY)
        item.sell_in -= 1
        return item

    def __update_quality_backstage_passes(self, item):
        """
            Updates backstage passes:
            Quality increases:
                - By 1 when there are more than 10 days until the sell by date
                - By 2 when there are 10 days or less 
                - By 3 when there are 5 days or less but
            Quality drops to 0 after the sell by date
        """

        match item.sell_in: 
            case item.sell_in if item.sell_in > 10 :
                item.quality = min(item.quality+1,MAX_ITEM_QUALITY)
            case item.sell_in if item.sell_in > 5 :
                item.quality = min(item.quality+2,MAX_ITEM_QUALITY)
            case item.sell_in if item.sell_in > 0 :
                item.quality = min(item.quality+3,MAX_ITEM_QUALITY)
            case _ :
                item.quality = 0
        item.sell_in -= 1
        return item

    def __update_quality_conjured(self, item):
        """
            Updates conjured items:
            Quality decreases by 2 before and by 4 after the sell by date
        """
        
        if item.quality > 0:
            if item.sell_in > 0:
                item.quality = max(item.quality-2, 0)
            else:
                item.quality = max(item.quality-4, 0)
        item.sell_in -= 1
        return item

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
