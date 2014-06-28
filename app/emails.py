# -*- coding: utf-8 -*- 
from flask.ext.mail import Message
from flask import render_template

from app import mail

from threading import Thread

def send_async_email(msg):
    mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    thr = Thread(target = send_async_email, args = [msg])
    thr.start()

from config import ADMINS

def follower_notification(followed, follower):
    send_email(u"[microblog] %s 关注了你!" % follower.nickname,
        ADMINS[0],
        [followed.email],
        render_template("follower_email.txt", 
            user = followed, follower = follower),
        render_template("follower_email.html", 
            user = followed, follower = follower))
