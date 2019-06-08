import json

from flask import Flask, make_response
from apscheduler.schedulers.background import BackgroundScheduler

from check_connect import check_connect

app = Flask(__name__)

bitcoin_list = []
with open('bitcon_node.json') as bitcoin_node:
    bitcoin_list = json.load(bitcoin_node)
    bitcoin_node.close()
    # print(bitcoin_list)
eth_list = []
bch_list = []
ltc_list = []

def check(list_node):
    for item in list_node:
        host = item['ip']
        port = item['port']
        flag = check_connect(host, port)
        if flag == False:
            list_node.remove(item)
    


def check_list():
    check(bitcoin_list)
    check(eth_list)
    check(bch_list)
    check(ltc_list)
    print("Checked!")


# print('Chuần bị công việc')
scheduler = BackgroundScheduler()
job = scheduler.add_job(check_list, 'interval', minutes=1)
scheduler.start()
# print("scheduled!")

@app.route("/api/get_node/<type>", methods=['GET'])
def check_connection(type):
    # print(type)
    list_node = []
    if type == 'btc':
        list_node = bitcoin_list
    elif type == 'eth':
        list_node = eth_list
    elif type == 'ltc':
        list_node = ltc_list

    response_list = []
    i = 0

    for item in list_node:
        # print("Checking for node {}".format(item) )
        host = item['ip']
        port = item['port']
        flag = check_connect(host, port)
        if flag == True:
            # print('Is conected to {}'.format(item))
            response_list.append(item)
            i = i + 1
        if i == 3:
            break
    return make_response(json.dumps(response_list))
