from celebrity_parsing_functions import *

#STARTING_LINK = "https://www.whosdatedwho.com/dating/matthew-mcconaughey"
#STARTING_LINK = "https://www.whosdatedwho.com/dating/cillian-murphy"
STARTING_LINK = "https://www.whosdatedwho.com/dating/emma-watson"

def main():
    celebrity_names = []
    celebrity_relationships = []
    celebrity_genders = []
    celebrity_ages = []

    current_link = STARTING_LINK
    stop = False
    while (len(celebrity_names) < 130 and stop == False):
        current_name = get_name(current_link)
        current_age = get_age(current_link)
        current_gender = get_gender(current_link)
        relationships = relationship_links(current_link)
        
        if relationships == []:
            print("Sampling ended early: Closed dating loop encountered.")
            break

        celebrity_names.append(current_name)
        celebrity_ages.append(current_age)
        celebrity_genders.append(current_gender)
        celebrity_relationships.append(relationships)

        next_link = relationships.pop()
        next_name = get_name(next_link)

        i = len(celebrity_names) - 1
        while (next_name in celebrity_names):
            if relationships == []:
                if i == 0:
                    print("Sampling ended early: Closed dating loop encountered.")
                    stop = True
                    break
                else:
                    i = i - 1
                    relationships = celebrity_relationships[i]
            else:
                next_link = relationships.pop()
                next_name = get_name(next_link)
        if stop:
            break 

        current_link = next_link 
        
    clean_genders = [gender for gender in celebrity_genders if gender is not None]
    men = sum(clean_genders) / len(clean_genders)
    women = 1-men
    clean_ages = [age for age in celebrity_ages if age is not None]
    average_age = sum(clean_ages) / len(clean_ages)
    print(f"Started with celebrity: ", celebrity_names[0])
    print(f"Sampled {len(celebrity_names)} celebrities: ", celebrity_names[0] + ", ..., " + celebrity_names[-1])
    print(f"Men: {men*100:.0f}%, Women: {women*100:.0f}%, Average Age: {average_age:.2f}")
    return


if __name__ == "__main__":
    main()