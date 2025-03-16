
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!

---
## 1. Prepare the environment

### 1.1 安装nodejs
https://nodejs.org/en/download/

### 1.2 安装python
https://www.python.org/downloads/

### 1.3 安装awscli
https://docs.amazonaws.cn/en_us/cli/latest/userguide/getting-started-install.html
https://awscli.amazonaws.com/AWSCLIV2.msi
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html
```
msiexec.exe /i AWSCLIV2.msi
aws --version
aws configure
```

## 2. 安装aws cdk
```
npm install -g aws-cdk
```
=>
```
C:\Users\jerry>npm install -g aws-cdk

added 1 package in 19s
npm notice
npm notice New major version of npm available! 10.9.2 -> 11.2.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.2.0
npm notice To update run: npm install -g npm@11.2.0
npm notice
```

## 3. 创建项目
```
mdkir aws-cdk-demo
cd aws-cdk-demo
cdk init app --language python
```

---
## 确保您在项目根目录下，并且已经安装了所需依赖：
```
.venv/Scripts/activate.bat
pip install -r requirements.txt
```

## 首次部署前，需要先合成 CloudFormation 模板：
```
$ cdk synth
[WARNING] aws-cdk-lib.aws_ec2.InstanceProps#keyName is deprecated.
  - Use `keyPair` instead - https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2-readme.html#using-an-existing-ec2-key-pair
  This API will be removed in the next major release.
Resources:
  MyVPCAFB07A31:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      EnableDnsSupport: true
      InstanceTenancy: default
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/Resource
  MyVPCPublicSubnet1Subnet0C75866A:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone:
        Fn::Select:
          - 0
          - Fn::GetAZs: ""
      CidrBlock: 10.0.0.0/24
      MapPublicIpOnLaunch: true
      Tags:
        - Key: aws-cdk:subnet-name
          Value: Public
        - Key: aws-cdk:subnet-type
          Value: Public
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PublicSubnet1
      VpcId:
        Ref: MyVPCAFB07A31
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet1/Subnet
  MyVPCPublicSubnet1RouteTable538A9511:
    Type: AWS::EC2::RouteTable
    Properties:
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PublicSubnet1
      VpcId:
        Ref: MyVPCAFB07A31
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet1/RouteTable
  MyVPCPublicSubnet1RouteTableAssociation8A950D8E:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId:
        Ref: MyVPCPublicSubnet1RouteTable538A9511
      SubnetId:
        Ref: MyVPCPublicSubnet1Subnet0C75866A
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet1/RouteTableAssociation
  MyVPCPublicSubnet1DefaultRouteAF81AA9B:
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId:
        Ref: MyVPCIGW30AB6DD6
      RouteTableId:
        Ref: MyVPCPublicSubnet1RouteTable538A9511
    DependsOn:
      - MyVPCVPCGWE6F260E1
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet1/DefaultRoute
  MyVPCPublicSubnet1EIP5EB6147D:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PublicSubnet1
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet1/EIP
  MyVPCPublicSubnet1NATGateway838228A5:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId:
        Fn::GetAtt:
          - MyVPCPublicSubnet1EIP5EB6147D
          - AllocationId
      SubnetId:
        Ref: MyVPCPublicSubnet1Subnet0C75866A
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PublicSubnet1
    DependsOn:
      - MyVPCPublicSubnet1DefaultRouteAF81AA9B
      - MyVPCPublicSubnet1RouteTableAssociation8A950D8E
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet1/NATGateway
  MyVPCPublicSubnet2Subnet4DDFF14C:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone:
        Fn::Select:
          - 1
          - Fn::GetAZs: ""
      CidrBlock: 10.0.1.0/24
      MapPublicIpOnLaunch: true
      Tags:
        - Key: aws-cdk:subnet-name
          Value: Public
        - Key: aws-cdk:subnet-type
          Value: Public
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PublicSubnet2
      VpcId:
        Ref: MyVPCAFB07A31
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet2/Subnet
  MyVPCPublicSubnet2RouteTableA6A1CD3D:
    Type: AWS::EC2::RouteTable
    Properties:
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PublicSubnet2
      VpcId:
        Ref: MyVPCAFB07A31
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet2/RouteTable
  MyVPCPublicSubnet2RouteTableAssociationF22D63CA:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId:
        Ref: MyVPCPublicSubnet2RouteTableA6A1CD3D
      SubnetId:
        Ref: MyVPCPublicSubnet2Subnet4DDFF14C
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet2/RouteTableAssociation
  MyVPCPublicSubnet2DefaultRoute24460202:
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId:
        Ref: MyVPCIGW30AB6DD6
      RouteTableId:
        Ref: MyVPCPublicSubnet2RouteTableA6A1CD3D
    DependsOn:
      - MyVPCVPCGWE6F260E1
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet2/DefaultRoute
  MyVPCPublicSubnet2EIP6F364C5D:
    Type: AWS::EC2::EIP
    Properties:
      Domain: vpc
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PublicSubnet2
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet2/EIP
  MyVPCPublicSubnet2NATGateway4D6E78B8:
    Type: AWS::EC2::NatGateway
    Properties:
      AllocationId:
        Fn::GetAtt:
          - MyVPCPublicSubnet2EIP6F364C5D
          - AllocationId
      SubnetId:
        Ref: MyVPCPublicSubnet2Subnet4DDFF14C
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PublicSubnet2
    DependsOn:
      - MyVPCPublicSubnet2DefaultRoute24460202
      - MyVPCPublicSubnet2RouteTableAssociationF22D63CA
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PublicSubnet2/NATGateway
  MyVPCPrivateSubnet1Subnet641543F4:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone:
        Fn::Select:
          - 0
          - Fn::GetAZs: ""
      CidrBlock: 10.0.2.0/24
      MapPublicIpOnLaunch: false
      Tags:
        - Key: aws-cdk:subnet-name
          Value: Private
        - Key: aws-cdk:subnet-type
          Value: Private
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PrivateSubnet1
      VpcId:
        Ref: MyVPCAFB07A31
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PrivateSubnet1/Subnet
  MyVPCPrivateSubnet1RouteTable133BD901:
    Type: AWS::EC2::RouteTable
    Properties:
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PrivateSubnet1
      VpcId:
        Ref: MyVPCAFB07A31
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PrivateSubnet1/RouteTable
  MyVPCPrivateSubnet1RouteTableAssociation85DFBFBB:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId:
        Ref: MyVPCPrivateSubnet1RouteTable133BD901
      SubnetId:
        Ref: MyVPCPrivateSubnet1Subnet641543F4
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PrivateSubnet1/RouteTableAssociation
  MyVPCPrivateSubnet1DefaultRouteA8EE6636:
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId:
        Ref: MyVPCPublicSubnet1NATGateway838228A5
      RouteTableId:
        Ref: MyVPCPrivateSubnet1RouteTable133BD901
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PrivateSubnet1/DefaultRoute
  MyVPCPrivateSubnet2SubnetA420D3F0:
    Type: AWS::EC2::Subnet
    Properties:
      AvailabilityZone:
        Fn::Select:
          - 1
          - Fn::GetAZs: ""
      CidrBlock: 10.0.3.0/24
      MapPublicIpOnLaunch: false
      Tags:
        - Key: aws-cdk:subnet-name
          Value: Private
        - Key: aws-cdk:subnet-type
          Value: Private
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PrivateSubnet2
      VpcId:
        Ref: MyVPCAFB07A31
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PrivateSubnet2/Subnet
  MyVPCPrivateSubnet2RouteTableDF3CB76C:
    Type: AWS::EC2::RouteTable
    Properties:
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC/PrivateSubnet2
      VpcId:
        Ref: MyVPCAFB07A31
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PrivateSubnet2/RouteTable
  MyVPCPrivateSubnet2RouteTableAssociationC373B6FE:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
      RouteTableId:
        Ref: MyVPCPrivateSubnet2RouteTableDF3CB76C
      SubnetId:
        Ref: MyVPCPrivateSubnet2SubnetA420D3F0
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PrivateSubnet2/RouteTableAssociation
  MyVPCPrivateSubnet2DefaultRoute37F90B5D:
    Type: AWS::EC2::Route
    Properties:
      DestinationCidrBlock: 0.0.0.0/0
      NatGatewayId:
        Ref: MyVPCPublicSubnet2NATGateway4D6E78B8
      RouteTableId:
        Ref: MyVPCPrivateSubnet2RouteTableDF3CB76C
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/PrivateSubnet2/DefaultRoute
  MyVPCIGW30AB6DD6:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyVPC
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/IGW
  MyVPCVPCGWE6F260E1:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      InternetGatewayId:
        Ref: MyVPCIGW30AB6DD6
      VpcId:
        Ref: MyVPCAFB07A31
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/VPCGW
  MyVPCRestrictDefaultSecurityGroupCustomResourceC3FF5EE0:
    Type: Custom::VpcRestrictDefaultSG
    Properties:
      ServiceToken:
        Fn::GetAtt:
          - CustomVpcRestrictDefaultSGCustomResourceProviderHandlerDC833E5E
          - Arn
      DefaultSecurityGroupId:
        Fn::GetAtt:
          - MyVPCAFB07A31
          - DefaultSecurityGroup
      Account:
        Ref: AWS::AccountId
    UpdateReplacePolicy: Delete
    DeletionPolicy: Delete
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyVPC/RestrictDefaultSecurityGroupCustomResource/Default      
  CustomVpcRestrictDefaultSGCustomResourceProviderRole26592FE0:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Action: sts:AssumeRole
            Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
      ManagedPolicyArns:
        - Fn::Sub: arn:${AWS::Partition}:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole 
      Policies:
        - PolicyName: Inline
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - ec2:AuthorizeSecurityGroupIngress
                  - ec2:AuthorizeSecurityGroupEgress
                  - ec2:RevokeSecurityGroupIngress
                  - ec2:RevokeSecurityGroupEgress
                Resource:
                  - Fn::Join:
                      - ""
                      - - "arn:"
                        - Ref: AWS::Partition
                        - ":ec2:"
                        - Ref: AWS::Region
                        - ":"
                        - Ref: AWS::AccountId
                        - :security-group/
                        - Fn::GetAtt:
                            - MyVPCAFB07A31
                            - DefaultSecurityGroup
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/Custom::VpcRestrictDefaultSGCustomResourceProvider/Role       
  CustomVpcRestrictDefaultSGCustomResourceProviderHandlerDC833E5E:
    Type: AWS::Lambda::Function
    Properties:
      Code:
        S3Bucket:
          Fn::Sub: cdk-hnb659fds-assets-${AWS::AccountId}-${AWS::Region}
        S3Key: 7fa1e366ee8a9ded01fc355f704cff92bfd179574e6f9cfee800a3541df1b200.zip
      Timeout: 900
      MemorySize: 128
      Handler: __entrypoint__.handler
      Role:
        Fn::GetAtt:
          - CustomVpcRestrictDefaultSGCustomResourceProviderRole26592FE0
          - Arn
      Runtime: nodejs20.x
      Description: Lambda function for removing all inbound/outbound rules from the VPC default security group
    DependsOn:
      - CustomVpcRestrictDefaultSGCustomResourceProviderRole26592FE0
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/Custom::VpcRestrictDefaultSGCustomResourceProvider/Handler    
      aws:asset:path: asset.7fa1e366ee8a9ded01fc355f704cff92bfd179574e6f9cfee800a3541df1b200      
      aws:asset:property: Code
  SecurityGroupDD263621:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow SSH (TCP port 22) in
      SecurityGroupEgress:
        - CidrIp: 0.0.0.0/0
          Description: Allow all outbound traffic by default
          IpProtocol: "-1"
      SecurityGroupIngress:
        - CidrIp: 0.0.0.0/0
          Description: Allow SSH Access
          FromPort: 22
          IpProtocol: tcp
          ToPort: 22
      VpcId:
        Ref: MyVPCAFB07A31
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/SecurityGroup/Resource
  MyEC2InstanceInstanceRole1A6C2310:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Action: sts:AssumeRole
            Effect: Allow
            Principal:
              Service: ec2.amazonaws.com
        Version: "2012-10-17"
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyEC2Instance
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyEC2Instance/InstanceRole/Resource
  MyEC2InstanceInstanceProfile9377ECBE:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Roles:
        - Ref: MyEC2InstanceInstanceRole1A6C2310
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyEC2Instance/InstanceProfile
  MyEC2InstanceB097982C:
    Type: AWS::EC2::Instance
    Properties:
      AvailabilityZone:
        Fn::Select:
          - 0
          - Fn::GetAZs: ""
      IamInstanceProfile:
        Ref: MyEC2InstanceInstanceProfile9377ECBE
      ImageId:
        Ref: SsmParameterValueawsserviceamiamazonlinuxlatestamzn2amihvmx8664gp2C96584B6F00A464EAD1953AFF4B05118Parameter
      InstanceType: t2.micro
      KeyName: your-key-pair-name
      SecurityGroupIds:
        - Fn::GetAtt:
            - SecurityGroupDD263621
            - GroupId
      SubnetId:
        Ref: MyVPCPublicSubnet1Subnet0C75866A
      Tags:
        - Key: Name
          Value: AwsCdkDemoStack/MyEC2Instance
      UserData:
        Fn::Base64: "#!/bin/bash"
    DependsOn:
      - MyEC2InstanceInstanceRole1A6C2310
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/MyEC2Instance/Resource
  CDKMetadata:
    Type: AWS::CDK::Metadata
    Properties:
      Analytics: v2:deflate64:H4sIAAAAAAAA/81Vy27bMBD8lvAY0GqdAkHhm2IUgYA2FuwghxpGsabW9tbUUuXDriro3ws9HDnp49IefOJqtDMcLpfkTTR+P47GV3B0I5XtR5rWUbXwoPYSju5Lheomqp4KtaxEDt/jH05MxLWQwoU1o58a3tA2WPBkWEyWlWDI8UXKY1k0QBrWmpSQQlFmP4Hbt0m1/AvD0gE8/kJZ1Ss53fBTOpWd6KJlLSsBByANa9Lky8+GT6qHQiVZHzdSd9qoff+dQ9GJJMWMP0JgtRMTbwNKQcXhdvoqHZyjLSfF4TbOMovOzXhqsV99v56LcNEaybIH8Pfg8QilmCzFtVhdjMHLcPHHMrUt1jVWE81N8PgIa40DPmCxc0ZRK/yc3AQfkrQZBnXZ9/R/79gNaHcBe/FvNi7HyYXY6LowYY+W8bmHuruv/4q9B7XLkb1coAqWfHlvTSiWVWP2NJXW5hhrPQt+bQJnp0OToVOWipcrz7KEt42fedDYXukKOGFNjB3ScZVhRtVQTy9CYPoWsK9Pu50tPJymc38yYeeBFS4rQX3Y3/tdMdWOGJMctme176M9lg9nb8a57JDbHTEnJtVv36H6VNtu6loS5FE1N7oxBM6FHLO7smEXllhRATpWygT2w/aFHBtCrIYCdqoNeq6eWrMhjXUt5+hMsArbS0ZOg/Mmf4Vt+AS8+p9ac6AM7R04lLFz6BcetsTbhpOChRw92lqmpd8ZfvMuGr+Nbq++OqKRDewpx2jejT8B9b4Ru/QHAAA=
    Metadata:
      aws:cdk:path: AwsCdkDemoStack/CDKMetadata/Default
    Condition: CDKMetadataAvailable
Parameters:
  SsmParameterValueawsserviceamiamazonlinuxlatestamzn2amihvmx8664gp2C96584B6F00A464EAD1953AFF4B05118Parameter:
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
  BootstrapVersion:
    Type: AWS::SSM::Parameter::Value<String>
    Default: /cdk-bootstrap/hnb659fds/version
    Description: Version of the CDK Bootstrap resources in this environment, automatically retrieved from SSM Parameter Store. [cdk:skip]
Conditions:
  CDKMetadataAvailable:
    Fn::Or:
      - Fn::Or:
          - Fn::Equals:
              - Ref: AWS::Region
              - af-south-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-east-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-northeast-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-northeast-2
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-northeast-3
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-south-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-south-2
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-southeast-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-southeast-2
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-southeast-3
      - Fn::Or:
          - Fn::Equals:
              - Ref: AWS::Region
              - ap-southeast-4
          - Fn::Equals:
              - Ref: AWS::Region
              - ca-central-1
          - Fn::Equals:
              - Ref: AWS::Region
              - ca-west-1
          - Fn::Equals:
              - Ref: AWS::Region
              - cn-north-1
          - Fn::Equals:
              - Ref: AWS::Region
              - cn-northwest-1
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-central-1
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-central-2
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-north-1
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-south-1
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-south-2
      - Fn::Or:
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-west-1
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-west-2
          - Fn::Equals:
              - Ref: AWS::Region
              - eu-west-3
          - Fn::Equals:
              - Ref: AWS::Region
              - il-central-1
          - Fn::Equals:
              - Ref: AWS::Region
              - me-central-1
          - Fn::Equals:
              - Ref: AWS::Region
              - me-south-1
          - Fn::Equals:
              - Ref: AWS::Region
              - sa-east-1
          - Fn::Equals:
              - Ref: AWS::Region
              - us-east-1
          - Fn::Equals:
              - Ref: AWS::Region
              - us-east-2
          - Fn::Equals:
              - Ref: AWS::Region
              - us-west-1
      - Fn::Equals:
          - Ref: AWS::Region
          - us-west-2


NOTICES         (What's this? https://github.com/aws/aws-cdk/wiki/CLI-Notices)

32775   (cli): CLI versions and CDK library versions have diverged

        Overview: Starting in CDK 2.179.0, CLI versions will no longer be in
                  lockstep with CDK library versions. CLI versions will now be
                  released as 2.1000.0 and continue with 2.1001.0, etc.

        Affected versions: cli: >=2.0.0 <=2.1005.0

        More information at: https://github.com/aws/aws-cdk/issues/32775


If you don’t want to see a notice anymore, use "cdk acknowledge <id>". For example, "cdk acknowledge 32775".
```

## 如果这是您第一次在这个 AWS 账户和区域中使用 CDK，需要先进行引导：
```
cdk bootstrap
```

## 部署堆栈
```
cdk deploy
```
系统会显示将要进行的更改，并询问您是否确认部署。输入 'y' 确认部署。
```
cdk deploy --debug    # 显示详细的调试信息
```

## 部署完成后，如果要查看堆栈状态：
```
cdk ls
```

## 如果需要删除资源
```
cdk destroy
```

注意事项：
在运行 cdk deploy 之前，请确保已经将代码中的 your-key-pair-name 替换为您实际的 EC2 密钥对名称
部署可能需要几分钟时间
部署完成后，您可以在 AWS Console 中查看创建的资源
记得在不使用时销毁资源以避免不必要的费用