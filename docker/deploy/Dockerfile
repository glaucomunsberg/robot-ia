FROM python:latest AS build

RUN pip install --root-user-action=ignore mkdocs-material

RUN pip install --root-user-action=ignore "mkdocs-material[imaging]"

RUN mkdir /app

WORKDIR /app

COPY mkdocs ./

RUN printf 'report' | mkdocs build -f ./mkdocs.yml -v

FROM nginx:1.23.4-alpine
COPY docker/deploy/nginx.conf /etc/nginx/conf.d/configfile.template
COPY docker/deploy/.htpasswd /etc/nginx/.htpasswd

COPY --from=build /app/site /usr/share/nginx/html

ENV PORT 8080
ENV HOST 0.0.0.0
EXPOSE 8080
CMD sh -c "envsubst '\$PORT' < /etc/nginx/conf.d/configfile.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"