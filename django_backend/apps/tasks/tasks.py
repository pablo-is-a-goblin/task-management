from celery import shared_task
from . import models as myModels
from django.core.mail import send_mail
import datetime
 
def assignment_mail(task):
    subject = "Assignment to '" + task.tile + "'"
    message = "The users assigned to this task are: \n"
    for user in task.assigned_to.all():
        message += "- " + user.username + "\n"
    return subject, message

def overdue_mail(task):
    subject = "Task '" + task.title + "' is overdue"
    message = "Here is the task description: " + task.description
    return subject, message

NOTIFICATION_TYPES = {
    'assignment' : assignment_mail,
    'overdue' : overdue_mail,
}

@shared_task
def send_task_notification(task_id, notification_type):
    """Send email notifications for task events"""

    task = myModels.Task.objects.get(id=task_id)

    email_list = []
    for user in task.assigned_to.all():
        email_list.append(user.email)

    subject, message = NOTIFICATION_TYPES[notification_type](task)
    send_mail(
        subject,
        message,
        "task.management.psp@gmail.com",
        email_list,
        fail_silently=False,
)

@shared_task
def generate_daily_summary():
    """Generate daily task summary for all users"""
    for user in myModels.User.objects.all():
        message = "Hi, " + user.username + ", you are assigned to these tasks:\n"
        for task in user.assignments.all():
            message += "- " + task.title
        send_mail(
            "Daily summary",
            message,
            "task.management.psp@gmail.com",
            [user.email],
            fail_silently=True
        )

@shared_task
def check_overdue_tasks():
    for task in myModels.Task.objects.all():
        if task.is_overdue() and not task.is_archived:
            send_task_notification(task.id, 'overdue')

@shared_task
def cleanup_archived_tasks():
    """Delete archived tasks older than 30 days"""
    for task in myModels.Task.objects.get(is_archived=True):
        if task.due_date > datetime.timedelta(days=30):
            task.delete()