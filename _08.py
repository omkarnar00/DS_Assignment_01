def are_brackets_balanced(s):
	stack = []
	for ch in s:
		if ch in ('(', '{', '['):
			stack.append(ch)
		else:
			if stack and ((stack[-1] == '(' and ch == ')') or
						(stack[-1] == '{' and ch == '}') or
						(stack[-1] == '[' and ch == ']')):
				stack.pop()
			else:
				return False
	return not stack

expr = "{()}[]"

if are_brackets_balanced(expr):
	print("Balanced")
else:
	print("Not Balanced")
