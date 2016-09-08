#coding:utf8
from calendar import monthrange
from datetime import date
import re
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from django.forms import CharField, Textarea, MultiWidget, MultiValueField, ChoiceField, TextInput
from libs.util import email_re


class ZMoneyField(CharField):
    def __init__(self, *args, **kwargs):
        super(ZMoneyField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        np = ['R$', ' ']
        if value:
            for i in np: value = value.replace(i, '')
        else:
            value = 0
        try:
            value = value.replace('.', '').replace(',', '.')
        except:
            pass
        return value

class ZMaskedField(CharField):
    def __init__(self, *args, **kwargs):
        super(ZMaskedField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        np = ['(', ')', '-', '.', '/', ' ']
        if value:
            for i in np: value = value.replace(i,'')
        return value

class ZColorPickerField(CharField):
    def to_python(self, value):
        return value

email_separator_re = re.compile(r'[^\w\.\-\+@_]+')


def _is_valid_email(email):
    return email_re.match(email)


class ZEmailListField(CharField):
    widget = Textarea

    def clean(self, value):
        super(ZEmailListField, self).clean(value)

        emails = email_separator_re.split(value)

        if not emails:
            raise ValidationError(u'Digite pelo menos um endereço de email.')

        for email in emails:
            if not _is_valid_email(email):
                raise ValidationError(u'%s não é um e-mail válido.' % email)

        return emails

VERIFICATION_VALUE_RE = r'^([0-9]{3,4})$'
class CCExpWidget(MultiWidget):
    """ Widget containing two select boxes for selecting the month and year"""
    def decompress(self, value):
        return [value.month, value.year] if value else [None, None]

    def format_output(self, rendered_widgets):
        html = u' / '.join(rendered_widgets)
        return u'<span style="white-space: nowrap">%s</span>' % html


class CCExpField(MultiValueField):
    EXP_MONTH = [('',' ----- ')] + [(x, x) for x in xrange(1, 13)]
    EXP_YEAR = [('',' ----- ')] + [(x, x) for x in xrange(date.today().year,date.today().year + 15)]
    default_error_messages = {
        'invalid_month': u'O mês digitado não é válido',
        'invalid_year': u'O ano digitado não é válido',
    }

    def __init__(self, *args, **kwargs):
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs: errors.update(kwargs['error_messages'])
        fields = (
            ChoiceField(choices=self.EXP_MONTH,error_messages={'invalid': errors['invalid_month']}),
            ChoiceField(choices=self.EXP_YEAR,error_messages={'invalid': errors['invalid_year']}),
        )
        super(CCExpField, self).__init__(fields, *args, **kwargs)
        self.widget = CCExpWidget(widgets =
        [fields[0].widget, fields[1].widget])

    def clean(self, value):
        exp = super(CCExpField, self).clean(value)
        if exp:
            if date.today() > exp:
                raise ValidationError(u'Data de expiração informada está expirada.')
        return exp

    def compress(self, data_list):
        if data_list:
            if data_list[1] in EMPTY_VALUES:
                error = self.error_messages['invalid_year']
                raise ValidationError(error)
            if data_list[0] in EMPTY_VALUES:
                error = self.error_messages['invalid_month']
                raise ValidationError(error)
            year = int(data_list[1])
            month = int(data_list[0])
            # find last day of the month
            day = monthrange(year, month)[1]
            return date(year, month, day)
        return None

class VerificationValueField(CharField):
    """
    Form field that validates credit card verification values (e.g. CVV2).
    See http://en.wikipedia.org/wiki/Card_Security_Code
    """

    widget = TextInput(attrs={'maxlength': 4})
    default_error_messages = {
        'required': u'Por favore, informe o código de segurança do cartão.',
        'invalid': u'O código de segurança que você informou não é válido.',
        }

    def clean(self, value):
        if value: value = value.replace(' ', '')
        if not value and self.required:
            raise ValidationError(self.error_messages['required'])
        if value and not re.match(VERIFICATION_VALUE_RE, value):
            raise ValidationError(self.error_messages['invalid'])
        return value