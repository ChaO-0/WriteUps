#! /usr/bin/env python2

import sys

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)



print 'Welcome XD'
UNIT = None


def get_mod(inp):
    global UNIT
    assert abs(UNIT) == 2**8
    ret = 1
    while inp > UNIT:
        ret *= UNIT
        inp //= UNIT
    return ret


def retrieve_file(filename):
    ff = open(filename)
    ret = ff.read()
    ff.close()
    return ret


flag = retrieve_file('flag.txt')
UNIT = int(retrieve_file('const.txt'))


n = 16514897111316923204217549632364643783031414237671381345043124387370066411813920027353684461112231468754044146034237728587508998612836498108534141051472935720935096917469187315102763393481677793869563496738377744796961951989137909322744918061952881113418229427280914403245397673285189680564955487704345443671135809898932694360632314230713192474219235806794925093824670389568933469568504137598692904504402367705313318247597576194806678718199208929321503962780176382824849304289226998673100761928826327244571873652527954448562318231080742551174390437588283938470525023767816426392311901385588066156310285724597897519949


message = repr('''
Name: Agent 013
Password: {}
Content: '''.format(flag) + raw_input())[1:-1].replace('\\\\', '\\')


m = int(message.encode('hex'), 16) % get_mod(n)
e = 2**16 + 1

c = pow(m, e, n)
print c
