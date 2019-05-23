from datetime import date, datetime
from sharing.models import UploadModel


def delete_unuseful():
    active_files = UploadModel.objects.filter(is_worked=True)
    for file in active_files:
        if file.ended_date <= date.today():
            print('Delete ' + file.title + ': ' + str(datetime.now()))
            file.is_worked = False
            file.delete()
        else:
            file.is_worked = True
