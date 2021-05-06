student_scores ={
  "Harry" : 81,
  "Ron" : 78,
  "Hermione" : 99,
  "Draco" : 74,
  "Neville" : 62,
}

# create student_grade empty
student_grades = {}
  
for student in student_scores:
  #print (student)     # print student (key) name only
  score = student_scores[student]
  #print(score)         # print only scores

  if score > 90 :
    student_grades[student] = " Outstanding"
  elif score > 81 :  
    student_grades[student] = " Exceeds Expectation"
  elif score> 71 :  
   student_grades[student] = "Acceptable" 
  else :
    student_grades[student] = "Fail"

print (student_grades)