
import datetime
import time

presentHour = datetime.datetime.now().hour

if 3 <= presentHour <= 11 :
 print("Good Morning, Manish Kumawat")

elif 11 <= presentHour <= 17:
   print("Good Afternoon, Manish Kumawat")

elif 17 <= presentHour <= 19 :
   print("Good Evening, Manish Kuamwat")

else:
   print("Good Night, MAnish Kumawat")




print("Welcome to rule based chatbot")

print(" You can me ask basic questions, Type 'bye' to exit from the chatbot")

# Chatbot memory creation [dictionary of responses]


responses = {
  "hello": "Hi, Welcome. How can i help you",
  "how are you": "I am very fine. Thankyou",
  "who are you":"I am a smart Ai chatbot",
  "motivate me": "Keep going. Every bug of your project makes you a better developer",
  "happy":
  "Great to here thet",
  "sad": "Ohh! I understand your situation",
  "what is functions": " Read the ch-7",
  "bye": "Exit to chatnot"
  }

# Method/function to get response of chatbot
def getResponseOfBot(userQuestion):
  userQuestion = userQuestion.lower()
  for eachKey in responses:
    if eachKey in userQuestion:
      return responses[eachKey]
    
  return "Sorry, I don't know about this"  


# Take usert input
while True:
     userInput = input("Please ask your question:")
     reply = getResponseOfBot(userInput)

     print("Bot response :", reply)

     if "bye" in userInput.lower():
        break

time.sleep(1)
