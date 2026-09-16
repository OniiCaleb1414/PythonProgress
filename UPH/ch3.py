import math

def Ga():
    name = input("Whats your name?: ")
    print("Good Afternoon " + name)
    
# Ga()    

def fill_It():
    name = "Rico"
    date = "14/11/2006"
    letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
        '''
    print(letter+ "\n")    
    letter = letter.replace("<|Name|>",name)
    letter = letter.replace("<|Date|>",date)
    print(letter+ "\n")

# fill_It()
        
def find_DS(sent):
    found = True
    num = sent.find("  ")
    if num < 0:
        found = False
    
    return found

# print(find_DS("soo yteheu kf kahcf jkalscfds  aacj"))            

def fix_DS(sent):
    if find_DS(sent):
        print("Sentence before: " + sent)
        sent = sent.replace("  "," ")
    
    print("Sentence: " + sent)    

# fix_DS("bvgf akdsljds alkdbvflkja alkjbh lkabvhf  kahvf kahds  kahjfd")    

def fix_sent(sent):
   print("Sentence before: "+  sent)
   sent = sent.replace(", ", ", \n")
   sent = sent.replace(". ", ". \n")
   print("Sentence after: "+  sent)
letter = "Dear Harry, this python course is nice. Thanks!"
   
# fix_sent(letter)   


