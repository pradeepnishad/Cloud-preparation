 
 The evolution of computing,

-> Dedicated Server.

* A physical server **wholly utilized by a single customer**.
* You have to guess your capacity.
* You’ll overpay for an underutilized server.
* You can’t vertically scale; you need a manual migration.
* Replacing a server is very difficult.
* You are limited by your Host Operating System.
* Multiple apps can result in conflicts in resource sharing.
* You have a **guarantee of security, privacy, and full utility of underlying resources**.

┌──────────────────────────────────────────────┐
│                                              │
│                WASTED SPACE                  │
│                                              │
│                                              │
│                                              │
│                                              │
├──────────────┬──────────────┬───────────────┤
│     App      │     App      │      App      │
├──────────────┴──────────────┴───────────────┤
│                                              │
│           Host Operating System              │
│                                              │
└──────────────────────────────────────────────┘


-> Virtual machine

• You can run multiple Virtual Machines on one machine.
• Hypervisor is the software layer that lets you run the VMs.
• A physical server is shared by multiple customers.
• You only pay for a fraction of the server.
• You’ll overpay for an underutilized Virtual Machine.
• You are limited by your Guest Operating System.
• Multiple apps on a single Virtual Machine can result in conflicts
  in resource sharing.
• Easy to export or import images for migration.
• Easy to vertically or horizontally scale.

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

-> Containers
### Docker Containers — Quick Notes

* **Virtual Machine running multiple containers**
* **Docker Daemon** is the software layer that allows you to run multiple containers.
* Containers help **maximize the utilization of available resources**, making it more **cost-effective**.
* Containers **share the same underlying OS/kernel**, so they are more lightweight and efficient than multiple VMs.
* Multiple applications can run **side by side** in isolated containers without interfering with each other.
* Containers avoid conflicts by keeping applications and their dependencies **isolated**.

                PHYSICAL SERVER
┌───────────────────────────────────────────────┐
│                                               │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│  │   VM 1  │  │   VM 2  │  │   VM 3  │       │
│  │         │  │         │  │         │       │
│  │ App     │  │Available│  │Available│       │
│  │ App     │  │ Space   │  │ Space   │       │
│  │ App     │  │         │  │ App     │       │
│  │         │  │ App     │  │ App     │       │
│  │ Docker  │  │ Docker  │  │ Docker  │       │
│  │ Daemon  │  │ Daemon  │  │ Daemon  │       │
│  │         │  │         │  │         │       │
│  │ Guest OS│  │ Guest OS│  │ Guest OS│       │
│  └─────────┘  └─────────┘  └─────────┘       │
│                                               │
│              ─── Hypervisor ───              │
│                                               │
│          Host Operating System                │
└───────────────────────────────────────────────┘


SFunctions

Serverless Compute = cloud provider manages the VMs and containers for you.
You simply upload your code and specify:
Memory required
Execution duration/timeout
You are responsible mainly for your code and data.
You don't manage:
Servers
VMs
OS
Containers
Infrastructure
Cost-effective: you generally pay based on the resources/time your code actually executes.
The underlying infrastructure is started when needed and can scale automatically.

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
│  │Guest OS│   │Guest OS│   │Guest OS│       │
│  └────────┘   └────────┘   └────────┘       │
│                                              │
│              ── Hypervisor ──               │
│                                              │
│          Host Operating System               │
└──────────────────────────────────────────────┘



## Types of Cloud Computing

The image shows the **3 main cloud service models**:

```text
          SaaS
   Software as a Service
          ↑
          │  For Customers
          │
          │
          PaaS
   Platform as a Service
          ↑
          │  For Developers
          │
          │
          IaaS
 Infrastructure as a Service
          ↑
          │  For Admins
```

### 1. IaaS — Infrastructure as a Service

**For:** System/Cloud Administrators

The cloud provider gives you the basic infrastructure:

* Virtual machines
* CPU & RAM
* Storage
* Networking
* Data centers

You manage things like:

* OS
* Applications
* Runtime
* Data

**Examples:** AWS, Microsoft Azure, Oracle Cloud

```text
You manage → OS → Apps → Data
Provider    → VM → Storage → Network → Hardware
```

**Example:** You create an EC2 VM on AWS and install Ubuntu + Docker yourself.

---

### 2. PaaS — Platform as a Service

**For:** Developers

The provider manages the infrastructure **and OS**, so developers can focus mainly on deploying applications.

```text
You manage → Application + Data
Provider    → Runtime + OS + VM + Storage + Network + Hardware
```

**Examples:** Heroku, AWS Elastic Beanstalk, Azure App Service

**Example:** You deploy your Python application to Heroku without worrying about configuring the underlying server.

---

### 3. SaaS — Software as a Service

**For:** End users / Customers

The provider manages **everything**, and you simply use the software.

```text
You manage → Basically just your usage/data
Provider    → Application → Runtime → OS → VM → Hardware → Everything
```

**Examples:**

* Gmail
* Microsoft 365
* Salesforce

You don't worry about installing, patching, maintaining, or scaling the application.

---

### Easy way to remember

Think of **ordering food** 🍔:

| Model    | You are responsible for           |
| -------- | --------------------------------- |
| **IaaS** | Kitchen + cooking setup + cooking |
| **PaaS** | Just preparing/cooking the food   |
| **SaaS** | Just eating the finished food     |

Or, for cloud:

> **IaaS → Manage infrastructure**
> **PaaS → Manage application**
> **SaaS → Just use the software**

**More control → IaaS → PaaS → SaaS → Less management**.
## Cloud Computing Deployment Models

There are **3 main deployment models** shown here:

### 1. Public Cloud ☁️

Everything is built on a **Cloud Service Provider (CSP)**.

Examples:

* AWS
* Azure
* Google Cloud

```text
Internet
   ↓
AWS / Azure / GCP
   ↓
VPC
 ├── Public Subnet
 └── Private Subnet
```

**Also called:** Cloud-Native / Cloud-First

👉 You use the provider's infrastructure instead of owning the physical servers.

---

### 2. Private Cloud 🏢

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

**Also called:** On-Premise

The company is responsible for managing the infrastructure, hardware, networking, etc.

**Example:** A company builds its own private cloud using **OpenStack**.

---

### 3. Hybrid Cloud 🔄

A combination of **On-Premise + Public Cloud**.

```text
 Company Data Center              AWS
┌──────────────────┐          ┌──────────────┐
│    OpenStack     │          │     VPC      │
│                  │          │              │
│ Private | Public │◄────────►│ Public|Private│
└──────────────────┘   VPN    └──────────────┘
```

The two environments are connected, commonly using a **VPN or dedicated private connection**.

### Easy way to remember

| Model             | Where is infrastructure?  |
| ----------------- | ------------------------- |
| **Public Cloud**  | CSP's data center         |
| **Private Cloud** | Company's own data center |
| **Hybrid Cloud**  | Both company + CSP        |


## Cross-Cloud / Multi-Cloud

**Cross-Cloud** means using **multiple cloud providers** in the same overall environment.

For example, you could use:

```text
              CROSS-CLOUD
                  │
       ┌──────────┴──────────┐
       │                     │
      AWS                   GCP
       │                     │
  Amazon EKS          GCP Kubernetes
       │                     │
       └─────── Azure Arc ───┘
```

### In this diagram

* **Amazon EKS** → Managed Kubernetes service on **AWS**
* **GCP Kubernetes Engine (GKE)** → Managed Kubernetes service on **Google Cloud**
* **Azure Arc** → Helps manage Kubernetes resources running across different environments/clouds from Azure.

So you could have:

```text
AWS                         GCP
│                           │
EKS                         GKE
│                           │
└──────── Azure Arc ────────┘
             │
       Central management
```

### Why use Cross-Cloud?

Companies may use multiple cloud providers to:

* Avoid **vendor lock-in**
* Use the **best service** from each cloud
* Improve **resilience/availability**
* Meet different **regional/compliance** requirements
* Distribute workloads across providers

### Cross-Cloud vs Hybrid Cloud

This distinction is important:

**Hybrid Cloud:**

```text
On-Premise + Public Cloud

Company DC ←→ AWS
```

**Multi-Cloud / Cross-Cloud:**

```text
AWS ←→ Azure ←→ GCP
```

👉 **Hybrid = different environments** (on-prem + cloud)
👉 **Multi-cloud = multiple cloud providers**
👉 **Cross-cloud** is often used to describe workloads/management spanning multiple clouds.


Summary for depluyment model

## Cloud Computing Deployment Models

This diagram gives a practical comparison of **Cloud, Hybrid, and On-Premise**.

### 1. Cloud ☁️

Everything is primarily hosted in a **Cloud Service Provider (CSP)**.

```text
Company
   ↓
AWS / Azure / GCP
   ↓
Cloud Resources
```

**Common for:**

* Startups
* SaaS companies
* New projects
* Small companies

**Why?**
They can avoid buying and maintaining their own data-center infrastructure.

---

### 2. Hybrid Cloud 🔄

Uses **both cloud and on-premise infrastructure**.

```text
          Hybrid
         /      \
   On-Premise   Cloud
       │          │
       └────┬─────┘
         Connected
```

For example, a bank might keep sensitive/legacy systems on-premise while running newer applications in AWS or Azure.

**Common for:**

* Banks
* FinTech
* Investment management
* Large organizations
* Companies with legacy infrastructure

**Why?**
Moving everything to the cloud may be difficult because of **migration effort, security, compliance, or existing investments in infrastructure**.

---

### 3. On-Premise 🏢

The organization **owns/operates the infrastructure in its own data center**.

```text
Company
   ↓
Own Data Center
   ↓
Servers / Storage / Network
   ↓
Virtual Machines / Applications
```

It's sometimes called a **Private Cloud**, but technically **on-premise and private cloud aren't always identical**. A private cloud specifically implies cloud-like capabilities such as self-service, resource pooling, and automation.

**Common for:**

* Government/public sector
* Hospitals handling highly sensitive data
* Large regulated enterprises
* Organizations with strict compliance requirements

---

### 🔥 Simple comparison

|                | Cloud      | Hybrid           | On-Premise   |
| -------------- | ---------- | ---------------- | ------------ |
| Infrastructure | CSP        | CSP + Company    | Company      |
| Data center    | Provider's | Both             | Company's    |
| Management     | Least      | Shared           | Most         |
| Initial cost   | Low        | Medium/High      | High         |
| Scalability    | ⭐⭐⭐        | ⭐⭐               | ⭐            |
| Example        | AWS        | AWS + Company DC | Company's DC |

### Remember it like this:

> **Cloud → Provider runs the infrastructure**
> **Hybrid → Provider + Company run infrastructure**
> **On-Premise → Company runs the infrastructure**

