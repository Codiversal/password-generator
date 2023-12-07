# Password Generator

This Python script generates customizable password wordlists based on specified criteria. It provides flexibility in defining password length, character sets, and language options. 
Supported languages for the moment are Latin and Greek.

## Usage

### Prerequisites

- Python 3.x installed on your system.

### Script Features

- **Customizable Passwords**: Generate passwords with specified length ranges.
- **Character Sets**: Choose the number of characters that your passwords want to be. Start from 1 character and go up to your desired number.
> **Caution:** The more characters you choose, the bigger the file will be and more time will be needed to create the wordlst.
- **Custom Characters**: Define a custom set of characters for password generation.
- **Language Selection**: Specify the language for the wordlist, such as Latin, Greek, or a combination of both.

## How to Run

1. Clone or download the repository:

    ```bash
    git clone https://github.com/Codiversal/password-generator.git
    cd password-generator
    ```

2. Run the script:

    ```bash
    python3 generate.py -m <max_length> -n <min_length> -o <output_file> -c <custom_char> -l <language>
    ```
> You don't have to define all the arguments to run the script. Choose only the arguments that you want. All arguments have default values (see below)
### Command-line Arguments

- `-m, --max_length`: Define the maximum length of characters in your wordlist (default is 1).
- `-n, --min_length`: Define the minimum length of characters in your wordlist (default is 1).
- `-o, --output_file`: Change the name of the output file (default is wordlist.txt).
- `-c, --custom_char`: Define a custom set of characters that you want to generate.
- `-l, --language`: Specify the language for the wordlist. Options include 'latin', 'greek', and 'combine' for a Latin and Greek combination of characters (default is 'latin').

### Examples

Generate a Latin wordlist with passwords of length 2 to 4 characters:

```bash
python3 generate.py -m 4 -n 2 -o latin_wordlist.txt
```

Generate a Greek wordlist with passwords of length 3:

```bash
python3 generate.py -m 3 -n 3 -o greek_wordlist.txt -l greek
```
Generate a wordlist with custom characters (from 1 to 5 characters):

```bash
python3 generate.py -m 5 -c "ABC123!@"
```
For more information, use the --help option:

```bash
python3 generate.py --help
```
If no arguments are givven, then the script will run with all its default values:

```bash
python3 generate.py
```
