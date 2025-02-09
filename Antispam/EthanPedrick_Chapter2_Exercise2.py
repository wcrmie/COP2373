# This program accepts an input of an email, and scores it on how likely it is to be a scam based on keywords.

# Make list
KEYWORDS = ["prize", "giveaway", "urgent", "banking", "invoice", "account upgrade", "inheritance", "verify", "declined", "termination", "locked", "gift card", "refund", "update", "tinyurl", "bit.ly", "expire", "limited", "offer", "customer"
                "client", "fee", "transfer", "fund", "unusual", "password", "official", "lottery", "sweepstakes", "raffle", "compromised"]

def main():

    # Get user input
    potential_scam = input("Copy (CTRL+C) and Paste (CTRL+V) an email here, then press enter to receive a score for how likely it is to be a scam. ").lower()
    score = scan(potential_scam)

    # Use the score to choose which message to send to the user; if there are more than 4 of the keywords in the email, it is probably a scam.
    if (score > 4):
        print(f"This email has a scam score of {score}, and is likely a scam. ")

    else:
        print(f"This email has a scam score of {score}, and is likely not a scam, but be careful regardless! ")

def scan(mail):

    # set zero variable
    score = 0

    # loop through the constant list
    for x in KEYWORDS:

        # add the count of any given entry to the score
        score += mail.count(x)
    return score

main()