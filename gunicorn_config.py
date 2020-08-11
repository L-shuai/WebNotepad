# 定义同时开启的处理请求的进程数量，根据网站流量适当调整
workers = 5

# 采用gevent库，支持异步处理请求，提高吞吐量
worker_class = "gevent"

# 这里8080可以随便调整
bind = "0.0.0.0:8000"

# 超时
timeout = 30