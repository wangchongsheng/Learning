from IPy import IP
def min_max_ip(ip,mask='32'):
    # if mask!=NULL:
        # net=ip+'/'+str(mask)
    # ip_list=[]
    # print("min_max_ip:",ip,mask)
    if mask>32:
        print("mask err")
        exit()
    try:
        ip_list = []
        net="%s/%s" %(ip,mask)
        ip=IP(net)
        ip_list.append(ip.net())
        ip_list.append(ip.broadcast())
        return(ip_list)
        # print(ip_list)
        # return ip_list[0]
    except:
        ip = (ip.split('.'))
        ip = ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + str(int(ip[-1])-1)
        ret=min_max_ip(ip,mask)
        return ret

aa=min_max_ip('192.168.0.100',29)
print(aa)