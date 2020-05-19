import csv 

teamname = []

def main(Jahr):
    # CSV Name
    filename = str(Jahr) + ('.csv')
    
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        k = 0
        for i in csv_reader:
            if k < 9:
                j = i[0]
                # Converting string to list 
                spielende_mannschaften = j.strip('["]').split(', ') 
                teama = spielende_mannschaften[0].strip('"')
                teamb = spielende_mannschaften[1].strip('"')
                teama = teama[1:-1]
                teamb = teamb[1:-1]
                teamname.append(teama)
                teamname.append(teamb)
            k += 1
        # printing final result and its type 
        print (teamname) 
            

#Jahr = input("Von welchem Jahr sollen die Spieldaten geladen werden? ")
main("2018")
