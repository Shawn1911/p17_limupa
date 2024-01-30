from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email_to_all_users(subject,message,email_list):
    # User = get_user_model()
    # users = User.objects.all()
    # email_list = [user.email for user in users]

    # try:
    result = send_mail(subject,message, 'azamovshahboz06082001@gmail.com', email_list)
    return result
    #     task_result = CeleryTaskResult.objects.create(task_id=send_email_to_all_users.request.id,result=result)
    #     return task_result.result
    # except Exception as e:
    #     task_result = CeleryTaskResult.objects.create(task_id=send_email_to_all_users.request.id, result=str(e))
    #     return task_result.result