# @Time    : 2018/3/27 0027 16:29
# @Author  : "Wang_Chongsheng"
# @Site    : 
# @File    : froms.py

from django import forms as DForms
from django.forms import fields
from django.forms import widgets
class DetailForm(DForms.Form):
    user1 = fields.CharField()
    user2 = fields.CharField(widget=widgets.TextInput(attrs={'class':'c1','placeholder':'用户名'}))
    user4 = fields.IntegerField()

    # 字符串
    user3 = fields.ChoiceField(choices=[(1, 'SH'), (2, 'BJ'), ])
    user5 = fields.CharField(
        widget=widgets.Select(choices=[(1, 'SH'), (2, 'BJ'), ])
    )
    user6 = fields.IntegerField(
        widget=widgets.Select(choices=[(1, 'SH'), (2, 'BJ'), ])
    )
    user7 = fields.IntegerField(
        widget=widgets.RadioSelect(choices=[(1, 'SH'), (2, 'BJ'), ])
    )



class FieldForm(DForms.Form):
    f1 = fields.CharField(
        required=False,
        initial="ohuo",
        error_messages={'required':'不能为空','invalid':'格式错误'},

        # validators=[RegexValidator(r'^[0-9]+$','1111',code='f1'),RegexValidator(r'^159[0-9]+$','222',code='f2')],
        label="haha",
        show_hidden_initial=True,
        disabled=False,
        label_suffix=">>"
    )
    # f2 = fields.RegexField(r'^159[0-9]+$')
    f3 = fields.FileField()
    f4 = fields.ChoiceField(
        initial=2,
        choices=[(1, '张三'), (2, '李四'),(3,'王二')],
    )
    f5 = fields.TypedChoiceField(
        coerce=lambda x: int(x),
        initial=2,
        choices=[(1, '张三'), (2, '李四'),(3,'王二')],
    )
    f6 = fields.MultipleChoiceField(
        initial=[1,2],
        choices=[(1, '张三'), (2, '李四'),(3,'王二')],
    )
    f7 = fields.SplitDateTimeWidget()
    f8 = fields.FilePathField(
        path='app01',
        allow_folders=True,
    )


class WidghtFrom(DForms.Form):
    w1 = fields.CharField(widget=widgets.ClearableFileInput)

class DBForm(DForms.Form):
    host = fields.CharField()
    host_type = fields.IntegerField(
        widget=widgets.Select(choices=[(0,'SH'),(1,'BJ')])
    )