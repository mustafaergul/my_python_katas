def boredom(staff):
    dep_scores = {"accounts": 1, "finance": 2, "canteen": 10, "regulation": 3,
                  "trading": 6, "change": 6, "IS": 8, "retail": 5,
                  "cleaning": 4, "pissing about": 25}

    vs = sum(dep_scores[v] for v in staff.values())

    if vs <= 80:
        return "kill me now"
    elif vs < 100:
        return "i can handle this"
    return "party time!!"


boredom({"tim": "IS", "jim": "finance", "randy": "pissing about",
         "sandy": "cleaning", "andy": "cleaning", "katie": "cleaning",
         "laura": "pissing about", "saajid": "regulation",
         "alex": "regulation", "john": "accounts", "mr": "canteen"})

boredom({"tim": "change", "jim": "accounts",
  "randy": "canteen", "sandy": "change", "andy": "change", "katie": "IS",
  "laura": "change", "saajid": "IS", "alex": "trading", "john": "accounts",
  "mr": "finance" })
