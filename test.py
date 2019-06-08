
bitcoin_list_1 = [
    {'ip': '50.250.156.59', 'port': 8333},
    {'ip': '50.250.156.59', 'port': 8333},
    {'ip': '50.250.156.59', 'port': 8333},
    {'ip': '35.53.87.161', 'port': 8},
]

node = bitcoin_list_1[2]
bitcoin_list_1.remove(node)
print(bitcoin_list_1)
# with open('bitcon_node.json', 'w') as bitcoin_node:
#     json.dump(bitcoin_list_1, bitcoin_node)
#     bitcoin_node.close()
# bitcoin_list = []
# with open('bitcon_node.json') as bitcoin_node:
#     bitcoin_list = json.load(bitcoin_node)
#     bitcoin_node.close()
#     print(bitcoin_list)
# eth_list = []
# bch_list = []
# ltc_list = []