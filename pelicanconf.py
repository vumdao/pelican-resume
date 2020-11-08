#!/usr/bin/env python
# -*- coding: utf-8 -*- #

PATH = 'content'

TIMEZONE = 'Asia/Bangkok'

DEFAULT_LANG = 'en'

THEME = '/site/theme'

AUTHOR = 'Vu Dao'

SITENAME = 'My Resume'

#Profile information
NAME = 'Vu Dao'
TAGLINE = 'Senior Devops Engineer'
PIC = 'profile.png'

#sidebar links
EMAIL = 'mail@gmail.com'
PHONE = '(+84) 933333333'
LINKEDIN = 'vu-dao-9280ab43'
GITHUB = 'vumdao'

CAREER_SUMMARY = 'Deep understanding in developing and maintaining applications running on AWS Cloud Services and Virtualization (Docker, k8s, vagrant, KVM, VirtualBox). Strong experience in Automation as well as CI/CD (Gitlab/Jenkins), monitoring and site-reliability.'

SKILLS = [
	{
		'type': 'LANGUAGES',
		'list': [
			'Python, Bash Shell, Java, Ruby'
		]
	},
	{
		'type': 'FRAMEWORKS',
		'list': [
			'Aws/Chalice (Allow to quickly create and deploy applications that use AWS Lambda.)',
			'AWS Cloud Development Kit (AWS CDK)',
			'Boto3, psycopg2, slackbot, redis, kubernetes, pyinotify, lxml, kafka, flask, smtplib, threading, requests, etc.'
		]
	},
	{
		'type': 'TOOL',
		'list': [
			'Postgresql, Redis, Cassandra, pgAdmin, pgbarman, MongoDB',
			'Gitlab, Github, Gerrit, Jenkins, Ansible, Portainer, Traefic',
			'ElasticSearch, Kibana, Fluentd, Datadog, Grafana, Zabbix, Glowroot',
			'Kafka, SorlCloud, SystemD',
			'Jira, '
		]
	}
]

CLOUDS = 'EC2, EFS, EKS, ECR, IAM, KMS, Lambda, RDS, Route53, S3, SQS, SNS, SES'

EXPERIENCES = [
	{
		'job_title': 'Experience Software Developer',
		'time': 'Jul 2011 – Mar 2017',
		'company': 'DEK Technologies',
		'details': 'Develop Multi-blade service configuration and Multi-blade software management based on OpenSAF source code which provides high availability and auto-scaling. Develop and maintain CI/CD system using jenkins, write function test (Java core framework) and system test (python) for feature developmetns and main requests'	
	}
]

EDUCATIONS = [
	{
		'degree': 'Bachelor\'s degree, Telecommunications Engineering',
		'meta': 'HCMC Uniersity of Technology',
		'time': '2006 - 2011'
	}
]

PROJECTS = [
	{
		'title': 'Alarm/Alert System',
		'tagline': {
			'Develop tools with Slack Webhook Integration to monitor product services such as alarm database, alarm renewal certification, service up/down and auto-healing',
			'Monitor replication lag and blocking queries in database',
			'Ensure all Kuberbenets statefulset pods of a service not in same worker node',
			'Alarm and auto-healling core services also important customers sites',
			'Using open source brotandgames /ciao (in Ruby) to health check endpoint URL such as custom domains, API, Zappier, Marketplace, etc.',
			'Monitor scheduled events such as building reports (Business intelligence), alert and auto healing for failed services due to race conditions or system unstable.',
			'Daily scan all ports in AWS Security groups to ensure no open ports to the world except port 80 and 443'
		}
	},
	{
		'title': 'High Availability Core MiddleWare Application',
		'tagline': {
			'Develop Multi-blade service configuration and Multi-blade software management based on OpenSAF source code which provides high availability.',
			'Develop Scale out/in multiple blades feature based on a template node.',
			'Trouble shooting and resolve bugs for correction packages. Plus Schedule delivery project versions to customers. Manage product store (GASK, FTP, PIwin, X-CI, Artifactory).',
			'Analysis and implement requirements/features from customers and responsible for continuous integration and product quality.',
			'Develop and maintain test cases and framework of Function test and System test (JCAT R2/R5 framework) and responsible for CI/CD Jenkins (Eiffel). Support BlueTrain, RDA and LCT, these ones perform regression test for all components in CBA.',
			'Perform all regression tests and light component tests (LCT) for CP versions.',
			'Mentor new members and provide training courses to new comers, share new techniques/ project features.'
		}
	}
]

LANGUAGES = [
	{
		'name': 'English',
		'description': 'Professional'
	}
]

INTERESTS = [
	'Yoga',
	'Running'
]
