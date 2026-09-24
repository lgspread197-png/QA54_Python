def total(*args):
    print(type(args),args)
    return sum(args)

print(total(1,3,2))
print(total(10,11))
print(total(12,20,30,50))
print(total())
print()

def print_scores(students,*scores):
    print(f"Students:{students}")
    print("scores: ",scores)

print_scores("Kristina",30,20,45)
print_scores("Alex",60)

def check_status_codes(*codes):
    for code in codes:
        assert code == 200

print(check_status_codes(200,200,200))
# print(check_status_codes(200,400,200))   AssertionError  assert code == 200


