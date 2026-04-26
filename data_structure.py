import random


for i in range(10):
    x = random.randint(5,10)
    print("random_num: ", x)



t = [1,2,3]
print("--------")
print(random.choice(t))


hist = {"a": 2, "b": 1, "c": 5, "d": 7, "e": 3}

def choose_from_hist(histogram):
    total_frequency = 0
    for i in histogram:
        total_frequency += histogram[i]
    list_values = list(histogram.keys())
    random_choice = random.choice(list_values)
    return "'" + str(random_choice) + "'" + " with probability of " + str(histogram[random_choice]) +  "/" + str(total_frequency)
    

print("random_choice_from_histogram -> ", choose_from_hist(hist))

def random_word(hist):
    t = []
    for (word, freq) in hist.items():
        t.extend([word] * freq)
    return random.choice(t)



print("random_word: ", random_word(hist))

