def oxford_comma(elements):
    if len(elements) == 1:
        return elements[0]
    elif len(elements) == 2:
        return f"{elements[0]} and {elements[1]}"
    else:
        comma_list = ", ".join(elements[:-1])
    return comma_list + f", and {elements[-1]}"
print(oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits"]))
