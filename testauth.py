from pprint import pprint

def plugin_init(opts):
    print 'plugin_init'
    pprint(opts)

def plugin_cleanup():
    print 'plugin_cleanup'

def unpwd_check(username, password):
    print username, password
    return True
