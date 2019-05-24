from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import os
from emoji import emojize

app = Flask(__name__)


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/vmj')
def my_form_vmj():
    return render_template('vmj-form.html')

@app.route('/vmj/cz')
def my_form_vmj_cz():
    return render_template('vmj-form.html')

@app.route('/vmj/hu')
def my_form_vmj_hu():
    return render_template('vmj-form.html')


@app.route('/', methods=['POST'])
def my_form_post():

    link = request.form['link']
    campaign = request.form['campaign']
    content = request.form['content']

    m = MakeUTMlink(link, campaign, content)

    return render_template('result.html', fb=m.fb, cpc=m.cpc, li=m.li, mail=m.mail)

@app.route('/vmj', methods=['POST'])
def vmj_form_post():

    link = request.form['link']
    sep = "?"
    link = link.split(sep, 1)[0]
    v = MakeUTMVMJ(link)

    print(emojize(":thumbs_up:"))

    return render_template('results_vmj.html', link=v.result_link)


class MakeUTMVMJ:
    def __init__(self, link):
        try:
            page_response = requests.get(link, timeout=10).text
            page_content = BeautifulSoup(page_response, 'lxml').select('#jd_reference')
            data_into_str = page_content[0].text.strip()
            ref = data_into_str
            self.result_link = link+"?utm_source=linkedin&utm_medium=social&utm_campaign=vmj&utm_content="+ref
        except:
            self.result_link = "Wprowadź poprawny link do ogłoszenia na hays.pl/hays-response.pl"




@app.route('/vmj/cz', methods=['POST'])
def vmj_form_post_cz():

    link = request.form['link']
    sep = "?"
    link = link.split(sep, 1)[0]
    v = MakeUTMVMJ_CZ(link)

    print(emojize(":thumbs_up:"))

    return render_template('results_vmj_cz.html', link_fb=v.result_link_fb, link_li=v.result_link_li)


class MakeUTMVMJ_CZ:
    def __init__(self, link):
        try:
            page_response = requests.get(link, timeout=10).text
            page_content = BeautifulSoup(page_response, 'lxml').select('#jd_reference')
            data_into_str = page_content[0].text.strip()
            ref = data_into_str
            self.result_link_li = link+"?utm_source=Linkedin&utm_medium=social&utm_campaign=vmj&utm_content="+ref
            self.result_link_fb = link+"?utm_source=Facebook&utm_medium=social&utm_campaign=vmj&utm_content="+ref
        except:
            self.result_link_li= "Please provide correct link to hays.cz/hays-response.cz website"
            self.result_link_fb= "Please provide correct link to hays.cz/hays-response.cz website"



@app.route('/vmj/hu', methods=['POST'])
def vmj_form_post_hu():

    link = request.form['link']
    sep = "?"
    link = link.split(sep, 1)[0]
    v = MakeUTMVMJ_HU(link)

    print(emojize(":thumbs_up:"))

    return render_template('results_vmj_hu.html', link_fb=v.result_link_fb, link_li=v.result_link_li)


class MakeUTMVMJ_HU:
    def __init__(self, link):
        try:
            page_response = requests.get(link, timeout=10).text
            page_content = BeautifulSoup(page_response, 'lxml').select('#jd_reference')
            data_into_str = page_content[0].text.strip()
            ref = data_into_str
            self.result_link_li = link+"?utm_source=Linkedin&utm_medium=social&utm_campaign=vmj&utm_content="+ref
            self.result_link_fb = link+"?utm_source=Facebook&utm_medium=social&utm_campaign=vmj&utm_content="+ref
        except:
            self.result_link_li = "Please provide correct link to hays.hu/hays-response.hu website"
            self.result_link_fb = "Please provide correct link to hays.hu/hays-response.hu website"



class MakeUTMlink:
    def __init__(self, link, campaign, content):
        if content == "":
            self.fb = link + "?umt_source=facebook&utm_medium=social&utm_campaign=" + campaign
            self.cpc = link + "?umt_source=facebook&utm_medium=cpc&utm_campaign=" + campaign
            self.li = link + "?umt_source=linkedin&utm_medium=social&utm_campaign=" + campaign
            self.mail = link+"?umt_source=newsletter&utm_medium=email&utm_campaign="+campaign
        else:
            self.fb = link + "?umt_source=facebook&utm_medium=social&utm_campaign=" + campaign+"&utm_content="+content
            self.cpc = link + "?umt_source=facebook&utm_medium=cpc&utm_campaign=" + campaign+"&utm_content="+content
            self.li = link + "?umt_source=linkedin&utm_medium=social&utm_campaign=" + campaign+"&utm_content="+content
            self.mail = link + "?umt_source=newsletter&utm_medium=email&utm_campaign=" + campaign+"&utm_content="+content







if __name__ == '__main__':
    app.run()