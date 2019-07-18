from smtplib import SMTP
from email.mime.text import MIMEText
from email.utils import formataddr

# 发件人邮箱账号
sender = '2602253843@qq.com'
# 发件人邮箱密码(当时申请smtp给的授权码)
pwd = 'hjhlbrgyvwgwebif'
# 收件人邮箱账号
to_user = '2602253843@qq.com'


def mail():
    ret = True
    try:
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr(["发件人昵称", sender])
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["收件人昵称", to_user])
        # 邮件的主题
        msg['Subject'] = "邮件主题"
        # 邮件内容

        # 发件人邮箱中的SMTP服务器
        smtp_server = SMTP('smtp.qq.com')
        smtp_server.login(sender, pwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
        smtp_server.sendmail(sender, [to_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        smtp_server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
