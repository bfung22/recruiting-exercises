from Inventory import Inventory
import unittest

'''
Test cases for inventory allocation
File: inventory_test.py
Must have both inventory_test.py and inventory.py in the same directory
Usage: [python] [inventory_test.py]
@Author: Benny Fung
'''

class InventoryTest(unittest.TestCase):
	
    def test_nothing(self):
    	print("\nTest: blank")
    	order = {}
    	shipment = []
    	expected = []
    	self.assertEqual(inv.allocate(order, shipment), expected)
    	print("PASSED!")
		
    def test_no_input(self):
    	print("\nTest: no order input")
    	order = {}
    	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 10 , 'orange': 2}}
    	warehouse_2 = {'name':'dm', 'inventory': { 'salt': 20 , 'orange': 4}}
    	shipment = [warehouse_1, warehouse_2]
    	expected = []
    	self.assertEqual(inv.allocate(order, shipment), expected)
    	print("PASSED!")

    def test_no_warehouses(self):
    	print("\nTest: no warehouse exists")
    	order = { 'apple': 5, 'orange': 5}
    	shipment = []
    	expected = []
    	self.assertEqual(inv.allocate(order, shipment), expected)
    	print("PASSED!")

    def test_lacking_inventory(self):
    	print("\nTest: not enough inventory -> no allocation")
    	order = { 'apple': 5}
    	warehouse = {'name':'owd', 'inventory': { 'apple': 2 }}
    	shipment = [warehouse]
    	expected = []
    	self.assertEqual(inv.allocate(order, shipment), expected)
    	print("PASSED!")

    def test_lacking_inventory2a(self):
	print("\nTest: not enough inventory -> no allocation (case 2a: multiple warehouses, lack of quantity in oranges)")
	order = { 'apple': 50, 'orange': 50}
	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 20 , 'orange': 10}}
	warehouse_2 = {'name':'dm', 'inventory': { 'apple': 30 , 'orange': 10}}
	shipment = [warehouse_1, warehouse_2]
	expected = []
	self.assertEqual(inv.allocate(order, shipment), expected)
	print("PASSED!")

    def test_lacking_inventory2b(self):
	print("\nTest: not enough inventory -> no allocation (case 2b: lack of quantity all around)")
	order = { 'apple': 50, 'orange': 50}
	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 20 , 'orange': 10}}
	warehouse_2 = {'name':'dm', 'inventory': { 'apple': 20 , 'orange': 10}}
	warehouse_3 = {'name':'pn', 'inventory': { 'apple': 5 , 'orange': 20}}
	shipment = [warehouse_1, warehouse_2, warehouse_3]
	expected = []
	self.assertEqual(inv.allocate(order, shipment), expected)
	print("PASSED!")

    def test_lacking_inventory3(self):
	print("\nTest: not enough inventory -> no allocation (case 3: does not contain all items in order)")
	order = { 'apple': 10, 'orange': 21, 'banana': 2}
	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 20 , 'orange': 10}}
	warehouse_2 = {'name':'dm', 'inventory': { 'apple': 30 , 'orange': 10}}
	shipment = [warehouse_1, warehouse_2]
	expected = []
	self.assertEqual(inv.allocate(order, shipment), expected)
	print("PASSED!")

    def test_split(self):
    	print("\nTest: split warehouse inventory (case: single item)")
    	order = { 'apple': 10}
    	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 5}}
    	warehouse_2 = {'name':'dm', 'inventory': { 'apple': 5}}
    	shipment = [warehouse_1, warehouse_2]
    	expected = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
    	self.assertEqual(inv.allocate(order, shipment), expected)
    	print("PASSED!")

    def test_split2(self):
    	print("\nTest: split warehouse inventory (case: multiple items)")
    	order = { 'apple': 5, 'orange': 10}
    	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 2 , 'orange': 1}}
    	warehouse_2 = {'name':'dm', 'inventory': { 'apple': 3 , 'orange': 15}}
    	shipment = [warehouse_1, warehouse_2]
    	expected = [{'owd': {'apple': 2, 'orange': 1}}, {'dm': {'apple':3, 'orange': 9}}]
    	self.assertEqual(inv.allocate(order, shipment), expected)
    	print("PASSED!")

    def test_split3(self):
	print("\nTest: split warehouse inventory (case: even)")
	order = { 'apple': 10, 'orange': 10}
	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 2 , 'orange': 1}}
	warehouse_2 = {'name':'dm', 'inventory': { 'apple': 2 , 'orange': 8}}
	warehouse_3 = {'name':'pn', 'inventory': { 'apple': 6 , 'orange': 1}}
	shipment = [warehouse_1, warehouse_2, warehouse_3]
	expected = [{'owd': {'apple': 2, 'orange': 1}}, {'dm': {'apple':2, 'orange': 8}}, {'pn': {'apple':6, 'orange': 1}}]
	self.assertEqual(inv.allocate(order, shipment), expected)
	print("PASSED!")

    def test_split4(self):
    	print("\nTest: split warehouse inventory (case: uneven split)")
    	order = { 'apple': 10, 'orange': 15}
    	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 6 , 'orange': 5}}
    	warehouse_2 = {'name':'dm', 'inventory': { 'apple': 4 , 'orange': 12}}
    	shipment = [warehouse_1, warehouse_2]
    	expected = [{'owd': {'apple': 6, 'orange': 5}}, {'dm': {'apple': 4, 'orange': 10}}]
    	self.assertEqual(inv.allocate(order, shipment), expected)
    	print("PASSED!")

		
    def test_no_match(self):
    	print("\nTest: no matches")
    	order = { 'apple': 2, 'orange': 2}
    	warehouse_1 = {'name':'owd', 'inventory': { 'mango': 2 , 'pineapple': 2}}
    	warehouse_2 = {'name':'dm', 'inventory': { 'salt': 3 , 'pepper': 12}}
    	shipment = [warehouse_1, warehouse_2]
    	expected = []
    	self.assertEqual(inv.allocate(order, shipment), expected)
    	print("PASSED!")

    def test_blank_shipment(self):
    	print("\nTest: zero inventory in warehouses")
    	order = { 'apple': 5, 'orange': 5}
    	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 0 , 'orange': 0}}
    	warehouse_2 = {'name':'dm', 'inventory': { 'apple': 0 , 'orange': 0}}
    	shipment = [warehouse_1, warehouse_2]
    	expected = []
    	self.assertEqual(inv.allocate(order, shipment), expected)
    	print("PASSED!")

    def test_matching_all(self):
    	print("\nTest: exact match case 1")
    	order = { 'apple': 5}
    	warehouse = {'name':'owd', 'inventory': { 'apple': 5}}
    	shipment = [warehouse]
    	expected = [{'owd': {'apple': 5}}]
    	self.assertEqual(inv.allocate(order, shipment), expected)
    	print("PASSED!")

    def test_matching_all2(self):
	print("\nTest: exact match case 2 (multiple orders)")
	order = { 'apple': 50, 'orange': 50}
	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 50 , 'orange': 50}}
	shipment = [warehouse_1]
	expected = [{'owd': {'apple': 50, 'orange': 50}}]
	self.assertEqual(inv.allocate(order, shipment), expected)
	print("PASSED!")

    def test_matching_all3(self):
	print("\nTest: exact match case 2 (priority)")
	order = { 'apple': 50, 'orange': 50}
	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 50 , 'orange': 50}}
	warehouse_2 = {'name':'dm', 'inventory': { 'apple': 50 , 'orange': 50}}
	shipment = [warehouse_1, warehouse_2]
	expected = [{'owd': {'apple': 50, 'orange': 50}}]
	self.assertEqual(inv.allocate(order, shipment), expected)
	print("PASSED!")


    def test_matching_all4(self):
	print("\nTest: exact match case 3 (priority)")
	order = { 'apple': 50, 'orange': 50}
	warehouse_1 = {'name':'owd', 'inventory': { 'apple': 50 , 'orange': 50}}
	warehouse_2 = {'name':'dm', 'inventory': { 'apple': 50 , 'orange': 50}}
	warehouse_3 = {'name':'pn', 'inventory': { 'apple': 0 , 'orange': 50}}
	shipment = [warehouse_1, warehouse_2, warehouse_3]
	expected = [{'owd': {'apple': 50, 'orange': 50}}]
	self.assertEqual(inv.allocate(order, shipment), expected)
	print("PASSED!")

if __name__ == '__main__':
	inv = Inventory()
	unittest.main()
