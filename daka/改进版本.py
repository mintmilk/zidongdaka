from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

def webclick():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        ua='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
        chrome_options.add_argument('user-agent=' + ua)
        d = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)
        d.implicitly_wait(30)
        d.set_window_size(1280,1080)
        d.get("https://ehall.yzu.edu.cn/infoplus/form/XNYQSB/start")
        d.find_element_by_id("username").click()
        d.find_element_by_id("username").clear()
        d.find_element_by_id("username").send_keys("MZ120201331")
        d.find_element_by_id("password").clear()
        d.find_element_by_id("password").send_keys("@WA3es4rd")
        d.find_element_by_xpath("/html/body/div/div[2]/div/div/div[2]/div/div/div/div[2]/form[1]/div[5]/input").click()
        print('账号登入')
        d.find_element_by_id("preview_start_button").click()
        print('开始办理')
        try:
            d.find_element_by_id("V1_CTRL8").click()
            d.find_element_by_id("V1_CTRL8").clear()
            d.find_element_by_id("V1_CTRL8").send_keys(u"动研2020")
            print('输入班级完成')
            d.find_element_by_id("fieldSFZX-0").click()  # 在校
            print('在校选项点击完成')
            d.find_element_by_id("V1_CTRL121").click()
            d.find_element_by_id("V1_CTRL121").clear()
            d.find_element_by_id("V1_CTRL121").send_keys(u"无")
            print('出行记录填写完毕')
            d.find_element_by_xpath("//*[@id=\"V1_CTRL115\"]").click()
            print('特别提醒勾选')
            d.find_element_by_xpath("//*[@id=\"V1_CTRL109\"]").click()
            print('上午体温')
            d.find_element_by_xpath("//*[@id=\"V1_CTRL111\"]").click()
            print('下午体温')
            d.find_element_by_xpath("//*[@id=\"V1_CTRL114\"]").click()
            print('无相关症状')
            d.find_element_by_xpath("//*[@id=\"V1_CTRL82\"]").click()
            print('承诺可靠')
            d.find_element_by_xpath("/html/body/div[4]/form/div/div[1]/div[2]/ul/li[1]/a").click()
            print('确认填报')
            time.sleep(1)
            d.find_element_by_xpath("/html/body/div[7]/div/div[2]/button").click()
            print('确定弹框完成')
            d.quit()
            res="帮你打过健康打卡了，wink~"
            send_email(res)
        except:
            d.find_element_by_xpath("/html/body/div[6]/div/div[2]/button").click()
            d.quit()
            res="打卡已经有人帮你打过啦，比心！"
            print(res)
            send_email(res)
    except:
        res="打卡程序中断了呜呜呜"
        webclick()
        send_email(res)
        

def send_email(a):
    # 发送邮件，需要第三方的smtp服务器，这里的密码是在邮箱网站申请授权码，不是自己的登录密码
    mail_user = '13218820256@163.com'
    mail_pass = 'AKTXLNBXMOKXGNCR'
    # 接收邮件，可设置为你的其他邮箱
    receivers = ['MZ120201331@yzu.edu.cn,']

    # 邮件内容，文本格式，把plain改成html是html格式
    message = MIMEText('%s 今天也要加油哦！'%(a), 'plain', 'utf-8')
    # 显示的发件人
    message['From'] = mail_user
    # 显示的收件人
    message['To'] = ','.join(receivers)
    message['Subject'] = Header('主人，%s'%(a), 'utf-8')

    try:
        # QQ邮箱SMTP服务器smtp.qq.com（端口465或587）SSL一般用465
        smtpObj = smtplib.SMTP_SSL('smtp.163.com', 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(mail_user, message['To'].split(','), message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


if __name__ == '__main__':
    webclick()

