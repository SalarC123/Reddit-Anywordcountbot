# Reddit-Bot

--- Anywordcountbot for Reddit ---

Type in the comment section of any reddit submission to call bot --> EXAMPLE -->    anywordcountbot   spez   reddit

'u/' is not needed for usernames and spaces between each word are not important

Bot will check through the submission and comment history to see how many times that the specified user has said the specified word

Bot checks the new stream of comments every 10 seconds to look for bot calls


Make sure to put your own information where it says ---> reddit = praw.Reddit(client_id = 'PUT_CLIENT_ID_HERE',
                                                                              client_secret = 'PUT_CLIENT_SECRET_HERE',
                                                                              password = 'PUT_PASSWORD_HERE',
                                                                              user_agent = 'PUT_USER_AGENT_HERE',
                                                                              username = 'PUT_USER_NAME_HERE')

client id and client secret will show up once you make a reddit developer application on this page     
https://www.reddit.com/prefs/apps

put the username and password of your reddit account and write your own user-agent that describes the app ---> EXAMPLE ----> anywordcountbot:v1.1 by 1Test2Bot3
