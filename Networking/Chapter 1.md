# 🌐 IP Address

## 1. Definition

An **IP address (Internet Protocol address)** is a numerical address used to **identify a device or network interface on a network**.

> **IP address = Address of a device on a network.**

---

## 2. IPv4

**IPv4** is the most commonly taught IP addressing format.

It contains **4 octets**, separated by dots.

```text
192.168.1.10
```

Each octet ranges from **0–255**.

```text
192 . 168 . 1 . 10
 ↑      ↑    ↑    ↑
Octet  Octet Octet Octet
```

---

## 3. IPv6

**IPv6** is the newer version of the Internet Protocol, designed to provide a **much larger number of IP addresses** than IPv4.

IPv6 uses **128 bits**, while IPv4 uses **32 bits**.

### IPv6 format:

It is written using **8 groups of hexadecimal values**, separated by colons.

Example:

```text
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

It can also be shortened:

```text
2001:db8:85a3::8a2e:370:7334
```

### Main difference:

| IPv4                  | IPv6                      |
| --------------------- | ------------------------- |
| 32-bit                | **128-bit**               |
| 4 octets              | **8 hexadecimal groups**  |
| `192.168.1.10`        | `2001:db8::1`             |
| Smaller address space | **Massive address space** |

---

## 4. Why Do We Use IP Addresses?

IP addresses allow devices to **identify and communicate with each other**.

```text
Computer A
192.168.1.10
      ↓
   Network
      ↓
Computer B
192.168.1.20
```

**Source IP** → where data comes from
**Destination IP** → where data needs to go

---

## 5. Private vs Public IP

**Private IP** → used inside private networks.

Examples:

```text
10.0.0.5
192.168.1.10
172.16.1.20
```

**Public IP** → used for communication over the public Internet.

---

## 6. AWS Example

AWS supports both IPv4 and IPv6 networking.

For example:

```text
VPC
 ↓
Subnet
 ↓
EC2
 ↓
Private IP
```

IP addressing is fundamental to:

* VPC
* Subnets
* CIDR
* Routing
* Security Groups
* NACLs
* EC2 networking

---

# 🎯 Exam Perspective

* **IPv4** → 32-bit, 4 decimal octets
* **IPv6** → 128-bit, 8 hexadecimal groups
* **IPv4 example** → `192.168.1.10`
* **IPv6 example** → `2001:db8::1`
* **IPv4 has a smaller address space**
* **IPv6 provides a vastly larger address space**

---

# 🧠 Quick Summary

> **IP address = Address used to identify and communicate with a device/network interface.**

```text
IPv4 → 32-bit → 192.168.1.10
IPv6 → 128-bit → 2001:db8::1
```

### Memory Trick

**IPv4 = 4 decimal groups**
**IPv6 = 8 hexadecimal groups + much larger address space**

# 🌐 Subnet

## 1. Definition

A **subnet (subnetwork)** is a smaller logical network created by dividing a larger IP network into smaller networks.

Simple definition:

> **Subnet = A smaller network created from a larger IP network.**

For example, suppose you have:

```text
10.0.0.0/16
```

You can divide it into smaller subnets such as:

```text
10.0.1.0/24
10.0.2.0/24
10.0.3.0/24
```

Each subnet represents a separate IP address range.

---

# 2. What Is a Subnet?

Think of a large network as an apartment building.

```text
Large Network
10.0.0.0/16
      │
      ├── Subnet 1 → 10.0.1.0/24
      ├── Subnet 2 → 10.0.2.0/24
      └── Subnet 3 → 10.0.3.0/24
```

Instead of putting every device/resource into one huge network, we divide the network into smaller sections.

This helps with:

* Organization
* Network management
* Routing
* Security
* Isolation
* Resource placement

---

# 3. How Does a Subnet Work?

A subnet is defined using **CIDR notation**.

Example:

```text
192.168.1.0/24
```

Here:

* `192.168.1.0` → Network address
* `/24` → Prefix length

The `/24` tells us how much of the IP address represents the **network portion**.

IPv4 has **32 bits**:

```text
192.168.1.0
 ↓
11000000.10101000.00000001.00000000
```

With `/24`:

```text
Network portion        Host portion
<------ 24 bits ------><-- 8 bits -->
```

Therefore:

```text
192.168.1.0/24
```

has:

* **24 bits** for the network
* **8 bits** for hosts

---

# 4. Why Do We Use Subnets?

### 🔹 1. Organize resources

You can place different types of resources into different networks.

```text
VPC
│
├── Web Subnet
├── Application Subnet
└── Database Subnet
```

---

### 🔹 2. Improve security

You can isolate sensitive resources.

For example:

```text
Internet
   ↓
Web Subnet
   ↓
Application Subnet
   ↓
Database Subnet
```

The database doesn't need to be directly accessible from the Internet.

---

### 🔹 3. Control network traffic

Different subnets can have different routing and network security configurations.

---

### 🔹 4. Efficiently use IP addresses

Instead of assigning one huge network to everything, you can divide the available address space according to requirements.

---

# 5. How to Calculate a Basic Subnet

For your AWS networking foundation, you should become comfortable with **CIDR and binary**.

Let's take:

```text
192.168.1.0/24
```

IPv4 has 32 bits.

```text
32 - 24 = 8 host bits
```

Number of total addresses:

```text
2⁸ = 256
```

So:

```text
192.168.1.0 → 192.168.1.255
```

Total:

**256 IP addresses**

For a traditional IPv4 subnet, commonly:

```text
Network address → 192.168.1.0
Usable hosts    → 192.168.1.1 - 192.168.1.254
Broadcast       → 192.168.1.255
```

⚠️ **AWS VPC subnets are different:** AWS reserves **5 IP addresses in every subnet**, so don't apply the traditional "network + broadcast = 2 unavailable" rule directly to AWS.

---

# 6. Subnet and CIDR

CIDR is extremely important for cloud networking.

For example:

```text
10.0.0.0/16
```

can be divided into:

```text
10.0.1.0/24
10.0.2.0/24
10.0.3.0/24
...
```

Think:

> **CIDR defines the IP range; subnet is the smaller network represented by that range.**

You'll use CIDR constantly when working with AWS VPCs.

---

# 7. AWS Subnets

This is where the concept becomes directly relevant to your AWS learning.

A **subnet in Amazon VPC** is a range of IP addresses within a VPC.

For example:

```text
VPC
10.0.0.0/16
      │
      ├── Public Subnet
      │   10.0.1.0/24
      │
      └── Private Subnet
          10.0.2.0/24
```

AWS resources such as EC2 instances can be launched into subnets.

---

# 8. Public vs Private Subnet

### Public Subnet

A subnet is generally considered **public** when its route table has a route to an **Internet Gateway**.

```text
Internet
   ↓
Internet Gateway
   ↓
Public Subnet
   ↓
EC2
```

A resource also needs an appropriate public addressing/configuration to communicate with the Internet.

### Private Subnet

A private subnet doesn't have a direct route to an Internet Gateway for direct Internet access.

```text
Internet
   ✕
Private Subnet
   ↓
EC2
```

A private subnet can still access the Internet **outbound** through a NAT Gateway when appropriately configured.

---

# 9. Scenario-Based Example

Imagine you're building a 3-tier application.

You have:

```text
VPC
10.0.0.0/16
```

You divide it into:

```text
                VPC
           10.0.0.0/16
                 │
       ┌─────────┼─────────┐
       ↓         ↓         ↓
      Web       App       DB
    Subnet     Subnet    Subnet
   10.0.1.0   10.0.2.0  10.0.3.0
      /24        /24       /24
```

Traffic could flow like:

```text
Internet
   ↓
Web Subnet
   ↓
App Subnet
   ↓
Database Subnet
```

This gives you better organization and allows you to apply different routing and security controls to different parts of the application.

---

# 10. When Should You Use Subnets?

Whenever you need to divide a network into smaller logical networks.

In AWS, you'll use subnets when designing:

* VPCs
* Web applications
* Multi-tier architectures
* Public/private network layouts
* Highly available architectures across Availability Zones
* Network security boundaries

For example, a production application might use:

```text
VPC
│
├── Public Subnet → Load Balancer
│
├── Private Subnet → Application servers
│
└── Private Subnet → Database
```

---

# 11. Subnet vs VPC

This is **very important** for AWS.

### VPC

A **VPC is your virtual network in AWS**.

### Subnet

A **subnet is a smaller IP network inside the VPC**.

Think:

```text
AWS
 ↓
VPC
 ↓
Subnets
 ↓
Resources
```

Example:

```text
VPC: 10.0.0.0/16
       │
       ├── Subnet: 10.0.1.0/24
       ├── Subnet: 10.0.2.0/24
       └── Subnet: 10.0.3.0/24
```

### Memory:

> **VPC = Big network**
> **Subnet = Smaller network inside VPC**

---

# 🎯 Exam Perspective

Look for these clues:

| Question clue                                 | Think                               |
| --------------------------------------------- | ----------------------------------- |
| Smaller network within a larger network       | **Subnet**                          |
| Divide a network into smaller networks        | **Subnetting**                      |
| IP range represented using `/24`, `/16`, etc. | **CIDR**                            |
| Network inside an AWS VPC                     | **Subnet**                          |
| Public subnet                                 | Route to **Internet Gateway**       |
| Private subnet                                | No direct route to Internet Gateway |
| Need outbound Internet from private subnet    | **NAT Gateway**                     |
| Different resources need network separation   | **Subnets**                         |

### Very important:

> **A subnet is an IP address range within a VPC.**

And:

> **Public/private is primarily determined by routing, not simply by the name of the subnet.**

---

# 🧠 Quick Summary

```text
                 VPC
              10.0.0.0/16
                   │
          ┌────────┼────────┐
          ↓        ↓        ↓
       Subnet    Subnet   Subnet
       /24       /24      /24
          ↓        ↓        ↓
       Resources Resources Resources
```

### Remember:

**IP address** → identifies a network interface/device
**CIDR** → describes an IP range
**Subnet** → smaller network/IP range
**VPC** → virtual network containing subnets

### 🔑 Memory Trick

> **VPC = City 🏙️**
> **Subnet = Neighborhood 🏘️**
> **IP address = House 📍**

And for your AWS networking path, the chain you should build in your head is:

```text
IP Address
     ↓
CIDR
     ↓
Subnet
     ↓
VPC
     ↓
Route Table
     ↓
Internet Gateway / NAT
     ↓
AWS Resources
```

This is one of the **most important foundations** before you start hands-on work with AWS VPC and EC2.


# 🌐 CIDR Range

## 1. Definition

**CIDR** stands for **Classless Inter-Domain Routing**.

A **CIDR range** is a way of representing a **range of IP addresses** using an IP address followed by a prefix length such as `/24`, `/16`, or `/28`.

Simple definition:

> **CIDR = A compact way to describe an IP address range and determine how much of the address represents the network and how much is available for hosts.**

Example:

```text
192.168.1.0/24
```

Here:

```text
192.168.1.0 → Network address
/24          → Prefix length
```

---

# 2. What Does `/24` Mean?

An IPv4 address contains **32 bits**.

```text
192.168.1.0
   ↓
32 bits total
```

The `/24` means:

> **The first 24 bits are the network portion.**

That leaves:

```text
32 - 24 = 8 host bits
```

So:

```text
Network bits             Host bits
<--------- 24 ---------><-- 8 -->
192.168.1.              .0
```

The host portion can have:

```text
2⁸ = 256
```

possible combinations.

Therefore:

```text
192.168.1.0/24
```

represents:

```text
192.168.1.0
       ↓
192.168.1.255
```

**256 total IPv4 addresses.**

---

# 3. Common CIDR Ranges

Here are some important ones:

| CIDR  | Host bits | Total IPv4 addresses |
| ----- | --------: | -------------------: |
| `/8`  |        24 |           16,777,216 |
| `/16` |        16 |               65,536 |
| `/20` |        12 |                4,096 |
| `/24` |         8 |                  256 |
| `/25` |         7 |                  128 |
| `/26` |         6 |                   64 |
| `/27` |         5 |                   32 |
| `/28` |         4 |                   16 |
| `/30` |         2 |                    4 |

The basic formula is:

> **Total addresses = 2^(32 − prefix length)**

For example:

```text
/26

32 - 26 = 6

2⁶ = 64 addresses
```

---

# 4. CIDR and Subnetting

This is where CIDR becomes important.

Suppose you have:

```text
10.0.0.0/16
```

This represents:

```text
10.0.0.0 → 10.0.255.255
```

You can divide this larger range into smaller subnet ranges.

For example:

```text
10.0.0.0/16
       ↓
   Subnetting
       ↓
 ┌───────────────┐
 ↓       ↓       ↓
/24     /24     /24

10.0.1.0/24
10.0.2.0/24
10.0.3.0/24
```

So:

> **CIDR allows you to define and divide IP address ranges into different-sized networks.**

---

# 5. Why Use CIDR?

CIDR is important because it allows you to:

### 🔹 Efficiently allocate IP addresses

You don't have to give every network a huge IP range.

For example:

```text
Small network → /28
Medium network → /24
Large network → /16
```

---

### 🔹 Create subnets

A large network can be divided into smaller networks.

```text
10.0.0.0/16
      ↓
10.0.1.0/24
10.0.2.0/24
10.0.3.0/24
```

---

### 🔹 Control network size

The prefix length determines how many addresses are available.

```text
/16 → Larger range
/24 → Smaller range
/28 → Much smaller range
```

Remember:

> **Smaller `/` number → larger network**

> **Larger `/` number → smaller network**

For example:

```text
/16 → 65,536 addresses
/24 → 256 addresses
/28 → 16 addresses
```

---

# 6. How to Read a CIDR Range

Let's take:

```text
10.10.0.0/16
```

### Step 1 — Identify the IP

```text
10.10.0.0
```

### Step 2 — Identify prefix length

```text
/16
```

### Step 3 — Calculate host bits

```text
32 - 16 = 16
```

### Step 4 — Calculate total addresses

```text
2¹⁶ = 65,536
```

### Step 5 — Determine range

```text
10.10.0.0 → 10.10.255.255
```

So:

```text
10.10.0.0/16
```

represents **65,536 IPv4 addresses**.

---

# 7. CIDR in AWS

CIDR is **extremely important in AWS networking**.

When creating an AWS VPC, you define an IP address range using CIDR.

For example:

```text
VPC
10.0.0.0/16
```

Then create subnets:

```text
VPC: 10.0.0.0/16
       │
       ├── Public Subnet
       │   10.0.1.0/24
       │
       ├── Private Subnet
       │   10.0.2.0/24
       │
       └── Database Subnet
           10.0.3.0/24
```

So the relationship is:

```text
CIDR
 ↓
Defines IP range
 ↓
VPC
 ↓
Subnets
 ↓
AWS Resources
```

---

# 8. Scenario-Based Example

Imagine you're designing a VPC for a web application.

You choose:

```text
VPC
10.0.0.0/16
```

You then divide it:

```text
              VPC
          10.0.0.0/16
                │
      ┌─────────┼─────────┐
      ↓         ↓         ↓
    Web        App        DB
   /24        /24        /24
10.0.1.0   10.0.2.0   10.0.3.0
```

Now each part of your architecture has its own IP range.

This makes it easier to:

* Organize resources
* Configure routing
* Apply security controls
* Plan IP addressing
* Build multi-tier architectures

---

# 9. CIDR vs IP Address vs Subnet

This distinction is **very important**.

### IP Address

Identifies a specific network interface/device.

```text
10.0.1.25
```

### CIDR

Describes an **IP range/network**.

```text
10.0.1.0/24
```

### Subnet

A smaller network created within a larger network.

```text
VPC
10.0.0.0/16
   ↓
Subnet
10.0.1.0/24
```

Think:

```text
IP Address → One address
CIDR       → Describes a range
Subnet     → Network using that range
```

---

# 10. Important CIDR Rule for AWS

When creating subnets inside a VPC:

> **The subnet CIDR must be a valid, non-overlapping portion of the VPC CIDR.**

Example:

```text
VPC
10.0.0.0/16
```

Valid:

```text
10.0.1.0/24
10.0.2.0/24
```

But you shouldn't create overlapping subnets such as:

```text
10.0.1.0/24
10.0.1.128/25
```

because the second range overlaps the first.

This becomes very important when you start building AWS VPCs.

---

# 🎯 Exam Perspective

### If you see:

> **"What does `/24` represent?"**

→ **24 network bits and 8 host bits**

---

> **"How many IPv4 addresses are in a `/24`?"**

→ **256**

---

> **"How many addresses are in `/26`?"**

```text
32 - 26 = 6
2⁶ = 64
```

→ **64**

---

> **"Which CIDR provides a larger address range: `/16` or `/24`?"**

→ **/16**

---

> **"What is used to define the IP address range of a VPC?"**

→ **CIDR block**

---

> **"Can two subnets in the same VPC have overlapping CIDR ranges?"**

→ **No**

---

# 🧠 Quick Summary

```text
                 CIDR
                  │
           Defines IP range
                  │
        ┌─────────┴─────────┐
        ↓                   ↓
   Network bits         Host bits
        │                   │
    / Prefix             Addresses
```

### The formula to remember:

```text
Host bits = 32 - Prefix length

Total IPv4 addresses = 2^(32 - Prefix length)
```

Examples:

```text
/16 → 2¹⁶ = 65,536
/24 → 2⁸  = 256
/26 → 2⁶  = 64
/28 → 2⁴  = 16
```

### 🔑 Memory Trick

> **`/` number tells you how many bits belong to the network.**

And:

> **Higher `/` → smaller range**
> **Lower `/` → larger range**

For your AWS networking path, keep this chain in mind:

```text
IP Address
    ↓
CIDR
    ↓
Subnet
    ↓
VPC
    ↓
Route Table
    ↓
Internet Gateway / NAT
    ↓
AWS Resources
```

**⭐ Most important takeaway:**
**CIDR is the notation used to define an IP network/range, and in AWS it is fundamental to designing VPCs and subnets.**


# 🌐 Ports

## 1. Definition

A **port** is a logical number used by a computer to identify **which application or network service should receive network traffic**.

Simple definition:

> **IP address identifies the device; port identifies the service/application on that device.**

For example:

```text id="5j3q9p"
192.168.1.10:443
       ↑     ↑
      IP    Port
```

Here:

* `192.168.1.10` → identifies the destination
* `443` → identifies the service receiving the traffic

---

# 2. What Is a Port / How Does It Work?

A single computer/server can run many network services at the same time.

For example:

```text id="j3z6cs"
                 Server
             192.168.1.10
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
    Port 22       Port 80      Port 443
       ↓            ↓            ↓
      SSH          HTTP        HTTPS
```

The **IP address** gets the traffic to the correct machine, while the **port number** helps deliver it to the correct network service.

---

# 3. Port Numbers

Port numbers range from:

```text id="g4nq4v"
0 → 65535
```

They are associated with **TCP or UDP**.

For example:

```text id="k7j8q1"
TCP 443
UDP 53
```

A TCP port and UDP port are technically separate, so the same number can be used by both protocols for different purposes.

---

# 4. Common Ports You Should Know

For your AWS and Cloud/DevOps learning, these are worth remembering:

|      Port | Protocol | Common service |
| --------: | -------- | -------------- |
| **20/21** | TCP      | FTP            |
|    **22** | TCP      | SSH            |
|    **23** | TCP      | Telnet         |
|    **25** | TCP      | SMTP           |
|    **53** | TCP/UDP  | DNS            |
|    **80** | TCP      | HTTP           |
|   **110** | TCP      | POP3           |
|   **143** | TCP      | IMAP           |
|   **443** | TCP      | HTTPS          |
|  **3389** | TCP      | RDP            |

You don't need to memorize every port in existence. Focus on the common ones.

### ⭐ Especially important for you:

```text
22   → SSH
53   → DNS
80   → HTTP
443  → HTTPS
3389 → RDP
```

Since you're working with **Windows/AVD infrastructure**, **RDP 3389** is particularly relevant.

---

# 5. Why Do We Use Ports?

Imagine a server has:

```text id="x7t1vz"
IP: 10.0.1.10
```

It might simultaneously run:

```text id="a8v1bw"
10.0.1.10:22   → SSH
10.0.1.10:80   → HTTP
10.0.1.10:443  → HTTPS
```

Without ports, the computer would know **which machine** the traffic is going to, but wouldn't have the same mechanism to distinguish between multiple network services.

So:

> **IP = Which device?**

> **Port = Which service?**

---

# 6. Ports and TCP/UDP

Ports operate at the **Transport layer**.

```text id="t2b9ls"
OSI Model
    ↓
Transport Layer
    ↓
TCP / UDP
    ↓
Port numbers
```

For example:

```text id="8p5d1e"
TCP
 ↓
Port 443
 ↓
HTTPS
```

or:

```text id="c7km9k"
UDP
 ↓
Port 53
 ↓
DNS
```

This connects directly to the **OSI vs TCP/IP** topic you just studied.

---

# 7. Well-Known Ports

Ports **0–1023** are commonly called **well-known ports** and are assigned to widely used services/protocols.

Examples:

```text id="q8s1yt"
22   → SSH
25   → SMTP
53   → DNS
80   → HTTP
443  → HTTPS
```

Ports above this range are commonly used for other applications/services.

For Cloud Practitioner, knowing the concept and common ports is more important than memorizing the entire port-number allocation.

---

# 8. Ports in AWS

This is where ports become **very important**.

AWS **Security Groups** use port numbers to control network traffic.

For example:

```text id="l8h9w2"
Internet
    ↓
Security Group
    ↓
Allow TCP 443
    ↓
EC2
```

This means HTTPS traffic can reach the EC2 instance on TCP port `443`, assuming the other required networking configuration is in place.

Another example:

```text id="j0f8p4"
Security Group
      ↓
Allow TCP 22
      ↓
EC2
      ↓
SSH
```

And for Windows:

```text id="s6g2fz"
Security Group
      ↓
Allow TCP 3389
      ↓
Windows EC2
      ↓
RDP
```

---

# 9. Ports and Firewalls

Firewalls use ports to determine which traffic should be allowed or blocked.

For example:

```text id="j5k8sd"
Internet
   ↓
Firewall / Security Group
   │
   ├── TCP 443 → ✅ Allow
   ├── TCP 22  → ✅ Allow
   └── TCP 23  → ❌ Deny
```

This is why you will frequently see rules such as:

```text
Protocol: TCP
Port: 443
Source: 0.0.0.0/0
Action: Allow
```

The **source CIDR** tells you *where the traffic is coming from*, while the **port** tells you *which service/port the traffic is trying to reach*.

---

# 10. Scenario-Based Example

Imagine you have an AWS EC2 web server:

```text id="l1d3n7"
EC2
10.0.1.10
```

You want users on the Internet to access your website.

Your security group could have:

```text id="6v2kz0"
Inbound Rule

Protocol → TCP
Port     → 443
Source   → Appropriate client range
```

Traffic:

```text id="0y6gk1"
User
 ↓
HTTPS request
 ↓
TCP 443
 ↓
Security Group
 ↓
EC2
 ↓
Web Application
```

If TCP `443` isn't allowed by the relevant security controls, the connection won't reach the service as intended.

---

# 11. Port vs IP Address

This distinction is **extremely important**.

### IP Address

Identifies the destination network interface/device.

```text id="jz0u4b"
10.0.1.10
```

### Port

Identifies the destination service/application endpoint.

```text id="n5v9cq"
443
```

Together:

```text id="kz5e8h"
10.0.1.10:443
│          │
IP         Port
│          │
Device     HTTPS service
```

### Memory Trick

> **IP = House address 🏠**
> **Port = Room/service inside the house 🚪**

---

# 12. Port vs Service

A port number isn't inherently the service itself.

For example:

```text
443 → commonly HTTPS
```

But the number `443` itself is simply a **port number**. The application/service using it determines what protocol or service operates there.

So for exam purposes:

> **443 → HTTPS** is the standard association you should remember.

---

# 🎯 Exam Perspective

### If you see:

> **"Which port is used for SSH?"**

→ **TCP 22**

### "Which port is used for HTTP?"

→ **TCP 80**

### "Which port is used for HTTPS?"

→ **TCP 443**

### "Which port is used for RDP?"

→ **TCP 3389**

### "Which port is commonly associated with DNS?"

→ **53**

### "Which OSI layer handles port numbers?"

→ **Transport Layer**

### "AWS security group needs to allow HTTPS traffic"

→ **TCP 443**

---

# 🧠 Quick Summary

```text id="1xq6e3"
                    Network Traffic
                          ↓
                    IP Address
                 "Which machine?"
                          ↓
                       Port
                "Which service?"
                          ↓
                  Application
```

### Important ports:

```text
22    → SSH
53    → DNS
80    → HTTP
443   → HTTPS
3389  → RDP
```

### The most important concept:

> **IP address identifies the destination; port number identifies the network service/application receiving the traffic.**

And remember the networking chain you're building:

```text id="3g4f8a"
IP Address
     ↓
CIDR / Subnet
     ↓
Routing
     ↓
TCP / UDP
     ↓
Port
     ↓
Application / Service
```

This is exactly the foundation you'll need when you start configuring **AWS VPC, Security Groups, NACLs, EC2, Load Balancers, and private/public connectivity**.
