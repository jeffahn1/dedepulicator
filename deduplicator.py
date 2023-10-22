import csv

# Website URL
with open("crm_duplicates.csv", "r") as before_list, open("/Users/jeffreyjahn/Desktop/Desktop/the_matrix/crm/cleaned_crm.csv", "w") as after_list:
    seen = set()
    # looping through 
    for row in before_list:
        # 
        if row in seen:
            continue
        seen.add(row)
        after_list.write(row)  
 
        # row is not contacted:
        
