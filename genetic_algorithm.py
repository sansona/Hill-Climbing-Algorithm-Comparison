import random
import string
import time


def measure_fitness(attempt, original):
    '''
    fitness = number of matches betwwen attempt & original @ same index
    '''
    assert type(attempt) == list and type(original) == list
    return len([i for i, j in zip(attempt, original) if i == j])


def run_genetic_algorithm(password):
    '''
    Utilize hill-climbing algorithm to "crack" password given fitness metric
    of string similarity
    '''
    assert password.isalnum()
    password_as_list = [x for x in password]

    chars = list(string.ascii_uppercase +
                 string.ascii_lowercase +
                 string.digits)

    start_time = time.time()

    # start off with random permutation of chars
    starting_guess = ''.join(random.choice(chars) for x in range(len(password)))
    guess = [x for x in starting_guess]
    fitness = measure_fitness(guess, password_as_list)

    num_guesses = 0
    # while guess is incorrect, randomly change one char in guess and compare
    # fitness scores. The more fit guess survives
    while guess != password_as_list:
        new_guess = guess[:]  # use slice since python shallow copies lists
        mutation_location = random.randint(0, len(guess) - 1)
        new_guess[mutation_location] = random.choice(chars)
        new_fitness = measure_fitness(new_guess, password_as_list)
        num_guesses += 1

        if new_fitness > fitness:
            guess = new_guess
            fitness = new_fitness

    end_time = time.time()

    print('Password: %s' % ''.join(guess))
    print('Number attempts: %s' % num_guesses)
    print('Time: %.3fs' % (end_time - start_time))


run_genetic_algorithm('rs2b324nh23ne4hnh23bpnnh23nefwt32423vtstsd34td34d23')
