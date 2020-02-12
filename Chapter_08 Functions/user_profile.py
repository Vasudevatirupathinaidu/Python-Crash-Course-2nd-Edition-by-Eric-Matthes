# Using Arbitrary Keyword Arguments
def bulid_profile(first, last, **user_info):
    """Bulid a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = bulid_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)