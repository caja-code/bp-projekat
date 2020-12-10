from student import Student
import csv
import json

def create_pocetni_model():
    student_model = [
        student("2018270000", "Marko Markovic"),
        student("2018270001", "Petar Petrovic"),
        student("2018270002", "Janko Jankovic"),
        student("2018270003", "Stefan Stefanovic"),
        student("2018270004", "Ivan Ivanovic")
    ]

    return student_model


newdata = []

with open("student_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",", qoutechar="'")
    #wrte.writerow(create_dummy model())
    for student in create_pocetni_model():
        writer.writerow([student.broj_indeksa, student.ime_prezime])

with open("student_data_csv", 'r', newline="") as infile:
    reader = csv.reader(infile, delimiter= ",", qoutechar="'")
    for row in reader:
        newdata.append(row)
        print(row)

with open("studebts_metadata.json", "w") as metafile:
    metadata = {}
    metadata["columns"] = ["indeks", "ime i prezime"]
    metadata["delimiter"] = ","
    json.dump(metadata, metafile)

with open("student_metadata.json", "r") as metafile:
    metadata = json.load(metafile)
    print(metadata["columns"])


newstudent = []

for s in newdata:
    print(s)
    newstudent.append(Student(s[0], s[1]))
    stud = Student("","")
    stud.__setattr__("broj_indeksa",s[0])
    stud.__setattr__("ime_prezime",s[1])
    print(stud.ime_prezime)