# Load libraries
import pandas
from flask import Flask
from asyncio import __main__

result = '''<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<style>
    table {
      border-collapse: collapse;
      width: 100%;
      margin: 0
    }

    th, td {
      text-align: left;
      padding: 8px;
    }

    tr:nth-child(even) {
      background-color: #f2f2f2;
    }

    th {
      background-color: #630031;
      color: white;
    }
 
    .btn {
        float: left;
        width: 8%;
        margin: 12px
        
    }
    
    .btn-primary {
        color: white;
        background-color: #630031;
        border-color: #CF4420
  }

    .btn-primary:hover {
      color: white;
      background-color: #CF4420;
      border-color: #CF4420

}

    header {
        margin: 18px;
}
    paragraph
    
    
  </style>

<title>Pathways Finder</title>
</head>
<header>
  <h1 style="font-size: 36px; color: #630031; text-shadow: 2px 2px 4px #CF4420;">VT Pathways Finder</h1>
    <form class="form" method="POST" action="/pathway1f">
      <button class="btn btn-primary" type="submit">Pathways 1f</button>
    </form>

    <form class="form" method="POST" action="/pathway1a">
      <button class="btn btn-primary" type="submit">Pathways 1a</button>
    </form>
    
    <form class="form" method="POST" action="/pathway2">
      <button class="btn btn-primary" type="submit">Pathways 2</button>
    </form>
    
    <form class="form" method="POST" action="/pathway3">
      <button class="btn btn-primary" type="submit">Pathways 3</button>
    </form>
    
    <form class="form" method="POST" action="/pathway4">
      <button class="btn btn-primary" type="submit">Pathways 4</button>
    </form>
    
    <form class="form" method="POST" action="/pathway5a">
      <button class="btn btn-primary" type="submit">Pathways 5a</button>
    </form>
    
    <form class="form" method="POST" action="/pathway5f">
      <button class="btn btn-primary" type="submit">Pathways 5f</button>
    </form>
    
    <form class="form" method="POST" action="/pathway6a">
      <button class="btn btn-primary" type="submit">Pathways 6a</button>
    </form>
    
    <form class="form" method="POST" action="/pathway6d">
      <button class="btn btn-primary" type="submit">Pathways 6d</button>
    </form>
    
    <form class="form" method="POST" action="/pathway7">
      <button class="btn btn-primary" type="submit">Pathways 7</button>
    </form>
</header>

<table border = "1">
<tr>
<th>Academic Year</th>
<th>Term</th>
<th>Subject</th>
<th>Course No.</th>
<th>Course Title</th>
<th>Instructor</th>
<th>GPA</th>
<th>A(%)</th>
<th>A-(%)</th>
<th>B+(%)</th>
<th>B(%)</th>
<th>B-(%)</th>
<th>C+(%)</th>
<th>C(%)</th>
<th>C-(%)</th>
<th>D+(%)</th>
<th>D(%)</th>
<th>D-(%)</th>
<th>F(%)</th>
<th>W</th>
<th>Graded Enrollment</th>
<th>CRN</th>
<th>Credits</th>
'''

end = '''
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<body>
'''

# Load dataset
file = "Grade Distribution-2.csv"
filep1a = "Pathways1a.csv"
filep1f = "Pathways1f.csv"
filep2 = "Pathways2.csv"
filep3 = "Pathways3.csv"
filep4 = "Pathways4.csv"
filep5a = "Pathways5a.csv"
filep5f = "Pathways5f.csv"
filep6a = "Pathways6a.csv"
filep6d = "Pathways6d.csv"
filep7 = "Pathways7.csv"

names = ['Academic Year', 'Term', 'Subject', 'Course No.', 'Course Title', 'Instructor', 'GPA', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'W', 'Graded Enrollment', 'CRN', 'Credits']
courseData = ['Subject', 'Course No.']
dataset = pandas.read_csv(file, names=names)
dataset = dataset.sort_values(by=['GPA', 'Course Title'], ascending=False)

pathways1a = pandas.read_csv(filep1a, names=courseData)
pathways1f = pandas.read_csv(filep1f, names=courseData)
pathways2 = pandas.read_csv(filep2, names=courseData)
pathways3 = pandas.read_csv(filep3, names=courseData)
pathways4 = pandas.read_csv(filep4, names=courseData)
pathways5a = pandas.read_csv(filep5a, names=courseData)
pathways5f = pandas.read_csv(filep5f, names=courseData)
pathways6a = pandas.read_csv(filep6a, names=courseData)
pathways6d = pandas.read_csv(filep6d, names=courseData)
pathways7 = pandas.read_csv(filep7, names=courseData)


def convertToSet(df):
    localSet = set()
    for index, row in df.iterrows():
        localSet.add(str(row['Course No.']) + str(row['Subject']))
    return localSet


p1a = convertToSet(pathways1a)
p1f = convertToSet(pathways1f)
p2 = convertToSet(pathways2)
p3 = convertToSet(pathways3)
p4 = convertToSet(pathways4)
p5a = convertToSet(pathways5a)
p5f = convertToSet(pathways5f)
p6a = convertToSet(pathways6a)
p6d = convertToSet(pathways6d)
p7 = convertToSet(pathways7)


def findCourses(path):
    returnString = ""
    for index, row in dataset.iterrows():
        if ((str(row['Course No.']) + str(row['Subject'])) in path): 
            returnString += "<tr>"
            returnString += "<td>" + str(row['Academic Year']) + "</td>"
            returnString += "<td>" + str(row['Term']) + "</td>"
            returnString += "<td>" + str(row['Subject']) + "</td>"
            returnString += "<td>" + str(row['Course No.']) + "</td>"
            returnString += "<td>" + str(row['Course Title']) + "</td>"
            returnString += "<td>" + str(row['Instructor']) + "</td>"
            returnString += "<td>" + str(row['GPA']) + "</td>"
            returnString += "<td>" + str(row['A']) + "</td>"
            returnString += "<td>" + str(row['A-']) + "</td>"
            returnString += "<td>" + str(row['B+']) + "</td>"
            returnString += "<td>" + str(row['B']) + "</td>"
            returnString += "<td>" + str(row['B-']) + "</td>"
            returnString += "<td>" + str(row['C+']) + "</td>"
            returnString += "<td>" + str(row['C']) + "</td>"
            returnString += "<td>" + str(row['C-']) + "</td>"
            returnString += "<td>" + str(row['D+']) + "</td>"
            returnString += "<td>" + str(row['D']) + "</td>"
            returnString += "<td>" + str(row['D-']) + "</td>"
            returnString += "<td>" + str(row['F']) + "</td>"
            returnString += "<td>" + str(row['W']) + "</td>"
            returnString += "<td>" + str(row['Graded Enrollment']) + "</td>"
            returnString += "<td>" + str(row['CRN']) + "</td>"
            returnString += "<td>" + str(row['Credits']) + "</td>"
    return returnString


findCourses(p3)

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def default():
    return result + findCourses(p1f) + end

@app.route("/pathway1f", methods=["POST", "GET"])
def pathway1f():
    return result + findCourses(p1f) + end


@app.route("/pathway1a", methods=["POST", "GET"])
def pathway1a():
    return result + findCourses(p1a) + end


@app.route("/pathway2", methods=["POST", "GET"])
def pathway2():
    return result + findCourses(p2) + end


@app.route("/pathway3", methods=["POST", "GET"])
def pathway3():
    return result + findCourses(p3) + end


@app.route("/pathway4", methods=["POST", "GET"])
def pathway4():
    return result + findCourses(p4) + end


@app.route("/pathway5a", methods=["POST", "GET"])
def pathway5a():
    return result + findCourses(p5a) + end


@app.route("/pathway5f", methods=["POST", "GET"])
def pathway5f():
    return result + findCourses(p5f) + end


@app.route("/pathway6a", methods=["POST", "GET"])
def pathway6a():
    return result + findCourses(p6a) + end


@app.route("/pathway6d", methods=["POST", "GET"])
def pathway6d():
    return result + findCourses(p6d) + end


@app.route("/pathway7", methods=["POST", "GET"])
def pathway7():
    return result + findCourses(p7) + end


if __name__ == "__main__":
    app.run()

