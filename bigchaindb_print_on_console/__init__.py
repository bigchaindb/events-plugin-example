# Hello, and welcome to this super simple plugin for BigchainDB.  In order to
# extend BigchainDB with custom listeners, you have to declare to which
# events_types you are interested.  If you omit this declaration, you will be
# automatically subscribed to ALL events. You can find a list of supported
# events in the BigchainDB docs.
events_types = 1


# The second thing you have to do is to define a function called `run` that
# takes a queue and process it. Every object extracted from the queue has two
# attributes:
# - type (int): a number identifying the type of the event
# - data (obj): the object representing the event
def run(queue):
    print('**************************************')
    print('Hello from bigchaindb_print_on_console')
    print('**************************************')
    while True:
        event = queue.get()
        print('************************* Got new block ************************')
        print(event.data['id'])
        print('****************************************************************')
