import os


def upload_to_appstore(path, name, pwd, altool_path):
    print('----- 验证App----->')
    # s = '%s ' '--validate-app -f %s '  '-u %s '  '-p %s '  '-t ios --output-format xml' % (altool_path, path, name, pwd)
    s = altool_path + " --validate-app -f " + path + " -u " + name + " -p " + pwd + " " + "--output-format xml"
    v = os.system(s)
    print('----------> ', v)
    if v == 0:
        print('----- 上传App----->')
        ss = '%s ' \
             '--upload-app -f %s  ' \
             '-u %s ' \
             '-p %s ' \
             '-t ios --output-format xml' % (altool_path, path, name, pwd)

        u = os.system(ss)
        if u == 0:
            print('----- 上传App 成功----->')
            pass
        else:
            raise Exception("上传 App Store 失败 !")
    else:
        raise Exception("验证 App 失败 !")


# meiyezhangmen@163.com
# Meiyezhangmen0987

upload_to_appstore("/Users/wenzheng/Desktop/RLW/yingyun_mall/YingYunStore/archive", "snake.s.smile@foxmail.com",
                   "xsyu-kifd-zbdw-jpkq",
                   "/Applications/Xcode.app/Contents/Applications/Application\ Loader.app/Contents/Frameworks/ITunesSoftwareService.framework/Versions/A/Support/altool")
