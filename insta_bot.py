from instapy import InstaPy

session = InstaPy(username = "<your username>", password = "<your password>")
session.login()

session.set_relationship_bounds(enabled = true, max_followers = 200)

session.set_do_follow(True, percentage = 100)

session.end()
