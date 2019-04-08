from flask import Flask, render_template, request

app = Flask(__name__)


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():

    link = request.form['link']
    campaign = request.form['campaign']
    content = request.form['content']

    m = MakeUTMlink(link, campaign, content)

    return render_template('result.html', fb=m.fb, cpc=m.cpc, li=m.li, mail=m.mail)

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