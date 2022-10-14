import random as rand

chance_rain = 0.5
chance_sprinkler = 0.5
chance_other = 0.0

# Smaller sample sizes were quite noisy
num_samples = 1_000_000


class Sample:
    def __init__(self):
        self.rain = 1 if (rand.random() <= chance_rain) else 0
        self.sprinkler = 1 if (rand.random() <= chance_sprinkler) else 0
        self.wet = 1 if (self.rain or self.sprinkler or rand.random() <= chance_other) else 0

    def __str__(self):
        return f"rain {self.rain} | sprinkle {self.sprinkler} | wet {self.wet}"


# All the following analysis could be done with generators and tracking the number of times traits coexist...
# But I think this structure is nice as it allows for easy building off from
samples = []

for i in range(num_samples):
    samples.append(Sample())


# samples_var is the sublist of samples where var is true
# samples_nvar is the sublist of samples where var is false
samples_r = [sample for sample in samples if sample.rain == 1]
samples_s = [sample for sample in samples if sample.sprinkler == 1]
samples_rns = [sample for sample in samples_r if sample.sprinkler == 0]
samples_rs = [sample for sample in samples_r if sample.sprinkler == 1]

print(f"Probability rain: {len(samples_r)/num_samples}")
print(f"Probability rain given no sprinklers: {len(samples_rns)/len(samples_s)}")
print(f"Probability rain given sprinklers: {len(samples_rs)/len(samples_s)}")
print(f"Rain and sprinklers independent generally\n")

samples_w = [sample for sample in samples if sample.wet == 1]
samples_rw = [sample for sample in samples_w if sample.rain == 1]
samples_sw = [sample for sample in samples_w if sample.sprinkler == 1]
samples_rsw = [sample for sample in samples_sw if sample.rain == 1]
samples_nsw = [sample for sample in samples_w if sample.sprinkler == 0]
samples_rnsw = [sample for sample in samples_nsw if sample.rain == 1]


print(f"Probability rain given wet: {len(samples_rw)/len(samples_w)}")
print(f"Probability rain given wet and sprinkler: {len(samples_rsw)/len(samples_sw)}")
print(f"Probability rain given wet and no sprinkler: {len(samples_rnsw)/len(samples_nsw)}")
print(f"Rain and sprinklers dependent given wet")
