
city_trees={}
while 1:
    print("""MENU:
            1.Add new city
            2.Display all cities
            3.Display given city
            4.Search city by given tree
            5.Delete city
            6.Modify trees in given city
            7.Exit
            """)
    ch=int(input())

    match ch:
        case 1:
            city=input("Enter city to be mentioned")
            tree_str=input("Enter tree")
            tree_l=tree_str.split(",")
            city_trees[city]=trees_l
        case 2:
            print("Ciry record are:")
            for city in city_trees:
                print("City is ",city)
                print("Trees are:",city_trees[city])
        case 3:
            c=input("Enter city u want to search:")
            if city in city_trees:
                print("City is "city)
                print("Trees are:",city_trees[city])
            else:
                print("City not present")
        case 4:
            t=input("Enter tree to be searched:")
            for city,trees in city_trees.items():
                if t in trees:
                    print("City:",city)
                
        case 5:
            c=input("Enter city u want to delete:")
            for city in city_trees:
                if city in city_trees:
                    del city_trees[c]
        case 6:
            c=input("Enter city whoes tree u want to update"))
            t=input("Enter tree u want to update")
            for city in city_trees:
                if c in city_trees:
                    city_trees[c]=t
                else:
                    city_trees[c]=t
        case 7:
            exit;
