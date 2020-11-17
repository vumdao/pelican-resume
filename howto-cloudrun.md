Steps:


### Generate Build output

docker run -v $PWD:/site vorakl/alpine-pelican pelican /site/content -o /site/output -s /site/pelicanconf.py


### Create Dockerfile with following content


```
# nginx state for serving content
FROM nginx:alpine
# Set working directory to nginx asset directory
WORKDIR /usr/share/nginx/html
# Remove default nginx static assets
RUN rm -rf ./*
COPY output .
# Containers run nginx with global directives and daemon off
EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]

```

### Using cloud build

vim cloudbuild.yaml

```

steps:
- name: 'gcr.io/cloud-builders/docker'
  args: [ 'build', '-t', 'gcr.io/$PROJECT_ID/myresume', '.' ]
- name: 'gcr.io/cloud-builders/docker'
  args: ['push', 'gcr.io/$PROJECT_ID/myresume']
- name: 'gcr.io/cloud-builders/gcloud'
  args:
  - 'run'
  - 'deploy'
  - 'cloudrunservice'
  - '--image'
  - 'gcr.io/$PROJECT_ID/myresume'
  - '--region'
  - 'asia-southeast1'
  - '--platform'
  - 'managed'
  - '--allow-unauthenticated'  
images:
- 'gcr.io/$PROJECT_ID/myresume'


```

### Build and Deploy

`gcloud builds submit --config cloudbuild.yaml`
