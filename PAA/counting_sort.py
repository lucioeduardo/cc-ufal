import os, psutil
import time
import numpy as np
from memory_profiler import memory_usage
import gc

process = psutil.Process(os.getpid())

op_count = 0

def counting_sort(arr, k):
    global op_count
    n = len(arr)

    count = (k+1)*[0]; #op_count += k+1
    output = n*[0]; #op_count += n

    for i in arr:
      op_count+=1
      count[i] += 1

    for i in range(1,k+1):
      op_count+=1
      count[i] += count[i-1]

    for i in range(n-1,-1,-1):
      output[count[arr[i]]-1] = arr[i]
      count[arr[i]] -= 1

      op_count+=2
    
    return output


def test(n, k, arr):
  global op_count
  op_count = 0

  start = time.time()
  mem_usage = memory_usage((counting_sort, [arr, max(arr)]))
  end = time.time()

  #print('N=%d K=%d:'%(n,k))
  # print('  Número de operações:', op_count)
  # print('  Número de comparações: 0')
  # print('  Uso de memória: %.2f MB'%max(mem_usage))
  # print('  Tempo em execução: %.6lfs'%(end-start))

  return {
    'Número de operações': op_count,
    'Número de comparações': 0,
    'Uso de memória': f'%.2f MB'%max(mem_usage),
    'Tempo de execução': f'%.2fs'%(end-start),
  }

def test_incr(arr,n,k):
  arr.sort()
  return test(n,k,arr)


def test_decr(arr,n,k):
  arr[::-1].sort()
  return test(n,k,arr)


n_list = [10**4, 10**5, 10**6, 10**7]
k_list = [10**2, 10**4, 10**6]


res = []

for n in n_list:
  for k in k_list:
    arr = np.random.randint(k, size=n)

    # print("\n\n",n,k)

    info = {'N':n, 'K':k, 'Método': 'Aleatório'}

    # print('Random:')

    info['Resultado'] = test(n,k,arr)

    res.append(info)

    # print('\nOrdem crescente:')
    info = {'N':n, 'K':k, 'Método': 'Crescente'}
    info['Resultado'] = test_incr(arr,n,k)

    res.append(info)

    # print('\nOrdem decrescente:')
    info = {'N':n, 'K':k, 'Método': 'Decrescente'}
    info['Resultado'] = test_decr(arr,n,k)
    res.append(info)

print(res)