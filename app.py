from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
app = Flask(__name__)

from flask import Flask, request, render_template

app = Flask(__name__)

# API_TOKEN = "86ef8bdd0f5eff2603eac6f4e1737e03e62f8a99&"
# CALL_BILTY_API = ('https://api-ssl.bitly.com/v3/shorten?format=json&access_token={}&longUrl={}')

@app.route('/')
def my_form():
    # tokens_pool = ['86ef8bdd0f5eff2603eac6f4e1737e03e62f8a99']  # Use your own.
    # shortener = Shortener(tokens=tokens_pool, max_cache_size=8192)
    # urls = ['https://paperswithcode.com/sota', 'https://arxiv.org/', 'https://arxiv.org/list/cs.LG/recent']
    # results = shortener.shorten_urls(urls)
    # print(results)

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


@app.route('/vmj/ro')
def my_form_vmj_ro():
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


    return render_template('results_vmj.html', link=v.result_link)


class MakeUTMVMJ:
    def __init__(self, link):
        try:
            page_response = requests.get(link, timeout=10).text
            page_content = BeautifulSoup(page_response, 'lxml').select('#jd_reference')
            data_into_str = page_content[0].text.strip()
            ref = data_into_str
            self.result_link = link+"?utm_source=linkedin&utm_medium=social&utm_campaign=vmj&utm_content="+ref+"&jobSource=VMJ"
        except:
            self.result_link = "Wprowadź poprawny link do ogłoszenia na hays.pl/hays-response.pl"




@app.route('/vmj/cz', methods=['POST'])
def vmj_form_post_cz():

    link = request.form['link']
    sep = "?"
    link = link.split(sep, 1)[0]
    v = MakeUTMVMJ_CZ(link)


    return render_template('results_vmj_cz.html', link_fb=v.result_link_fb, link_li=v.result_link_li)


class MakeUTMVMJ_CZ:
    def __init__(self, link):
        try:
            page_response = requests.get(link, timeout=10).text
            page_content = BeautifulSoup(page_response, 'lxml').select('#jd_reference')
            data_into_str = page_content[0].text.strip()
            ref = data_into_str
            self.result_link_li = link+"?utm_source=Linkedin&utm_medium=social&utm_campaign=vmj&utm_content="+ref+"&jobSource=VMJ"
            self.result_link_fb = link+"?utm_source=Facebook&utm_medium=social&utm_campaign=vmj&utm_content="+ref+"&jobSource=VMJ"
        except:
            self.result_link_li= "Please provide correct link to hays.cz/hays-response.cz website"
            self.result_link_fb= "Please provide correct link to hays.cz/hays-response.cz website"



@app.route('/vmj/hu', methods=['POST'])
def vmj_form_post_hu():

    link = request.form['link']
    sep = "?"
    link = link.split(sep, 1)[0]
    v = MakeUTMVMJ_HU(link)



    return render_template('results_vmj_hu.html', link_fb=v.result_link_fb, link_li=v.result_link_li)


class MakeUTMVMJ_HU:
    def __init__(self, link):
        try:
            page_response = requests.get(link, timeout=10).text
            page_content = BeautifulSoup(page_response, 'lxml').select('#jd_reference')
            data_into_str = page_content[0].text.strip()
            ref = data_into_str
            self.result_link_li = link+"?utm_source=Linkedin&utm_medium=social&utm_campaign=vmj&utm_content="+ref+"&jobSource=VMJ"
            self.result_link_fb = link+"?utm_source=Facebook&utm_medium=social&utm_campaign=vmj&utm_content="+ref+"&jobSource=VMJ"
        except:
            self.result_link_li = "Please provide correct link to hays.hu/hays-response.hu website"
            self.result_link_fb = "Please provide correct link to hays.hu/hays-response.hu website"



@app.route('/vmj/ro', methods=['POST'])
def vmj_form_post_ro():

    link = request.form['link']
    sep = "?"
    link = link.split(sep, 1)[0]
    v = MakeUTMVMJ_RO(link)



    return render_template('results_vmj_ro.html', link_fb=v.result_link_fb, link_li=v.result_link_li)


class MakeUTMVMJ_RO:
    def __init__(self, link):
        try:
            page_response = requests.get(link, timeout=10).text
            page_content = BeautifulSoup(page_response, 'lxml').select('#jd_reference')
            data_into_str = page_content[0].text.strip()
            ref = data_into_str
            self.result_link_li = link+"?utm_source=Linkedin&utm_medium=social&utm_campaign=vmj&utm_content="+ref+"&jobSource=VMJ"
            self.result_link_fb = link+"?utm_source=Facebook&utm_medium=social&utm_campaign=vmj&utm_content="+ref+"&jobSource=VMJ"
        except:
            self.result_link_li = "Please provide correct link to hays.ro website"
            self.result_link_fb = "Please provide correct link to hays.ro website"




class MakeUTMlink:
    def __init__(self, link, campaign, content):
        if content == "":
            self.fb = link + "?utm_source=facebook&utm_medium=social&utm_campaign=" + campaign
            print(self.fb)
            # data = requests.get(CALL_BILTY_API.format(API_TOKEN, self.fb)).json()
            # self.fb_short = (data['data']['url'])

            self.cpc = link + "?utm_source=facebook&utm_medium=cpc&utm_campaign=" + campaign
            # data = requests.get(CALL_BILTY_API.format(API_TOKEN, self.cpc)).json()
            # self.cpc_short = (data['data']['url'])

            self.li = link + "?utm_source=linkedin&utm_medium=social&utm_campaign=" + campaign
            # data = requests.get(CALL_BILTY_API.format(API_TOKEN, self.li)).json()
            # self.li_short = (data['data']['url'])

            self.mail = link+"?utm_source=newsletter&utm_medium=email&utm_campaign="+campaign
            # data = requests.get(CALL_BILTY_API.format(API_TOKEN, self.mail)).json()
            # self.mail_short = (data['data']['url'])

        else:
            self.fb = link + "?utm_source=facebook&utm_medium=social&utm_campaign=" + campaign+"&utm_content="+content
            self.cpc = link + "?utm_source=facebook&utm_medium=cpc&utm_campaign=" + campaign+"&utm_content="+content
            self.li = link + "?utm_source=linkedin&utm_medium=social&utm_campaign=" + campaign+"&utm_content="+content
            self.mail = link + "?utm_source=newsletter&utm_medium=email&utm_campaign=" + campaign+"&utm_content="+content







if __name__ == '__main__':
    app.run()