import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WAD_Team4D.settings')

import django
django.setup()

from upskill_photography.models import Picture, Category, User, UserProfile
from PIL import Image


def populate():
    cat = add_cat("Buildings")
    print(cat)
    return None
    add_picture(cat, "car", Image.open("population_script_files/car.jpg"), add_UserProfile("Test_User")) 


    user_james = add_UserProfile("James")
    user_oliver = add_UserProfile("Oliver")
    user_rojhat = add_UserProfile("Rojhat")
    user_annie = add_UserProfile("Annie")
    user_profiles = [user_james,
                    user_oliver,
                    user_rojhat,
                    user_annie,
                    ]

    pictures = [
        {'uploading user': user_james,
         'title': 'cats',
         'image': 'static/images/',
         'likes': '10',
         'views': '120',
         },
        {'uploading user': user_james,
         'title': 'europe',
         'image': 'static/images/',
         'likes': '104',
         'views': '1205',
         },
        {'uploading user': user_oliver,
         'title': 'space',
         'image': 'static/images/',
         'likes': '130',
         'views': '1120',
         },
        {'uploading user': user_rojhat,
         'title': 'bugatti',
         'image': 'static/images/',
         'likes': '10',
         'views': '120',
         },
        {'uploading user': user_oliver,
         'title': 'pagani',
         'image': 'static/images/',
         'likes': '10046',
         'views': '134456',
         },
        {'uploading user': user_rojhat,
         'title': 'dogs',
         'image': 'static/images/',
         'likes': '14',
         'views': '99',
         },
        {'uploading user': user_annie,
         'title': 'lions',
         'image': 'static/images/',
         'likes': '104',
         'views': '1204',
         },
    ]
    cats = {'animals': {'Pictures': picture1, 'views': 128, 'likes': 64},
            'space ': {'Pictures': picture3, 'views': 64, 'likes': 32},
            'cars':  {'Pictures': picture5, 'views': 32, 'likes': 16}}
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pictures']:
            add_picture(c, p['title'], p['image'], p['uploading_user'], views=p['views'])

    for c in Category.objects.all():
        for p in Picture.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_UserProfile(name):
    user = User.objects.get_or_create(username=name)
    user.save()
    return UserProfile.objects.get(user=use)


def add_cat(name):
    cat = Category.objects.get_or_create(name=name)[0]
    cat.name = name
    cat.save()
    return cat


def add_picture(cat, title, image, uploading_user, views=0, likes=0):
    p = Picture.objects.get_or_create(category=cat, title=title)[0]
    p.title = Picture.title
    p.uploading_user = Picture.uploading_user
    p.image = Picture.image
    p.views = Picture.views
    p.likes = Picture.likes
    p.save()
    return p


if __name__ == '__main__':
    print('Starting upskillphotography population script...')
    populate()
