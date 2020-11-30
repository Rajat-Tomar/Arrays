if __name__ == '__main__':
	n = int(input())

	arr = list(map(int, input().rstrip().split()))
	m = map(str, arr[::-1])
	print(" ".join(m))