from lab_classes import User, Tweet


def build_feed():
    # Community: friends meeting up for a trip to the museum.
    maya = User('maya')
    theo = User('theo')
    users = [maya, theo]

    posts = [
        Tweet('maya', 'Museum day! Tickets booked for 10am. #MuseumDay #Art'),
        Tweet('theo', "Find me by the statue, just kidding, everything is a statue. "
                      "I'll be by the entrance. #Lost"),
        Tweet('maya', 'Found you! Heading to the dinosaur wing next. #Dinos'),
        Tweet('theo', 'The gift shop is the real exhibit.'),
    ]

    # A small story: the group follows along, one follow is a mis-click,
    # and Theo's joke gets liked (with one accidental like undone).
    maya.follow()
    maya.follow()
    maya.follow()
    maya.unfollow()    # someone dropped out of the trip
    theo.follow()

    posts[1].like()
    posts[1].like()
    posts[1].like()
    posts[1].unlike()  # tapped it twice by accident
    posts[2].like()

    return users, posts


def main():
    users, posts = build_feed()

    print('=== Museum Crew ===')
    for user in users:
        print(user)
        print('  followers:', user.followers)

    print('=== Museum Feed ===')
    for post in posts:
        print(post)
        print('  likes:', post.likes)
        print('  hashtags:', post.hashtags())


if __name__ == '__main__':
    main()