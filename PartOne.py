variable = input("phrase in camel case: ")

def change_case(camel_str):
   snake_str = ""
   for letter in camel_str:
      if letter.isupper():
         snake_str += "_" + letter.lower()
      else:
         snake_str += letter
   return snake_str

print(change_case(variable))