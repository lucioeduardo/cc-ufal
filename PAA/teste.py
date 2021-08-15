import time

start = time.time()

arr = [5]*10**6

count=0

for i in range(10**8):
  arr[10525] += 1
  count = arr[10525]

end = time.time()

print(end-start)