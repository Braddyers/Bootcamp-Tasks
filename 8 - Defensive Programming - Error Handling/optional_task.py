#This is a very simple program that will help a content moderator sort through a user comments section for a website that requires users to register an account.
#To help the website succeed, certain useful posts and their threads need to be promoted and some posts that are considered not useful should addressed by the moderator.
#The moderater identifies and inputs whether a user's comment has a negative, neutral or positive sentiment:
    #Negative sentiment posts include anything that falls under: bullying/dicrimination, words that are violent in nature or are spam.
    #Neutral sentiment posts that are neutral in nature and are objective.
    #Positive sentiment posts include any: constructive assistance, expressions of joy or appreciation.
    
#An old user has had a registered account for 30 days or more. They are generally better informed and can be more readily 'trusted'. 
    #Old user's positive and neutral posts should be promoted and the associated thread reposted.
#A new user has had a registered account for 3 days or less. They are generally less informed and CANNOT BE TRUSTED according to the website owner.
    #New user's negative posts should be removed.

#The program should output and 'flag' comments accordingly after input so that the moderator can then either promote or remove comment. 

#Logic error scenario:
    #User by the name of Lord_Farquaad posted a comment with negative sentiment. Lord_Farquaad's account is 42 days old, but the moderator didn't see that.
    #The moderator inputs "negatiive" instead of "negative".
    #The program runs and compiles.
    #"Should be promoted, thread should be reposted."
    #This leads to the moderator accidentally promoting the negative post and it's thread.
    #Only positive and neutral posts of old users should be promoted, not negative ones.
    #Logic error.

#Initialise variables
account_age_in_days = "42"                                                      #"42" is supposed to be an integer, cannot concatentate two different data types in line 29 (runtime error).
sentiment = (input("Type of sentiment (positive, neutral or negative): "))      #Extra parenthesis (syntax error).

#Old user's neutral and positive posts that should be promoted
if account_age_in_days >= 30 and sentiment != "negative":                       #!= "negative" accounts for ANY input. So if "Gumdrop buttons" was typed in, the program will still run and compile and output: "Should be promoted, thread should be reposted.". 
    print("Should be promoted, thread should be reposted.")

#New user's negative posts should be removed
if account_age_in_days < 3 and sentiment == "negative":
    print("Comment should be removed.")

#Possible solution:
#To specify that there can only be three inputs of sentiments entered in a options, then "!= negative" is inclusive of "positive" and "neutral" sentiments only.
#Maybe a drop down menu on the front end to only have to click between three options.