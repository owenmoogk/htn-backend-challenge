import json

with open('input.json', 'r') as f:
    data = json.load(f)

for i, item in enumerate(data):
    item['model'] = 'userData.user'
    item['pk'] = i + 1
    item['fields'] = {
        'name': item.pop('name'),
        'company': item.pop('company'),
        'email': item.pop('email'),
        'phone': item.pop('phone'),
        'skills': [
            {
                'name': skill['skill'],
                'rating': skill['rating']
            } for skill in item['skills']
        ]
    }

with open('user.json', 'w') as f:
    json.dump(data, f, indent=4)
