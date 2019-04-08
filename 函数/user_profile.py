def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一起"""
    profile = {}
    profile["first_name"] = str(first)
    profile["last_name"] = str(last)
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physucs')
print(user_profile)
