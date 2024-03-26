from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Matthew Diani! This is my first code change'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/favorite-course')
def favoritecourse(): # put application's code here
    subject=request.args.get('subject')
    course_number=request.args.get('course_number')

    return render_template('favorite-course.html', subject=subject, course_number= course_number)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')
@app.route('/about-css')
def aboutcss():
    render_template('about-css.html')



@app.route('/log-in')
def login(): # put application's code here
    return render_template('log-in.html')
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
