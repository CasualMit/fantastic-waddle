# switches
## basis config
hostname : `hostname $HOSTNAME`

priveledged-EXEC mode : `enable secret class`

Console-verbinding:
```
line console 0
password cisco
login
```

wachtwoord telnet : 
```line vty 0 15
password cisco
login
```
encrypt de weergave van passwords in show running : `service password-encryption`

cancel domain lookup with `shift + crtl + 6`
### example
```
enable
config terminal
hostname S1
no ip domain-lookup
enable secret class
line console 0
logging synchronous
password cisco
login
exit
line vty 0 15
transport input ssh
password cisco
login
exit
service password-encryption
banner motd # This is a secure system, unauthorized use is prohibited! #
exit
copy running-config startup-config
```

## VLAN
```
configure terminal
(config)# vlan 20
    (config-vlan)# name $name
    (config-vlan)# end
```

### config VLAN to a port
```
configure terminal 
    (config)# interface $interface_id
    (config-if)# switchport mode access
    (config-if)# switchport access vlan $vlan-id
```

### Trunk
```
configure terminal
    (config)# interface $interface_id
    (config-if)# switchport mode dynamic desirable / (config-if)# switchport mode trunk
    (config-if)# switchport trunk native vlan 999
    (config-if)# switchport trunk encapsulation dot1q
```

### VTP server
```
(config)# vtp mode server
(config)# vtp domain CCNA
(config)# vtp password cisco12345
```

### VTP client
```
(config)# vtp mode client
(config)# vtp domain CCNA
(config)# vtp password cisco12345
```

## STP
`(config)# spanning-tree mode`
`(config)# spanning-tree vlan 1,10,30,50,70 root primary`
`(config)# spanning-tree vlan 1,10,30,50,70 root secondary`



### portfast
Only apply to single devices connected directly to a switch.
```
(config)# interface fa0/11
    (config-if)# spanning-tree portfast
    (config-if)# spanning-tree bpduguard enable
```

## Etherchannel
```
(config-)# interface range $trunk_interfaces_to_add
    (config-if)# shutdown   (to protect from errors)
    (config-if)# channel-group 1 mode active
```
```
  (config-)# interface port-channel 3
      (config-if)# switchport mode trunk
```

