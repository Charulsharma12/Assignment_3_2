a = input("Write the string to be reversed:") #Input string that has to be reversed

#Building a function that can reverse the string 
def string_reverse(reverse_string):
   reverse_string = reverse_string[::-1]
   print(reverse_string)
   return reverse_string
#Call the function to reverse the string 
string_reverse(a)


