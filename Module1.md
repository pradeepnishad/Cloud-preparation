# Cloud Computing Notes

## 1. Evolution of Computing

### Dedicated Server

A **dedicated server** is a physical server wholly utilized by a single customer.

#### Characteristics

- A physical server is **wholly utilized by a single customer**.
- You have to guess your required capacity.
- You may **overpay for an underutilized server**.
- You can't vertically scale easily; you need a manual migration.
- Replacing a server is very difficult.
- You are limited by your **Host Operating System**.
- Multiple applications can result in conflicts during resource sharing.
- You have a **guarantee of security, privacy, and full utility of the underlying resources**.

#### Architecture

```text
┌──────────────────────────────────────────────┐
│                                              │
│                 WASTED SPACE                 │
│                                              │
│                                              │
├──────────────┬──────────────┬───────────────┤
│     App      │     App      │      App      │
├──────────────┴──────────────┴───────────────┤
│                                              │
│             Host Operating System            │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 2. Virtual Machines

A **Virtual Machine (VM)** allows you to run multiple virtual machines on one physical machine.

### Characteristics

- You can run **multiple VMs on one physical machine**.
- A **Hypervisor** is the software layer that allows you to run VMs.
- A physical server can be shared by multiple customers.
- You only pay for a fraction of the physical server.
- You may still overpay for an **underutilized VM**.
- You are limited by your **Guest Operating System**.
- Multiple applications on a single VM can result in conflicts during resource sharing.
- VM images are easy to **export/import for migration**.
- VMs are easy to **vertically or horizontally scale**.

### Architecture

```text
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐  │
│  │ Wasted      │   │ Wasted      │   │ Wasted      │  │
│  │ Space       │   │ Space       │   │ Space       │  │
│  │             │   │             │   │             │  │
│  ├─────────────┤   ├─────────────┤   ├─────────────┤  │
│  │     App     │   │     App     │   │     App     │  │
│  │             │   │     App     │   │             │  │
│  │             │   │             │   │             │  │
│  │   Guest OS  │   │   Guest OS  │   │   Guest OS  │  │
│  └──────┬──────┘   └──────┬──────┘   └──────┬──────┘  │
│         VM                 VM                 VM        │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                     Hypervisor                          │
├─────────────────────────────────────────────────────────┤
│                 Host Operating System                   │
└─────────────────────────────────────────────────────────┘
```

---

## 3. Containers

### Docker Containers

- A **Virtual Machine can run multiple containers**.
- **Docker Daemon** is the software layer that allows you to run and manage multiple containers.
- Containers help **maximize the utilization of available resources**, making them more cost-effective.
- Containers **share the same underlying OS/kernel**, so they are more lightweight and efficient than multiple VMs.
- Multiple applications can run **side by side** in isolated containers without interfering with each other.
- Containers avoid conflicts by keeping applications and their dependencies **isolated**.

### Architecture

```text
                    PHYSICAL SERVER
┌───────────────────────────────────────────────┐
│                                               │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│  │   VM 1  │  │   VM 2  │  │   VM 3  │       │
│  │         │  │         │  │         │       │
│  │ App     │  │Available│  │Available│       │
│  │ App     │  │ Space   │  │ Space   │       │
│  │         │  │ App     │  │ App     │       │
│  │ Docker  │  │ Docker  │  │ Docker  │       │
│  │ Daemon  │  │ Daemon  │  │ Daemon  │       │
│  │         │  │         │  │         │       │
│  │ Guest OS│  │ Guest OS│  │ Guest OS│       │
│  └─────────┘  └─────────┘  └─────────┘       │
│                                               │
│              ─── Hypervisor ───              │
│                                               │
│          Host Operating System               │
└───────────────────────────────────────────────┘
```

---

## 4. Serverless Compute

**Serverless Compute** means the cloud provider manages the underlying **VMs and containers** for you.

### Characteristics

You simply:

1. Upload your code.
2. Specify the required memory.
3. Specify the execution duration/timeout.

You are mainly responsible for:

- Your code
- Your data

You don't manage:

- Servers
- VMs
- Operating Systems
- Containers
- Infrastructure

### Cost

Serverless can be cost-effective because you generally pay based on the **resources/time your code actually executes**.

The underlying infrastructure can be started when needed and can scale automatically.

### Architecture

```text
                    PHYSICAL SERVER
┌──────────────────────────────────────────────┐
│                                              │
│  ┌────────┐   ┌────────┐   ┌────────┐       │
│  │   VM   │   │   VM   │   │   VM   │       │
│  │        │   │        │   │        │       │
│  │ FFFFFF │   │Available│  │Available│      │
│  │ FFFF   │   │ Space   │  │ Space   │      │
│  │ FFFFFF │   │ FFFFFF │   │ FFF    │      │
│  │ F      │   │        │   │ F      │      │
│  │        │   │        │   │        │       │
│  │ Docker │   │ Docker │   │ Docker │       │
│  │ Daemon │   │ Daemon │   │ Daemon │       │
│  │        │   │        │   │        │       │
│  │ Guest OS│  │ Guest OS│  │ Guest OS│       │
│  └────────┘   └────────┘   └────────┘       │
│                                              │
│              ── Hypervisor ──               │
│                                              │
│          Host Operating System               │
└──────────────────────────────────────────────┘
```

> **Key idea:** Serverless does not mean there are no servers. It means **you don't manage the servers**.

---

# 5. Cloud Computing Service Models

There are three main cloud service models:

```text
              SaaS
     Software as a Service
              ↑
              │  For Customers
              │
              PaaS
      Platform as a Service
              ↑
              │  For Developers
              │
              IaaS
 Infrastructure as a Service
              ↑
              │  For Admins
```

## 5.1 IaaS — Infrastructure as a Service

**For:** System / Cloud Administrators

The cloud provider gives you the basic infrastructure:

- Virtual machines
- CPU & RAM
- Storage
- Networking
- Data centers

You manage:

- Operating System
- Applications
- Runtime
- Data

### Responsibility

```text
You manage → OS → Apps → Data

Provider    → VM → Storage → Network → Hardware
```

### Examples

- AWS
- Microsoft Azure
- Oracle Cloud

### Example

You create an **EC2 VM on AWS** and install Ubuntu + Docker yourself.

---

## 5.2 PaaS — Platform as a Service

**For:** Developers

The provider manages the infrastructure **and OS**, so developers can focus mainly on deploying applications.

### Responsibility

```text
You manage → Application + Data

Provider    → Runtime + OS + VM + Storage + Network + Hardware
```

### Examples

- Heroku
- AWS Elastic Beanstalk
- Azure App Service

### Example

You deploy a Python application to Heroku without worrying about configuring the underlying server.

---

## 5.3 SaaS — Software as a Service

**For:** End Users / Customers

The provider manages **everything**, and you simply use the software.

### Responsibility

```text
You manage → Basically just your usage/data

Provider    → Application → Runtime → OS → VM → Hardware → Everything
```

### Examples

- Gmail
- Microsoft 365
- Salesforce

You don't worry about installing, patching, maintaining, or scaling the application.

---

## Easy Way to Remember SaaS, PaaS, and IaaS

Think of **ordering food**:

| Model | You are responsible for |
|---|---|
| **IaaS** | Kitchen + cooking setup + cooking |
| **PaaS** | Preparing/cooking the food |
| **SaaS** | Eating the finished food |

For cloud:

> **IaaS → Manage infrastructure**  
> **PaaS → Manage application**  
> **SaaS → Just use the software**

**More control → IaaS → PaaS → SaaS → Less management**

---

# 6. Cloud Computing Deployment Models

The main deployment models covered here are:

1. Public Cloud
2. Private Cloud / On-Premise
3. Hybrid Cloud
4. Cross-Cloud / Multi-Cloud

---

## 6.1 Public Cloud

Everything is built on a **Cloud Service Provider (CSP)**.

### Examples

- AWS
- Azure
- Google Cloud

### Architecture

```text
Internet
   ↓
AWS / Azure / GCP
   ↓
VPC
 ├── Public Subnet
 └── Private Subnet
```

**Also known as:** Cloud-Native / Cloud-First

You use the provider's infrastructure instead of owning the physical servers.

### Common Use Cases

- Startups
- SaaS companies
- New projects
- Small companies

### Why?

Companies can avoid buying and maintaining their own data-center infrastructure.

---

## 6.2 Private Cloud / On-Premise

Everything is built and hosted in the **company's own data center**.

```text
Company Data Center
       ↓
   OpenStack
       ↓
 ┌───────────────┐
 │ Public Subnet │
 │ Private Subnet│
 └───────────────┘
```

**Also known as:** On-Premise

The company is responsible for managing:

- Infrastructure
- Hardware
- Networking
- Data center operations

### Example

A company builds its own private cloud using **OpenStack**.

### Common Use Cases

- Government / Public Sector
- Hospitals handling sensitive data
- Large regulated enterprises
- Organizations with strict compliance requirements

---

## 6.3 Hybrid Cloud

A combination of **On-Premise + Public Cloud**.

```text
       Company Data Center              AWS
      ┌──────────────────┐          ┌──────────────┐
      │    OpenStack     │          │     VPC      │
      │                  │          │              │
      │ Private | Public │◄────────►│ Public|Private│
      └──────────────────┘    VPN   └──────────────┘
```

The two environments are connected, commonly using a **VPN or dedicated private connection**.

### Common Use Cases

- Banks
- FinTech
- Investment management
- Large organizations
- Companies with legacy infrastructure

### Why Hybrid?

Moving everything to the cloud may be difficult because of:

- Migration effort
- Security requirements
- Compliance
- Existing investments in infrastructure

---

## 6.4 Cross-Cloud / Multi-Cloud

**Cross-Cloud** means using **multiple cloud providers** in the same overall environment.

```text
                 CROSS-CLOUD
                      │
          ┌───────────┴───────────┐
          │                       │
         AWS                     GCP
          │                       │
     Amazon EKS              GCP Kubernetes
          │                       │
          └────── Azure Arc ──────┘
```

### Technologies in the Example

- **Amazon EKS** → Managed Kubernetes service on AWS
- **GCP Kubernetes Engine (GKE)** → Managed Kubernetes service on Google Cloud
- **Azure Arc** → Helps manage Kubernetes resources running across different environments/clouds from Azure

### Example

```text
AWS                         GCP
│                           │
EKS                         GKE
│                           │
└──────── Azure Arc ────────┘
             │
       Central management
```

### Why Use Cross-Cloud?

Companies may use multiple cloud providers to:

- Avoid **vendor lock-in**
- Use the **best service** from each cloud
- Improve **resilience / availability**
- Meet different **regional / compliance** requirements
- Distribute workloads across providers

---

# 7. Hybrid Cloud vs Multi-Cloud

This distinction is important.

### Hybrid Cloud

Uses **different environments**:

```text
On-Premise + Public Cloud

Company DC ←→ AWS
```

### Multi-Cloud / Cross-Cloud

Uses **multiple cloud providers**:

```text
AWS ←→ Azure ←→ GCP
```

### Remember

> **Hybrid = On-Premise + Cloud**

> **Multi-Cloud = Multiple Cloud Providers**

> **Cross-Cloud = Workloads or management spanning multiple clouds**

---

# 8. Deployment Model Summary

| Model | Infrastructure | Data Center | Management | Typical Example |
|---|---|---|---|---|
| **Cloud** | CSP | Provider's | Least | AWS |
| **Hybrid** | CSP + Company | Both | Shared | AWS + Company DC |
| **On-Premise** | Company | Company's | Most | Company's DC |
| **Multi-Cloud** | Multiple CSPs | Multiple providers | Distributed | AWS + Azure + GCP |

### Quick Memory Trick

```text
Cloud
  ↓
Provider runs infrastructure

Hybrid
  ↓
Provider + Company run infrastructure

On-Premise
  ↓
Company runs infrastructure

Multi-Cloud
  ↓
Multiple cloud providers
```

---

# 9. Big Picture

The evolution can be remembered as:

```text
Dedicated Server
       ↓
Virtual Machines
       ↓
Containers
       ↓
Serverless
```

And cloud service models:

```text
IaaS
  ↓
PaaS
  ↓
SaaS

More control → Less management
```

And deployment models:

```text
Public Cloud
Private / On-Premise
Hybrid Cloud
Multi-Cloud
```
