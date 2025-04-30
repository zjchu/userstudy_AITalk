import streamlit as st
import imaplib
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import email
from email.header import decode_header
import numpy as np
import random

def send_email(email, password, array, dataset):
    # 构建邮件主体
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email  # 收件人邮箱
    msg['Subject'] = fr'{dataset} Number of submissions'
    
    # 邮件正文
    string = ''.join([str(element) for element in array])
    text = MIMEText(string)
    msg.attach(text)
     
    # 发送邮件
    try:
        smtp = smtplib.SMTP('smtp.126.com')
        smtp.login(email, password)
        smtp.sendmail(email, email, msg.as_string())
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('邮件发送失败，错误信息：', e)

if __name__ == '__main__':
    #dataset = 'BIWI'
    #dataset = 'VOCASET' 
    myemail = st.secrets["my_email"]["email"]  # 邮箱账号
    password =  st.secrets["my_email"]["password"]  # 邮箱密码

    array=[0 for x in range(10)]
    array1=[0 for x in range(9)]
    send_email(myemail, password, array, 'BIWI')
    send_email(myemail, password, array, 'vocaset')
    send_email(myemail, password, array1, 'multiface')


