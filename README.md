# ETL Totesys Project -Various Artists
![Static Badge](https://img.shields.io/badge/GitHub_Actions_Status-DEPLOYED-green?logo=github)
![Static Badge](https://img.shields.io/badge/Testing_Status-PASS-green)
![Static Badge](https://img.shields.io/badge/Maintained%3F-no-red.svg)

![Static Badge](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Static Badge](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Static Badge](https://img.shields.io/badge/TERRAFORM-green?style=for-the-badge&logo=terraform&logoColor=white&labelColor=purple&color=purple)
![Static Badge](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Static Badge](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)


The project creates applications to Extract, Transform and Load data from an operational database for our client Terriffic Totes. The data is archived in a data lake, and is made available in a remodelled OLAP data warehouse hosted in AWS.

- [ETL Totesys Project -Various Artists](#etl-totesys-project--various-artists)
  - [Features](#features)
  - [Technologies](#technologies)
  - [Installation](#installation)
    - [Project requirements](#project-requirements)
    - [Python dependencies](#python-dependencies)
    - [Setup](#setup)
  - [Usage](#usage)
    - [Unit tests](#unit-tests)
    - [Pre-deployment checks](#pre-deployment-checks)
    - [Deployment](#deployment)
  - [Authors](#authors)
  - [Project status](#project-status)

## Features
- Three PEP8 compliant python applications that interact with AWS and database infrastructure and manipulate data as required (details below)
- Use of Terraform for automated provisioning and managing of AWS infrastructure
- Use of GitHub Actions for continuous integration and deployment
- Monitoring and alerting through AWS SNS and Cloudwatch
- Extensive testing and documentation of main applications and utility functions

## Technologies
The project uses a number of technologies and AWS serviuce
- **Programming:** Python, SQL, HCL
- **Database:** PostgreSQL
- **AWS Services:** [IAM](https://aws.amazon.com/iam/), [RDS](https://aws.amazon.com/rds/), [Lambda](https://aws.amazon.com/lambda/), [S3](https://aws.amazon.com/s3/), [Secrets Manager](https://aws.amazon.com/secrets-manager/), [Cloudwatch](https://aws.amazon.com/cloudwatch/), [SNS](https://aws.amazon.com/sns/)
- **IaC:** [Terraform](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- **CI/CD:** GitHub Actions
- **Project management:** GitHub Projects

<!-- ## ETL Architecture
visual
- **Extract:** Application to continually ingest new and updated data from tables in <code>totesys</code> database and store in *ingestion* S3 bucket as <code>csv</code> files

- **Transform:** Application to remodel tables into a predefined schema suitable for a OLAP data warehouse and store data in *processed* S3 bucket in <code>parquet</code> format

- **Load:** Application to load data into data warehouse at defined intervals
 -->

## Installation
The installation steps below make extensive use of the [Makefile](Makefile).
### Project requirements
- Ensure you have Python 3.9 or greater installed
- Add your AWS credentials (with relevent permissions) to GitHub Secrets using the following keys:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
 
### Python dependencies
A full list of core python dependencies for production can be found in the [requirements.txt](requirements.txt), the main python dependencies include:
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
- [pg8000](https://github.com/tlocke/pg8000)
- [pandas](https://pandas.pydata.org/docs/user_guide/index.html)
- [awswrangler](https://aws-sdk-pandas.readthedocs.io/en/stable/)

### Setup

After forking and cloning repo:

1. Setup development environment.

``` make
    make create-environemnt
```

2. Install development dependencies e.g bandit, safety, flake8 etc.

``` make
    make dev-setup
```

3. Install python libraries.
``` make
    make requirements
```

## Usage
After setup, you can run each application locally.

``` make
<!-- Execute the extract application -->
make pyrun file=src/extract.py
```

### Unit tests
After setup, you can run all tests locally.

``` make 
<!-- Execute all unit tests -->
    make unit-tests
```

### Pre-deployment checks
After setup, you can run all checks (bandit, safety, falke8 and coverage).

```make
<!-- Run all pre-deployment checks -->
    make run-checks
```

### Deployment
The project uses GitHub Actions for CI/CD and you can see more details in the [test_and_deploy.yml](test_and_deploy) file. 

**Note: The CI/CD process is set to trigger upon any push, or merge of a pull request, to the main branch.**

## Authors
- [Atif Khan](http://www.github.com/atif-hussain-khan)
- [Dave Geddes](http://www.github.com/dabruge)
- [Angus Hirst](http://www.github.com/Pandangus)
- [Louis Kelly](http://www.github.com/LouKelly)
- [Lucy Adams](http://www.github.com/tricia-mcmillan)
- [Weronika Falinska](http://www.github.com/makikooni)

## Project status
Closed on 11th August 2023.
