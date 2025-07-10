# Silverfort

The identity security platform you deserve

### What is Silverfort Identity Security platform
Silverfort's patented technology aims to protect organizations from identity-based attacks by integrating with existing identity and access management solutions, such as AD (Active Directory) and cloud-based services, and extending secure access controls like Risk-Based Authentication and MFA (Multi-Factor Authentication) to all their resources. This includes on-prem and cloud resources, legacy systems, command-line tools and service accounts.

<br>

### Key Capabilities
Authentication Firewall
- Stop unauthorized access with zero trust policies
- Build identity security policies on top of existing IAM platforms
- Protect access to domain resources on identity level

Universal MFA
- Extend Multi-Factor Authentication to any system and service
- Apply MFA on resources like RDP, Remote Powershell, PSExec, SSH, etc.
- Protect LOTL (Living Of The Land) tools using MFA

Non-Human Identity (NHI) Security
- Discover and protect non-human identities
- Secure service accounts using Virtual Fencing policies
- Auto discover and auto protect NHI's using behavior patterns 

Identity Threat Detection & Response (ITDR)
- Detect and respond to identity attack in real time
- Prevent attacks like Brute Force attacks, Impossible Travel, Kerberoasting, AS-Rep Roasting, etc.
- Apply dynamic risk-based policies using Authentication Firewall and/or Universal MFA using ITDR detections

Identity Security Posture Management (ISPM)
- Uncover, map and analyze identity security exposures in on-prem and cloud IAM platforms
- Monitor privileged users, permissions, security roles, etc.

Privileged Access Security (PAS)
- Identify and enforce least privilege access
- Leverage Just-in-Time (JiT) access for critical assets
- Monitor and enforce Tier zeroing model and Tier zero assets

<br>


### Use in the Cyberhell Workshop

In this workshop we will use Silverfort to protect our environment from lateral movement using storel credentails of an admin account in the Active Directory domain. Levering the Tiering model, Domain Admins and Enterprise Admins should be limited to authenticating to critical Tier 0 assets - like Domain Controllers - from trusted Tier 0 hosts.
<br>
In the workshop we will use the Authentication Firewall to block attemps of Remote Powershell usage for lateral movement.

<br>


---
 
### Learn More & Get Started
 
- [Silverfort website](https://www.silverfort.com)
- [Silverfort documentation](https://docs.silverfort.com)