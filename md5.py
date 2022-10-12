

import hashlib

value = input("请输入该文件的官网MD5值:")

def QuerySql():
    # 定义文件名
    txtName = r'xxx'
    # 打印文本MD5
    md5_hash = hashlib.md5()
    with open(txtName,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        print("\n文件的MD5(大写的32位)：" + (md5_hash.hexdigest()).upper())
        print("\n文件的MD5(小写的32位)：" + (md5_hash.hexdigest()).lower())
        print("\n文件的MD5(大写的16位)："+(md5_hash.hexdigest())[8:-8].upper())
        print("\n文件的MD5(小写的16位)：" + (md5_hash.hexdigest())[8:-8].lower())
        if value == md5_hash.hexdigest() or md5_hash.hexdigest()[8:-8]:
            print("和官网的md5值一致!")
        else:
            print('该文件为欺诈文件！')
QuerySql()

