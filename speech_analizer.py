'''
Alexander J. Padin
Midterm 1, problem 5

This python script will analize two given speeches and will return the longest passage in common.
This solution was develop using Dynamic programming.
'''

SPEECH_1 = "I stand here today humbled by the task before us, grateful for the trust you have bestowed, mindful of the sacrifices borne by our ancestors. I thank President Bush for his service to our nation, as well as the generosity and cooperation he has shown throughout this transition. Forty-four Americans have now taken the presidential oath. The words have been spoken during rising tides of prosperity and the still waters of peace. Yet, every so often the oath is taken amidst gathering clouds and raging storms. At these moments, America has carried on not simply because of the skill or vision of those in high office, but because We the People have remained faithful to the ideals of our forbearers, and true to our founding documents. So it has been. So it must be with this generation of Americans. That we are in the midst of crisis is now well understood. Our nation is at war, against a far-reaching network of violence and hatred. Our economy is badly weakened, a consequence of greed and irresponsibility on the part of some, but also our collective failure to make hard choices and prepare the nation for a new age. Homes have been lost; jobs shed; businesses shuttered. Our health care is too costly; our schools fail too many; and each day brings further evidence that the ways we use energy strengthen our adversaries and threaten our planet."
SPEECH_2 = "Thank you. Thank you very much. It is an honor as always, my fellow Republicans, to join you at our national convention and add my voice to yours as we nominate the next president of the United States, my friend, Governor Mitt Romney. I had hopes once of addressing under different circumstances, but our fellow Americans had another plan four years ago and I accept their decision. I thank President Bush for his service to our nation. I am conscious of the debt I owe America.  And I thank you for the honor. When we nominate Mitt Romney, we do so with a greater purpose than winning an advantage for our party.  We charged him with the care of by a higher cause.  His election represents the best hopes for our country, and the world. It is said that this election will turn on domestic and economic issues.  But what Mitt Romney knows, and what we know is the success at home also depends on our leadership in the world.  It is our willingness to shape world events for the better that has kept a safe, increased our prosperity, preserved our liberty and transformed human history. At our best, America has led.  We have led by our example as a shining city on a hill.  We have lead in the direction of patriots from both parties.  We have led shoulder to shoulder with steadfast friends and allies."

s1 = SPEECH_1.split()
s2 = SPEECH_2.split()
s1_len = len(s1)
s2_len = len(s2)

def maxime(a, b):
	if a > b:
		return a
	else:
		return b

def check_speeches(s1, s2, s1_len, s2_len):
	table = [[0 for x in xrange(s2_len + 1)] for x in xrange(s1_len + 1)] 
	s_length = 0

	i = 0
	while i <= s1_len:
		j = 0
		while  j <= s2_len:
			if i == 0 or j == 0:
				pass
			elif s1[i - 1] == s2[j - 1]:
				table[i][j] = (table[i - 1][j - 1]) + 1
 				s_length = maxime(s_length, table[i][j])
			else:
				pass
			j += 1
		i += 1
	return s_length

print "Longest common substring of:", check_speeches(s1, s2, s1_len, s2_len)

