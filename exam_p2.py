import string

def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    f = open(file_name,"r")
    allEntires = f.readlines()
    all = []
    for entry in allEntires:
        temp = entry.strip().split(",")
        temp[2] = int(temp[2])
        all.append(temp)
    return all

def total_births(year):
    """

    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    total = 0
    allEntires = process_file("babynames/yob"+str(year)+".txt")
    for entry in allEntires:
        total+=entry[2]
    return total  

def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    totalBirths = total_births(year)
    allEntires = process_file("babynames/yob"+str(year)+".txt")
    for entry in allEntires:
        if entry[0]==name and entry[1]==gender:
            return entry[2]/totalBirths  # delete this line and replace with your code here


def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    max_prop = -1
    max_year = -1
    for y in range(1880,2011):
        current_proportion = proportion(name,gender,y)
        if current_proportion > max_prop:
            max_prop = current_proportion
            max_year = y
    return max_year 


def main():
    print (highest_year ('Sarah', 'F'))

if __name__ == '__main__':
    main()
