from day4_task1.item_package.item_module import Item

it1 = Item()
it2 = Item()

it1.desc = "Fan"
it1.id = 11
it1.quantity = 2
it1.price = 100.00

it2.desc = "Table"
it2.id = 22
it2.quantity = 15
it2.price = 200.00

it1.calc_final_price()
it2.calc_final_price()
