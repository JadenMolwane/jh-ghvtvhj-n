from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/response")
def render_1():
    sel1 = request.args['Q1']
    sel2 = request.args['Q2']
    sel3 = request.args['Q3']
   

    if sel1 == '15-16' and sel2 == 'Yes' and sel3 == 'Yes':
        reply= "You got the job!"
    elif sel1 == '15-16' and sel2 == 'No' and sel3 =='Yes':
        reply= "You got the job!"
    elif sel1 == '15-16' and sel2 == 'Yes' and sel3 =='No':
        reply= "You got the job!"
    elif sel1 == '15-16' and sel2 == 'No' and sel3 =='No':
        reply= "You did not get the job"
    elif sel1 == '17-18' and sel2 == 'Yes' and sel3 == 'Yes':
        reply= "You got the job!"
    elif sel1 == '17-18' and sel2 == 'No' and sel3 =='Yes':
        reply= "You got the job!"
    elif sel1 == '17-18' and sel2 == 'Yes' and sel3 =='No':
        reply= "You got the job!"
    elif sel1 == '17-18' and sel2 == 'No' and sel3 =='No':
        reply= "You did not get the job"
    elif sel1 == '19-20' and sel2 == 'Yes' and sel3 == 'Yes':
        reply= "You got the job!"
    elif sel1 == '19-20' and sel2 == 'No' and sel3 =='Yes':
        reply= "You got the job!"
    elif sel1 == '19-20' and sel2 == 'Yes' and sel3 =='No':
        reply= "You got the job!"
    elif sel1 == '19-20' and sel2 == 'No' and sel3 =='No':
        reply= "You got the job!"
    elif sel1 == '21+' and sel2 == 'Yes' and sel3 == 'Yes':
        reply= "You got the job!"
    elif sel1 == '21+' and sel2 == 'No' and sel3 =='Yes':
        reply= "You got the job!"
    elif sel1 == '21+' and sel2 == 'Yes' and sel3 =='No':
        reply= "You got the job!"
    elif sel1 == '21+' and sel2 == 'No' and sel3 =='No':
        reply= "You got the job!"
    else:
        reply = "Please answer all the questions in the form"
    return render_template('index2.html', response = reply)

    

if __name__=="__main__":
    app.run(debug=False)