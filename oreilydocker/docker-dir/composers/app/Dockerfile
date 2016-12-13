FROM alpine
MAINTAINER Ivan Ka
RUN apk update && apk add ruby
# add && update certificates
RUN apk add --update ruby ruby-io-console ca-certificates && update-ca-certificates && rm -rf /var/cache/apk/*
RUN gem install sinatra --no-ri --no-rdoc
RUN gem install redis --no-ri --no-rdoc
ADD counter.rb counter.rb
EXPOSE 4567
ENTRYPOINT ["ruby","counter.rb"]
