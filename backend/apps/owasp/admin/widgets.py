"""Custom widgets for OWASP admin."""

from django import forms
from django.utils.safestring import mark_safe


class ChannelIdWidget(forms.TextInput):
    """Custom widget for channel_id with search functionality."""

    def __init__(self, *args, **kwargs):
        """Initialize the widget with custom attributes.

        Args:
            *args: Positional arguments passed to parent.
            **kwargs: Keyword arguments passed to parent.

        """
        super().__init__(*args, **kwargs)
        self.attrs.update({"class": "vForeignKeyRawIdAdminField", "placeholder": "Channel ID"})

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget with a search button.

        Args:
            name (str): The name of the widget.
            value: The current value of the widget.
            attrs (dict): Additional HTML attributes.
            renderer: The form renderer.

        Returns:
            str: The rendered HTML with search button.

        """
        widget_html = super().render(name, value, attrs, renderer)

        search_button = (
            "<a href='/a/slack/conversation/' class='related-lookup'"
            f"id='lookup_id_{name}' title='Look up related objects'></a>"
        )

        return mark_safe(f"{widget_html}{search_button}")  # noqa: S308
