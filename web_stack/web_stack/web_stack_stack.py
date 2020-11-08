import os.path
import re
from aws_cdk import (
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elbv2,
    aws_route53 as _route53,
    aws_iam as iam,
    core
)


class RunAllAtOnce:
    def __init__(self):
        instance_id = 'i-0a18e712e3529e433'
        alb_stack = AlbSingleEnvStack(app, "ALB", env=env_us, instance_id=instance_id)

        alb_stack.alb_listener_443()
        alb_stack.add_listener_80()
        alb_stack.pelican_8000()


class AlbSingleEnvStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, env, instance_id) -> None:
        super().__init__(scope, id, env=env)
        self.instance_id = instance_id

        # pelican.com ACM cert
        self.sel_cert_arn = "arn:aws:acm:us-east-2:111111111111:certificate/b8299bf5-ae3b-4f69-a696-f1d839428f5f"

        self.vpc = ec2.Vpc.from_vpc_attributes(
            self, "VPC", vpc_id='vpc-44a44b44',
            availability_zones=['us-east-2a', 'us-east-2c'],
            public_subnet_ids=['subnet-bbbbbbbb', 'subnet-cccccccc'])

        self.target = elbv2.InstanceTarget(instance_id=instance_id)

        self.lb = elbv2.CfnLoadBalancer(
            scope=self,
            id='LB',
            ip_address_type='ipv4',
            name='pelican-alb',
            security_groups=['sg-13a02c7a', 'sg-12a02c7b', 'sg-3bb23e52', 'sg-14a02c7d'],
            type='application',
            scheme='internet-facing',
            subnets=['subnet-bbbbbbbb', 'subnet-cccccccc'],
            tags=[core.CfnTag(key='env', value='dev')],
            load_balancer_attributes=[elbv2.CfnLoadBalancer.LoadBalancerAttributeProperty(
                key='idle_timeout.timeout_seconds',
                value='180'
            )]
        )

        core.Tag.add(self.lb, key='cfn.single-env.stack', value='alb-stack')

        self.alb_dns = self.lb.attr_dns_name

        self.listener_443 = None

    def alb_listener_443(self):
        """ ALB port 443 """
        app_target_group = elbv2.CfnTargetGroup(
            self,
            "AppTG",
            name='pelican-tg',
            health_check_path="/health-check.do",
            health_check_protocol='HTTP',
            port=9000,
            protocol="HTTP",
            target_type="instance",
            vpc_id='vpc-44a44b44',
            targets=[{'id': self.instance_id, 'port': 9000}]
        )
        self.listener_443 = elbv2.CfnListener(
            scope=self,
            id='Listener443',
            default_actions=[
                elbv2.CfnListener.ActionProperty(
                    target_group_arn=app_target_group.ref,
                    type="forward"
                )
            ],
            certificates=[elbv2.CfnListener.CertificateProperty(certificate_arn=self.sel_cert_arn)],
            load_balancer_arn=self.lb.ref,
            port=443,
            protocol="HTTPS"
        )

    def add_listener_80(self):
        elbv2.CfnListener(
            scope=self,
            id='Listener80',
            default_actions=[
                elbv2.CfnListener.ActionProperty(
                    type='redirect',
                    redirect_config=elbv2.CfnListener.RedirectConfigProperty(
                        status_code='HTTP_301',
                        host='#{host}',
                        path='/#{path}',
                        query='#{query}',
                        port='443',
                        protocol='HTTPS'
                    )
                )
            ],
            load_balancer_arn=self.lb.ref,
            port=80,
            protocol="HTTP"
        )

    def pelican_8000(self):
        """ pelican 8000 """
        pelican_target_group = elbv2.CfnTargetGroup(
            self,
            "PelicanTG",
            name='tg-pelican',
            health_check_path="/",
            port=8000,
            protocol="HTTP",
            target_type="instance",
            vpc_id='vpc-44a44b44',
            targets=[{'id': self.instance_id, 'port': 8000}]
        )
        elbv2.CfnListenerRule(
            scope=self,
            id='PelicanListenerRule',
            actions=[
                elbv2.CfnListenerRule.ActionProperty(
                    type='forward',
                    target_group_arn=pelican_target_group.ref
                )
            ],
            conditions=[
                {
                    "field": "host-header",
                    "hostHeaderConfig": {
                        "values": [
                            'resume.pelican.com'
                        ]
                    }
                }
            ],
            listener_arn=self.listener_443.ref,
            priority=9
        )


class Route53SingleEnvStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, env, alb_dns, **kwargs) -> None:
        super().__init__(scope, id, env=env, **kwargs)

        hosted_zone = 'Z1111111111Z'

        hz = _route53.HostedZone.from_hosted_zone_attributes(
            self, id="HostedZone", hosted_zone_id=hosted_zone, zone_name='pelican.com')

        record = 'resume.pelican.com'
        _route53.CnameRecord(
            self, 'Cname',
            domain_name=alb_dns,
            record_name=record,
            zone=hz,
            ttl=core.Duration.minutes(1)
        )
