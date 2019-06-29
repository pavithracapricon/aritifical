import re   
test_string = "Geeksforgeeks,    is best @# Computer Science Portal.!!!" 
print ("The original string is : " +  test_string) 
res = len(re.findall(r'\w+', test_string)) 
print ("The number of words in string are : " +  str(res))
