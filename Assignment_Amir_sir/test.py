# def format_string():
#     l = input().split(" ")
#     count = 1
#     for i in l:
#         if i == "Python":
#             print('"Python"',end = " ")
#             continue
#         if i == "coders":
#             print("'coders'")
#             continue
#         if count%2 != 0:
#             print("'", i, "'", sep = "", end = " ")
#         else:
#             print('"', i, '"', sep = "", end = " ")
#         count += 1
# format_string()

# name = input()
# def normalize(passed_name):
#     new_name = passed_name.replace('é', 'e').replace('ë', 'e').replace('á', 'a').replace('å', 'aa').replace('œ', 'oe').replace('æ', 'ae')
#     return new_name
# print(normalize(name))
# a = input().split()
# n = input()
# count = 0
# for i in a:
#     if i == n:
#         print(count, end=' ')
#     count += 1 
# if __name__ == '__main__':
#     students = []
#     N = int(input())
#     for _ in range(N):
#         name = input()
#         grade = float(input())
#         students.append([name, grade])
    
#     grades = []
#     for i in range(N):
#         grades.append(students[i][1])
    
#     grades.sort()
#     grades = list(set(grades))
#     second_lowest= []
#     for i in range(N):
#         if grades[1] == students[i][1]:
#             second_lowest.append(students[i][0])
    
#     second_lowest.sort()
#     for i in second_lowest:
#         print(i)

# letters = 'abcdefghijklmnopqrstuvwxyz'
# double_alphabet = {}
# for letter in letters:
#     double_alphabet[letter] = letter*2
# print(double_alphabet)

# groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
# my_dict = dict.fromkeys(groups)
# n = int(input())
# for i in range(n):
#     my_dict[groups[i]] = int(input())
# print(my_dict)

# value_of_cards = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, '10' : 10, 'Jack' :11, 'Queen' : 12, 'King' : 13, 'Ace' : 14}
# sum = 0
# for _ in range(6):
#     a = input()
#     sum += value_of_cards[a]
# average = sum / 6
# print(average)
def select_dates(potential_dates):
    b = []
    for i in potential_dates:
        if i['age'] > 30 and ('art' in i['hobbies']) and i['city'] == 'Berlin':
            b.append(i['name'])
        a = ', '.join(b)
    return a
potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
                    "hobbies": ["jogging", "music"], "city": "Hamburg"},
                   {"name": "Sasha", "gender": "male", "age": 18,
                    "hobbies": ["rock music", "art"], "city": "Berlin"}, 
                   {"name": "Maria", "gender": "female", "age": 35,
                    "hobbies": ["art"], "city": "Berlin"},
                   {"name": "Daniel", "gender": "non-conforming", "age": 50,
                    "hobbies": ["boxing", "reading", "art"], "city": "Berlin"}, 
                   {"name": "John", "gender": "male", "age": 41,
                    "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]
print(select_dates(potential_dates))

#end code