import requests


# def do_registration():
#     url = 'https://phs3.na4u.ru/matmech/registration'
#     csrf_token = 'ToYkuK797xFzHDA0bsC3fveWRrAvla2irQ6qMvj7lOUzqDwEUPia8yZGngNSyYOc'
#     data = {'name': 'lobster2_not_twin', 'password': 'lobster_cool', 'about': 'me', 'csrfmiddlewaretoken': csrf_token}
#     r = requests.post(url, data=data, cookies={'csrfmiddlewaretoken': csrf_token})
#     print(r.text)
#     print(r)
#     print(type(r))
#     # print(r.json())
#     # print(r.content)
#     pass
#
# def get_token():
#     url = 'https://phs3.na4u.ru/matmech/registration'
#     r = requests.get(url)
#     print(r.text)


def do_reg_2():
    URL = 'https://phs3.na4u.ru/matmech/registration'
    client = requests.session()
    # Retrieve the CSRF token first
    client.get(URL)  # sets cookie
    if 'csrftoken' in client.cookies:
        # Django 1.6 and up
        csrftoken = client.cookies['csrftoken']
    else:
        # older versions
        csrftoken = client.cookies['csrf']
    reg_data = dict(name='lobster2_not_twin', password='lobster_cool', about='me', csrfmiddlewaretoken=csrftoken, next='/')
    client.headers = dict(referer=URL)
    r = client.post(URL, data=reg_data)
    print(r.text)
    print(r)

# do_reg_2()


def log_to_acc():
    URL = 'https://phs3.na4u.ru/matmech/login'
    client = requests.session()
    # Retrieve the CSRF token first
    client.get(URL)  # sets cookie
    if 'csrftoken' in client.cookies:
        # Django 1.6 and up
        csrftoken = client.cookies['csrftoken']
    else:
        # older versions
        csrftoken = client.cookies['csrf']

    log_data = dict(name='lobster2_not_twin', password='lobster_cool', csrfmiddlewaretoken=csrftoken, next='/')
    client.headers = dict(referer=URL)
    r = client.post(URL, data=log_data)
    print(r.text)
    # print(r)
    pass

# log_to_acc()

def get_curr_acc():
    URL = 'https://phs3.na4u.ru/matmech/me'
    session_key = 'VBWY3vbfx2sVvKsaJlaKo9H88cqBzYcs7HLi0b8uBZP4yYRAqh'
    client = requests.session()
    # Retrieve the CSRF token first
    # client.get(URL)  # sets cookie
    # if 'csrftoken' in client.cookies:
    #     # Django 1.6 and up
    #     csrftoken = client.cookies['csrftoken']
    # else:
    #     # older versions
    #     csrftoken = client.cookies['csrf']
    # client.headers = dict(referer=URL)
    cookies = dict(matmech_user_name='lobster2_not_twin', matmech_session_key=session_key)#, csrftoken=csrftoken)
    r = client.get(URL, cookies=cookies)
    print(r.text)


# get_curr_acc()


