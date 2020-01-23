def sandwich_order(topping1,topping2,topping3,topping4,topping5):
    print('Your sandwich has {}, {}, {}, {} and {}'.format(topping1,topping2,topping3,topping4,topping5))

sandwich_order('anchovies','bacon','cheese','sweetorn','tuna')

sandwich_list = [
    'item1',
    'item2',
    'item3'
]

sandwich_list.insert(0,'addeditem1')
sandwich_list.insert(1,'addeditem2')

print(sandwich_list)

