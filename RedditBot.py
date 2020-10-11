import praw
import re
import time

reddit = praw.Reddit("bot1")

def anywordcountbot():

    '''
    anywordcountbot() handles all the work that the bot needs to
    preform without any other functions. The bot will continuously
    check reddit submissions looking for "anywordcountbot <user> <word>"
    until it has found a match. It will respond with how many times a
    person said a certain word and will keep going until the code is
    manually stopped.
    '''

    while True:
        # Checks each comment in the generated stream of new comments
        # Skips bot calls that were made before the bot was running
        for comment in reddit.subreddit('all').stream.comments(skip_existing = True):
            try:
                # Checks for bot-name, username, word-to-check
                text = re.compile(r'anywordcountbot(\s)+(\w)+(\s)+(\w)+',re.I).search(comment.body).group()
            except:
                # Goes to next submission if word doesn't show up
                continue
            wordcount = 0
            # Divides comment into the bot-name, username, word-to-check
            commentattributes = text.split()
            try:
                # Checks each submission title and increases count for every instance
                for submission in reddit.redditor(commentattributes[1]).submissions.new(limit=None):
                    if commentattributes[2] in submission.title:
                        for word in submission.title.split():
                            if commentattributes[2].lower() == word.lower():
                                wordcount += 1
                    # Checks each submission text to increase count
                    if commentattributes[2] in submission.selftext:
                        for word in submission.selftext.split():
                            if commentattributes[2].lower() == word.lower():
                                wordcount += 1
                # Checks each comment and increases count for every instance
                for usercomment in reddit.redditor(commentattributes[1]).comments.new(limit=None):
                    if commentattributes[2] in usercomment.body:
                        for word in usercomment.body.split():
                            if commentattributes[2].lower() == word.lower():
                                wordcount += 1
            except:
                comment.reply(f'{commentattributes[1]} is not a real Reddit user!\n\nMake sure to omit the u/ and follow this format (letter case and spacing do not matter):\n\nanywordcountbot usertocheck  wordtocheck')
                continue
            # If the wordcount is one, times will not be plural ↓
            times = 'times'
            if wordcount == 1:
                times = times[:4]
            comment.reply(f'u/{commentattributes[1].title()} has said {commentattributes[2]} {wordcount} {times}')
            time.sleep(3)

anywordcountbot()
