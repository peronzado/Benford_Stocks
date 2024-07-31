import pandas as pd
import collections
import matplotlib.pyplot as plt
import sys
import math

def main(file_path):
    # Read the Excel spreadsheet
    df = pd.read_excel(file_path)

    day = input("Please specify the day: ").strip()
    month = input("Please specify the month: ").strip()
    year = input("Please specify the year: ").strip()

    #with open(f'total.txt','a') as file:
    #    file.write(f'{day}/{month}/{year} - Total Values: {df.iloc[:, 0]}\n')

    #total number of digits extracted
    num_rows = df.shape[0]

    # Extract the first digit of each number
    first_digits = df.iloc[:, 0].astype(str).str[0]

    # Extract the second digits
    second_digits = df.iloc[:, 0].astype(str).str[1]

    # Extract the third digits
    third_digits = df.iloc[:, 0].astype(str).str[2]

    # Count the occurrences of each digit
    digit_counts = collections.Counter(first_digits)

    # Count the occurrences of each second digit
    digit_counts_second = collections.Counter(second_digits)

    # Count the occurrences of each third digit
    digit_counts_third = collections.Counter(third_digits)

    with open(f'digit_counts.txt','a') as file:
        file.write(f'{day}/{month}/{year} - First Digits: {digit_counts}, Second Digits: {digit_counts_second}, Third Digits: {digit_counts_third}\n')

    # Prepare data for plotting
    digits = list(map(str, range(1, 10)))
    counts = [(digit_counts[digit]/num_rows)*100 for digit in digits]
    #counts = counts/

    digits_sec_third = list(map(str, range(0, 10)))
    counts_sec = [(digit_counts_second[digit]/num_rows)*100 for digit in digits_sec_third]
    counts_thi = [(digit_counts_third[digit]/num_rows)*100 for digit in digits_sec_third]

    with open(f'first_digit_difference.txt','a') as file:
        file.write(f'{day}/{month}/{year} - Errors: ')
        for digit in digits:
            real = math.log10(1+(1/int(digit)))*100
            seen = (digit_counts[digit]/num_rows)*100
            error = abs(seen-real)
            file.write(f'Digit: {digit}, Expected: {real:.3f}, Seen: {seen:.3f}, Difference = {error:.3f}| ')
        file.write(f'\n')

    # Plot the results
    plt.bar(digits, counts , color='blue')
    plt.xlabel('First Digit')
    plt.ylabel('Frequency (%)')
    plt.title(f'First Digit NB Law Validation - Total Value Dealt in BRL - {day}/{month}/{year}')
    first_filename = f'first_digit-{year}{month}{day}.png'
    plt.savefig(first_filename)
    #plt.show()
    plt.close()

    # Plot the results
    plt.bar(digits_sec_third, counts_sec , color='red')
    plt.xlabel('Second Digit')
    plt.ylabel('Frequency (%)')
    plt.title(f'Second Digit NB Law Validation - Total Value Dealt in BRL - {day}/{month}/{year}')
    second_filename = f'second_digit-{year}{month}{day}.png'
    plt.savefig(second_filename)
    #plt.show()
    plt.close()

    # Plot the results
    plt.bar(digits_sec_third, counts_thi , color='green')
    plt.xlabel('Third Digit')
    plt.ylabel('Frequency (%)')
    plt.title(f'Third Digit NB Law Validation - Total Value Dealt in BRL - {day}/{month}/{year}')
    third_filename = f'third_digit-{year}{month}{day}.png'
    plt.savefig(third_filename)
    #plt.show()
    plt.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Newcomb.py <ExcelFileName.xlsx>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
