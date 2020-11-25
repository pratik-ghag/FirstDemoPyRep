def person(name,**data ):
    print(name)
    # since we have key value pair hence i and j both
    for i, j in data.items():
        print(i,j)


person('pratik',age=23,city='Mumbai',mob=982114112)