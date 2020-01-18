def aida_function2(nama, umur):
    import json
    aida = {"name" : nama, "age" : umur,
            "address" : "Jalan Sukabirus no A54, Bandung",
            "hobbies" : ["watching movies", "hanging out", "listening music"],
            "is_married" : False,
            "list_school" : {"name_school" : "SMK Telkom Sandhy Putra Banjarbaru",
                   "year_in" : "2013", "year_out" : "2016",
                   "major" : "Teknik Jaringan Akses"},
            "skills" : [{"skill_name" : "Python Programming", "level" : "beginner"},
                        {"skill_name" : "Solving Problem Creatively", "level" : "advance"}],
            "interest_in_coding" : True}
    
    return json.dumps(aida)
