import random
import string

def generate_device_name(device, description): 
    """ This function generates a name 
    of a VNF running in SYD data center  
    """  
    datacenter = 'SYD' 
    devices = {'firewall': 'Cisco_MX', 'wireless': 'Cisco_MR'} 

    type = devices[device] 
    name = f"{type}--{description}__{datacenter}"  
     
    return name 

def is_ipv4_address(ip): 
    """ Return True if ipv4 address, 
    False if not 
    """  
    octet_range = range(256) 
    octets = ip.split('.') 

    if len(octets) != 4: 
        return False 
    elif any(not octet.isdigit() for octet in octets): 
        return False 
    elif any(int(octet) not in octet_range for octet in octets): 
        return False 

    return True


if __name__ == "__main__":
        characters = string.ascii_lowercase
        description = ''.join(random.choice(characters) for i in range(30))
        device = ['wireless', 'firewall'][random.randrange(0, 2)]
        print(device)
        print(description)
        print(generate_device_name(device, description))
