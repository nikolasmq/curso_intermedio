def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname":"Nicolas", "lastname":"Quintero"}
    super_list = [
        {"firstname":"Nicolas", "lastname":"Quintero"},
        {"firstname":"Yeny", "lastname":"Mejia"},
        {"firstname":"Alejandro", "lastname":"Quintero"},
        {"firstname":"Celeste", "lastname":"Quintero"},
        {"firstname":"Lila", "lastname":"Velez"}
    ]

    super_dict = {
        "natural_nums" : [1,2,3,4,5,6,7,8,9],
        "integer_nums" : [-2,-1,0,1,2],
        "floating_nums": [1.2,2.0,3.0,3.5,2.5,1.5]
    }

    for key, value in super_dict.items():
        print(key, " - ", value)

if __name__== '__main__':
    main()