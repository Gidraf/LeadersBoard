from flask import *
import jsonpickle

app = Flask(__name__)

########################
# Flask Server Example #
########################

##LEADERBOARD
## This will be a list with simple dict inside (eg. [{name: Joe, score: 10},{name: Jane, score: 20}])
leaderboard = []
id = 0


# INDEX PAGE
@app.route('/')
def home():
    return render_template('index.html')

# GET LEADERBOARD
@app.route('/api/getleaders')
def get_leader():
    global leaderboard
    print "Getting Leaderboard"
    print leaderboard
    return jsonpickle.encode(leaderboard)

# ADD ENTRY
@app.route('/api/addentry',methods=['POST'])
def add_entry():
    global leaderboard,id
    print "Adding Entry"
    content = request.get_json(silent=False)
    id += 1;
    leaderboard += [{"id":id,"name":content["name"],"score":content["score"]}]
    return jsonpickle.encode(leaderboard)

# REMOVE ENTRY
@app.route('/api/rmentry/', methods=['DELETE'])
def rm_entry(entry_id):
    global leaderboard
    print "Removing Entry!"

    for entry in leaderboard:
        if entry["id"] == entry_id:
            leaderboard.remove(entry)
            break;

    return jsonpickle.encode(leaderboard)

if __name__ == "__main__":

    app.debug = True
    app.run(port=80)
