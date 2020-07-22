import praw

reddit = praw.Reddit(client_id="PUT_CLIENT_ID_HERE",
                     client_secret="PUT_CLIENT_SECRET_HERE",
                     password="PUT_PASSWORD_HERE",
                     user_agent="PUT_USER_AGENT_HERE",
                     username="PUT_USER_NAME_HERE")

def anywordcountbot():
    # Looks through all recent comments on reddit
    comments = reddit.subreddit('all').stream.comments(skip_existing=True)
    while True:
        # Checks each comment in the generated stream of new comments
        for comment in comments:
            try:
                # Checks for bot-name, username, word-to-check
                text = re.compile(r'anywordcountbot(\s)+(\w)+(\s)+(\w)+',re.I).search(comment.body).group()
            except:
                continue
            else:
                # Creates word counter
                wordcount = 0
                # Divides comment into the bot-name, username, word-to-check
                commentattributes = text.split()
                # Checks each submission title and increases count for every instance
                for submission in reddit.redditor(commentattributes[1]).submissions.new(limit=None):
                    if commentattributes[2] in submission.title:
                        for word in submission.title.split():
                            if commentattributes[2] in word:
                                wordcount += 1
                    # Checks each submission text to increase count
                    if commentattributes[2] in submission.selftext:
                        for word in submission.selftext.split():
                            if commentattributes[2] in word:
                                wordcount += 1
                # Checks each comment and increases count for every instance
                for usercomment in reddit.redditor(commentattributes[1]).comments.new(limit=None):
                    if commentattributes[2] in usercomment.body:
                        for word in usercomment.body.split():
                            if commentattributes[2] in word:
                                wordcount += 1
                # If the wordcount is one then times will not be plural ↓
                times = 'times'
                if wordcount == 1:
                    times = times[:4]
                comment.reply(f'u/{commentattributes[1].title()} has said {commentattributes[2]} {wordcount} {times}')
        sleep(10)
        print('Checking again')

anywordcountbot()
