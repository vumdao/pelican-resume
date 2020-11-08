# pelican-resume - Generate static resume web page

## Quick Run ( .*/run.sh* )
```
sed -i 's/THEME = .*'/THEME = "theme"/g'
rm -r output
pelican content/ -s pelicanconf.py -p 8000
pelican -l content -o output -s pelicanconf.py -p 8000 -r
```

### The theme uses CDN bootstrap https://getbootstrap.com/docs/4.3/getting-started/introduction/ to fix the issue of missing background when printing/generate PDF

### Awesome Font: https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css


## Building static web page

1. Run docker-compose in the EC2 instance: Create */mnt/pelican/site*, copy the theme and *pelicanconf.py* to there (Need to change permission for mount volume folder)

    ``` docker-compose up -d ```

2. Create AWS Resources Using CDK

 General:
- Create AWS target group which listen to port 8000
- Create domain point to the ALB
- Generate listen rule from the ALB
 
* Init stack
``` 
cdk init -l python
cdk deploy '*'
```

## Example
![Image of Example](https://github.com/vumdao/pelican-resume/blob/main/example.png?raw=true)
