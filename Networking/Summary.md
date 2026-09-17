

# Networking Fundamentals — Complete Tutorial

## The goal

By the end, you should be able to look at something like:

```text
Azure VNet
10.0.0.0/16
│
├── AVD Subnet
│   10.0.1.0/24
│
├── Application Subnet
│   10.0.2.0/24
│
└── Database Subnet
    10.0.3.0/24
```

and answer:

* What addresses exist in each subnet?
* Is `10.0.1.50` part of `10.0.1.0/24`?
* How does an AVD VM reach another subnet?
* How does it reach the Internet?
* What is the default gateway?
* Which route is selected?
* How does DNS resolve a server name?
* What happens if DNS fails?
* What happens if TCP 443 is blocked?
* Where does NAT happen?
* Why would an AVD machine fail to contact a domain controller?

That is the level of understanding we're targeting. Your uploaded material explicitly identifies this kind of reasoning as the actual target rather than merely memorizing definitions. 

---

# PART 1 — IPv4

## 1. What is an IP address?

An IP address identifies a network interface on an IP network.

IPv4 uses **32 bits**.

Those 32 bits are divided into four groups of 8:

```text
192.168.1.10

192       168       1        10
│          │        │         │
8 bits    8 bits   8 bits    8 bits
```

Therefore:

```text
8 + 8 + 8 + 8 = 32 bits
```

Each 8-bit section is called an **octet**.

Each octet can represent:

```text
0 → 255
```

because:

```text
2^8 = 256
```

values exist:

```text
0, 1, 2, ... 255
```

This is why IPv4 addresses look like:

```text
10.20.30.40
172.16.5.20
192.168.1.100
```

Your uploaded material identifies the same fundamentals: IPv4 is 32-bit, uses four octets, each octet is 8 bits, and each ranges from 0–255. 

---

# 2. Decimal → binary

This is important because subnetting becomes much easier once you understand binary.

The eight positions in an octet are:

```text
128 64 32 16 8 4 2 1
```

For example, let's convert:

```text
192
```

Start with:

```text
128
```

192 contains 128:

```text
192 - 128 = 64
```

64 contains 64:

```text
64 - 64 = 0
```

So:

```text
192 = 128 + 64
```

Therefore:

```text
11000000
```

### 168

```text
168 = 128 + 32 + 8
```

Therefore:

```text
10101000
```

### 10

```text
10 = 8 + 2
```

Therefore:

```text
00001010
```

### 1

```text
1 = 1
```

Therefore:

```text
00000001
```

So:

```text
192.168.1.10
```

becomes:

```text
11000000.10101000.00000001.00001010
```

You don't need to convert every IP to binary in your head eventually, but you need to understand the underlying mathematics.

---

# PART 2 — Network portion vs Host portion

This is where networking becomes interesting.

Consider:

```text
192.168.1.10/24
```

The `/24` tells us:

```text
First 24 bits = network
Remaining 8 bits = host
```

Visually:

```text
192.168.1     .10
<--- network ---> <host>
```

More accurately:

```text
11000000.10101000.00000001 | 00001010
          24 bits            8 bits
```

The network identifies **which network** you're on.

The host portion identifies **which device/interface inside that network**.

---

# PART 3 — CIDR

CIDR means **Classless Inter-Domain Routing**.

You will constantly see notation such as:

```text
10.0.0.0/16
192.168.1.0/24
10.10.20.64/26
```

The number after `/` is the number of network bits.

For IPv4:

```text
Total bits = 32
```

Therefore:

```text
Host bits = 32 - prefix
```

Example:

```text
/24
```

means:

```text
32 - 24 = 8 host bits
```

And:

```text
2^8 = 256
```

addresses.

Your source gives exactly this relationship and the common `/24` example. 

---

# PART 4 — CIDR table you should memorize

This table is extremely useful.

| CIDR | Host bits | Total addresses | Traditional usable hosts |
| ---- | --------: | --------------: | -----------------------: |
| /16  |        16 |          65,536 |                   65,534 |
| /17  |        15 |          32,768 |                   32,766 |
| /18  |        14 |          16,384 |                   16,382 |
| /19  |        13 |           8,192 |                    8,190 |
| /20  |        12 |           4,096 |                    4,094 |
| /21  |        11 |           2,048 |                    2,046 |
| /22  |        10 |           1,024 |                    1,022 |
| /23  |         9 |             512 |                      510 |
| /24  |         8 |             256 |                      254 |
| /25  |         7 |             128 |                      126 |
| /26  |         6 |              64 |                       62 |
| /27  |         5 |              32 |                       30 |
| /28  |         4 |              16 |                       14 |
| /29  |         3 |               8 |                        6 |
| /30  |         2 |               4 |                        2 |

The `-2` rule is for traditional IPv4 subnet calculations. Cloud providers can reserve additional addresses, so **always check the platform's rules** when calculating usable addresses in AWS/Azure. Your source specifically warns about this. 

---

# PART 5 — Subnet mask

CIDR and subnet masks describe the same boundary in different ways.

For:

```text
192.168.1.0/24
```

the subnet mask is:

```text
255.255.255.0
```

Why?

Binary:

```text
11111111.11111111.11111111.00000000
```

There are:

```text
24 ones
```

Therefore:

```text
/24
```

---

## Important subnet masks

| CIDR | Subnet mask     |
| ---- | --------------- |
| /16  | 255.255.0.0     |
| /17  | 255.255.128.0   |
| /18  | 255.255.192.0   |
| /19  | 255.255.224.0   |
| /20  | 255.255.240.0   |
| /21  | 255.255.248.0   |
| /22  | 255.255.252.0   |
| /23  | 255.255.254.0   |
| /24  | 255.255.255.0   |
| /25  | 255.255.255.128 |
| /26  | 255.255.255.192 |
| /27  | 255.255.255.224 |
| /28  | 255.255.255.240 |
| /29  | 255.255.255.248 |
| /30  | 255.255.255.252 |

You don't need to memorize all of these immediately. But `/24–/30` should become very familiar.

---

# PART 6 — Network address, host addresses and broadcast

Consider:

```text
192.168.1.10/24
```

The network is:

```text
192.168.1.0/24
```

Therefore:

```text
Network address:
192.168.1.0
```

First traditional host:

```text
192.168.1.1
```

Last traditional host:

```text
192.168.1.254
```

Broadcast:

```text
192.168.1.255
```

So:

```text
192.168.1.0       ← network
192.168.1.1
192.168.1.2
...
192.168.1.254     ← last host
192.168.1.255     ← broadcast
```

Your source uses this exact example. 

---

# PART 7 — How to calculate a subnet

Let's do this properly.

Suppose:

```text
192.168.10.50/26
```

First:

```text
32 - 26 = 6 host bits
```

Therefore:

```text
2^6 = 64
```

addresses per subnet.

So the block size is:

```text
64
```

The possible ranges are:

```text
0–63
64–127
128–191
192–255
```

Our IP is:

```text
192.168.10.50
```

50 belongs to:

```text
0–63
```

Therefore:

```text
Network:
192.168.10.0/26
```

Traditional host range:

```text
192.168.10.1
        ↓
192.168.10.62
```

Broadcast:

```text
192.168.10.63
```

This is one of the core exercises identified in your material. 

---

# PART 8 — The block-size method

This is the easiest subnetting method for practical work.

For:

```text
/26
```

mask:

```text
255.255.255.192
```

Block size:

```text
256 - 192 = 64
```

Therefore:

```text
0
64
128
192
```

are subnet boundaries.

For `/27`:

```text
255.255.255.224
```

Block:

```text
256 - 224 = 32
```

Boundaries:

```text
0
32
64
96
128
160
192
224
```

For `/28`:

```text
255.255.255.240
```

Block:

```text
256 - 240 = 16
```

Boundaries:

```text
0
16
32
48
64
80
96
112
128
144
160
176
192
208
224
240
```

This method is worth mastering.

---

# PART 9 — Does an IP belong to a subnet?

Example:

```text
Subnet:
192.168.10.64/26
```

Possible ranges:

```text
192.168.10.0–63
192.168.10.64–127
192.168.10.128–191
192.168.10.192–255
```

Question:

```text
192.168.10.100
```

100 falls between:

```text
64–127
```

Therefore:

```text
YES
```

It belongs to:

```text
192.168.10.64/26
```

Your source specifically identifies this as a must-have practical skill. 

---

# PART 10 — Private IP addresses

There are three major private IPv4 ranges:

```text
10.0.0.0/8
```

```text
172.16.0.0/12
```

```text
192.168.0.0/16
```

Therefore these are private:

```text
10.1.2.3
10.200.50.20

172.16.1.1
172.31.255.254

192.168.1.1
192.168.100.50
```

But:

```text
172.15.1.1
```

is **not** inside the private `172.16.0.0/12` range.

And:

```text
172.32.1.1
```

is also not private.

---

# PART 11 — Public IP

A public IP is an address that can be used for communication across the public Internet, subject to routing and other controls.

Conceptually:

```text
Internet
   |
Public IP
   |
Router/NAT
   |
Private network
   |
VM
```

Your source highlights this public/private distinction as especially important for cloud networking. 

---

# PART 12 — Default Gateway

Suppose your machine has:

```text
IP:
192.168.1.20

Subnet:
192.168.1.0/24

Gateway:
192.168.1.1
```

Your machine wants:

```text
192.168.1.30
```

Same subnet.

It can communicate locally.

But if it wants:

```text
8.8.8.8
```

that isn't inside:

```text
192.168.1.0/24
```

So it sends the packet toward the default gateway.

```text
Computer
192.168.1.20
      |
      ↓
192.168.1.1
Default Gateway
      |
      ↓
Router
      |
      ↓
Internet
```

Your source describes this exact local-vs-outside-subnet behavior. 

---

# PART 13 — Routing

Routing answers:

> **Where should this packet go next?**

Imagine:

```text
Source:
10.0.1.10

Destination:
10.0.3.20
```

The source machine/router needs a route telling it how to reach:

```text
10.0.3.0/24
```

A simplified route table might look like:

```text
Destination       Next hop
10.0.1.0/24       Local
10.0.3.0/24       Router-A
0.0.0.0/0         Internet Gateway
```

Your source identifies destination, next hop, default route and longest-prefix matching as core routing concepts. 

---

# PART 14 — What is 0.0.0.0/0?

This is the **default route**.

It effectively means:

> "Any IPv4 destination that doesn't match a more specific route."

For example:

```text
10.0.1.0/24
10.0.2.0/24
0.0.0.0/0
```

If destination is:

```text
10.0.2.50
```

the `/24` route matches.

If destination is:

```text
8.8.8.8
```

the specific internal routes don't match, so:

```text
0.0.0.0/0
```

can be selected.

---

# PART 15 — Longest Prefix Match

Suppose routing table contains:

```text
10.0.0.0/8
10.0.0.0/16
10.0.1.0/24
0.0.0.0/0
```

Destination:

```text
10.0.1.50
```

Multiple routes technically match.

Which one wins?

The **most specific route**, meaning the longest prefix:

```text
10.0.1.0/24
```

wins over:

```text
10.0.0.0/16
```

which wins over:

```text
10.0.0.0/8
```

This concept becomes very important when you start working with cloud route tables.

---

# PART 16 — DNS

DNS means **Domain Name System**.

Its basic job:

```text
Name → IP address
```

For example:

```text
google.com
     ↓
DNS
     ↓
IP address
```

Your source describes the basic client → DNS server → IP resolution flow and lists A, AAAA, CNAME, MX, caching, TTL, forward and reverse lookup as concepts to know. 

---

# PART 17 — Why do we need DNS?

Imagine having to remember:

```text
142.x.x.x
104.x.x.x
172.x.x.x
...
```

for every website/server.

Instead:

```text
google.com
fileserver.company.com
portal.company.com
```

are human-friendly names.

DNS translates them into IP addresses.

---

# PART 18 — DNS resolution

Suppose:

```text
Client:
10.0.1.20
```

asks:

```text
What is fileserver.company.com?
```

Conceptually:

```text
Client
  |
  | DNS query
  ↓
DNS resolver/server
  |
  | lookup
  ↓
DNS records
  |
  ↓
10.0.2.20
```

Then the client knows:

```text
fileserver.company.com
=
10.0.2.20
```

Important:

**DNS doesn't itself establish the application connection.**

It provides the information needed to locate the destination.

---

# PART 19 — DNS records

## A record

Hostname → IPv4

```text
server.company.com
        ↓
10.0.1.20
```

---

## AAAA

Hostname → IPv6

```text
server.company.com
        ↓
2001:db8::20
```

---

## CNAME

Alias → another hostname.

Example:

```text
app.company.com
       ↓
CNAME
       ↓
server01.company.com
```

---

## MX

Mail server information.

Example concept:

```text
company.com
   ↓
MX
   ↓
mail.company.com
```

---

## SRV

Extremely important for **Active Directory**.

SRV records help clients locate specific services.

For example:

```text
_ldap._tcp.dc._msdcs.company.com
```

can help locate domain controllers providing LDAP-related services.

This is one reason DNS is so important in AD environments.

---

# PART 20 — DNS suffix

Suppose:

```text
DNS suffix:
company.local
```

You type:

```text
fileserver
```

Windows can construct:

```text
fileserver.company.local
```

The full name:

```text
fileserver.company.local
```

is an **FQDN — Fully Qualified Domain Name**.

This is especially useful in Windows enterprise environments.

---

# PART 21 — DNS cache

Your machine may cache DNS responses.

You can see the cache:

```powershell
ipconfig /displaydns
```

Flush it:

```powershell
ipconfig /flushdns
```

Why might you flush DNS?

For example:

```text
Old DNS result
      ↓
Cached locally
      ↓
DNS record changed
      ↓
Client still using old result
```

Flushing can force a fresh lookup.

---

# PART 22 — DNS troubleshooting

These commands are extremely useful:

```powershell
ipconfig /all
```

Look at:

```text
IPv4 Address
Subnet Mask
Default Gateway
DNS Servers
DNS Suffix
```

Then:

```powershell
nslookup server01.company.com
```

Or:

```powershell
Resolve-DnsName server01.company.com
```

If resolution fails, investigate:

```text
DNS server
   ↓
Network connectivity
   ↓
DNS zone
   ↓
Record
   ↓
Suffix
   ↓
Forwarding
```

---

# PART 23 — DNS failure vs network failure

This distinction is **critical**.

Suppose:

```text
fileserver.company.com
```

doesn't work.

### First test DNS

```powershell
nslookup fileserver.company.com
```

If:

```text
Name → IP
```

works:

```text
DNS ✅
```

Then test connectivity.

```powershell
Test-NetConnection fileserver.company.com -Port 443
```

If DNS resolves but TCP fails:

```text
DNS ✅
Network/service ❌
```

That is a completely different problem.

---

# PART 24 — DHCP

DHCP automatically provides network configuration.

A device can obtain:

```text
IP address
Subnet mask
Default gateway
DNS server
Lease information
```

Your source lists these DHCP-provided parameters and the DORA process. 

---

# PART 25 — DORA

DHCP's classic four-step process:

```text
D — Discover
O — Offer
R — Request
A — Acknowledge
```

Conceptually:

```text
Client
   |
   | DHCP Discover
   ↓
DHCP Server
   |
   | DHCP Offer
   ↓
Client
   |
   | DHCP Request
   ↓
DHCP Server
   |
   | DHCP ACK
   ↓
Client gets configuration
```

---

# PART 26 — TCP

TCP is connection-oriented.

A simplified TCP connection starts with:

```text
Client             Server

SYN  ------------>

     <------------ SYN-ACK

ACK  ------------>
```

This is the **three-way handshake**.

Then data transfer occurs.

TCP provides mechanisms involving:

* sequencing
* acknowledgements
* retransmission
* flow control
* reliable delivery

Your source specifically lists these TCP concepts. 

---

# PART 27 — UDP

UDP is connectionless.

There isn't a TCP-style three-way handshake.

Conceptually:

```text
Client
  |
  | UDP packet
  ↓
Server
```

UDP is often useful where low overhead or timing matters more than TCP-style reliability.

Examples include:

```text
DNS
DHCP
VoIP
some streaming/application traffic
```

Don't reduce the distinction to:

> TCP = slow, UDP = fast.

The more useful distinction is:

```text
TCP:
connection + reliability mechanisms

UDP:
connectionless + minimal transport overhead
```

---

# PART 28 — Ports

An IP address identifies the network destination.

A port identifies a particular service endpoint.

For example:

```text
10.0.1.20:443
```

means:

```text
IP:
10.0.1.20

Port:
443
```

If we specify protocol:

```text
TCP 10.0.1.20:443
```

we're describing a TCP connection to port 443 on that host.

Your source specifically emphasizes ports as critical to cloud troubleshooting. 

---

# PART 29 — Important ports for you

Memorize these first:

| Port | Protocol | Service     |
| ---: | -------- | ----------- |
|   22 | TCP      | SSH         |
|   53 | UDP/TCP  | DNS         |
|   67 | UDP      | DHCP server |
|   68 | UDP      | DHCP client |
|   80 | TCP      | HTTP        |
|  123 | UDP      | NTP         |
|  443 | TCP      | HTTPS       |
|  445 | TCP      | SMB         |
| 3389 | TCP      | RDP         |
|  389 | TCP/UDP  | LDAP        |
|  636 | TCP      | LDAPS       |
| 5985 | TCP      | WinRM HTTP  |
| 5986 | TCP      | WinRM HTTPS |

For your AVD/Windows career, I'd additionally learn the common **Active Directory/Kerberos/DNS-related ports** later.

---

# PART 30 — NAT

NAT = **Network Address Translation**.

It translates IP addresses between network contexts.

A common example:

```text
Private VM
10.0.1.10
     |
     ↓
NAT
     |
     ↓
Public IP
203.x.x.x
     |
     ↓
Internet
```

Your source identifies private-to-Internet connectivity, source/destination NAT and PAT as concepts to understand. 

---

# PART 31 — Why NAT?

Private addresses such as:

```text
10.0.1.10
```

are not globally unique Internet addresses.

A NAT device can translate:

```text
10.0.1.10
```

into a public address when accessing the Internet.

Conceptually:

```text
10.0.1.10:50000
       ↓
NAT
       ↓
203.x.x.x:40001
       ↓
Internet
```

---

# PART 32 — Source NAT vs Destination NAT

### Source NAT

Changes the source address.

Example:

```text
10.0.1.10
   ↓
203.x.x.x
```

Common for outbound traffic.

### Destination NAT

Changes the destination address.

Conceptually:

```text
Public IP
    ↓
Private server
```

Often used for inbound publishing/port forwarding/load-balancing scenarios.

---

# PART 33 — IPv6

IPv6 uses **128 bits**.

IPv4:

```text
32 bits
```

IPv6:

```text
128 bits
```

IPv6 uses hexadecimal.

Example:

```text
2001:db8:abcd:0012:0000:0000:0000:0001
```

Can be shortened to:

```text
2001:db8:abcd:12::1
```

Your source identifies 128-bit addressing, hexadecimal notation, compression, unicast, multicast, link-local addressing and `/64` subnetting as the IPv6 basics you should learn. 

---

# PART 34 — IPv6 `::` compression

Suppose:

```text
2001:db8:0000:0000:0000:0000:0000:0001
```

can become:

```text
2001:db8::1
```

The `::` represents consecutive groups of zeros.

You generally use `::` only once in an address because otherwise the exact number of omitted groups would be ambiguous.

---

# PART 35 — IPv6 link-local

IPv6 has addresses beginning with:

```text
fe80::
```

These are **link-local** addresses.

They're used for communication on the local link and are important to understand when troubleshooting IPv6 networking.

---

# PART 36 — Subnetting in cloud

Now connect everything.

Suppose you have:

```text
Azure VNet:
10.0.0.0/16
```

You divide it:

```text
10.0.1.0/24
10.0.2.0/24
10.0.3.0/24
```

Conceptually:

```text
VNet
10.0.0.0/16
│
├── Web
│   10.0.1.0/24
│
├── App
│   10.0.2.0/24
│
└── DB
    10.0.3.0/24
```

Your uploaded material uses essentially this VNet/subnet model as the final practical exercise. 

---

# PART 37 — How does one subnet reach another?

Suppose:

```text
VM1:
10.0.1.10

VM2:
10.0.2.20
```

VM1 wants to communicate with VM2.

VM1 determines:

```text
10.0.2.20
```

is not in its own subnet:

```text
10.0.1.0/24
```

Therefore it needs routing.

Conceptually:

```text
VM1
10.0.1.10
   |
   ↓
Route table
   |
   ↓
10.0.2.0/24
   |
   ↓
Azure networking
   |
   ↓
VM2
10.0.2.20
```

Cloud platforms provide virtual networking infrastructure that handles this traffic according to the applicable routes and security controls.

---

# PART 38 — How does a VM reach the Internet?

Suppose:

```text
VM:
10.0.1.10
```

Destination:

```text
8.8.8.8
```

Conceptually:

```text
VM
10.0.1.10
   |
   ↓
Route table
   |
   ↓
Default route
0.0.0.0/0
   |
   ↓
Internet connectivity mechanism
   |
   ↓
Internet
   |
   ↓
8.8.8.8
```

If the architecture uses NAT, the private source address can be translated to a public source address for the outbound connection.

---

# PART 39 — The most important troubleshooting model

When an application isn't working, **don't randomly test things**.

Go layer by layer.

Suppose:

```text
AVD user:
"I can't access app.company.com"
```

### Step 1 — DNS

```powershell
nslookup app.company.com
```

Does it resolve?

```text
YES → continue
NO  → troubleshoot DNS
```

---

### Step 2 — IP connectivity

You now know:

```text
app.company.com
       ↓
10.0.2.50
```

Can you reach the destination?

Investigate routing/connectivity.

---

### Step 3 — Port

Suppose the application uses HTTPS:

```text
TCP 443
```

Run:

```powershell
Test-NetConnection app.company.com -Port 443
```

Possible:

```text
DNS       ✅
TCP 443   ❌
```

Now investigate:

* NSG
* firewall
* route
* service
* load balancer
* network security controls

---

### Step 4 — Application

Suppose:

```text
DNS       ✅
Routing   ✅
TCP 443   ✅
```

but the application still doesn't work.

Now you're likely dealing with an application/authentication/configuration problem rather than basic DNS.

---

# PART 40 — AVD + Active Directory + DNS

This is especially important for **your existing AVD work**.

Imagine:

```text
Azure VNet
10.0.0.0/16
│
├── AVD Subnet
│   10.0.1.0/24
│   │
│   ├── AVD-01
│   ├── AVD-02
│   └── AVD-03
│
└── AD Subnet
    10.0.2.0/24
    │
    ├── DC01
    └── DC02
```

The AVD session host may need to locate domain controllers.

DNS helps it discover services.

So:

```text
AVD Session Host
       |
       ↓
DNS
       |
       ↓
AD DNS records
       |
       ↓
Domain Controller
       |
       ↓
Active Directory
```

If DNS is incorrectly configured:

```text
AVD VM
   |
   X
DNS resolution
   |
   X
Domain Controller discovery
```

You can consequently see failures involving:

* domain join
* authentication
* Group Policy
* domain controller discovery
* Kerberos
* access to internal resources

This is why your original material correctly emphasizes **AD + DNS** as particularly valuable for enterprise AVD.

---

# PART 41 — A real AVD troubleshooting scenario

Imagine a user says:

> "I can't access `fileserver.company.local` from my AVD session."

Don't immediately restart the VM.

Work through:

### 1. Check IP configuration

```powershell
ipconfig /all
```

Check:

```text
IP address
Subnet
Gateway
DNS servers
DNS suffix
```

---

### 2. Resolve the hostname

```powershell
Resolve-DnsName fileserver.company.local
```

If it fails:

```text
Investigate DNS
```

---

### 3. If DNS resolves

Suppose:

```text
fileserver.company.local
        ↓
10.0.3.20
```

Now test the appropriate service port.

For SMB:

```powershell
Test-NetConnection fileserver.company.local -Port 445
```

---

### 4. If port fails

Investigate:

```text
Route
NSG
Firewall
Network security
Server availability
```

---

### 5. If port works

Then investigate:

```text
SMB
Permissions
Authentication
User access
Share configuration
```

This is the difference between **systematic troubleshooting** and simply trying random fixes.

---

# PART 42 — The full networking picture

Put everything together:

```text
                      INTERNET
                          |
                     Public IP
                          |
                         NAT
                          |
                    Cloud Router
                          |
                    Route Table
                          |
              +-----------+-----------+
              |                       |
        Web Subnet               App Subnet
        10.0.1.0/24             10.0.2.0/24
              |                       |
           Web VM                  App VM
              |                       |
              +-----------+-----------+
                          |
                    Internal routing
                          |
                     DNS Server
                          |
                     AD / Domain
                          |
                    Domain Controller
```

And when an application request occurs:

```text
User
 ↓
Application hostname
 ↓
DNS
 ↓
IP address
 ↓
Routing
 ↓
Security controls
 ↓
TCP/UDP
 ↓
Port
 ↓
Application
```

That's the mental model I want you to develop.

---

# PART 43 — Questions you should be able to answer

## Beginner

### Q1. How many bits does IPv4 have?

**Answer:** 32 bits.

### Q2. How many bits are in each IPv4 octet?

**Answer:** 8.

### Q3. What's the maximum value of an IPv4 octet?

**Answer:** 255.

### Q4. What does `/24` mean?

**Answer:** 24 network bits and 8 host bits.

### Q5. How many addresses are in `/24`?

**Answer:**

```text
2^8 = 256
```

### Q6. What are private IPv4 ranges?

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

---

# Intermediate questions

### Q7. Find the network for:

```text
192.168.5.20/24
```

Answer:

```text
Network:
192.168.5.0

Host range:
192.168.5.1–254

Broadcast:
192.168.5.255
```

---

### Q8. Find the network for:

```text
192.168.5.100/26
```

Block size:

```text
64
```

Ranges:

```text
0–63
64–127
128–191
192–255
```

Therefore:

```text
Network:
192.168.5.64

Broadcast:
192.168.5.127
```

Traditional host range:

```text
192.168.5.65–126
```

---

### Q9. Does this IP belong?

```text
Subnet:
10.0.2.0/24

IP:
10.0.2.200
```

Yes.

---

### Q10.

```text
Subnet:
10.0.2.0/24

IP:
10.0.3.200
```

No.

---

# Advanced foundational questions

### Q11. Why does a computer need a default gateway?

Because destinations outside the local subnet need to be forwarded to a router/next hop.

---

### Q12. What does `0.0.0.0/0` mean?

The IPv4 default route — it matches destinations not covered by a more specific route.

---

### Q13. What happens when DNS fails?

The hostname may not resolve to an IP, so applications using the hostname may be unable to locate their destination.

---

### Q14. If DNS works but TCP 443 fails, is it necessarily a DNS problem?

No.

You have:

```text
DNS → working
TCP 443 → failing
```

Investigate network/security/service connectivity.

---

### Q15. What's the difference between an IP and a port?

```text
IP → identifies the network destination/interface

Port → identifies the service endpoint
```

Example:

```text
10.0.1.20:443
```

---

### Q16. What's the difference between TCP and UDP?

TCP establishes a connection and provides reliability mechanisms.

UDP is connectionless and has lower transport overhead.

---

# PART 44 — Your subnetting practice set

Do these **without looking at the answers first**.

### Level 1

**1.**

```text
192.168.1.50/24
```

Find:

* Network
* First host
* Last host
* Broadcast
* Total addresses

---

**2.**

```text
10.0.0.25/26
```

Find the subnet.

---

**3.**

```text
10.0.0.100/26
```

Find:

* Network
* Broadcast
* Host range

---

### Level 2

**4.**

```text
172.16.50.130/27
```

Find the network.

---

**5.**

```text
192.168.10.200/28
```

Find:

* Network
* Broadcast
* Host range

---

**6.**

Does:

```text
10.10.10.75
```

belong to:

```text
10.10.10.64/26
```

?

---

### Level 3

**7.**

Does:

```text
192.168.100.130
```

belong to:

```text
192.168.100.128/27
```

?

---

**8.**

How many addresses does:

```text
10.20.0.0/20
```

contain?

---

**9.**

How many `/24` networks can you create from:

```text
10.0.0.0/16
```

?

---

**10.**

You have:

```text
10.0.0.0/16
```

You need at least 10 separate subnets.

What prefix would you consider?

---

# PART 45 — Your networking troubleshooting questions

These are much more important for your career than memorizing definitions.

### Scenario 1

An AVD VM can access:

```text
8.8.8.8
```

but cannot access:

```text
fileserver.company.local
```

What would you investigate first?

**Think:** DNS.

---

### Scenario 2

```text
nslookup fileserver.company.local
```

returns:

```text
10.0.2.20
```

but:

```powershell
Test-NetConnection fileserver.company.local -Port 445
```

fails.

What does that tell you?

**DNS is working.** Investigate routing, firewall, NSG/security rules, server availability, or SMB service.

---

### Scenario 3

An AVD VM has:

```text
IP: 10.0.1.20
DNS: 8.8.8.8
```

but your organization's internal DNS zone is:

```text
company.local
```

What potential issue might exist?

The VM may not be able to resolve internal AD/DNS names correctly through a public DNS resolver.

---

### Scenario 4

Two VMs:

```text
VM1:
10.0.1.10/24

VM2:
10.0.2.10/24
```

Are they in the same subnet?

**No.**

They're in:

```text
10.0.1.0/24
10.0.2.0/24
```

respectively.

---

### Scenario 5

A VM has:

```text
10.0.1.10/24
```

and wants:

```text
10.0.1.50
```

Does it need to send the traffic to the default gateway?

Not for the initial local-subnet routing decision; the destination is on the same subnet.

---

# PART 46 — What you should memorize vs understand

## Memorize

```text
IPv4 = 32 bits
IPv6 = 128 bits

Private IPv4:
10/8
172.16/12
192.168/16

Host bits = 32 - prefix

Addresses = 2^host_bits
```

And become familiar with:

```text
/24 = 256
/25 = 128
/26 = 64
/27 = 32
/28 = 16
/29 = 8
/30 = 4
```

Also:

```text
22 → SSH
53 → DNS
67/68 → DHCP
80 → HTTP
123 → NTP
443 → HTTPS
445 → SMB
3389 → RDP
389 → LDAP
636 → LDAPS
```

---

## Understand deeply

Don't merely memorize:

> "Gateway is 192.168.1.1."

Understand **why** traffic uses a gateway.

Don't merely memorize:

> "/26 = 64."

Understand:

```text
32 - 26 = 6
2^6 = 64
```

Don't merely memorize:

> "DNS converts names to IP."

Understand:

```text
Name
 ↓
DNS query
 ↓
Resolver
 ↓
DNS server/records
 ↓
IP
 ↓
Routing
 ↓
TCP/UDP
 ↓
Port
 ↓
Application
```

---

# PART 47 — Your learning order

For your specific **AVD → Azure/AWS Cloud → DevOps/SRE** direction, I'd study in this order:

```text
PHASE 1
IPv4
 ↓
Binary
 ↓
Subnet masks
 ↓
CIDR
 ↓
Subnetting
 ↓
Network/host/broadcast
```

Then:

```text
PHASE 2
Private/Public IP
 ↓
Default Gateway
 ↓
Routing
 ↓
Route tables
 ↓
Longest-prefix match
 ↓
NAT
```

Then:

```text
PHASE 3
DNS
 ↓
DNS records
 ↓
FQDN
 ↓
DNS suffix
 ↓
DNS cache
 ↓
Forward/reverse lookup
 ↓
Conditional forwarding
 ↓
Private DNS
```

Then:

```text
PHASE 4
DHCP
 ↓
DORA
 ↓
IP configuration
```

Then:

```text
PHASE 5
TCP
 ↓
3-way handshake
 ↓
UDP
 ↓
Ports
 ↓
Connectivity testing
```

Then:

```text
PHASE 6
IPv6 basics
```

Finally:

```text
PHASE 7
Azure VNet
 ↓
Subnets
 ↓
NSG
 ↓
Route tables
 ↓
NAT Gateway
 ↓
Private endpoints
 ↓
Azure DNS
 ↓
VPN
 ↓
Peering
 ↓
AVD networking
 ↓
AD + DNS
```

This ordering is also consistent with the progression in your uploaded material, which puts IPv4/binary/CIDR/subnetting before routing/NAT/DNS and ultimately cloud networking. 

## The benchmark I would use for you

Before moving heavily into AWS/Azure hands-on networking, you should be able to solve these **instantly or nearly instantly**:

```text
192.168.1.50/24
→ network?
→ broadcast?
→ host range?

10.0.1.100/26
→ network?
→ broadcast?
→ belongs to which subnet?

172.16.10.130/27
→ network?
→ host range?

10.0.1.10 → 10.0.2.20
→ same subnet?
→ if not, how does traffic travel?

10.0.1.10 → 8.8.8.8
→ local or remote?
→ which route?
→ what is 0.0.0.0/0?

server.company.local
→ how does the name become an IP?

server.company.local resolves
but TCP 443 fails
→ DNS problem or connectivity/security problem?

AVD VM can't find DC
→ what DNS/AD things do you check?

AVD VM can resolve DC
but can't reach LDAP/LDAPS
→ what do you investigate?
```

Once you can answer those confidently, **your networking fundamentals are genuinely strong enough to start applying them to Azure VNet/AWS VPC labs rather than just studying theory**.
