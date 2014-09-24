from frasco import Feature, action, current_app
from frasco_forms import url_for_upload
import hashlib
import urllib


class UsersAvatarFeature(Feature):
    name = "users_avatar"
    requires = ["users", "forms"]
    defaults = {"avatar_column": "avatar_filename",
                "default_url": None,
                "use_gravatar": True,
                "gravatar_email_column": None,
                "gravatar_size": 80}

    def init_app(self, app):
        self.user_model = app.features.models.ensure_model(app.features.users.model,
            **dict([(self.options["avatar_column"], str)]))
        self.user_model.avatar_url = property(self.get_avatar_url)

    def get_avatar_url(self, user):
        filename = getattr(user, self.options["avatar_column"], None)
        if filename:
            return url_for_upload(filename)
        if self.options["use_gravatar"]:
            emailcol = self.options["gravatar_email_column"] or \
                current_app.features.users.options["email_column"]
            email = getattr(user, emailcol, None)
            if email:
                return self.get_gravatar_url(email)
        return self.options["default_url"]

    @action("gravatar_url", default_option="email", as_="gravatar_url")
    def get_gravatar_url(self, email, size=None, default=None):
        h = hashlib.md5(email.lower()).hexdigest()
        size = size or self.options["gravatar_size"]
        url = "http://www.gravatar.com/avatar/%s?s=%s" % (h, size)
        default = default or self.options["default_url"]
        if default:
            url += "&d=%s" % urllib.quote(default)
        return url