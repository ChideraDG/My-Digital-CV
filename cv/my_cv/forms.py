from django import forms


class ContactForm(forms.Form):
    """
    A form for handling general contact inquiries.

    Attributes:
        name (CharField): The name of the person submitting the form.
        email (EmailField): The email address of the person submitting the form.
        subject (CharField): The subject of the contact inquiry.
        message (CharField): The message being sent.

    Example:
        >>> from django import forms
        >>> form = ContactForm({
        ...     'name': 'John Doe',
        ...     'email': 'john@example.com',
        ...     'subject': 'Test Subject',
        ...     'message': 'This is a test message.'
        ... })
        >>> form.is_valid()
        True
    """
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-a',
            'placeholder': 'Your Name',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg form-control-a',
            'placeholder': 'Your Email',
            'required': 'required'
        })
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg form-control-a',
            'placeholder': 'Subject',
            'required': 'required'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Message',
            'cols': 45,
            'rows': 8,
            'required': 'required'
        })
    )
