def run(queue):
    print('**************************************')
    print('Hello from bigchaindb_print_on_console')
    print('**************************************')
    while True:
        event = queue.get()
        print('************************* Got new block ************************')
        print(event.data['id'])
        print('****************************************************************')
