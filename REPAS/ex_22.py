import uuid
from xml.dom import minidom 
doc = minidom.Document()

students = doc.createElement('students')
doc.appendChild(students)
student_id = [str(uuid.uuid4()) for _ in range(5)]
info = [
    ["Roc", "Bigas", "rbigas34@gmail.com", "21356478L"],
    ["Juan", "Gomez", "jgomez@gmail.com", "12345678M"],
    ["Maria", "Lopez", "mlopez@gmail.com", "87654321N"],
    ["Carlos", "Santos", "csantos@gmail.com", "98765432O"],
    ["Elena", "Martinez", "emartinez@gmail.com", "56789012P"],
    ["Pedro", "Fernandez", "pfernandez@gmail.com", "34567890Q"]
]
for student_info in info:
    student = doc.createElement('student')
    student.setAttribute("ID", str(uuid.uuid4()))
    subchilds = [doc.createElement('name'), doc.createElement('surname'), doc.createElement('email'), doc.createElement('dni')]
    for i, subchild in enumerate(subchilds):
        text_node = doc.createTextNode(student_info[i])
        subchild.appendChild(text_node)
        student.appendChild(subchild)
    students.appendChild(student)

xml_str = doc.toprettyxml(indent ="\t")
print(xml_str)

with open("ex_22.xml", "wt") as f:
    f.write(xml_str)