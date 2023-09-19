import redis

red = redis.Redis(
    host = 'redis-19935.c72.eu-west-1-2.ec2.cloud.redislabs.com',
    port = 19935,
    password = 'a7OsFvbShnIlf6lLFHNuRFut7yguxAQr'
)
red.delete('var1')
print(red.get('var1'))