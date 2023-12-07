import string
import itertools
import argparse
import sys

def generate_passwords_sequence(max_length):
    def language_selection(language):
        try:
            if language == 'latin':
                #If you want to create a latin wordlist.
                characters = string.ascii_letters + string.digits + string.punctuation
                return characters
            if language == 'greek':
                #Use the Greek letters to generate passwords
                greek_characters = 'αάΑΆβΒγΓδΔεέΕΈζΖηήΗΉθΘιίΙΊκΚλΛμΜνΝξΞοόΟΌπΠρΡσΣτΤυύΥΎφΦχΧψΨωώΩΏ'
                characters = greek_characters + string.digits + string.punctuation
                return characters
            if language == 'combine':
                #Use a combination of Latin and Greek.
                greek_characters = 'αάΑΆβΒγΓδΔεέΕΈζΖηήΗΉθΘιίΙΊκΚλΛμΜνΝξΞοόΟΌπΠρΡσΣτΤυύΥΎφΦχΧψΨωώΩΏ'
                characters = string.ascii_letters + greek_characters + string.digits + string.punctuation
                return characters
            else: #if none of the above arguments are given, raise an error!
                raise ValueError("Wrong language! Use '-l greek' or '-l combine' as an argument! Type '--help' for more information!")
        except ValueError as e:
            print(e)
            sys.exit() #exit the app!

    if custom_password:
        characters = custom_password
    else:
        characters = language_selection(language)

    passwords_list = []

    for length in range(min_password_length, max_password_length + 1):
        combinations = itertools.product(characters, repeat=length)
        passwords_list.extend([''.join(combination) for combination in combinations])

    return passwords_list

def export_to_txt(passwords, output_file):
    with open(output_file, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

if __name__ == "__main__":
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description='Generate a password wordlist using the following arguments.')

    # Add command-line arguments
    parser.add_argument('-m', '--max_length', type=int, default=1, help='Define the maximum length of characters in your wordlist. Default is 1')
    parser.add_argument('-n', '--min_length', type=int, default=1, help='Define the minimum length of characters in your wordlist. Default is 1')
    parser.add_argument('-o', '--output_file', default='wordlist.txt', help='Change the name of the output file. Default name is wordlist.txt')
    parser.add_argument('-c', '--custom_char', help='Define custom set of characters that you want to generate.')
    parser.add_argument('-l', '--language', default='latin', help="Default language is Latin. Write '-l greek' for Greek characters and '-l combine' for a Latin and Greek combination of characters.")

    # Parse command-line arguments
    args = parser.parse_args()

    # Extract values from arguments
    max_password_length = args.max_length
    output_file = args.output_file
    min_password_length = args.min_length
    custom_password = args.custom_char
    language = args.language

    # Generate passwords
    passwords_list = generate_passwords_sequence(max_password_length)

    # Export passwords to a file
    export_to_txt(passwords_list, output_file)

    print(f"{len(passwords_list)} passwords generated and exported to {output_file}.")
