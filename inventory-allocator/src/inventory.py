class Inventory:

'''
Inventory allocator that outputs in accordance to order and shipment input
File: inventory.py
Must have both inventory_test.py and inventory.py in the same folder/directory
Usage: [python] [inventory_test.py] 
@Author: Benny Fung
'''
    # order: the desired item(s) 
    # shipment: different warehouses that may or may not contain the desired order(s) and its quantity

    def allocate(self, order, shipment):
        result = []
        product = {item: 0 for item in order.keys()}
        if len(product) == 0:
            return result

        for warehouse in shipment:
            name = warehouse['name']
            checkout = {}
            items = list(product.keys())
            for item in product.keys():
                available = warehouse['inventory'].get(item, -1)
                if available != -1:
                    expected = order[item] - product[item]
                    if expected > 0 and available > 0:
                        if expected <= available:
                            checkout[item] = expected
                        else:
                            product[item] += available
                            checkout[item] = available
            if checkout:
                result.append({name: checkout})
        
        return result