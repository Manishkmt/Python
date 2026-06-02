
#! Write a function that takes a string and returns the count of vowels and consonants Separately

def func(userInput):

  vowels = "aeiouAEIOU"

  countVowel = 0
  countConsonants = 0

  for eachChar in userInput:
    if(eachChar.isalpha()):
      if(eachChar in vowels):
        countVowel += 1
      else:
        countConsonants +=1
  return countVowel,countConsonants

vowel, consonants= func("Manish Kuamwat")

print(f"vowel is {vowel} and consonants is {consonants}")