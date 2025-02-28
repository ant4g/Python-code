import random
import re
import string

import requests
from bs4 import BeautifulSoup
import click


def get_html(URL):
    site = requests.get(URL)
    err = site.status_code
    if err != 200:
        print("Error occured !")
        exit(1)

    return site.content.decode()


def get_text(URL):
    soup = BeautifulSoup(get_html(URL), 'html.parser')
    st = soup.get_text()

    return st


def count(word_list, min_length):
    list = {}
    for word in word_list:
        if len(word) < min_length:
            continue
        elif word not in list:
            list[word] = 1
        else:
            list[word] += 1

    return list


def common(list):
    sorted_list = sorted(list.items(), key=lambda item: item[1], reverse=True)

    print("Najczęściej występujące słowa to: ")
    return sorted_list


def get_all_w(url):
    raw_text = get_text(url)
    words = re.findall(r'\w+', raw_text)

    return words


def sorted_words(words, min_length):
    occurence = count(words, min_length)
    sort_occ = common(occurence)

    return sort_occ


def pass_mutations(base):
    mutations = []

    mutations.append(base.capitalize())
    mutations.append(base.upper())
    mutations.append(base.lower())

    #year:
    current_year = 2025
    for year in [current_year, current_year - 1, current_year - 2]:
        mutations.append(base + str(year))
        mutations.append(str(year) + base)

    #symbols:
    for s in ['!', '?', '.', '_', '@', '#', '$', '&']:
        mutations.append(base + str(s))
        mutations.append(str(s) + base)

    #numbers:
    for n in ['123', '456', '678', '901', '2020']:
        mutations.append(base + str(n))
        mutations.append(str(n) + base)

    random_s = ''.join(random.choices(string.ascii_lowercase + string.digits + string.punctuation, k=3))
    mutations.append(base + random_s)

    return mutations


@click.command()
@click.option('--url', '-u', prompt='Web URL', help='URL of webpage to extract from.')
@click.option('--length', '-l', default=0, help='Minimum word length ( default: 0, no limits.')
@click.option('--output', '-o', default='wyjście.txt', help='Place you want to save output of this script')
def main(url, length, output):
    mutations = pass_mutations("summer")

    print(get_text(url))
    all_words = get_all_w(url)

    st = sorted_words(all_words, length)
    with open(f'{output}', 'w') as f:
        f.write("Najczęściej występujące słowa na stronie:\n\n")
        for i in range(10):
            f.write(st[i][0] + "\n")
            print(st[i][0])

        f.write("Passwords: \n")
        for m in mutations:
            f.write(m + '\n')


if __name__ == '__main__':
    main()
