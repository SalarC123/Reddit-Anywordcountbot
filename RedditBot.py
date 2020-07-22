import praw

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     password="",
                     user_agent="",
                     username="")

    # Looks through all recent comments on reddit
        comments = reddit.subreddit('all').stream.comments(skip_existing=True)
        while True:
            # Checks each comment in the generated stream of new comments
            for comment in comments:
                try:
                    # Checks for bot-name, username, word-to-check
                    text = re.compile(r'anywordcountbot(\s)+u/(\w)+(\s)+(\w)+',re.I).search(comment.body).group()
                except:
                    continue
                else:
                    # Creates word counter
                    wordcount = 0
                    # Divides comment into the bot-name, username, word-to-check
                    commentattributes = text.split()
                    # Checks each submission and increases count for every instance
                    for submission in reddit.redditor(commentattributes[1][2:]).stream.submissions(skip_existing=True):
                        if commentattributes[2] in submission:
                            wordcount += 1
                    # # Checks each comment and increases count for every instance
                    for usercomment in reddit.redditor(commentattributes[1][2:]).stream.submissions(skip_existing=True):
                        if commentattributes[2] in usercomment:
                            wordcount += 1
                    comment.reply(f'{commentattributes[1]} has said {commentattributes[2]} {wordcount} times')
            sleep(10)
            print('Checking again')
