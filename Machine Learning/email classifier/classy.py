# Simple Email class
class Email:
    def __init__(self):
        self.body = "empty"
        self.label = None


emails = []  # list of Emails
pY = 1  # pY means Y=1 in other words the probability that the email is a spam
# pNotY means Y=0 (1-pY) in other words the probability that the email is not a spam
pNotY = 1
# bag of spam map (please see bag model in Naive Bayes to understand its role)
bagSpam = dict()
# bag of non spam map (please see bag model in Naive Bayes to understand its role)
bagNonSpam = dict()
bagSpamTotal = 0
bagNonSpamTotal = 0

# Training the machine from exisiting dataset of emails that we have previously labeled as spam or no spam
# Mathematically speaking we are going to achieve two things through this function:
# a. Calculate P(Y); Y takes two values either 1 in case of spam or 0 otherwise.
# b. Create enough material to calculate P(X_i) later; X_i is the number of occurence of the ith word of the document


def train(trainData):
    numSpam = 0
    total = 0
    for email in trainData:
        if email.label == True:
            numSpam += 1
        total += 1
        # We use this email's data to increase the machine's knowledge
        proccessEmail(email.body, email.label)

    global pY
    global pNotY
    pY = numSpam / float(total)
    pNotY = 1 - pY

# Proccessing the email in a way we make the machine learn of the way the words' frequnecies are distributed in a spam or non spam email


def proccessEmail(body, label):
    global bagSpamTotal
    global bagNonSpamTotal
    for word in body:
        if label == True:
            if word in bagSpam:
                bagSpam[word] = bagSpam.get(word, 0) + 1
                bagSpamTotal += 1
            else:
                bagSpam[word] = 1
                bagSpamTotal += 1
        else:
            if word in bagSpam:
                bagNonSpam[word] = bagNonSpam.get(word, 0) + 1
                bagNonSpamTotal += 1
            else:
                bagNonSpam[word] = 1
                bagNonSpamTotal += 1

# How frequent that word shows up knowing that the email is spam or non spam
# Mathematically speaking we are going to calculate P(X_i | Y)


def conditionalWord(word, label):
    if label == True:
        if word in bagSpam:
            return float(bagSpam[word]) / float(bagSpamTotal)
        else:
            return 1

    if word in bagNonSpam:
        return float(bagNonSpam[word]) / float(bagNonSpamTotal)
    else:
        return 1

# This function basically applies the conditionalWord logic to the whole email's body

def conditionalBody(body, label):
    conditionalBody = 1
    for word in body:
        conditionalBody *= conditionalWord(word, label)

    return conditionalBody

#The touch down function! 

def classifyEmail(email):
    isSpam = pY * conditionalBody(email.body, True)
    isNotSpam = pNotY * conditionalBody(email.body, False)
    return 1 if isSpam > isNotSpam else 0


import os
#Read an already declared spam emails dataset
for filename in os.listdir(os.getcwd() + "/data/TrainSpam/"):
    file = open("data/TrainSpam/" + filename, "r")
    email = Email()
    email.body = file.read()
    email.body = email.body.split()
    email.label = True
    emails.append(email)

#Read an already declared non spam (ham) emails dataset
for filename in os.listdir(os.getcwd() + "/data/TrainHam/"):
    file = open("data/TrainHam/" + filename, "r")
    email = Email()
    email.body = file.read()
    email.body = email.body.split()
    email.label = False
    emails.append(email)

#Train using the dataset
train(emails)

spamFlagged = 0
spamNonFlagged = 0
totalTest = 0

for filename in os.listdir(os.getcwd() + "/data/TestSpam/"):
    file = open("data/TestSpam/" + filename, "r")
    email = Email()
    email.body = file.read()
    email.body = email.body.split()
    if classifyEmail(email) == 1:
        spamFlagged += 1
    else:
        spamNonFlagged += 1
    totalTest += 1

print(spamFlagged)
print(spamNonFlagged)
print(totalTest)
