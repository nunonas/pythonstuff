class Album:
	'class of music albums'
	albumCount = 0

	def __init__(self, name, artist):
		self.name = name
		self.artist = artist
		Album.albumCount += 1
	
	def displayNumAlbums(self):
		print "The total number of albums in the database is %d" % Album.albumCount

	def displayAlbum(self):
		print "The album in question is:", self.name, "from", self.artist


album1 = Album("Teens of Denial", "Car Seat Headrest")
album1.displayAlbum()

print Album.__doc__
#print Album.__dict__
