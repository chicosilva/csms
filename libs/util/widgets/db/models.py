#coding:utf8
from django.db.models import FloatField, IntegerField, CharField
from libs.util.widgets.db.fields import ZMoneyField, ZMaskedField, ZColorPickerField, ZEmailListField
from libs.util.widgets.db.widgets import ZMoneyWidget, ZMaskedWidget, ZColorPickerWidget, ColorPickerWidget, \
    ZEmailListWidget


class MoneyField(FloatField):
    symbol = 'R$ '
    show_symbol = None
    symbol_stay = None

    def __init__(self, symbol=None, show_symbol=None, symbol_stay=None, *args, **kwargs):
        if symbol is not None: self.symbol = symbol
        if show_symbol is not None: self.show_symbol = show_symbol
        if symbol_stay is not None: self.symbol_stay = symbol_stay
        super(MoneyField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': ZMoneyField, 'widget': ZMoneyWidget(self.symbol, self.show_symbol, self.symbol_stay)}
        defaults.update(kwargs)
        return super(MoneyField, self).formfield(**defaults)

class MaskedCharField(CharField):
    mask = None

    def __init__(self, mask=None, *args, **kwargs):
        if mask: self.mask = mask
        super(MaskedCharField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': ZMaskedField, 'widget': ZMaskedWidget(self.mask)}
        defaults.update(kwargs)
        return super(MaskedCharField, self).formfield(**defaults)


class ColorPickerField(CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 7
        super(ColorPickerField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs.update({"widget": ColorPickerWidget})
        return super(ColorPickerField, self).formfield(**kwargs)

class EmailListField(CharField):
    def __init__(self, *args, **kwargs):
        super(EmailListField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs.update({'form_class': ZEmailListField, "widget": ZEmailListWidget})
        return super(EmailListField, self).formfield(**kwargs)
