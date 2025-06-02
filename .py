# ASSIGNMENT-4
# TASK 1:
try:
  with open('sample.txt', 'r') as file:
    for index, line in enumerate(file, start=1):
      print(f"Line {index}: {line.strip()}")
except:
  print("the file dose not exist")

# TASK 2:
n1=input("enter text to write to the file")
file = open('output.txt', 'w')
file.write(n1)
print("data succefully written to output.txt file")

n2=input("enter additional text to write to the file")
file.write(n2)
print("data succefully appended")
file.close

file = open('output.txt', 'r')
content = file.read()       # Stores file content in 'content'
print(content)              # Displays the content
file.close()

