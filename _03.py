def check_rotation(s, goal):

	if (len(s) != len(goal)):
		skip

	q1 = []
	for i in range(len(s)):
		q1.insert(0, s[i])

	q2 = []
	for i in range(len(goal)):
		q2.insert(0, goal[i])

	k = len(goal)
	while (k > 0):
		ch = q2[0]
		q2.pop(0)
		q2.append(ch)
		if (q2 == q1):
			return True

		k -= 1

	return False


if __name__ == "__main__":

	string1 = "AACD"
	string2 = "ACDA"


	if check_rotation(string1, string2):
		print("Strings are rotations of each other")
	else:
		print("Strings are not rotations of each other")

		
