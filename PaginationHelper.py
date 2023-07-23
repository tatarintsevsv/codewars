# https://www.codewars.com/kata/515bb423de843ea99400000a/train/python

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.items = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.items)

    # returns the number of pages
    def page_count(self):
        return len(self.items) // self.items_per_page + 1 if len(self.items) % self.items_per_page > 0 else 0

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= self.page_count():
            return -1
        return self.items_per_page if page_index < self.page_count()-1 else len(self.items) % self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        return (item_index // self.items_per_page) if (item_index >= 0) and (item_index < self.item_count()) else -1


import codewars_test as test

collection = range(1,25)
helper = PaginationHelper(collection, 10)

test.assert_equals(helper.page_index(0), 0)
test.assert_equals(helper.page_index(24), -1)
quit()

test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
test.assert_equals(helper.page_count(), 2)
test.assert_equals(helper.item_count(), 6)
test.assert_equals(helper.page_item_count(0), 4)
test.assert_equals(helper.page_item_count(1), 2)
test.assert_equals(helper.page_item_count(2), -1, 'since the page is invalid')

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid
