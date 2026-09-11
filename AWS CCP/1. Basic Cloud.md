# ☁️ Cloud Computing Notes

> **Purpose:** Build a clear foundation in Cloud Computing and AWS for an **AWS Cloud Engineer / DevOps** path.
>
> These notes are organized for **understanding first, revision second, and hands-on practice third**.

---

## 📚 Table of Contents

- [1. Evolution of Computing](#1-evolution-of-computing)
  - [Dedicated Servers](#11-dedicated-servers)
  - [Virtual Machines](#12-virtual-machines)
  - [Containers](#13-containers)
  - [Serverless Compute](#14-serverless-compute)
  - [Evolution at a Glance](#15-evolution-at-a-glance)
- [2. Cloud Service Models](#2-cloud-service-models)
  - [IaaS](#21-iaas)
  - [PaaS](#22-paas)
  - [SaaS](#23-saas)
  - [Service Model Comparison](#24-service-model-comparison)
- [3. Cloud Deployment Models](#3-cloud-deployment-models)
  - [Public Cloud](#31-public-cloud)
  - [Private Cloud / On-Premise](#32-private-cloud--on-premise)
  - [Hybrid Cloud](#33-hybrid-cloud)
  - [Multi-Cloud / Cross-Cloud](#34-multi-cloud--cross-cloud)
  - [Deployment Model Comparison](#35-deployment-model-comparison)
- [
---

# 1. Evolution of Computing

A simple way to understand the evolution of computing infrastructure is:


Dedicated Server
       ↓
Virtual Machines
       ↓
Containers
       ↓
Serverless


As you move down this stack, the provider generally manages more of the underlying infrastructure and the customer focuses more on the application.

---

## 1.1 Dedicated Servers

A **dedicated server** is a physical server used entirely by one customer.

### Architecture


┌──────────────────────────────────────────────┐
│              Physical Server                │
│                                              │
│  ┌────────────┬────────────┬────────────┐   │
│  │    App     │    App     │    App     │   │
│  └────────────┴────────────┴────────────┘   │
│                                              │
│          Host Operating System               │
│                                              │
│              Wasted Capacity                 │
└──────────────────────────────────────────────┘


### Characteristics

- One customer uses the physical server.
- Capacity must be estimated in advance.
- You may pay for capacity that is not being used.
- Increasing capacity can require manual changes or migration.
- Replacing physical hardware is difficult.
- Applications share the same host environment.
- Multiple applications can create resource conflicts.
- The customer has direct use of the underlying physical resources.

### Main problem


              Physical Capacity
                    │
        ┌───────────┴───────────┐
        │                       │
     Used                  Unused
      40%                    60%
                              ↑
                         Wasted capacity


**Key idea:** Dedicated servers provide dedicated resources, but they can be expensive and inflexible.

---

# 1.2 Virtual Machines

A **Virtual Machine (VM)** is a software-defined computer running on a physical machine.

A **hypervisor** allows multiple VMs to share the same physical hardware.

### Architecture


┌─────────────────────────────────────────────────────┐
│                 Physical Server                     │
│                                                     │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │
│ │     VM 1     │ │     VM 2     │ │     VM 3     │ │
│ │              │ │              │ │              │ │
│ │     App      │ │     App      │ │     App      │ │
│ │              │ │              │ │              │ │
│ │   Guest OS   │ │   Guest OS   │ │   Guest OS   │ │
│ └──────────────┘ └──────────────┘ └──────────────┘ │
│                                                     │
├─────────────────────────────────────────────────────┤
│                    Hypervisor                       │
├─────────────────────────────────────────────────────┤
│              Host Operating System                  │
└─────────────────────────────────────────────────────┘


### Characteristics

- Multiple VMs can run on one physical server.
- The **hypervisor** manages access to the physical hardware.
- Physical resources can be shared between customers/workloads.
- A customer pays for the resources allocated to their VM rather than an entire physical server.
- You can still over-provision or underutilize a VM.
- Each VM has its own **Guest OS**.
- Applications inside a VM can still compete for that VM's resources.
- VM images can be exported/imported for migration.
- VMs can be scaled vertically or horizontally depending on the platform and architecture.

### Key idea

> **VM = virtual computer with its own operating system.**

---

# 1.3 Containers

Containers provide application-level isolation while sharing the underlying operating system kernel.

In the material here, **Docker** is used as the container technology.

### Architecture


┌─────────────────────────────────────────────────────┐
│                 Physical Server                     │
│                                                     │
│ ┌────────────────┐ ┌────────────────┐ ┌───────────┐│
│ │      VM 1      │ │      VM 2      │ │    VM 3   ││
│ │                │ │                │ │           ││
│ │ App + Container│ │ App + Container│ │App+Cont.  ││
│ │                │ │                │ │           ││
│ │   Guest OS     │ │   Guest OS     │ │ Guest OS  ││
│ └────────────────┘ └────────────────┘ └───────────┘│
│                                                     │
│                    Hypervisor                       │
│                                                     │
│                Host Operating System               │
└─────────────────────────────────────────────────────┘


### Important concepts

- Containers isolate applications and their dependencies.
- Containers can run side by side.
- Containers share the underlying OS kernel.
- Because they do not each need a complete guest OS, containers can be lightweight compared with traditional VMs.
- Containerization can improve resource utilization.
- Docker provides tools for building, running, and managing containers.

### VM vs Container


Virtual Machine
    ↓
Virtual hardware
    ↓
Guest OS
    ↓
Application


Container
    ↓
Container runtime
    ↓
Shared OS kernel
    ↓
Application + dependencies


### Key idea

> **Container = isolated application environment that shares the host kernel.**

---

# 1.4 Serverless Compute

> **Serverless does NOT mean there are no servers.**

It means the **cloud provider manages the underlying servers/infrastructure for you**.

The customer focuses primarily on code and configuration rather than provisioning and maintaining servers.

### Conceptual architecture


                 YOUR CODE
                     │
                     ▼
             Serverless Platform
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Compute    Compute    Compute
       capacity   capacity   capacity
          │          │          │
          └──────────┼──────────┘
                     ▼
             Provider manages
              infrastructure


### What you typically provide

Depending on the service, you may specify things such as:

- Application/function code
- Memory
- Timeout/execution limits
- Configuration
- Permissions
- Data sources

### What the provider manages

Typically, the provider handles much of:

- Servers
- VMs
- Operating systems
- Infrastructure
- Scaling of the underlying platform

### Cost concept

Serverless can be cost-effective for workloads where compute is used intermittently because pricing is generally tied to usage rather than maintaining an always-running server.

### Key idea

> **Serverless = you manage the application/code; the provider manages the underlying infrastructure.**

---

# 1.5 Evolution at a Glance

| Technology | Main idea | Customer manages | Relative overhead |
|---|---|---|---|
| **Dedicated Server** | One customer owns/uses physical server | Hardware + OS + apps | High |
| **VM** | Multiple virtual computers share hardware | Guest OS + apps | Lower than dedicated hardware |
| **Container** | Isolated applications share OS kernel | Application + dependencies | Lower than full VMs |
| **Serverless** | Provider runs the infrastructure | Mainly code/configuration | Lowest infrastructure management |

### Mental model


More infrastructure control
           ↑
           │
   Dedicated Server
           │
           │
           VM
           │
           │
       Container
           │
           │
       Serverless
           │
           ↓
Less infrastructure management


---

# 2. Cloud Service Models

The three common service models are:


IaaS
 ↓
PaaS
 ↓
SaaS

More infrastructure management
            ↓
       Less management


The key question is:

> **Who is responsible for what?**

---

# 2.1 IaaS

## Infrastructure as a Service

IaaS provides fundamental computing infrastructure through the cloud.

Examples include:

- Virtual machines
- CPU
- Memory
- Storage
- Networking

### Customer responsibility


YOU MANAGE
├── Operating System
├── Applications
├── Runtime
└── Data


### Provider responsibility


PROVIDER MANAGES
├── Physical servers
├── Data center
├── Physical networking
├── Physical storage
└── Underlying infrastructure


### Example

You create an **EC2 instance**, choose an operating system, and install/configure your applications.

### Think

> **IaaS = "Give me the infrastructure; I'll manage the system."**

---

# 2.2 PaaS

## Platform as a Service

PaaS provides a managed platform on which developers can deploy applications.

The provider manages more of the infrastructure and operating system.

### Customer responsibility


YOU MANAGE
├── Application
└── Data


### Provider responsibility


PROVIDER MANAGES
├── Runtime
├── Operating System
├── VM / compute infrastructure
├── Storage
├── Networking
└── Physical infrastructure


### Examples

- Heroku
- AWS Elastic Beanstalk
- Azure App Service

### Think

> **PaaS = "Give me a platform; I'll focus on my application."**

---

# 2.3 SaaS

## Software as a Service

SaaS provides a complete software application to the end user.

The provider manages almost everything required to run the application.

### Customer


YOU
 ↓
Use the software


### Provider


PROVIDER
 ↓
Application
 ↓
Runtime
 ↓
Operating System
 ↓
Infrastructure
 ↓
Hardware


### Examples

- Gmail
- Microsoft 365
- Salesforce

### Think

> **SaaS = "Give me the finished software; I'll use it."**

---

# 2.4 Service Model Comparison

| | **IaaS** | **PaaS** | **SaaS** |
|---|---|---|---|
| Main user | Admin / Cloud Engineer | Developer | End User |
| Infrastructure | Provider | Provider | Provider |
| OS | Customer | Provider | Provider |
| Runtime | Customer | Provider | Provider |
| Application | Customer | Customer | Provider |
| Data | Customer | Customer | Customer controls usage/data |
| Management | More | Medium | Less |

### Easy memory trick


IaaS → Infrastructure
PaaS → Platform
SaaS → Software


Or:


IaaS → "I manage the OS"
PaaS → "I manage the application"
SaaS → "I use the application"


### Important relationship

> **More control → IaaS → PaaS → SaaS → Less infrastructure management**

---

# 3. Cloud Deployment Models

The main deployment approaches in these notes are:


1. Public Cloud
2. Private Cloud / On-Premise
3. Hybrid Cloud
4. Multi-Cloud / Cross-Cloud


These answer a different question from IaaS/PaaS/SaaS.

### Service model vs deployment model


SERVICE MODEL
"What does the provider manage?"

IaaS / PaaS / SaaS


DEPLOYMENT MODEL
"Where/how is the infrastructure deployed?"

Public / Private / Hybrid / Multi-Cloud


---

# 3.1 Public Cloud

In a public cloud, infrastructure is provided by a **Cloud Service Provider (CSP)**.

Examples:

- AWS
- Microsoft Azure
- Google Cloud

### Conceptual architecture


                Users
                  │
                  ▼
              Internet
                  │
                  ▼
           Public Cloud CSP
                  │
        ┌─────────┴─────────┐
        │                   │
     Public              Private
     Subnet               Subnet


### Common use cases

- Startups
- SaaS companies
- New applications
- Organizations that want to avoid owning physical data-center infrastructure

### Key idea

> **Public Cloud = use infrastructure provided by a cloud provider.**

---

# 3.2 Private Cloud / On-Premise

A private/on-premise environment is hosted and managed within the organization's own infrastructure.

Example technology mentioned in the source:

- OpenStack

### Conceptual architecture


             Company
                 │
                 ▼
         Company Data Center
                 │
             OpenStack
                 │
        ┌────────┴────────┐
        │                 │
      Public            Private
      Network            Network


### The organization manages

- Physical infrastructure
- Hardware
- Networking
- Data-center operations
- Cloud platform/software
- Workloads

### Common use cases

- Government/public-sector environments
- Organizations with strict compliance requirements
- Large enterprises
- Organizations with existing data-center investments

### Key idea

> **Private / On-Premise = the organization operates the infrastructure itself.**

---

# 3.3 Hybrid Cloud

**Hybrid Cloud = On-Premise + Public Cloud connected together.**

### Architecture


       COMPANY DATA CENTER                    AWS
       ┌──────────────────┐            ┌──────────────┐
       │                  │            │              │
       │   Private        │            │     VPC      │
       │   Environment    │◄──────────►│              │
       │                  │ VPN /      │              │
       └──────────────────┘ Connection └──────────────┘


The environments can be connected using technologies such as:

- VPN
- Dedicated/private connectivity

### Why use hybrid cloud?

Organizations may not be able or willing to move everything to the public cloud because of:

- Existing infrastructure investments
- Legacy applications
- Compliance requirements
- Security requirements
- Migration effort

### Common examples

- Banks
- FinTech
- Investment organizations
- Large enterprises
- Organizations with legacy systems

### Key idea

> **Hybrid = company infrastructure + public cloud working together.**

---

# 3.4 Multi-Cloud / Cross-Cloud

**Multi-cloud** means using more than one cloud provider.

Example:


              MULTI-CLOUD
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
         AWS     Azure      GCP


A workload or organization may use services from multiple providers.

### Technologies mentioned in the source

- **Amazon EKS** → managed Kubernetes service on AWS
- **Google Kubernetes Engine (GKE)** → managed Kubernetes service on Google Cloud
- **Azure Arc** → helps manage resources across different environments/clouds

### Example


AWS                         GCP
 │                           │
 EKS                         GKE
 │                           │
 └──────── Azure Arc ────────┘
                 │
                 ▼
          Central management


### Why use multiple clouds?

Possible reasons include:

- Reduce vendor lock-in
- Use specialized services from different providers
- Meet regional/compliance requirements
- Distribute workloads
- Improve resilience where appropriate

### Key idea

> **Multi-Cloud = multiple cloud providers.**

---

# 3.5 Deployment Model Comparison

| Model | Infrastructure | Main owner/operator | Example |
|---|---|---|---|
| **Public Cloud** | Cloud provider | CSP | AWS |
| **Private / On-Premise** | Organization | Company | Company data center |
| **Hybrid Cloud** | Company + CSP | Both | Company DC + AWS |
| **Multi-Cloud** | Multiple CSPs | Multiple providers | AWS + Azure + GCP |

### Quick memory


Public Cloud
→ Provider runs the infrastructure

Private / On-Premise
→ Company runs the infrastructure

Hybrid
→ Company + Provider

Multi-Cloud
→ Multiple Cloud Providers


---

# 4. Important Differences

## 4.1 VM vs Container

| VM | Container |
|---|---|
| Has its own guest OS | Shares host OS kernel |
| Heavier | Lightweight |
| More isolation at OS level | Application/process-level isolation |
| Usually slower to start | Usually faster to start |
| Includes OS overhead | Less OS overhead |
| Good for full OS environments | Good for portable applications |

### Remember


VM
Application
   ↓
Guest OS
   ↓
Virtual hardware


Container
Application
   ↓
Container
   ↓
Shared OS kernel


---

## 4.2 Scalability vs Elasticity

These concepts are related but not identical.


Scalability
= Ability to increase/decrease capacity

Elasticity
= Automatically adjust capacity according to demand


Example:


Traffic ↑
   ↓
2 servers → 10 servers

Traffic ↓
   ↓
10 servers → 2 servers


If the adjustment is automated according to demand, that demonstrates elasticity.

---

## 4.3 Serverless ≠ No Servers

This is a very common misconception.


❌ Serverless = There are no servers

✅ Serverless = You don't manage the servers


The cloud provider still operates the underlying infrastructure.

---

## 4.4 Hybrid vs Multi-Cloud

### Hybrid


On-Premise + Cloud

Company DC  ←→  AWS


### Multi-Cloud


Multiple Cloud Providers

AWS  +  Azure  +  GCP


### One-line memory

> **Hybrid = different environments**

> **Multi-Cloud = multiple cloud providers**

---

## 4.5 Service Model vs Deployment Model

Don't mix these two categories.

### Service model


IaaS
PaaS
SaaS


Answers:

> **"How much does the provider manage?"**

### Deployment model


Public
Private
Hybrid
Multi-Cloud


Answers:

> **"Where/how is the infrastructure deployed?"**

---

# 5. Exam Memory Sheet

## ☁️ Computing Evolution


Dedicated Server
       ↓
Virtual Machine
       ↓
Container
       ↓
Serverless


### Core idea

> Moving toward serverless generally means **less infrastructure management for the customer**.

---

## 🧩 Service Models


IaaS → Infrastructure
PaaS → Platform
SaaS → Software



IaaS
↓
More control

PaaS
↓
Less infrastructure management

SaaS
↓
Mostly use the finished application


---

## 🌍 Deployment Models


Public Cloud
→ Provider infrastructure

Private / On-Premise
→ Company infrastructure

Hybrid
→ Company + Public Cloud

Multi-Cloud
→ Multiple Cloud Providers


---

## ⭐ High-Value Definitions

| Term | Remember |
|---|---|
| Dedicated Server | One customer uses physical server |
| VM | Virtual computer with guest OS |
| Hypervisor | Enables/manages VMs on physical hardware |
| Container | Isolated application sharing OS kernel |
| Serverless | Provider manages servers/infrastructure |
| IaaS | Infrastructure provided; customer manages more |
| PaaS | Platform provided; customer focuses on application |
| SaaS | Finished software provided to user |
| Public Cloud | Provider-owned infrastructure |
| Private Cloud | Organization-controlled infrastructure |
| Hybrid | On-premise + public cloud |
| Multi-Cloud | Multiple cloud providers |

-