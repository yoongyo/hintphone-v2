from django import forms
import sys
sys.path.append('..')
from hint.models import Theme
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'id': 'username',
            'type': 'text',
            'class': 'mt-4 mb-2',
            'value': "",
            'required autofocus': True,
            'placeholder': 'ID',
            'autocomplete': 'off',
            'style': 'outline:0;color:white;border:none;width:100%;'
                    'background-color:#548CA8 ;box-shadow: 0 2px 0 0 white;'
        }
    ))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'type': 'password',
                'class': 'mt-2',
                'placeholder': 'Password',
                'required data-eye': True,
                'autocomplete': 'off',
                'style': 'outline:0;color:white;border:none;width:100%;'
                         'background-color:#548CA8 ;box-shadow: 0 2px 0 0 white;'
            }
        ),
    )

class HintForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'hintCount', 'hint1', 'hint2', 'hint3', 'hint4', 'hint5', 'hint6', 'hint7', 'hint8', 'hint9',
                  'hint10', 'hint11', 'hint12', 'hint13', 'hint14', 'hint15', 'hint16', 'hint17', 'hint18', 'hint19',
                  'hint20', 'sub_hint1', 'sub_hint2', 'sub_hint3', 'sub_hint4', 'sub_hint5', 'sub_hint6', 'sub_hint7',
                  'sub_hint8', 'sub_hint9', 'sub_hint10', 'sub_hint11', 'sub_hint12', 'sub_hint13', 'sub_hint14',
                  'sub_hint15', 'sub_hint16', 'sub_hint17', 'sub_hint18', 'sub_hint19', 'sub_hint20', 'hint21', 'hint22',
                  'hint23', 'hint24', 'hint25', 'hint26', 'hint27', 'hint28', 'hint29', 'hint30', 'sub_hint21', 'sub_hint22',
                  'sub_hint23', 'sub_hint24', 'sub_hint25', 'sub_hint26', 'sub_hint27', 'sub_hint28', 'sub_hint29', 'sub_hint30',
                  'enterKey', 'textHint1', 'textHint2', 'textHint3', 'textHint4', 'textHint5', 'textHint6', 'textHint7', 'textHint8',
                  'textHint9', 'textHint10', 'textHint11', 'textHint12', 'textHint13', 'textHint14', 'textHint15', 'textHint16',
                  'textHint17', 'textHint18', 'textHint19', 'textHint20', 'textHint21', 'textHint21', 'textHint22', 'textHint23',
                  'textHint24', 'textHint25', 'textHint26', 'textHint27', 'textHint28', 'textHint29', 'textHint30',
                  'sub_textHint1', 'sub_textHint2', 'sub_textHint3', 'sub_textHint4', 'sub_textHint5', 'sub_textHint6', 'sub_textHint7',
                  'sub_textHint8', 'sub_textHint9', 'sub_textHint10', 'sub_textHint11', 'sub_textHint12', 'sub_textHint13', 'sub_textHint14',
                  'sub_textHint15', 'sub_textHint16', 'sub_textHint17', 'sub_textHint18', 'sub_textHint19', 'sub_textHint20', 'sub_textHint21',
                  'sub_textHint22', 'sub_textHint23', 'sub_textHint24', 'sub_textHint25', 'sub_textHint26', 'sub_textHint27',
                  'sub_textHint28', 'sub_textHint29', 'sub_textHint30',
                  'sub_textHint31', 'sub_textHint32', 'sub_textHint33', 'sub_textHint34', 'sub_textHint35', 'sub_textHint36',
                  'sub_textHint37','sub_textHint38', 'sub_textHint39', 'sub_textHint40', 'sub_textHint41', 'sub_textHint42',
                  'sub_textHint43', 'sub_textHint44',
                  'sub_textHint45', 'sub_textHint46', 'sub_textHint47', 'sub_textHint48', 'sub_textHint49',
                  'sub_textHint50', 'sub_textHint51',
                  'sub_textHint52', 'sub_textHint53', 'sub_textHint54', 'sub_textHint55', 'sub_textHint56',
                  'sub_textHint57',
                  'sub_textHint58', 'sub_textHint59', 'sub_textHint60',
                  'sub_textHint61',
                  'sub_textHint62', 'sub_textHint63', 'sub_textHint64', 'sub_textHint65', 'sub_textHint66',
                  'sub_textHint67',
                  'sub_textHint68', 'sub_textHint69', 'sub_textHint70',
                  'sub_textHint71',
                  'sub_textHint72', 'sub_textHint73', 'sub_textHint74', 'sub_textHint75', 'sub_textHint76',
                  'sub_textHint77',
                  'sub_textHint78', 'sub_textHint79', 'sub_textHint80',
                  'textHint31', 'textHint32', 'textHint33', 'textHint34', 'textHint35', 'textHint36', 'textHint37',
                  'textHint38',
                  'textHint39', 'textHint40', 'textHint41', 'textHint42', 'textHint43', 'textHint44', 'textHint45',
                  'textHint46',
                  'textHint47', 'textHint48', 'textHint49', 'textHint50', 'textHint51', 'textHint52',
                  'textHint53',
                  'textHint54', 'textHint55', 'textHint56', 'textHint57', 'textHint58', 'textHint59', 'textHint60',
                  'textHint61', 'textHint62', 'textHint63', 'textHint64', 'textHint65', 'textHint66', 'textHint67',
                  'textHint68',
                  'textHint69', 'textHint70', 'textHint71', 'textHint72', 'textHint73', 'textHint74', 'textHint75',
                  'textHint76',
                  'textHint77', 'textHint78', 'textHint79', 'textHint80', 'timer'
                  ]
        widgets = {
            'textHint1': CKEditorWidget(
                attrs={
                    'style': 'width: 100%'
                }
            ),
            'textHint2': CKEditorWidget(),
            'textHint3': CKEditorWidget(),
            'textHint4': CKEditorWidget(),
            'textHint5': CKEditorWidget(),
            'textHint6': CKEditorWidget,
            'textHint7': CKEditorWidget,
            'textHint8': CKEditorWidget,
            'textHint9': CKEditorWidget,
            'textHint10': CKEditorWidget,
            'textHint11': CKEditorWidget,
            'textHint12': CKEditorWidget,
            'textHint13': CKEditorWidget,
            'textHint14': CKEditorWidget,
            'textHint15': CKEditorWidget,
            'textHint16': CKEditorWidget,
            'textHint17': CKEditorWidget,
            'textHint18': CKEditorWidget,
            'textHint19': CKEditorWidget,
            'textHint20': CKEditorWidget,
            'textHint21': CKEditorWidget,
            'textHint22': CKEditorWidget,
            'textHint23': CKEditorWidget,
            'textHint24': CKEditorWidget,
            'textHint25': CKEditorWidget,
            'textHint26': CKEditorWidget,
            'textHint27': CKEditorWidget,
            'textHint28': CKEditorWidget,
            'textHint29': CKEditorWidget,
            'textHint30': CKEditorWidget,
            'textHint31': CKEditorWidget,
            'textHint32': CKEditorWidget,
            'textHint33': CKEditorWidget,
            'textHint34': CKEditorWidget,
            'textHint35': CKEditorWidget,
            'textHint36': CKEditorWidget,
            'textHint37': CKEditorWidget,
            'textHint38': CKEditorWidget,
            'textHint39': CKEditorWidget,
            'textHint40': CKEditorWidget,
            'textHint41': CKEditorWidget,
            'textHint42': CKEditorWidget,
            'textHint43': CKEditorWidget,
            'textHint44': CKEditorWidget,
            'textHint45': CKEditorWidget,
            'textHint46': CKEditorWidget,
            'textHint47': CKEditorWidget,
            'textHint48': CKEditorWidget,
            'textHint49': CKEditorWidget,
            'textHint50': CKEditorWidget,
            'textHint51': CKEditorWidget,
            'textHint52': CKEditorWidget,
            'textHint53': CKEditorWidget,
            'textHint54': CKEditorWidget,
            'textHint55': CKEditorWidget,
            'textHint56': CKEditorWidget,
            'textHint57': CKEditorWidget,
            'textHint58': CKEditorWidget,
            'textHint59': CKEditorWidget,
            'textHint60': CKEditorWidget,
            'textHint61': CKEditorWidget,
            'textHint62': CKEditorWidget,
            'textHint63': CKEditorWidget,
            'textHint64': CKEditorWidget,
            'textHint65': CKEditorWidget,
            'textHint66': CKEditorWidget,
            'textHint67': CKEditorWidget,
            'textHint68': CKEditorWidget,
            'textHint69': CKEditorWidget,
            'textHint70': CKEditorWidget,
            'textHint71': CKEditorWidget,
            'textHint72': CKEditorWidget,
            'textHint73': CKEditorWidget,
            'textHint74': CKEditorWidget,
            'textHint75': CKEditorWidget,
            'textHint76': CKEditorWidget,
            'textHint77': CKEditorWidget,
            'textHint78': CKEditorWidget,
            'textHint79': CKEditorWidget,
            'textHint80': CKEditorWidget,

            'sub_textHint1': CKEditorWidget(),
            'sub_textHint2': CKEditorWidget(),
            'sub_textHint3': CKEditorWidget(),
            'sub_textHint4': CKEditorWidget(),
            'sub_textHint5': CKEditorWidget(),
            'sub_textHint6': CKEditorWidget(),
            'sub_textHint7': CKEditorWidget(),
            'sub_textHint8': CKEditorWidget(),
            'sub_textHint9': CKEditorWidget(),
            'sub_textHint10': CKEditorWidget(),
            'sub_textHint11': CKEditorWidget(),
            'sub_textHint12': CKEditorWidget(),
            'sub_textHint13': CKEditorWidget(),
            'sub_textHint14': CKEditorWidget(),
            'sub_textHint15': CKEditorWidget(),
            'sub_textHint16': CKEditorWidget(),
            'sub_textHint17': CKEditorWidget(),
            'sub_textHint18': CKEditorWidget(),
            'sub_textHint19': CKEditorWidget(),
            'sub_textHint20': CKEditorWidget(),
            'sub_textHint21': CKEditorWidget(),
            'sub_textHint22': CKEditorWidget(),
            'sub_textHint23': CKEditorWidget(),
            'sub_textHint24': CKEditorWidget(),
            'sub_textHint25': CKEditorWidget(),
            'sub_textHint26': CKEditorWidget(),
            'sub_textHint27': CKEditorWidget(),
            'sub_textHint28': CKEditorWidget(),
            'sub_textHint29': CKEditorWidget(),
            'sub_textHint30': CKEditorWidget(),
            'sub_textHint31': CKEditorWidget(),
            'sub_textHint32': CKEditorWidget(),
            'sub_textHint33': CKEditorWidget(),
            'sub_textHint34': CKEditorWidget(),
            'sub_textHint35': CKEditorWidget(),
            'sub_textHint36': CKEditorWidget(),
            'sub_textHint37': CKEditorWidget(),
            'sub_textHint38': CKEditorWidget(),
            'sub_textHint39': CKEditorWidget(),
            'sub_textHint40': CKEditorWidget(),
            'sub_textHint41': CKEditorWidget(),
            'sub_textHint42': CKEditorWidget(),
            'sub_textHint43': CKEditorWidget(),
            'sub_textHint44': CKEditorWidget(),
            'sub_textHint45': CKEditorWidget(),
            'sub_textHint46': CKEditorWidget(),
            'sub_textHint47': CKEditorWidget(),
            'sub_textHint48': CKEditorWidget(),
            'sub_textHint49': CKEditorWidget(),
            'sub_textHint50': CKEditorWidget(),
            'sub_textHint51': CKEditorWidget(),
            'sub_textHint52': CKEditorWidget(),
            'sub_textHint53': CKEditorWidget(),
            'sub_textHint54': CKEditorWidget(),
            'sub_textHint55': CKEditorWidget(),
            'sub_textHint56': CKEditorWidget(),
            'sub_textHint57': CKEditorWidget(),
            'sub_textHint58': CKEditorWidget(),
            'sub_textHint59': CKEditorWidget(),
            'sub_textHint60': CKEditorWidget(),
            'sub_textHint61': CKEditorWidget(),
            'sub_textHint62': CKEditorWidget(),
            'sub_textHint63': CKEditorWidget(),
            'sub_textHint64': CKEditorWidget(),
            'sub_textHint65': CKEditorWidget(),
            'sub_textHint66': CKEditorWidget(),
            'sub_textHint67': CKEditorWidget(),
            'sub_textHint68': CKEditorWidget(),
            'sub_textHint69': CKEditorWidget(),
            'sub_textHint70': CKEditorWidget(),
            'sub_textHint71': CKEditorWidget(),
            'sub_textHint72': CKEditorWidget(),
            'sub_textHint73': CKEditorWidget(),
            'sub_textHint74': CKEditorWidget(),
            'sub_textHint75': CKEditorWidget(),
            'sub_textHint76': CKEditorWidget(),
            'sub_textHint77': CKEditorWidget(),
            'sub_textHint78': CKEditorWidget(),
            'sub_textHint79': CKEditorWidget(),
            'sub_textHint80': CKEditorWidget(),
            'timer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': ''
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': '',
                }
            ),
            'enterKey': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': '',
                }
            ),
            'hintCount': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'style': '',
                }
            ),
            'hint1': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint1': forms.FileInput(
                attrs={
                    'id': 'sub1_file',
                    'style': 'border-color:black;display: none',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint2': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint2': forms.FileInput(
                attrs={
                    'id': 'sub2_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint3': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint3': forms.FileInput(
                attrs={
                    'id': 'sub3_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint4': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint4': forms.FileInput(
                attrs={
                    'id': 'sub4_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint5': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint5': forms.FileInput(
                attrs={
                    'id': 'sub5_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint6': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint6': forms.FileInput(
                attrs={
                    'id': 'sub6_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint7': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint7': forms.FileInput(
                attrs={
                    'id': 'sub7_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint8': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint8': forms.FileInput(
                attrs={
                    'id': 'sub8_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint9': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint9': forms.FileInput(
                attrs={
                    'id': 'sub9_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint10': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint10': forms.FileInput(
                attrs={
                    'id': 'sub10_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint11': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint11': forms.FileInput(
                attrs={
                    'id': 'sub11_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint12': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint12': forms.FileInput(
                attrs={
                    'id': 'sub12_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint13': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint13': forms.FileInput(
                attrs={
                    'id': 'sub13_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint14': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint14': forms.FileInput(
                attrs={
                    'id': 'sub14_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint15': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint15': forms.FileInput(
                attrs={
                    'id': 'sub15_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint16': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint16': forms.FileInput(
                attrs={
                    'id': 'sub16_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint17': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint17': forms.FileInput(
                attrs={
                    'id': 'sub17_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint18': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint18': forms.FileInput(
                attrs={
                    'id': 'sub18_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint19': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint19': forms.FileInput(
                attrs={
                    'id': 'sub19_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint20': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint20': forms.FileInput(
                attrs={
                    'id': 'sub20_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint21': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint21': forms.FileInput(
                attrs={
                    'id': 'sub21_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint22': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint22': forms.FileInput(
                attrs={
                    'id': 'sub22_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint23': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint23': forms.FileInput(
                attrs={
                    'id': 'sub23_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint24': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint24': forms.FileInput(
                attrs={
                    'id': 'sub24_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint25': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint25': forms.FileInput(
                attrs={
                    'id': 'sub25_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint26': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint26': forms.FileInput(
                attrs={
                    'id': 'sub26_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint27': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint27': forms.FileInput(
                attrs={
                    'id': 'sub27_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint28': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint28': forms.FileInput(
                attrs={
                    'id': 'sub28_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint29': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint29': forms.FileInput(
                attrs={
                    'id': 'sub29_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'hint30': forms.FileInput(
                attrs={
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
            'sub_hint30': forms.FileInput(
                attrs={
                    'id': 'sub30_file',
                    'style': 'border-color:black;display: none;',
                    'onchange': 'checkSize(this)'
                }
            ),
        }