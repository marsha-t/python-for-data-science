def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)

    if obj_type == int:
        print("Type not found")
    elif obj_type == str:
        print(f"{object} is in the kitchen : {obj_type}")
    else:
        print(f"{obj_type.__name__.capitalize()} : {obj_type}")
    return 42
