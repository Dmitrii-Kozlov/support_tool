from celery import task
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from .models import Case


@task
def case_update_mail(case_id):
    case = get_object_or_404(
        Case.objects.select_related('module', 'author', 'author__profile', 'author__profile__airline',).prefetch_related('emails_list'), pk=case_id)
    comments = case.comments.select_related('author', 'author__profile', 'author__profile__airline').all()
    subject = f'Заявка № {case.id} - {case.title}'
    message = f'Тема: "{case.title}"\n\n' \
              f'Описание:\n\n{case.description}.\n\n' \
              f'создано { case.timestamp() } (UTC) '\
              f'пользователем {case.author.first_name} {case.author.last_name} ({case.author.profile.airline})\n\n'\
              '----------------\n\n'
    for comment in comments:
        message += f'{comment.body}\n\n'\
                   f'создано { comment.timestamp() } (UTC) '\
                   f'пользователем {comment.author.first_name} {comment.author.last_name} ({comment.author.profile.airline})\n\n'\
                   '----------------\n\n'
    mail_sent = send_mail(subject,
                          message,
                          'admin@support_tool.com',
                          [user.email for user in case.emails_list.all()])
    return mail_sent
