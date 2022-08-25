import io
import pathlib
from adbutils import adb


d = adb.device()
d.sync.push(b"Hello Android", "/data/local/tmp/hi.txt") # 推送二进制文本
d.sync.push(io.BytesIO(b"Hello Android"), "/data/local/tmp/hi.txt") # 推送可读对象Readable object
d.sync.push("/tmp/hi.txt", "/data/local/tmp/hi.txt") # 推送本地文件
d.sync.push(pathlib.Path("/tmp/hi.txt"), "/data/local/tmp/hi.txt") # 推送本地文件

# 读取文件
for chunk in d.sync.iter_content("/data/local/tmp/hi.txt"):
    print("Chunk", chunk)

d.sync.push(b"Hello world", "/data/local/tmp/hi.txt")
output = d.sync.read_text("/data/local/tmp/hi.txt", encoding="utf-8")
# Expect output: "Hello world"
output = d.sync.read_bytes("/data/local/tmp/hi.txt")
# Expect output: b"Hello world"

# 拷贝到本地
d.sync.pull("/data/local/tmp/hi.txt", "hi.txt")

# 获取包的信息
info = d.package_info("com.example.demo")
if info:
    print(info)
	# output example:
    # {
	# "version_name": "1.2.3", "version_code": "12", "signature": "0xff132",
    # "first_install_time": datetime-object, "last_update_time": datetime-object,
    # }