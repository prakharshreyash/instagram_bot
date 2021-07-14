from instapy import InstaPy

session = InstaPy(username = "tanay_s15", password = "prakharsingh")
session.login()

session.set_relationship_bounds(enabled = true, max_followers = 200)

session.set_do_follow(True, percentage = 10)

session.end()
