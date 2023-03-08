from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load datasets
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
dataset = pd.read_csv(file, names=names)
dataset = dataset.sort_values(by=['GPA', 'Course Title'], ascending=False)

pathways1a = pd.read_csv(filep1a, names=courseData)
pathways1f = pd.read_csv(filep1f, names=courseData)
pathways2 = pd.read_csv(filep2, names=courseData)
pathways3 = pd.read_csv(filep3, names=courseData)
pathways4 = pd.read_csv(filep4, names=courseData)
pathways5a = pd.read_csv(filep5a, names=courseData)
pathways5f = pd.read_csv(filep5f, names=courseData)
pathways6a = pd.read_csv(filep6a, names=courseData)
pathways6d = pd.read_csv(filep6d, names=courseData)
pathways7 = pd.read_csv(filep7, names=courseData)


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
    return dataset.loc[(dataset['Course No.'].astype(str) + dataset['Subject']).isin(path)]


@app.route("/", methods=["POST", "GET"])
def index():
    # Render the index template with links to each pathway
    return render_template("initial.html")

@app.route("/pathway1f", methods=["POST", "GET"])
def pathway1f():
    filename = "pathway1f"
    courses = findCourses(p1f)
    subjects = courses["Subject"].unique()  # get unique subjects from the dataset
    courseTitles = courses["Course Title"].unique()  # get unique subjects from the dataset
    courseNums = courses["Course No."].unique()  # get unique subjects from the dataset
    instructors = courses["Instructor"].unique()  # get unique subjects from the dataset

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway1f/subject", methods=["POST", "GET"])
def pathway1fsubject():
    filename = "pathway1f"
    term = request.form.get("term")  # get the selected subject from the form
    credit = request.form.get("credit")  
    subject = request.form.get("subject")  
    title = request.form.get("title") 
    num = request.form.get("courseNum") 
    instructor = request.form.get("instructor")

    courses = findCourses(p1f)
    subjects = courses["Subject"].unique()  # get unique subjects from the dataset
    courseTitles = courses["Course Title"].unique()  
    courseNums = sorted(courses["Course No."].unique(), reverse=False)  # get unique subjects from the dataset
    instructors = courses["Instructor"].unique()  

    if subject and subject != "All":  # filter data by subject if subject is not "All"
        courses = courses.loc[courses["Subject"] == subject]
    if term and term != "All": 
        courses = courses.loc[courses["Term"] == term]
    if title and title != "All":
        courses = courses.loc[courses["Course Title"] == title]
    if instructor and instructor != "All":
        courses = courses.loc[courses["Instructor"] == instructor]
    if credit and credit != "All": 
        x = pd.to_numeric(courses['Credits'], errors='coerce')
        courses = courses.loc[x == int(credit)]
    if num and num != "All": 
        x = pd.to_numeric(courses['Course No.'], errors='coerce')
        courses = courses.loc[x == int(num)]

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)
    


@app.route("/pathway1a", methods=["POST", "GET"])
def pathway1a():
    filename = "pathway1a"    
    courses = findCourses(p1a)
    subjects = courses["Subject"].unique()  
    courseTitles = courses["Course Title"].unique() 
    courseNums = courses["Course No."].unique()  
    instructors = courses["Instructor"].unique()  

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway1a/subject", methods=["POST", "GET"])
def pathway1asubject():
    filename = "pathway1a"
    term = request.form.get("term")  # get the selected subject from the form
    credit = request.form.get("credit")  
    subject = request.form.get("subject")  
    title = request.form.get("title") 
    num = request.form.get("courseNum") 
    instructor = request.form.get("instructor")

    courses = findCourses(p1a)
    subjects = courses["Subject"].unique()  # get unique subjects from the dataset
    courseTitles = courses["Course Title"].unique()  
    courseNums = sorted(courses["Course No."].unique(), reverse=False)  # get unique subjects from the dataset
    instructors = courses["Instructor"].unique()  

    if subject and subject != "All":  # filter data by subject if subject is not "All"
        courses = courses.loc[courses["Subject"] == subject]
    if term and term != "All": 
        courses = courses.loc[courses["Term"] == term]
    if title and title != "All":
        courses = courses.loc[courses["Course Title"] == title]
    if instructor and instructor != "All":
        courses = courses.loc[courses["Instructor"] == instructor]
    if credit and credit != "All": 
        x = pd.to_numeric(courses['Credits'], errors='coerce')
        courses = courses.loc[x == int(credit)]
    if num and num != "All": 
        x = pd.to_numeric(courses['Course No.'], errors='coerce')
        courses = courses.loc[x == int(num)]

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway2", methods=["POST", "GET"])
def pathway2():
    filename = "pathway2"
    courses = findCourses(p2)
    subjects = courses["Subject"].unique()  
    courseTitles = courses["Course Title"].unique() 
    courseNums = courses["Course No."].unique()  
    instructors = courses["Instructor"].unique()  

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway2/subject", methods=["POST", "GET"])
def pathway2subject():
    filename = "pathway2"
    term = request.form.get("term")  # get the selected subject from the form
    credit = request.form.get("credit")  
    subject = request.form.get("subject")  
    title = request.form.get("title") 
    num = request.form.get("courseNum") 
    instructor = request.form.get("instructor")

    courses = findCourses(p2)
    subjects = courses["Subject"].unique()  # get unique subjects from the dataset
    courseTitles = courses["Course Title"].unique()  
    courseNums = sorted(courses["Course No."].unique(), reverse=False)  # get unique subjects from the dataset
    instructors = courses["Instructor"].unique()  

    if subject and subject != "All":  # filter data by subject if subject is not "All"
        courses = courses.loc[courses["Subject"] == subject]
    if term and term != "All": 
        courses = courses.loc[courses["Term"] == term]
    if title and title != "All":
        courses = courses.loc[courses["Course Title"] == title]
    if instructor and instructor != "All":
        courses = courses.loc[courses["Instructor"] == instructor]
    if credit and credit != "All": 
        x = pd.to_numeric(courses['Credits'], errors='coerce')
        courses = courses.loc[x == int(credit)]
    if num and num != "All": 
        x = pd.to_numeric(courses['Course No.'], errors='coerce')
        courses = courses.loc[x == int(num)]

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway3", methods=["POST", "GET"])
def pathway3():
    filename = "pathway3"
    courses = findCourses(p3)
    subjects = courses["Subject"].unique()  
    courseTitles = courses["Course Title"].unique() 
    courseNums = courses["Course No."].unique()  
    instructors = courses["Instructor"].unique()  

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway3/subject", methods=["POST", "GET"])
def pathway3subject():
    filename = "pathway3"
    term = request.form.get("term")  # get the selected subject from the form
    credit = request.form.get("credit")  
    subject = request.form.get("subject")  
    title = request.form.get("title") 
    num = request.form.get("courseNum") 
    instructor = request.form.get("instructor")

    courses = findCourses(p3)
    subjects = courses["Subject"].unique()  # get unique subjects from the dataset
    courseTitles = courses["Course Title"].unique()  
    courseNums = sorted(courses["Course No."].unique(), reverse=False)  # get unique subjects from the dataset
    instructors = courses["Instructor"].unique()  

    if subject and subject != "All":  # filter data by subject if subject is not "All"
        courses = courses.loc[courses["Subject"] == subject]
    if term and term != "All": 
        courses = courses.loc[courses["Term"] == term]
    if title and title != "All":
        courses = courses.loc[courses["Course Title"] == title]
    if instructor and instructor != "All":
        courses = courses.loc[courses["Instructor"] == instructor]
    if credit and credit != "All": 
        x = pd.to_numeric(courses['Credits'], errors='coerce')
        courses = courses.loc[x == int(credit)]
    if num and num != "All": 
        x = pd.to_numeric(courses['Course No.'], errors='coerce')
        courses = courses.loc[x == int(num)]

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway4", methods=["POST", "GET"])
def pathway4():
    filename = "pathway4"
    courses = findCourses(p4)
    subjects = courses["Subject"].unique()  
    courseTitles = courses["Course Title"].unique() 
    courseNums = courses["Course No."].unique()  
    instructors = courses["Instructor"].unique()  

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway4/subject", methods=["POST", "GET"])
def pathway4subject():
    filename = "pathway4"
    term = request.form.get("term")  # get the selected subject from the form
    credit = request.form.get("credit")  
    subject = request.form.get("subject")  
    title = request.form.get("title") 
    num = request.form.get("courseNum") 
    instructor = request.form.get("instructor")

    courses = findCourses(p4)
    subjects = courses["Subject"].unique()  # get unique subjects from the dataset
    courseTitles = courses["Course Title"].unique()  
    courseNums = sorted(courses["Course No."].unique(), reverse=False)  # get unique subjects from the dataset
    instructors = courses["Instructor"].unique()  

    if subject and subject != "All":  # filter data by subject if subject is not "All"
        courses = courses.loc[courses["Subject"] == subject]
    if term and term != "All": 
        courses = courses.loc[courses["Term"] == term]
    if title and title != "All":
        courses = courses.loc[courses["Course Title"] == title]
    if instructor and instructor != "All":
        courses = courses.loc[courses["Instructor"] == instructor]
    if credit and credit != "All": 
        x = pd.to_numeric(courses['Credits'], errors='coerce')
        courses = courses.loc[x == int(credit)]
    if num and num != "All": 
        x = pd.to_numeric(courses['Course No.'], errors='coerce')
        courses = courses.loc[x == int(num)]

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway5a", methods=["POST", "GET"])
def pathway5a():
    filename = "pathway5a"
    courses = findCourses(p5a)
    subjects = courses["Subject"].unique()  
    courseTitles = courses["Course Title"].unique() 
    courseNums = courses["Course No."].unique()  
    instructors = courses["Instructor"].unique()  

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway5a/subject", methods=["POST", "GET"])
def pathway5asubject():
    filename = "pathway5a"
    term = request.form.get("term")  # get the selected subject from the form
    credit = request.form.get("credit")  
    subject = request.form.get("subject")  
    title = request.form.get("title") 
    num = request.form.get("courseNum") 
    instructor = request.form.get("instructor")

    courses = findCourses(p5a)
    subjects = courses["Subject"].unique()  # get unique subjects from the dataset
    courseTitles = courses["Course Title"].unique()  
    courseNums = sorted(courses["Course No."].unique(), reverse=False)  # get unique subjects from the dataset
    instructors = courses["Instructor"].unique()  

    if subject and subject != "All":  # filter data by subject if subject is not "All"
        courses = courses.loc[courses["Subject"] == subject]
    if term and term != "All": 
        courses = courses.loc[courses["Term"] == term]
    if title and title != "All":
        courses = courses.loc[courses["Course Title"] == title]
    if instructor and instructor != "All":
        courses = courses.loc[courses["Instructor"] == instructor]
    if credit and credit != "All": 
        x = pd.to_numeric(courses['Credits'], errors='coerce')
        courses = courses.loc[x == int(credit)]
    if num and num != "All": 
        x = pd.to_numeric(courses['Course No.'], errors='coerce')
        courses = courses.loc[x == int(num)]

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway5f", methods=["POST", "GET"])
def pathway5f():
    filename = "pathway5f"
    courses = findCourses(p5f)
    subjects = courses["Subject"].unique()  
    courseTitles = courses["Course Title"].unique() 
    courseNums = courses["Course No."].unique()  
    instructors = courses["Instructor"].unique()  

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway5f/subject", methods=["POST", "GET"])
def pathway5fsubject():
    filename = "pathway5f"
    term = request.form.get("term")  # get the selected subject from the form
    credit = request.form.get("credit")  
    subject = request.form.get("subject")  
    title = request.form.get("title") 
    num = request.form.get("courseNum") 
    instructor = request.form.get("instructor")

    courses = findCourses(p5f)
    subjects = courses["Subject"].unique()  # get unique subjects from the dataset
    courseTitles = courses["Course Title"].unique()  
    courseNums = sorted(courses["Course No."].unique(), reverse=False)  # get unique subjects from the dataset
    instructors = courses["Instructor"].unique()  

    if subject and subject != "All":  # filter data by subject if subject is not "All"
        courses = courses.loc[courses["Subject"] == subject]
    if term and term != "All": 
        courses = courses.loc[courses["Term"] == term]
    if title and title != "All":
        courses = courses.loc[courses["Course Title"] == title]
    if instructor and instructor != "All":
        courses = courses.loc[courses["Instructor"] == instructor]
    if credit and credit != "All": 
        x = pd.to_numeric(courses['Credits'], errors='coerce')
        courses = courses.loc[x == int(credit)]
    if num and num != "All": 
        x = pd.to_numeric(courses['Course No.'], errors='coerce')
        courses = courses.loc[x == int(num)]

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway6a", methods=["POST", "GET"])
def pathway6a():
    filename = "pathway6a"
    courses = findCourses(p6a)
    subjects = courses["Subject"].unique()  
    courseTitles = courses["Course Title"].unique() 
    courseNums = courses["Course No."].unique()  
    instructors = courses["Instructor"].unique()  

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway6a/subject", methods=["POST", "GET"])
def pathway6asubject():
    filename = "pathway6a"
    term = request.form.get("term")  # get the selected subject from the form
    credit = request.form.get("credit")  
    subject = request.form.get("subject")  
    title = request.form.get("title") 
    num = request.form.get("courseNum") 
    instructor = request.form.get("instructor")

    courses = findCourses(p6a)
    subjects = courses["Subject"].unique()  # get unique subjects from the dataset
    courseTitles = courses["Course Title"].unique()  
    courseNums = sorted(courses["Course No."].unique(), reverse=False)  # get unique subjects from the dataset
    instructors = courses["Instructor"].unique()  

    if subject and subject != "All":  # filter data by subject if subject is not "All"
        courses = courses.loc[courses["Subject"] == subject]
    if term and term != "All": 
        courses = courses.loc[courses["Term"] == term]
    if title and title != "All":
        courses = courses.loc[courses["Course Title"] == title]
    if instructor and instructor != "All":
        courses = courses.loc[courses["Instructor"] == instructor]
    if credit and credit != "All": 
        x = pd.to_numeric(courses['Credits'], errors='coerce')
        courses = courses.loc[x == int(credit)]
    if num and num != "All": 
        x = pd.to_numeric(courses['Course No.'], errors='coerce')
        courses = courses.loc[x == int(num)]

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway6d", methods=["POST", "GET"])
def pathway6d():
    filename = "pathway6d"
    courses = findCourses(p6d)
    subjects = courses["Subject"].unique()  
    courseTitles = courses["Course Title"].unique() 
    courseNums = courses["Course No."].unique()  
    instructors = courses["Instructor"].unique()  

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway6d/subject", methods=["POST", "GET"])
def pathway6dsubject():
    filename = "pathway6d"
    term = request.form.get("term")  # get the selected subject from the form
    credit = request.form.get("credit")  
    subject = request.form.get("subject")  
    title = request.form.get("title") 
    num = request.form.get("courseNum") 
    instructor = request.form.get("instructor")

    courses = findCourses(p6d)
    subjects = courses["Subject"].unique()  # get unique subjects from the dataset
    courseTitles = courses["Course Title"].unique()  
    courseNums = sorted(courses["Course No."].unique(), reverse=False)  # get unique subjects from the dataset
    instructors = courses["Instructor"].unique()  

    if subject and subject != "All":  # filter data by subject if subject is not "All"
        courses = courses.loc[courses["Subject"] == subject]
    if term and term != "All": 
        courses = courses.loc[courses["Term"] == term]
    if title and title != "All":
        courses = courses.loc[courses["Course Title"] == title]
    if instructor and instructor != "All":
        courses = courses.loc[courses["Instructor"] == instructor]
    if credit and credit != "All": 
        x = pd.to_numeric(courses['Credits'], errors='coerce')
        courses = courses.loc[x == int(credit)]
    if num and num != "All": 
        x = pd.to_numeric(courses['Course No.'], errors='coerce')
        courses = courses.loc[x == int(num)]

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway7", methods=["POST", "GET"])
def pathway7():
    filename = "pathway7"
    courses = findCourses(p7)
    subjects = courses["Subject"].unique()  
    courseTitles = courses["Course Title"].unique() 
    courseNums = courses["Course No."].unique()  
    instructors = courses["Instructor"].unique()  

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)

@app.route("/pathway7/subject", methods=["POST", "GET"])
def pathway7subject():
    filename = "pathway7"
    term = request.form.get("term")  # get the selected subject from the form
    credit = request.form.get("credit")  
    subject = request.form.get("subject")  
    title = request.form.get("title") 
    num = request.form.get("courseNum") 
    instructor = request.form.get("instructor")

    courses = findCourses(p7)
    subjects = courses["Subject"].unique()  # get unique subjects from the dataset
    courseTitles = courses["Course Title"].unique()  
    courseNums = sorted(courses["Course No."].unique(), reverse=False)  # get unique subjects from the dataset
    instructors = courses["Instructor"].unique()  

    if subject and subject != "All":  # filter data by subject if subject is not "All"
        courses = courses.loc[courses["Subject"] == subject]
    if term and term != "All": 
        courses = courses.loc[courses["Term"] == term]
    if title and title != "All":
        courses = courses.loc[courses["Course Title"] == title]
    if instructor and instructor != "All":
        courses = courses.loc[courses["Instructor"] == instructor]
    if credit and credit != "All": 
        x = pd.to_numeric(courses['Credits'], errors='coerce')
        courses = courses.loc[x == int(credit)]
    if num and num != "All": 
        x = pd.to_numeric(courses['Course No.'], errors='coerce')
        courses = courses.loc[x == int(num)]

    return render_template("pathway1f.html", courses=courses.to_dict('records'), subjects=subjects, courseTitles=courseTitles, instructors=instructors, courseNums=courseNums, filename=filename)


if __name__ == "__main__":
    app.run()

