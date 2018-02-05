class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                               "I don't want to get sued",
                               "So I'll stop right there"])

on_and_on = Song(["I was born under water",
                  "With three dollars and six dimes",
                  "Yeah you may laugh",
                  "Because you did not do the math"])
happy_bday.sing_me_a_song()
on_and_on.sing_me_a_song()
