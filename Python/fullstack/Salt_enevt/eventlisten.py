# @Time    : 2017/12/16 15:56
# @Author  : "Wang_Chongsheng"
# @File    : eventlisten.py
# @Software: PyCharm

# _*_ coding: utf-8 _*_
'''
Use this script dump the event data out to the terminal.It needs to know what the socke_dir is.
This script is a generic tool to test enent output
'''

# Import python libs
from __future__ import  absolute_import, print_function
import  optparse
import  pprint
import  time
import os

# Import Salt libs
import salt.utils.event

# Import 3rd-party libs
import salt.ext.six as six

def parse():
    '''
    Parse the script command line inputs
    '''
    parser = optparse.OptionParser()

    parser.add_option(
        '-s',
        '--sock-dir',
        dest='sock_dir',
        default='/var/run/salt',
        help=('Statically define the directory holding the salt unix socket for communication')
    )
    parser.add_option(
        '-n',
        '--node',
        dest='node',
        default='master',
        help=('State if the listener will attach to a master or a minion deemon,pass "master"or"minion"')
    )
    parser.add_option(
        '-f',
        '--func_count',
        default='',
        help=('Return a count of the number of minions whicj have replied to a job with a give func.')
    )
    parser.add_option(
        '-i',
        '--id',
        default='',
        help=('If connecting to a live master or minion,pass in the id')
    )
    parser.add_option(
        '-t',
        '--transport',
        default='zeromq',
        help=('Transport to use.(Defailt: \'zeromq\')')
    )

    options,args = parser.parse_args()

    opts = {}

    for k,v in six.iteritems(options.__dict__):
        if v is not None:
            opts[k] = v
    opts['sock_dir'] = os.path.join(opts['sock_dir'],opts['node'])

    if 'minion' in options.node:
        if args:
            opts['id'] = args[0]
            return opts
        if options.id:
            opts['id'] = options.id
        else:
            opts['id'] = options.node

    return

def check_access_and_print_warning(sock_dir):
    '''
    Check if this user is able to access the socket
    directory and print a warning if not
    :param sock_dir:
    :return:
    '''
    if (os.access(sock_dir, os.R_OK) and
            os.access(sock_dir, os.W_OK) and
            os.access(sock_dir, os.X_OK)):
        return
    else:
        print('WARNING:Events will not be reported (not able to access {0})'.format(sock_dir))

def listen(opts):
    '''
    Attach to the pub socket and grab messages
    :param opts:
    :return:
    '''
    event = salt.utils.event.get_event(
        opts['node'],
        sock_dir=opts['sock_dir'],
        transport = opts['transport'],
        opts=opts,
        listen=True
    )
    check_access_and_print_warning(opts['sock_dir'])
    print(event.puburi)
    jib_counter = 0
    found_minions = []
    while True:
        ret = event.get_event(full=True)
        if ret is None:
            continue
        if opts['fun_count']:
            data = ret.get('data',False)
            if data:
                if 'id' in six.iteritems(data) and data.get('id',False) not in found_minions:
                    if data['run'] == opts['func_count']:
                        jib_counter +=1
                        found_minions.append(data['id'])
                        print('Reply received from [{0}].Total replies now:[{1}].'.format(ret['data']['id'],jib_counter))
                    continue
        else:
            print('Event filred at {0}'.format(time.asctime()))
            print('*'* 25)
            print('Tag: {0}'.format(ret['tag']))
            print('Data:')
            pprint.pprint(ret['data'])

if __name__ == '__main__':
    opts = parse()
listen(opts)