import lcm
from Communication import message_t

def my_handler(channel, data):
    msg = message_t.decode(data)
    
    print("Received message on channel \"%s\"" % channel)
    print("   timestamp   = %s" % str(msg.timestamp))
    print("   Danger     = %s" % str(msg.danger))
    print("")

lc = lcm.LCM()
subscription = lc.subscribe("Obstacle", my_handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass

lc.unsubscribe(subscription)
