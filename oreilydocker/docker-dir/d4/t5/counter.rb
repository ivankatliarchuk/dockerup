require 'sinatra'
require 'redis'

# bind all network interfaces
set :bind, '0.0.0.0'

# instantiate connection to redis
configure do
  $redis = Redis.new(:host => 'redis')
end

# call function get with root path
get '/' do
  count = $redis.incr('count')

  "<h1>Hello Ivan Ka</h1>"
  "<p>This page has been viewed #{count} times!</p>"
end
