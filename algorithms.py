import random
import string
import time
import matplotlib.pyplot as plt
from collections import OrderedDict

CHARS = list(string.ascii_uppercase +
             string.ascii_lowercase +
             string.digits)
# -----------------------------------------------------------------------------


def format_password(password):
    assert password.isalnum()
    return [x for x in password]

# -----------------------------------------------------------------------------


def run_brute_force(fpassword):
    '''
    Brute force algorithm to "crack" password - generate random strings until
    password is generated
    '''
    start_time = time.time()

    starting_guess = ''.join(random.choice(CHARS)
                             for x in range(len(fpassword)))
    guess = [x for x in starting_guess]

    num_guesses = 0
    while guess != fpassword:
        guess = list(''.join(random.choice(CHARS)
                             for x in range(len(fpassword))))
        num_guesses += 1

    end_time = time.time()
    '''
    print('Brute force algorithm\n')
    print('Number attempts: %s' % num_guesses)
    print('Time: %.3fs\n' % (end_time - start_time))
    '''
    return num_guesses, end_time - start_time

# -----------------------------------------------------------------------------


def measure_fitness(attempt, original):
    '''
    fitness = number of matches betwwen attempt & original @ same index
    '''
    assert type(attempt) == list and type(original) == list
    return len([i for i, j in zip(attempt, original) if i == j])

# -----------------------------------------------------------------------------


def run_genetic_algorithm(fpassword):
    '''
    Utilize hill-climbing algorithm to "crack" password given fitness metric
    of string similarity
    '''
    start_time = time.time()

    # start off with random permutation of CHARS
    starting_guess = ''.join(random.choice(CHARS)
                             for x in range(len(fpassword)))
    guess = [x for x in starting_guess]
    fitness = measure_fitness(guess, fpassword)

    num_guesses = 0
    # while guess is incorrect, randomly change one char in guess and compare
    # fitness scores. The more fit guess survives
    while guess != fpassword:
        new_guess = guess[:]  # use slice since python shallow copies lists
        mutation_location = random.randint(0, len(guess) - 1)
        new_guess[mutation_location] = random.choice(CHARS)
        new_fitness = measure_fitness(new_guess, fpassword)
        num_guesses += 1

        if new_fitness > fitness:
            guess = new_guess
            fitness = new_fitness

    end_time = time.time()

    '''
    print('Genetic algorithm\n')
    print('Number attempts: %s' % num_guesses)
    print('Time: %.3fs\n\n' % (end_time - start_time))
    '''
    return num_guesses, end_time - start_time

# -----------------------------------------------------------------------------


def run_simulations(n_iter=5):
    '''
    simulates cracking passwords for passwords up to n_iter chars using
    brute force & hill climbing algorithms. 

    Returns list with times of brute force/hill climbing
    '''
    print('Password cracking in progress...')
    brute_data = OrderedDict()
    genetic_data = OrderedDict()

    for len_pw in range(1, n_iter):
        pw = ''.join(random.choice(CHARS) for x in range(len_pw))
        password = format_password(pw)
        b_n, btime = run_brute_force(password)
        gen_n, gtime = run_genetic_algorithm(password)

        brute_data[b_n] = btime
        genetic_data[gen_n] = gtime

    # dict where key=time for brute force and value=genetic time
    time_dict = OrderedDict(zip(brute_data.values(), genetic_data.values()))

    relative_time = []
    for k, v in time_dict.items():
        relative_time.append(k/v)

    return relative_time

# -----------------------------------------------------------------------------


def plot_relative_times(time_list):
    x = range(1, len(time_list) + 1)
    print(time_list)

    fig, ax = plt.subplots()
    ax.bar(x, height=time_list, log=True)
    plt.xticks(x, [str(i) for i in x])

    for i, v in enumerate(time_list):
        if i == 0:
            # to prevent rounding to 0.0x
            plt.text(i+0.8, v, str(round(v, 2)) + str('x'), size=16,
                     color='black', fontweight='bold')
        elif i == 1:
            # to prevent rounding to 0.0x
            plt.text(i+0.70, v, str(round(v, 2)) + str('x'), size=16,
                     color='black', fontweight='bold')
        else:
            plt.text(i+0.65, v, str(round(v)) + str('x'), size=16,
                     color='black', fontweight='bold')

    plt.xlabel('Password length (chars)')
    plt.ylabel('Brute force time/Genetic algorithm time')
    plt.show()


# -----------------------------------------------------------------------------

if __name__ == '__main__':
    time_data = run_simulations(5)
    plot_relative_times(time_data)

# -----------------------------------------------------------------------------
