from django.forms import (
    Form,
    CharField,
    DateTimeField,
    EmailField,
    FileField
)


class VisitForm(Form):

    visitor = CharField()
    date_time = DateTimeField()
    reason = CharField()
    email=EmailField()
    
class VisitorNameForm(Form):
    visitor_name= CharField()


class reportform(Form):
    pass    

class UploadCsvForm(Form):

    csv_file = FileField()