# TODO 
# have python store in memory info about the band Deep Purple

ian_paice = {
    "name" : "Ian Paice",
    "is_active_member": "Y",
    "year_joined": 1985
}
roger_glover = {
    "name" : "Roger Glover",
    "is_active_member": "Y",
    "year_joined": 1985
}
albums_years = {
"Shades of Deep Purple": 1968,
"The Book of Taliesyn":1968,
"Deep Purple": 1969,
"Deep Purple in Rock":1970,
"Fireball":1971,
"Machine Head": 1972,
"Who Do We Think We Are": 1973,
"Burn": 1974,
"Stormbringer": 1974,
"Come Taste the Band": 1975,
"Perfect Strangers": 1984,
"The House of Blue Light": 1987,
"Slaves and Masters": 1990,
"The Battle Rages On..": 1993,
"Purpendicular": 1996,
"Abandon": 1998,
"Bananas" : 2003,
"Rapture of the Deep" : 2005,
"Now What?!" : 2013,
"Infinite":2017,
"Whoosh!" : 2020,
"Turning to Crime" : 2021
}

band = {
    "name": "Deep Purple",
    "member_num": 5,
    "num_records": 22,
    "debut_year": 1967,
    "currently_active": True,
    "active_from_year": 1968, 
    "active_to_year" : 2024,
    "members" : [
                 "Ian Gillan", 
                 "Don Airey", 
                 "Simon McBride"
                 ],
    "tour_years" : [
        1968, 1969, 1970, 1971, 1972, 1973, 
        1974, 1975, 1976, 1984, 1985, 1987,
        1988, 1991, 1993, 1994, 1995, 1996, 
        1997, 1998, 1999, 2000, 2001, 2003, 
        2004, 2005, 2006, 2007, 2008, 2009, 
        2010, 2011, 2012, 2013, 2014, 2015, 
        2016, 2017, 2018, 2019, 2022, 2023
        ],
    "albums" : albums_years

}

# print(band["name"], band["tour_years"])

# print(band["active_to_year"] - band["active_from_year"])

# for key in band["tour_years"]:
#     print (key)

for val in band["tour_years"]:
    if val == 1991 :
        print(val)
