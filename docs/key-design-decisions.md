#why this architecture?

Balances current tooling (Ansible) with AWS-native operational excellence.

#why AWS systems manager (SSM) instead of SSH?

- No open port 22 required
- No SSH key management and rotation burden across hundreds of instances
- Auditable secure sessions
- Works across VPCs, Private Subnets, and accounts via SSM endpoints

#Why CloudWatch

- Native AWS service, no extra infrastructure
- Cross-account metric sharing via CloudWatch Observability (same AWS Org)
- Built-in dashboards, alarms, and SNS notifications
- Retention up to 15 months for trend analysis
- cost-effective at scale

#Why EventBridge and Lambda

Automatically detects new EC2 instances and reduces manual onboarding work.




