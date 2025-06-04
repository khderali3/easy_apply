import redis

try:
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    pong = r.ping()
    if pong:
        print("✅ Redis connection successful (PONG)")
    else:
        print("❌ Redis connection failed")
except Exception as e:
    print("❌ Error connecting to Redis:", str(e))