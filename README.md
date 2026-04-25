# Lucidity-Disk-Monitoring-Solution-for-Cloud-Environments
Scalable-AWS-Disk-Monitoring-Solution

##Background

A large Enterprise is operating mulitple AWS accounts containing EC2 workloads. A scalable solution is required to proactively detect the disk space issues before they impact availability. currently, organization uses Ansible and wants to leverage the existing stack with cloud-native services where they add operational value. 

#Proposed Solution

Hybrid Architecture using:

- Ansible
- AWS Systems Manager
- CloudWatch Agent
- Amazon CloudWatch Dashboard
- CloudWatch Alarms 
- Amazon SNS 
- AWS EventBridge and Lambda
- AWS Organization + IAM Roles

#High-level Architecture

1. EC2 Instances across multiple AWS Accounts
2. CloudWatch Agent installed using Ansible
3. Metrics sent to Central Monitoring Account
4. CloudWatch Dashboard with Alarms
5. SNS Email Alerts

- For new EC2 Launch Events:
1. AWS EventBridge
2. AWS Lambda
3. Auto-tag and Auto-enroll into Ansible inventory

#Key Components

1. Access Management
- Use AWS Organizations with IAM roles in each member account.
- Central monitoring account assumes read-only/management roles using STS.

2. VM Discovery
- Ansible Dynamic Inventory plugin discovers EC2 instances using tags and regions.

3. Metrics Collection

CloudWatch Agent collects:

- disk_used_percent
- free space
- inode utilization
- mount path

4. Aggregation
- Metrics Centralized into CloudWatch Dashboards.

5. Alerting
- CloudWatch Alarm when disk usage is greater than 80% and SNS sends a message.

6. Auto-Onboarding
- New EC2 launches trigger Eventbridge, Lambda, tagging, onboarding workflow

7. Scalability
- supports growth in AWS accounts, regions, EC2 Instances, teams/environments
- No redesign required

#Repository Structure
Lucidity-Disk-Monitoring-Solution-for-Cloud-Environments/
│── README.md
│── ansible/
│   ├── inventory_aws_ec2.yml
│   ├── playbook-install-cloudwatch-agent.yml
│   ├── cloudwatch-config.json
│   └── ansible.cfg
│── lambda/
│   └── auto_onboard.py
│── iam/
│   └── cross-account-role-policy.json
│── docs/
│   └── key-design-decisions.md
