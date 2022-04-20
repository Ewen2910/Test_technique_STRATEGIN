from ctypes import sizeof
from flask import Flask
import json
import random

app = Flask(__name__)

@app.route("/health", methods=['GET'])

def health():
    return "200"

@app.route("/longestCommonStreak", methods=['GET'])
def error_params():
    return "Enter Params like that /longestCommonStreak/firstword/secondword"

@app.route("/longestCommonStreak/<wo>/<wt>", methods=['GET'])

def longestCommonStreak(wo, wt):
    
    save = ""
    streak = ""
    z = 0
    
    for i in range(0, len(wo)):
        for j in range(0,len(wt)):
            if z + i == len(wo):
                break
            if wt[j] == wo[i + z]:
                streak += wt[j]
                z += 1
            else:
                streak = ""
                z = 0
            if len(streak) > len(save):
                save = streak
        streak = ""
        z = 0
    return save
@app.route("/emailValidation", methods=['GET'])
def error_param():
    return "Enter Params like that /emailValidation/mail"

@app.route("/emailValidation/<mail>", methods=['GET'])

def emailValidation(mail):
    save= ""
    
    for i in range(0, len(mail)):
        if (mail[i] == '.'):
            if len(save) == 0 or save[len(save)-1] == '@':
                save += mail[i]
            else: return "False"
            
        if (mail[i] == '@'):
            if len(save)== 3:
                return  "False"
            if len(save) == 0 or save[len(save)-1] == '.':
                save += mail[i]
            else : return "False"
    return "True"

if __name__ =='__main__':
    app.run(debug=True)
    print("api Start")