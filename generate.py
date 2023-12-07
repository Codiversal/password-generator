import string
import itertools
import argparse
import sys
from tqdm import tqdm

def generate_passwords_sequence(max_length):
    def language_selection(language):
        try:
            if language == 'latin':
                characters = string.ascii_letters + string.digits + string.punctuation
                return characters
            if language == 'greek':
                greek_characters = 'αάΑΆβΒγΓδΔεέΕΈζΖηήΗΉθΘιίΙΊκΚλΛμΜνΝξΞοόΟΌπΠρΡσΣτΤυύΥΎφΦχΧψΨωώΩΏ'
                characters = greek_characters + string.digits + string.punctuation
                return characters
            if language == 'combine':
                greek_characters = 'αάΑΆβΒγΓδΔεέΕΈζΖηήΗΉθΘιίΙΊκΚλΛμΜνΝξΞοόΟΌπΠρΡσΣτΤυύΥΎφΦχΧψΨωώΩΏ'
                characters = string.ascii_letters + greek_characters + string.digits + string.punctuation
                return characters
            else:
                raise ValueError("Wrong language! Use '-l greek' or '-l combine' as an argument! Type '--help' for more information!")
        except ValueError as e:
            print(e)
            sys.exit()

    if custom_password:
        characters = custom_password
    else:
        characters = language_selection(language)

    passwords_list = []
    total_combinations = sum(len(characters) ** length for length in range(min_password_length, max_password_length + 1))

    with tqdm(total=total_combinations, desc="Generating passwords", unit="combination") as pbar:
        for length in range(min_password_length, max_password_length + 1):
            combinations = itertools.product(characters, repeat=length)
            for combination in combinations:
                passwords_list.append(''.join(combination))
                pbar.update(1)

    return passwords_list

def export_to_txt(passwords, output_file):
    total_passwords = len(passwords)
    with tqdm(total=total_passwords, desc="Exporting passwords to txt", unit="password") as pbar:
        with open(output_file, 'w') as file:
            for password in passwords:
                file.write(password + '\n')
                pbar.update(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a password wordlist using the following arguments.')
    parser.add_argument('-m', '--max_length', type=int, default=1, help='Define the maximum length of characters in your wordlist. Default is 1')
    parser.add_argument('-n', '--min_length', type=int, default=1, help='Define the minimum length of characters in your wordlist. Default is 1')
    parser.add_argument('-o', '--output_file', default='wordlist.txt', help='Change the name of the output file. Default name is wordlist.txt')
    parser.add_argument('-c', '--custom_char', help='Define custom set of characters that you want to generate.')
    parser.add_argument('-l', '--language', default='latin', help="Default language is Latin. Write '-l greek' for Greek characters and '-l combine' for a Latin and Greek combination of characters.")
    args = parser.parse_args()

    max_password_length = args.max_length
    output_file = args.output_file
    min_password_length = args.min_length
    custom_password = args.custom_char
    language = args.language

    passwords_list = generate_passwords_sequence(max_password_length)

    export_to_txt(passwords_list, output_file)

    print(f"{len(passwords_list)} passwords generated and exported to {output_file}.")
