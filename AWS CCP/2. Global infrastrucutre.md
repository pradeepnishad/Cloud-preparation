# AWS Cloud & SAA-C03 Learning Notes

> Beginner-friendly AWS notes focused on understanding concepts, remembering exam points, and building practical intuition.
>
> **Goal:** Learn AWS well enough to work toward an AWS Cloud Engineer / DevOps role — not just memorize certification questions.

---

## 📚 Table of Contents

1. [AWS Account & IAM Setup](#1-aws-account--iam-setup)
2. [Cloud Computing Benefits](#2-cloud-computing-benefits)
3. [AWS Global Infrastructure](#3-aws-global-infrastructure)
4. [AWS Regions](#4-aws-regions)
5. [Region Selection](#5-how-to-choose-an-aws-region)
6. [Region vs Availability Zone](#6-region-vs-availability-zone)
7. 

---

# 1. AWS Account & IAM Setup

## 1.1 Root User

The **AWS Root User** is the account owner and has extremely powerful permissions.

Use the root user only for tasks that specifically require it.

### Basic flow


Root User
    |
    | Create
    v
IAM User
    |
    | Permissions
    v
Group / Policy
    |
    | Authentication protection
    v
MFA
    |
    v
AWS Console


### Recommended approach


ROOT USER
   |
   +--> MFA enabled
   |
   +--> Kept for account-level/emergency tasks

IAM USER
   |
   +--> MFA enabled
   |
   +--> Used for normal learning/work


---

## 1.2 IAM User

An **IAM user** is an identity within an AWS account.

For a user who needs console access:


IAM
 |
 +-- Users
       |
       +-- Create user


Example:


Username: cloud-user
Console access: Enabled


### Important

If the user only needs console access, don't create access keys unnecessarily.

Create only the credentials the user actually needs.

---

## 1.3 IAM Groups

Instead of managing permissions individually for every user, users can be placed into groups.


AWS Account
    |
    +-- IAM User
           |
           +-- AWS-Admins
                  |
                  +-- Policy
                       |
                       +-- Permissions


Example learning setup:


Group: AWS-Admins
Policy: AdministratorAccess


### Why groups?

Groups make permission management easier when multiple users need similar access.

---

## 1.4 IAM Policies

An **IAM policy** defines what an identity is allowed to do.

Conceptually:


Policy
   |
   +-- Who?
   +-- What AWS resource?
   +-- What action?
   +-- Under what conditions?


Example:


Developer
   |
   +-- Read S3 objects
   +-- Cannot delete S3 objects


### Least privilege

Give an identity **only the permissions it actually needs**.

> `AdministratorAccess` is useful for a dedicated learning account, but it is not a good default for production users.

---

## 1.5 MFA

**MFA = Multi-Factor Authentication**

It adds another authentication factor in addition to the password.

Typical flow:


Username + Password
        |
        v
Authenticator code
        |
        v
AWS Console


A virtual MFA device can use an authenticator app that generates time-based codes.

### Two-code setup

During MFA registration, AWS may ask for two consecutive codes:


Code 1
  |
  | wait for next code
  v
Code 2


The second code must be the newly generated code, not a repeat of the first.

---

## 1.6 Final IAM Learning Setup


                    AWS ACCOUNT
                         |
          +--------------+--------------+
          |                             |
      ROOT USER                    IAM USER
          |                             |
         MFA                           MFA
          |                             |
   Account tasks                  AWS-Admins
                                        |
                                        v
                              AdministratorAccess
                                        |
                                        v
                              AWS Resources
                         +-------+-------+-------+
                         |       |       |       |
                        EC2      S3      VPC   ...


### Remember

| Term | Meaning |
|---|---|
| Root user | AWS account owner / highly privileged identity |
| IAM user | Identity used for normal access in this learning setup |
| IAM group | Collection used to manage users with common permissions |
| IAM policy | Defines permissions |
| MFA | Additional authentication factor |
| AdministratorAccess | Very broad administrative permissions |

> **IAM itself has no charge**, but the AWS resources you create using your permissions can cost money.

---

# 2. Cloud Computing Benefits

Cloud computing provides organizations with infrastructure and services without requiring them to own and operate all of the underlying physical infrastructure themselves.

## 2.1 Agility 🚀

**Agility = ability to move quickly.**

Traditional infrastructure may require:


Buy server
   |
Ship server
   |
Install
   |
Configure
   |
Deploy
   |
Weeks


Cloud:


AWS Console / Terraform
        |
        v
   Create resource
        |
        v
      Minutes


### Remember

> **Cloud increases speed and agility.**

---

## 2.2 Pay-as-you-go 💰

Instead of making large upfront infrastructure purchases, cloud services can use usage-based pricing.


On-premises
    |
    +-- Buy hardware upfront
    +-- Maintain hardware
    +-- Replace hardware


Cloud
    |
    +-- Provision resources
    +-- Pay according to usage


### CAPEX vs OPEX

**CAPEX (Capital Expenditure)**


Large upfront investment
        |
        v
Buy physical infrastructure


**OPEX (Operational Expenditure)**


Ongoing operating expense
        |
        v
Pay for services/resources


### Important

> Pay-as-you-go does **not** automatically mean cloud is cheaper.

Poorly managed AWS resources can still generate a large bill.

---

## 2.3 Economies of Scale 📈

Cloud providers operate infrastructure at enormous scale.


                     AWS
                      |
        +-------------+-------------+
        |             |             |
     Customer A    Customer B    Customer C
        |             |             |
        +-------------+-------------+
                      |
              Massive scale
                      |
              Lower unit costs


The provider can spread infrastructure costs across a very large customer base.

---

## 2.4 Global Reach 🌎

AWS has infrastructure in many geographic locations.


Users in India
      |
      v
Mumbai Region

Users in Europe
      |
      v
European Region

Users in Singapore
      |
      v
Singapore Region


Choosing an appropriate Region can help place workloads closer to users and reduce network latency.

---

## 2.5 Security 🔐

Cloud providers handle security responsibilities such as physical data-center security.

Customers are still responsible for correctly configuring many aspects of their workloads.

Examples:


IAM
Security Groups
Encryption
S3 permissions
Network controls
MFA


This leads to the:

> **Shared Responsibility Model**

A simple mental model:


AWS
 |
 +-- Physical infrastructure
 +-- Data-center security
 +-- Underlying cloud infrastructure

Customer
 |
 +-- Access configuration
 +-- Data
 +-- Permissions
 +-- Application configuration
 +-- Security settings


The exact responsibility depends on the AWS service being used.

---

## 2.6 Reliability 🛡️

Cloud architectures can use:

- Backups
- Replication
- Disaster recovery
- Fault tolerance
- Multiple Availability Zones

Example:


             Load Balancer
                  |
          +-------+-------+
          |               |
          v               v
        EC2-A           EC2-B
        AZ-1             AZ-2


If one component fails, another component may continue serving the workload.

---

## 2.7 High Availability

**High Availability (HA)** means designing a system to minimize downtime and remain available despite component failures.

Example:


             Application
                  |
             Load Balancer
              /       \
             /         \
          EC2-A       EC2-B
          AZ-1         AZ-2


If EC2-A fails:


EC2-A  ❌

EC2-B  ✅
  |
  v
Application can continue serving users


### Remember

> **Multiple AZs are a common building block for high availability.**

---

## 2.8 Scalability 📈

**Scalability = ability to increase or decrease capacity to handle workload changes.**

Example:


Normal traffic
     |
     v
  2 servers

Higher traffic
     |
     v
  10 servers


Scaling can happen in different ways:

### Vertical scaling

Increase the size of one resource.


Small EC2
   |
   v
Larger EC2


### Horizontal scaling

Add more instances.


1 EC2
  |
  v
5 EC2


---

## 2.9 Elasticity 🔄

**Elasticity = automatically adjusting capacity as demand changes.**

Example:


Traffic increases
       |
       v
Auto Scaling
       |
       v
2 EC2 ---> 10 EC2


Traffic decreases
       |
       v
Auto Scaling
       |
       v
10 EC2 ---> 2 EC2


### Scalability vs Elasticity

| Concept | Meaning |
|---|---|
| Scalability | Ability to increase/decrease capacity |
| Elasticity | Automatic adjustment of capacity according to demand |
| High Availability | Designed to minimize downtime |

### Easy memory trick


Scalability = CAN scale
Elasticity  = AUTOMATICALLY scales
HA          = STAYS AVAILABLE


---

# 3. AWS Global Infrastructure

## 3.1 What is it?

The **AWS Global Infrastructure** is AWS's globally distributed physical infrastructure and networking used to provide cloud services.

Think:


              AWS GLOBAL INFRASTRUCTURE
                         |
        +----------------+----------------+
        |                |                |
        v                v                v
     Regions            PoPs        Other locations
        |
        v
Availability Zones
        |
        v
Data centers / facilities


AWS infrastructure is physically distributed and connected through AWS networking.

---

# 4. AWS Regions

## 4.1 What is an AWS Region?

An **AWS Region** is a geographically distinct location containing one or more Availability Zones.


              AWS REGION
             "Mumbai"
                  |
        +---------+---------+
        |         |         |
        v         v         v
       AZ-1      AZ-2      AZ-3


### Remember

> **Region = geographic area**

A Region is not the same thing as a single data center.

---

## 4.2 Why use multiple Regions?

Regions are geographically separated and operate independently from other Regions.

This separation can help with:

- Disaster recovery
- Geographic requirements
- Data residency requirements
- Global deployments
- Business continuity

Example:


          Application
               |
       +-------+-------+
       |               |
       v               v
   Mumbai Region   Singapore Region
       |               |
    AZs / AZs       AZs / AZs


If an entire Region becomes unavailable, another Region can be used as part of a disaster-recovery design.

---

# 5. How to Choose an AWS Region

When selecting a Region, consider four major factors.

## 5.1 Compliance 🔐

Ask:

> **Where am I legally allowed or required to store/process this data?**

Example:


Customer data
     |
     v
Regulatory requirement
     |
     v
Choose an appropriate Region


---

## 5.2 Cost 💰

AWS service pricing can vary by Region.

Ask:

> **How much will this workload cost in each candidate Region?**

Don't choose a Region based only on price.

---

## 5.3 Service Availability 🧰

Not every AWS service or feature is available in every Region.

Ask:

> **Are the AWS services/features I need available in this Region?**

Example:


Need Service X
      |
      v
Mumbai
  |
  +-- Not available
      |
      v
Choose a supported Region


Always check current AWS service availability when planning a real deployment.

---

## 5.4 Latency 🚀

Ask:

> **How close is the Region to my users?**

Example:


Indian users
     |
     v
Mumbai Region
     |
     v
Generally lower network latency


Compared with:


Indian users
     |
     v
US Region
     |
     v
Generally higher network latency


### Easy memory trick


C - Compliance
C - Cost
S - Service availability
L - Latency

CCSL


Or ask:

> **Is it legal? Is it affordable? Is the service available? Is it close to my users?**

---

# 6. Region vs Availability Zone

This distinction is extremely important.

## Region

A geographic area containing one or more Availability Zones.


          Mumbai Region
                |
        +-------+-------+
        |       |       |
       AZ-1    AZ-2    AZ-3


## Availability Zone

An isolated location/infrastructure grouping within a Region.

A Region's AZs are designed to provide isolation from failures while being connected through AWS networking.

---

## 6.1 AZ failure

If you use multiple AZs:


          Mumbai Region
          /            \
       AZ-1            AZ-2
        |                |
      EC2-A            EC2-B


If:


AZ-1 ❌


AZ-2 can potentially continue serving traffic.

---

## 6.2 Region failure

If the entire Region fails:


Mumbai Region ❌
      |
      +-- AZ-1 unavailable
      +-- AZ-2 unavailable
      +-- AZ-3 unavailable


Multiple AZs within that Region do not protect you from a **complete Regional failure**.

A multi-Region design may be required for that level of disaster recovery.

### Exam memory

> **AZ failure → multiple AZs**

> **Region failure → multiple Regions**

---

# 7. Important AWS Global Infrastructure Components

## 7.1 Availability Zones

Used to isolate infrastructure and improve availability within a Region.


Region
 |
 +-- AZ-1
 +-- AZ-2
 +-- AZ-3


---

## 7.2 Points of Presence (PoPs)

AWS uses Points of Presence for services such as CloudFront.

The main idea:

> **Put content closer to users.**

Example:


                 Origin
                   |
               CloudFront
                   |
        +----------+----------+
        |          |          |
        v          v          v
      PoP        PoP        PoP
    Mumbai     London    Singapore
        |          |          |
      Users      Users      Users


For cached content, CloudFront can serve users from locations closer to them.

Useful for:

- HTML
- CSS
- JavaScript
- Images
- Videos

---

## 7.3 AWS Direct Connect

**Direct Connect** provides a dedicated network connection from an organization's network to AWS.

Typical concept:


On-premises
    |
    | Dedicated connection
    v
Direct Connect
    |
    v
AWS


Useful when organizations need dedicated connectivity and predictable network characteristics.

---

## 7.4 Local Zones

A **Local Zone** places selected AWS infrastructure closer to a specific metropolitan area.

Main purpose:

> **Very low latency for workloads that need to be physically closer to users.**


AWS Region
    |
    v
Local Zone
    |
    v
Nearby users / workloads


---

## 7.5 Wavelength Zones

**AWS Wavelength** brings AWS infrastructure close to telecommunications/5G networks.

Simplified:


AWS Region
    |
    v
Wavelength Zone
    |
    v
5G network
    |
    v
Mobile users / devices


Useful for workloads where very low latency to mobile/5G networks matters.

---

# 8. SAA-C03 Memory Sheet

## Cloud Benefits


Agility           -> Deploy quickly
Pay-as-you-go     -> Pay based on usage
Economies of scale-> Provider operates at huge scale
Global reach      -> Deploy in multiple geographic locations
Security          -> Security controls + shared responsibility
Reliability       -> Backups / replication / fault tolerance
High Availability -> Minimize downtime
Scalability       -> Increase/decrease capacity
Elasticity        -> Automatically adjust capacity


---

## Global Infrastructure


AWS Global Infrastructure
        |
        +-- Region
        |     |
        |     +-- Availability Zone
        |             |
        |             +-- Data centers / facilities
        |
        +-- Points of Presence
        |
        +-- Local Zones
        |
        +-- Wavelength Zones
        |
        +-- Direct Connect locations


---

## Region


REGION
= Geographically distinct location
= Contains one or more AZs


## Availability Zone


AZ
= Isolated infrastructure grouping within a Region
= Helps design for high availability


## PoP / Edge


PoP
= Network location used by AWS services such as CloudFront
= Helps bring content/services closer to users


## Local Zone


Local Zone
= Selected AWS infrastructure closer to a metropolitan area
= Low-latency workloads


## Wavelength


Wavelength Zone
= AWS infrastructure close to 5G networks
= Very low latency to mobile/5G applications

