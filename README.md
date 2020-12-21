![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/lxa725f5clysj5aawcxt.png)

{% github vumdao/pelican-resume %}

**Quick Run** `./run.sh`
```
sed -i 's/THEME = .*'/THEME = "theme"/g'
rm -r output
pelican content/ -s pelicanconf.py -p 8000
pelican -l content -o output -s pelicanconf.py -p 8000 -r
```

The theme uses [CDN bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/) to fix the issue of missing background when printing/generate PDF and [Awesome Font](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css)

##Building static web page
- Run docker-compose in the EC2 instance: Clone the code and run docker-compose
`docker-compose up -d`

###Create AWS Resources Using CDK
**General**
- Create AWS target group which listen to port 8000
- Create domain point to the ALB
- Generate listen rule from the ALB
- Using CDK to deploy AWS resources as cloudformation (Need to install CDK python tool and libs, [AWS CDK First Start](https://docs.aws.amazon.com/cdk/latest/guide/hello_world.html))
```
cp web_stack
cdk deploy '*'
```
[Web stack cdk code] (https://github.com/vumdao/pelican-resume/blob/master/web_stack/web_stack/web_stack_stack.py)

## Demo
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/0j37kjhdei9no3lhp1iu.png)
