# Infrastructure as Code (Iac)  
**aws cli**  

### Ajánlot videólista  
- [AWS CLI for Beginners: The Complete Guide](https://www.youtube.com/watch?v=PWAnY-w1SGQ)  

### Linkek, források  
- [Infrastructure as code - Wikipedia](https://en.wikipedia.org/wiki/Infrastructure_as_code)
- [AWS Command Line Interface](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-welcome.html)  
    - install: [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html)  
        - [YUM install, nem támogatott](https://iqcode.com/code/shell/install-aws-cli-2-yum)  
    - configure: [Quick configuration with aws configure](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-quickstart.html) 
    - using: [Using the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-using.html)  


## Mi az az Iac?  
*Infrastructure as Code*

- kódbázis ami infrastruktúrát alakít ki
- a probléma 2 féle megközelítése. "Declarative vs. imperative approaches to IaC"  
- Deklaratív(functional): a kívánt állapot leírása (pl. Ansible Desired State Configuration, Powershell Desired State Configuration (DSC))  
    - "A declarative approach defines the desired state of the system, including what resources you need and any properties they should have, and an IaC tool will configure it for you."  
    - "A declarative approach also keeps a list of the current state of your system objects, which makes taking down the infrastructure simpler to manage."  
- Imperatív(procedural)
    - "An imperative approach instead defines the specific commands needed to achieve the desired configuration, and those commands then need to be executed in the correct order. "

Sok IaC-eszköz deklaratív megközelítést használ, és automatikusan biztosítja a kívánt infrastruktúrát.  
Ha módosul a kívánt állapot (DSC), valamilyen eszköz(tool Ansible, Kubernetes) ezeket a változtatásokat alkamazza, ellenőrzi a rendszeren.  
Egy imperatív eszköz manuális bevatkozást igényel, viszont sokkal rugalmasabb eszköz, egyedi megoldásokra jobban alkalmas.   
Az IaC-eszközök gyakran mindkét megközelítésben működnek, de általában az egyik megközelítést részesítik előnyben a másikkal szemben.   

![cicd](./pics/cicd1.png "DevOps")

### IaC előnyei  
Az infrastruktúra kiépítése történelmileg időigényes és költséges manuális folyamat volt. Mostanra az infrastruktúra-kezelés egyre jobban eltávolodik az adatközpontok fizikai hardverétől. Ugyanakkor az on-premise és a felhős infrastruktúra kezelése központosítható ezekkel az eszközökkel.  
A felhővel megnőtt az infrastruktúra-összetevők száma, naponta több alkalmazás kerül dev, test, stage, production környezetbe, és az infrastruktúrát gyakran fel kell skálázni a jobb kihasználtság miatt.  
Bár a legtöbb feladat megoldható grafikus felületről, az IaC "tömbösíthető", automatizálható feladatok esetént megkerülhetetlen.

- Költségcsökkentés    
- Gyorsabb deploy  
- Kevesebb hiba  
- Konzisztensebb infrastruktúra (pl névkonvenciók)  
- Azonos konfigurációk  
- **CI/CD - continuous integration/continuous delivery**  

Néhány egyszerű scripttel mindig a megfelelő infrastruktúrát tudjuk előállítani az alkalmazásainknak  
Így az alkalmazástelepítések nem várakoznak az infrastruktúrára, és a rendszergazdák nem kezelik az időigényes manuális folyamatokat.
A CI/CD a folyamatos automatizáláson és folyamatos felügyeleten alapul az alkalmazás teljes életciklusa során, az integrációtól és teszteléstől a szállításig és telepítésig.
Ahhoz, hogy egy környezet automatizálható legyen, konzisztensnek kell lennie. Az alkalmazástelepítések automatizálása nem működik, ha a fejlesztőcsapat egyféleképpen telepíti az alkalmazásokat vagy konfigurálja a környezeteket, az üzemeltetési csoportok pedig más módon telepítik és konfigurálják.  
A fejlesztői és üzemeltetési csapatok DevOps-megközelítésen keresztüli összehangolása kevesebb hibát, manuális telepítést és következetlenséget eredményez.  
Az IaC minden használatkor ugyanazt a környezetet hozza létre.  
A DevOps bevált gyakorlatait az IaC infrastruktúrájára is alkalmazzák. Az infrastruktúra ugyanazon a CI/CD folyamaton mehet keresztül, mint egy alkalmazás a szoftverfejlesztés során, ugyanazt a tesztelést és verzióvezérlést alkalmazva az infrastruktúra kódjára.  

Ismertebb eszközök: 
- Red Hat Ansible Automation Platform  
- [Terraform](https://www.terraform.io/)  
- Saltstack
- AWS CloudFormation
---  
### aws-cli

* Install
* Credentials
* Configure parancs: ```aws configure```
    - Access key-t kell készíteni. Vigyázz csak egyszer adja vissza a secretet.
    - keyid, accesskey, region, output (json, yaml) 
    - létrejövő fájlok, windows esetén: ``` $env:USERPROFILE\.aws ```, linux esetén ```~/.aws```
    - profile (lehet több is ) [profile nameofprofile], credentials [nameofprofile]
    - akár környezeti változóként is használható [Environment variables to configure the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-envvars.html)  
    ```
    config:
    [default]
    region = eu-west-2
    output = json

    [profile secondprofile]
    region = eu-west-1
    output = json
    
    credentials:
    [default]
    aws_access_key_id = AKIA3Z6OFD6BLDID2W6V
    aws_secret_access_key = sS***************************************k

    [secondprofile]
    aws_access_key_id = AKIA3Z6OFD6BLDID2W6V
    aws_secret_access_key = sS***************************************k

    használat paraméterként, különben default
    --profile secondprofile
    ```     
* Command syntax:  aws [command] [subcommand] [parameters]  
    - van TAB-ra completer, külön telepíteni kell én kihagytam  
    ```
    példák:  
    aws ec2 describe-key-pairs  
    aws ec2 describe-key-pairs --profile secondprofile  
    ```
* Skeletons and input files [AWS CLI skeletons and input files](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-skeleton.html)  


### EC2

[ec2 aws dokumentáció](https://docs.aws.amazon.com/cli/latest/reference/ec2/)

1. create key pair  
[create-key-pair](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-key-pair.html)  

``` 
aws ec2 create-key-pair --key-name test2key --query 'KeyMaterial' --output text > test2key.pem  

aws ec2 create-key-pair --key-name demokey1 --key-format 'ppk' --output text > demokey1.ppk  

aws ec2 describe-key-pairs  
aws ec2 delete-key-pair --key-name test1  
```

2. AMI  ami id pl.: ami-0cff7528ff583bf9a  -régióként változik az ami ID

```
aws ec2 run-instances --image-id ami-078a289ddf4b09ae0 --count 1 --instance-type t2.micro --key-name demokey1

aws ec2 run-instances --generate-cli-skeleton > ec2.json 

aws ec2 run-instances --cli-input-json file://ec2demo.json

{    
    "ImageId": "ami-078a289ddf4b09ae0",
    "KeyName": "demokey1",
    
    "InstanceType": "t2.micro",
    "Monitoring": {
        "Enabled": true
    }
}

aws ec2 stop-instances --instance-ids i-061843cc22fda92e3
aws ec2 stop-instances --instance-ids i-061843cc22fda92e3

aws ec2 terminate-instances --instance-ids 	i-061843cc22fda92e3 i-032090fc299f9275e
aws ec2 terminate-instances --instance-ids 	i-032090fc299f9275e

```
[15 aws cli examples](https://www.thegeekstuff.com/2016/04/aws-ec2-cli-examples/)  



### IAM

*Csoport kezelés, user kezelés*  
[IAM cli](https://docs.aws.amazon.com/cli/latest/reference/iam/index.html)  

```
aws iam create-group --group-name DevOps1Users  
aws iam list-groups  
aws iam list-groups-for-user --user-name DOUser1  

aws iam create-user --user-name DOUser1  
aws iam add-user-to-group --user-name DOUser1 --group-name DevOps1Users  
```

[Jelszó userhez](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/create-login-profile.html)  
```  
aws iam create-login-profile --generate-cli-skeleton > create-login-profile.json    
aws iam create-login-profile --cli-input-json file://create-login-profile.json  

aws iam add-user-to-group --user-name DOUser1 --group-name DevOps1Users  
```  


### VPC
[Create an IPv4-enabled VPC and subnets using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-subnets-commands-example.html)  
- Subnet  
- a kettő együtt  

  


### aws cli in python  

- [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/)  
- [boto3](https://pypi.org/project/boto3/)  
- [Python Code Samples for Amazon EC2](https://docs.aws.amazon.com/code-samples/latest/catalog/code-catalog-python-example_code-ec2.html)  
