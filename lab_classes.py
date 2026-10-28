class User:
    """A museum-goer's account in our little museum feed.

    >>> maya = User('maya')
    >>> maya.username, maya.followers
    ('maya', 0)
    >>> maya.follow(); maya.follow(); maya.unfollow()
    >>> maya.followers
    1
    >>> maya.unfollow(); maya.unfollow()
    >>> maya.followers
    0
    >>> theo = User('theo')
    >>> theo.followers
    0
    >>> print(maya)
    @maya
    >>> maya == User('maya'), maya == theo, maya == 'maya'
    (True, False, False)
    """

    def __init__(self, username):
        self.username = username
        self.followers = 0

    def follow(self):
        self.followers += 1

    def unfollow(self):
        # Followers can't go below zero.
        if self.followers > 0:
            self.followers -= 1

    def __str__(self):
        return '@' + self.username

    def __eq__(self, other):
        # Same username means same account; anything else is unequal.
        if not isinstance(other, User):
            return False
        return self.username == other.username

    def __hash__(self):
        return hash(self.username)


class Tweet:
    """A post about the museum trip (author is a username string).

    >>> t = Tweet('theo', "I'll be by the entrance")
    >>> t.author, t.text, t.likes
    ('theo', "I'll be by the entrance", 0)
    >>> t.like(); t.like(); t.unlike()
    >>> t.likes
    1
    >>> t.unlike(); t.unlike()
    >>> t.likes
    0
    >>> print(t)
    @theo: I'll be by the entrance
    >>> Tweet('maya', 'Statues #Art #Art #Dinos!').hashtags()
    ['Art', 'Art', 'Dinos!']
    >>> Tweet('theo', 'gift#shop is not a tag').hashtags()
    []
    >>> Tweet('theo', '# alone #').hashtags()
    ['', '']
    """

    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.likes = 0

    def like(self):
        self.likes += 1

    def unlike(self):
        # Likes can't go below zero.
        if self.likes > 0:
            self.likes -= 1

    def hashtags(self):
        # Words starting with '#', minus that first character.
        return [word[1:] for word in self.text.split() if word.startswith('#')]

    def __str__(self):
        return '@' + self.author + ': ' + self.text
