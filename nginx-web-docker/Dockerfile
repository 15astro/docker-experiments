FROM  alpine:3.8

# packages & configure
RUN adduser -D -g 'nginx' nginx  \
    && apk add --no-cache nginx \
    && mkdir -p /www \
        /etc/nginx/conf.d \
        /etc/nginx/hosts.d \
        /etc/nginx/keys \
        /var/lib/nginx \
        /run/nginx/ \
    && chown -R nginx:nginx /var/lib/nginx /www

# external
EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
