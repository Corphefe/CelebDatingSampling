from celebrity_parsing_functions import *

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    celebrity_names = []
    celebrity_genders = []
    celebrity_ages = []
    for letter in alphabet:
        links_to_celebs = alphabet_links(letter)
        for link in links_to_celebs:
            celebrity_name = get_name(link)
            celebrity_age = get_age(link)
            celebrity_gender = get_gender(link)

            celebrity_names.append(celebrity_name)
            celebrity_ages.append(celebrity_age) 
            celebrity_genders.append(celebrity_gender)

    clean_genders = [gender for gender in celebrity_genders if gender is not None]
    men = sum(clean_genders) / len(clean_genders)
    women = 1-men
    clean_ages = [age for age in celebrity_ages if age is not None]
    average_age = sum(clean_ages) / len(clean_ages)
    print(f"Sampled {len(celebrity_names)} celebrities: ", celebrity_names[0] + ", ..., " + celebrity_names[-1])
    print(f"Men: {men*100:.0f}%, Women: {women*100:.0f}%, Average Age: {average_age:.2f}")
    return

if __name__ == "__main__":
    main() 