from flask import Blueprint, request, jsonify,current_app
from flask.ext.pymongo import PyMongo
from hadoopstack.services.cluster import make_connection
from hadoopstack.services.cluster import spawn_instances

app_v1 = Blueprint('v1', __name__, url_prefix='/v1')
#from hadoopstack.main import mongo
#app_v1.config.from_object('config')
mongo = PyMongo()



@app_v1.route('/')
def version():
    return "v1 API. Jobs and clusters API are accessible at /jobs and \
    /clusters respectively"

@app_v1.route('/clusters/', methods = ['GET','POST'])
def clusters():
    if request.method == 'POST':
        data = request.json
	#mongo.db.cluster.insert(data)
        num_tt = int(data['cluster']['node-recipes']['tasktracker'])
        num_jt = int(data['cluster']['node-recipes']['jobtracker'])        
        num_vms = num_jt + num_tt
	j = { "name" : "mongo" }
	mongo.db.things.insert( j )
        conn=make_connection()
        spawn_instances(conn,num_vms)
            
        return jsonify(**request.json)    
        
    return app_v1.name


