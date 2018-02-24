

def update(text,macList,mcList,ipList):
    result = []
    for i in range(len(macList)):
        text.replace("dst='\"69:47:88:ff:9f:84'\"",macList[i])
        text.replace("target_mac='69:47:88:ff:9f:84'",mcList[i])
        text.replace("target_ip='192.166.0.60'",ipList[i])
        result.append(text)
    print(result)

text = "send Ethernet(src='ac:de:48:00:11:22', dst='69:47:88:ff:9f:84', payload=ARP(opcode=ARP.REPLY, sender_mac='ac:de:48:00:11:22', sender_ip='192.166.0.100', target_mac='69:47:88:ff:9f:84', target_ip='192.166.0.60'))"


l1 = []
l1.append("dst='bd:d0:8a:2a:dc:bb'")


l2=[]
l2.append("target_mac='bd:d0:8a:2a:dc:bb'")

l3=[]
l3.append("target_ip='192.166.0.168'")
update(text,l1,l2,l3)

#
# sender_mac='bd:d0:8a:2a:dc:bb',
#     sender_ip='192.166.0.168',