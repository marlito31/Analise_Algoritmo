from timeit import default_timer as timer
import random

greedy_weight_results = []
greedy_value_results = []
dynamic_results = []

# Classe de item para auxiliar na ordenação para as abordagens gulosas
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Abordagem gulosa, priorizando o peso
def GreedyWeightFirstKnapsack(values, weights, capacity):
    items = [Item(values[i], weights[i]) for i in range(len(values))]
    
    items.sort(key=lambda x: x.weight)
    
    total_value = 0
    total_weight = 0
    
    for item in items:
        if total_weight + item.weight <= capacity:
            total_weight += item.weight
            total_value += item.value
        else:
            continue
    
    greedy_weight_results.append(total_value)
    return total_value


# Abordagem gulosa, priorizando o valor
def GreedyValueFirstKnapsack(values, weights, capacity):
    items = [Item(values[i], weights[i]) for i in range(len(values))]

    items.sort(key=lambda x: x.value, reverse=True)
    
    total_value = 0
    total_weight = 0
    
    for item in items:
        if total_weight + item.weight <= capacity:
            total_weight += item.weight
            total_value += item.value
        else:
            continue
    
    greedy_value_results.append(total_value)
    
    return total_value

# Abordagem dinâmica
def DynamicKnapsack(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    dynamic_results.append(dp[capacity])
    
    return dp[capacity]


total = 0

print('CRIANDO OS SETS\n')

start = timer()
v2 = random.sample(range(10**2), 10**2)
v3 = random.sample(range(10**3), 10**3)
v4 = random.sample(range(10**4), 10**4)
v5 = random.sample(range(10**5), 10**5)

w2 = random.sample(range(10**2), 10**2)
w3 = random.sample(range(10**3), 10**3)
w4 = random.sample(range(10**4), 10**4)
w5 = random.sample(range(10**5), 10**5)

end = timer()
total += end - start
total_set = total
print('Criação dos Sets = {:.2f}ms\n'.format(total_set * 1000))

# Weight First
print('GULOSO - WEIGHT FIRST\n')

print("\nn = 10^2\n")
start = timer()
GreedyWeightFirstKnapsack(v2, w2, 10**2)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^3\n")
start = timer()
GreedyWeightFirstKnapsack(v3, w3, 10**3)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^4\n")
start = timer()
GreedyWeightFirstKnapsack(v4, w4, 10**4)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^5\n")
start = timer()
GreedyWeightFirstKnapsack(v5, w5, 10**5)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

total_greedy_weight_first = total - total_set

print('TEMPO TOTAL GREEDY WEIGHT FIRST = {:.2f}ms\n'.format(total_greedy_weight_first * 1000))

# Value First
print('GULOSO - VALUE FIRST\n')

print("\nn = 10^2\n")
start = timer()
GreedyValueFirstKnapsack(v2, w2, 10**2)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^3\n")
start = timer()
GreedyValueFirstKnapsack(v3, w3, 10**3)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^4\n")
start = timer()
GreedyValueFirstKnapsack(v4, w4, 10**4)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^5\n")
start = timer()
GreedyValueFirstKnapsack(v5, w5, 10**5)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

total_greedy_value_first = total - total_set

print('TEMPO TOTAL GREEDY VALUE FIRST = {:.2f}ms\n'.format(total_greedy_value_first * 1000))

# Programação Dinâmica
print('DYNAMIC PROGRAMMING\n')

print("\nn = 10^2\n")
start = timer()
DynamicKnapsack(v2, w2, 10**2)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^3\n")
start = timer()
DynamicKnapsack(v3, w3, 10**3)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^4\n")
start = timer()
DynamicKnapsack(v4, w4, 10**4)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start

print("\nn = 10^5\n")
start = timer()
DynamicKnapsack(v5, w5, 10**5)
end = timer()
print('Execução = {:.2f}ms\n'.format((end - start) * 1000))

total += end - start
total_dynamic = total - total_set

print('TEMPO TOTAL PROGRAMACAO DINAMICA = {:.2f}ms\n'.format(total_dynamic * 1000))

correct_weight = 0
correct_value = 0

print('\nCALCULANDO PRECISÃO:')
for i in range(len(dynamic_results)):
    if greedy_weight_results[i] == dynamic_results[i]:
        correct_weight+=1
    if greedy_value_results[i] == dynamic_results[i]:
        correct_value+=1

print('Greedy Weight First acertou {}% das vezes ({} de {})\n'.format((correct_weight/len(dynamic_results)) * 100, correct_weight, len(dynamic_results)))

print('Greedy Value First acertou {}% das vezes ({} de {})\n'.format((correct_value/len(dynamic_results)) * 100, correct_value, len(dynamic_results)))
