from django import forms
from information.models import SerialEntrepreneur, Angel, Reviews, Person, SocialProfile


class Onboard_Serial(forms.ModelForm):
    name = forms.SlugField(label="Your name", required=True)
    email = forms.EmailField(label="Email - all the same boring stuff",
                             required=True,
                             max_length=120)
    angel_profile = forms.URLField(label="Angel Profile",
                                   required=True,
                                   max_length=120)
    crunchbase_profile = forms.URLField(label="Crunchbase profile",
                                        required=False,
                                        max_length=120)
    twitter_profile = forms.URLField(label="Twitter profile",
                                     required=False,
                                     max_length=120)
    linkedin_profile = forms.URLField(label="Linkedin profile",
                                      required=False,
                                      max_length=120)
    angel1 = forms.CharField(label="Best angel",
                             required=False,
                             max_length=30)
    angel1_review = forms.CharField(label="Why is he/she great?",
                                    required=False,
                                    max_length=200)
    angel2 = forms.CharField(label="2nd best angel",
                             required=False,
                             max_length=30)
    angel2_review = forms.CharField(label="Why is he/she great?",
                                    required=False,
                                    max_length=200)
    angel3 = forms.CharField(label="3rd best angel",
                             required=False,
                             max_length=30)
    angel3_review = forms.CharField(label="Why is he/she great?",
                                    required=False,
                                    max_length=200)


# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = SerialEntrepreneur
#         fields = ('person', 'social', 'timestamp', 'reviews')
#         widgets = {
#             'person': Textarea(attrs={'cols': 80, 'rows': 20}),
#         }

    class Meta:
        model = SerialEntrepreneur
        fields = [
            'name',
            'email',
            'angel_profile',
            'crunchbase_profile',
            'twitter_profile',
            'linkedin_profile',
            'angel1',
            'angel1_review',
            'angel2',
            'angel2_review',
            'angel3',
            'angel3_review',
        ]


class Onboard_Angel(forms.ModelForm):
    name = forms.SlugField(label="Your name", required=True)
    email = forms.EmailField(label="Email - all the same boring stuff",
                             required=True,
                             max_length=120)
    angel_profile = forms.URLField(label="Angel Profile",
                                   required=True,
                                   max_length=120)
    acredited = forms.BooleanField(label="Are you an acredited investor?",
                                   required=True)
    past_investments = forms.IntegerField(
                             label="How many investments to date?",
                             required=True)
    acquisitions = forms.IntegerField(label="Number of acquisitions to date",
                                      required=True)
    ipos = forms.IntegerField(label="How many IPOs to date", required=True)
    yearly_investments = forms.IntegerField(
                               label="Number of investments per year",
                               required=True)

    class Meta:
        model = Angel
        fields = []
        # fields = [
        #     'name',
        #     'email',
        #     'angel_profile',
        #     'acredited',
        #     'past_investments',
        #     'acquisitions',
        #     'ipos',
        #     'yearly_investments',
        # ]
