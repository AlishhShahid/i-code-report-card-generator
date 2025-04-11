students_data = []

while True:
  student_name = str(input("Enter the student's name: "))
  try:
    roll_number = int(input("Enter the student's roll number: "))
    math = int(input("Enter marks obtained in Math: "))
    physics = int(input("Enter marks obtained in Physics: "))
    urdu = int(input("Enter marks obtained in Urdu: "))
    english = int(input("Enter marks obtained in English: "))
    computer = int(input("Enter marks obtained in Computer: "))
  except ValueError:
        print("❌ Please enter a valid number.")
        continue  
  total = math + english + physics + computer + urdu
  percentage = float((total/500)*100)

  students = {
    "name": student_name,
    "roll_number": roll_number,
    "math": math,
    "physics": physics,
    "urdu": urdu,
    "english": english,
    "computer": computer,
    "total": total,
    "percentage": percentage
  }
  students_data.append(students)
  
  more_detail = input("\nDo you want to insert more? Press 'Y' for Yes or 'N' for No: ").upper()
  while more_detail not in ["Y", "N"]:
    print("❌ Invalid choice! Please enter only Y or N.")
    more_detail = input("\nDo you want to insert more? Press 'Y' for Yes or 'N' for No: ").upper() 
  if more_detail == "N":
      break

        
print(" \nStudents Report Card!")
for student in students_data:
  print(f"\nRecord of {student['name']} inserted successfully.")
  print(f"Student Name: {student['name']}")
  print(f"Roll Number: {student['roll_number']}")
  print(f"Math: {student['math']}\nPhysics: {student['physics']}\nUrdu: {student['urdu']}\nEnglish: {student['english']}\nComputer: {student['computer']}")
  print(f"Total Marks: {student['total']}")
  print(f"Percentage: {student['percentage']:.2f}%")
  if student['percentage'] >= 40 and student['percentage'] <= 49:
    print("Grade: F")
  elif student['percentage'] >= 50 and student['percentage'] <= 59:
    print("Grade: C")
  elif student['percentage'] >= 60 and student['percentage'] <= 69:
    print("Grade: B")
  elif student['percentage'] >= 70 and student['percentage'] <= 79:
    print("Grade: A")
  elif student['percentage'] >= 80:
    print("Grade: A+")


  