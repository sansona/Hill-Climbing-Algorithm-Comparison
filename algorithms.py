import random
import string
import time

# ------------------------------------------------------------------------------


def format_password(password):
    assert password.isalnum()
    return [x for x in password]

# ------------------------------------------------------------------------------


def run_brute_force(fpassword):
    '''
    Brute force algorithm to "crack" password- generate random strings until
    password is generated
    '''
    chars = list(string.ascii_uppercase +
                 string.ascii_lowercase +
                 string.digits)

    start_time = time.time()

    starting_guess = ''.join(random.choice(chars)
                             for x in range(len(fpassword)))
    guess = [x for x in starting_guess]

    num_guesses = 0
    while guess != fpassword:
        guess = list(''.join(random.choice(chars)
                             for x in range(len(fpassword))))
        num_guesses += 1

    end_time = time.time()

    print('Brute force algorithm\n')
    print('Number attempts: %s' % num_guesses)
    print('Time: %.3fs\n\n' % (end_time - start_time))

# ------------------------------------------------------------------------------


def measure_fitness(attempt, original):
    '''
    fitness = number of matches betwwen attempt & original @ same index
    '''
    assert type(attempt) == list and type(original) == list
    return len([i for i, j in zip(attempt, original) if i == j])

# ------------------------------------------------------------------------------


def run_genetic_algorithm(fpassword):
    '''
    Utilize hill-climbing algorithm to "crack" password given fitness metric
    of string similarity
    '''

    chars = list(string.ascii_uppercase +
                 string.ascii_lowercase +
                 string.digits)

    start_time = time.time()

    # start off with random permutation of chars
    starting_guess = ''.join(random.choice(chars)
                             for x in range(len(fpassword)))
    guess = [x for x in starting_guess]
    fitness = measure_fitness(guess, fpassword)

    num_guesses = 0
    # while guess is incorrect, randomly change one char in guess and compare
    # fitness scores. The more fit guess survives
    while guess != fpassword:
        new_guess = guess[:]  # use slice since python shallow copies lists
        mutation_location = random.randint(0, len(guess) - 1)
        new_guess[mutation_location] = random.choice(chars)
        new_fitness = measure_fitness(new_guess, fpassword)
        num_guesses += 1

        if new_fitness > fitness:
            guess = new_guess
            fitness = new_fitness

    end_time = time.time()

    print('Genetic algorithm\n')
    print('Number attempts: %s' % num_guesses)
    print('Time: %.3fs' % (end_time - start_time))

# ------------------------------------------------------------------------------


def main():
    pw = 'sr2'
    password = format_password(pw)
    run_brute_force(password)
    run_genetic_algorithm(password)

# ------------------------------------------------------------------------------


if __name__ == '__main__':
    main()

# ------------------------------------------------------------------------------
