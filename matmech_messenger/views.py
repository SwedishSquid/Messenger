from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect,\
    HttpResponseServerError, HttpResponseBadRequest, JsonResponse
from .models import Guest, PrivateChat, PrivateMessage, GuestSession
from django.template import loader
from django.urls import reverse
import random
import time
import json
import hashlib


from .views_helper import su_cut, generate_random_key, set_default_if_empty,\
    get_bool_value_from_request, anti_ddos, anti_ddos_decorator, my_hash


def openaccount(request):
    try:
        user_name = su_cut(request.COOKIES['matmech_user_name'], 100)
        session_key = su_cut(request.COOKIES['matmech_session_key'], 100)
        user = Guest.objects.get(name=user_name)

        if len(GuestSession.objects.filter(session_key=session_key, guest=user)) == 0:
            user_name = 'default'
            user = Guest.objects.get(name=user_name)
    except:
        user_id = 1
        user = Guest.objects.get(id=1)
    return user


def login(request):
    if request.method == 'POST':
        guest_name = su_cut(request.POST['name'], 100)
        guest_hashed_password = my_hash(su_cut(request.POST['password'], 100))
        if (len(Guest.objects.filter(name=guest_name))) == 0:
            return JsonResponse({'result': 'error', 'information': 'account not found'})
        else:
            this_user = Guest.objects.get(name=guest_name)
            if this_user.hashed_password == guest_hashed_password:
                try:
                    http_user_agent = su_cut(request.META['HTTP_USER_AGENT'], 500)
                except:
                    http_user_agent = 'no informations'
                session_key = generate_random_key(50)
                new_session_for_user = GuestSession(guest=this_user,
                                                    session_key=session_key, http_user_agent=http_user_agent)
                new_session_for_user.save()
                context = {
                    'result': 'success',
                    'user_id': this_user.id,
                    'session_key': session_key,
                    'user_name': guest_name,
                }
                return JsonResponse(context)
            else:
                return JsonResponse({'result': 'error', 'information': 'password incorrect'})
    else:
        return render(request, "matmech/csrf_token.html")
        return JsonResponse({'result': 'error', 'information': 'request must be post'})


def registration(request):
    if request.method == 'POST':
        guest_name = su_cut(request.POST['name'], 100)
        guest_hashed_password = my_hash(su_cut(request.POST['password'], 100))
        about = su_cut(request.POST['about'], 5000)
        pub_date = timezone.now()
        if (len(Guest.objects.filter(name=guest_name))) == 1:
            return JsonResponse({'result': 'error', 'information': 'name reserved'})
        else:
            new_user = Guest(name=guest_name, hashed_password=guest_hashed_password,
                             about=about, pub_date=pub_date)
            new_user.save()
            try:
                http_user_agent = su_cut(request.META['HTTP_USER_AGENT'], 500)
            except:
                http_user_agent = 'no informations'
            session_key = generate_random_key(50)
            new_session_for_user = GuestSession(guest=new_user,
                                                session_key=session_key, http_user_agent=http_user_agent)
            new_session_for_user.save()
            context = {
                'result': 'success',
                'user_id': new_user.id,
                'session_key': session_key,
                'user_name': guest_name,
            }
            return JsonResponse(context)
    else:
        return render(request, "matmech/csrf_token.html")
        return JsonResponse({'result': 'error', 'information': 'request must be post'})


def main(request):
    json_result = {"text": "hi on our website"}
    return JsonResponse(json_result)


def all_guests(request):
    guests = [guest.json() for guest in Guest.objects.all()]
    return JsonResponse({'guests': guests})


def my_account(request):
    user = openaccount(request)
    return JsonResponse(user.json())


def my_chats(request):
    return HttpResponseRedirect("matmech/chats/private/")
    user = openaccount(request)
    print(dir(user))
    private_chats = json.dumps(user.privatechat_set.all())
    return JsonResponse(private_chats)


def private_chats(request):
    user = openaccount(request)
    chats_list = user.privatechat_set.all()
    result_chats_list = [chat.json(user) for chat in chats_list]
    context = {
        'chats_list': result_chats_list
    }
    return JsonResponse(context)


def account(request, guest_id):
    return JsonResponse({'result': 'error', 'information': Guest.objects.get(id=guest_id).json()})


def private_chat(request, guest_id):
    user = openaccount(request)
    other_user = Guest.objects.get(id=guest_id)
    try:
        this_chat = PrivateChat.objects.filter(authors=user.id).get(authors=other_user.id)
    except:
        this_chat = PrivateChat()
        this_chat.save()
        this_chat.authors.add(guest_id.id)
        this_chat.authors.add(user.id)

        this_chat.save()
    messages_list = [message.json() for message in this_chat.privatemessage_set.all()]

    if len(messages_list) == 0:
        a = PrivateMessage(private_chat=this_chat, author=user, text="first message in this chat",
                           pub_date=timezone.now())
        a.save()
    if this_chat.authors.all()[0] == user:
        this_chat.author_1_not_checked_messages_count = 0
        this_chat.save()
    else:
        this_chat.author_2_not_checked_messages_count = 0
        this_chat.save()

    context = {
        'messages_list': messages_list,
        'other_user': other_user.name,
    }

    return JsonResponse({'result': 'success', 'information': context})


def private_chat_message(request, guest_id, message_id):
    user = openaccount(request)
    other_user = Guest.objects.get(id=guest_id)
    this_chat = PrivateChat.objects.filter(authors=user.id).get(authors=other_user.id)
    message = this_chat.privatemessage_set.get(id=message_id)

    context = {
        'message': message.json(),
        'other_user': other_user.id,
    }

    return JsonResponse({'result': 'success', 'information': context})


def private_chat_message_read(request, guest_id, message_id):
    user = openaccount(request)
    other_user = Guest.objects.get(id=guest_id)
    this_chat = PrivateChat.objects.filter(authors=user.id).get(authors=other_user.id)
    message = this_chat.privatemessage_set.get(id=message_id)
    if message.author != user:
        message.is_read = True
        message.save()
        return JsonResponse({'result': 'success'})
    else:
        return JsonResponse({'result': 'error', 'information': 'its your message'})


def send_message(request, guest_id):
    if request.method == "POST":
        user = openaccount(request)
        user_request_id = su_cut(request.POST['user_request_id'], 100)
        user_request = Guest.objects.get(id=user_request_id)
        message_text = su_cut(request.POST['message_text'], 1000)
        if len(PrivateChat.objects.filter(authors=user.id).filter(authors=user_request.id)) > 0:

            chat = PrivateChat.objects.filter(authors=user.id).get(authors=user_request.id)
        else:
            chat = PrivateChat()
            chat.save()
            chat.authors.add(user_request.id)
            chat.authors.add(user.id)

            chat.save()

        if len(message_text) > 0:
            chat.privatemessage_set.create(message_text=message_text, author=user, pub_date=timezone.now())
            if (chat.authors.all()[0] == user):
                chat.author_2_not_checked_messages_count += 1
            else:
                chat.author_1_not_checked_messages_count += 1
            chat.save()
        return JsonResponse({'result': 'success', 'information': 'yes'})
    else:
        return render(request, "matmech/csrf_token.html")
