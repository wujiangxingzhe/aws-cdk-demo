from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class AwsCdkDemoStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 创建 VPC
        vpc = ec2.Vpc(self, "MyVPC",
            max_azs=2,  # 使用2个可用区
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                )
            ]
        )

        # 创建安全组
        security_group = ec2.SecurityGroup(self, "SecurityGroup",
            vpc=vpc,
            description="Allow SSH (TCP port 22) in",
            allow_all_outbound=True
        )

        # 添加入站规则 - 允许 SSH 访问
        security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH Access"
        )

        # 创建 EC2 实例
        ec2_instance = ec2.Instance(self, "MyEC2Instance",
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            security_group=security_group,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T2,
                ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            key_name="xiaozhuang-saa"  # 替换为您的密钥对名称
        )