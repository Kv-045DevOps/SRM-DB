from app import app
from app import dbconnect
from flask import Flask, jsonify, request
import json
import requests

connect = dbconnect.connect_db("srmsystem")
cursor = connect.cursor()

@app.route('/get-dep', methods=['GET'])
def get_dep():
    data = {"Department":[]}
    cursor.execute('SELECT * FROM department')
    records = cursor.fetchall()
    for i in records:
        var = {'name':i[1]}
        data["Department"].append(var)
    data = json.dumps(data)
    return data

@app.route('/get-team', methods=['GET'])
def get_team():
    data = {"Team":[]}
    cursor.execute('SELECT * FROM team')
    records = cursor.fetchall()
    for i in records:
        var = {'team_id':i[0], 'name':i[1], 'manager_id':i[2], 'depart_id':i[3]}
        data["Team"].append(var)
    return json.dumps(data)

@app.route('/get-empl', methods=['GET'])
def get_empl():
    data = {"Employee":[]}
    cursor.execute('SELECT * FROM employee')
    records = cursor.fetchall()
    for i in records:
        var = {'name':i[1], 'sname':i[2], 'exp':i[3], 'position':i[4], 'salary':i[5], 'coefficient':i[6], 'team_id':i[7]}
        data["Employee"].append(var)
    return json.dumps(data)

@app.route('/set_department', methods=['POST'])
def set_department():
    datajson = request.data
    data = json.loads(datajson)
    cursor.execute("INSERT INTO department (name) VALUES ('"+data['name']+"')")
    connect.commit()
    return ""

@app.route('/set_team', methods=['POST'])
def set_team():
    datajson = request.data
    data = json.loads(datajson)
    if data['manager_id'] == "": cursor.execute("INSERT INTO team (name, id_department) VALUES ('"+data['name']+"', '"+data['depart_id']+"')")
    else: cursor.execute("INSERT INTO team (name, id_manager, id_department) VALUES ('"+data['name']+"', '"+data['manager_id']+"', '"+data['depart_id']+"')")
    connect.commit()
    return ""
@app.route('/set_employee', methods=['POST'])
def set_employee():
    datajson = request.data
    data = json.loads(datajson)
    cursor.execute("INSERT INTO employee (fname, sname, exp, position, salary, coef, team_id) VALUES ('"+data['name']+"', '"+data['sname']+"', '"+data['exp']+"', '"+data['position']+"', '"+data['salary']+"', '"+data['coefficient']+"', '"+data['team_id']+"')")
    connect.commit()
    return ""
