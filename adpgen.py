import sys
#-*- coding: utf-8 -*-
"""
    Takes as input a string (the data payload) and a packet format.
    Outputs a string representing the binary byte structure of the resulting
    packet.
"""
def make_packet(data = None, protocol = 'UDP'):
    opacket = None
    if protocol == 'UDP':
        opacket = get_udp(data)
    wave = bin2wave(opacket)
    print wave
    

def get_udp(data, sourceport = False, destport = 80, checksum = False):
    #get the source port if applicable
    if sourceport:
        src = str2bin(sourceport)
    else:
        src = '0000000000000000'
    print "src: " + src
    
    dest = str2bin(str(destport))
    print "dest: " + dest
    
    #TODO: udp checksum function
    if checksum:
        print "derp"
        check = '0000000000000000'
    else:
        check = '0000000000000000'
    print "check: " + check
    
    payload = str2bin(data)
    print "payload: " + payload
    
    length = str2bin(str(8 + len(data)))
    #length = str2bin(str(len(payload)))
    print "length: " +length
    print len(data)
    
    packet = src + dest + check + length + payload
    print "packet: " + packet
    
    return packet

def bin2wave(datin):
    waveout = ''
    lastbit = 0
    for bit in datin:
        bit = int(bit)
        if bit:
            if lastbit:
                waveout = waveout + u'\u203E'
            else:
                waveout = waveout + u'|\u203E'
        elif lastbit:
            waveout = waveout + '|_'
        else:
            waveout = waveout + '_'
        lastbit = bit
    return waveout
    
#def get_udp_checksum(data, srcport, destport, length sourceIP, destIP):

def str2bin(st):
    binout = ''
    for byte in bytearray(st):
        binary = format(byte, 'b')
        for zero in range(0, 8 - len(binary)):
            binary = '0' + binary
        binout = binout + binary
    return str(binout)
    
if __name__ == "__main__":
    make_packet("8==>")
