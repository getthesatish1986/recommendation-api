from flask import Flask, render_template, request
#import recommendationsh

app = Flask(__name__,template_folder='template3')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/confirm',methods=['GET','POST'])
def register():
    print('hi')
    if request.method == 'POST':
        a = request.form.getlist('select-1')
        b = request.form.getlist('select-2')
        c = request.form.get('text')
        d = request.form.get('text-2')
        #e = 10
        e =request.form.get('text-1')
        #which='j'
        which=request.form.get('Recommendation type')

        ug = ','
        ug = ug.join(a)

        ug_spec = ','
        ug_spec = ug_spec.join(b)

       # Interest = ','
        #Interest = Interest.join(c)

        #Skill = ','
        #Skill = Skill.join(d)

        dic = {"ug":str(ug),"ugsp":str(ug_spec),"irt":str(c),"ski":str(d),'wrk': 'No', 'job': ' ', 'mas': ' '}
        #dic = {'ug': 'BE', 'ugsp': 'Computer Science', 'irt': 'Data Science', 'ski': 'Python,SQL', 'wrk': 'No', 'job': ' ', 'mas': ' '}
        print(dic)

        # res = recommendation.get_recommendations_job(request.args.get('UG','Mechanical Engineering','dddd','ddddd',10))
        #return render_template('confirm_page.html', name=ug,age=ug_spec,city=Interest)
        #ab = recommendationsh.get_recommendations_job(str(ug),str(ug_spec),str(Interest),str(Skill),int(e))
        ab = recommendationsh.rec(which,dic,int(e))
        print(ab)

        return render_template('index.html', first=ab[1], sec=ab[2],thir=ab[3],four=ab[4],fifth=ab[5],sixth=ab[6],seven=ab[7],eight=ab[8],nine=ab[9],ten=ab[10])
        # return recommendation.get_recommendations_job('BE','Electronics and Communication Engineering','Embedded Design;Circuit Design','simulation;embedded,IOT',10)

if __name__ == '__main__':
    app.run(debug=True)


