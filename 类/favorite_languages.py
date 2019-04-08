from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarch'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'OC'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
            language.lower() + ',')

