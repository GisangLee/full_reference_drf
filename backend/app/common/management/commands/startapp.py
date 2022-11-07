import os

from django.conf import settings
from django.core.management import CommandError
from django.core.management.templates import TemplateCommand


class Command(TemplateCommand):
    help = (
        "Creates a Django app directory structure for the given app name in "
        "the current directory or optionally in the given directory."
    )
    missing_args_message = "You must provide an application name."

    def handle(self, **options):
        app_name = options.pop("name")

        version = self._input_version()
        options["api_version"] = f"v{version}"

        self._create_app(
            app_name=app_name,
            app_or_api="app",
            template_name="app_template",
            **options,
        )
        self._create_app(
            app_name=app_name,
            app_or_api="api",
            template_name="api_template",
            **options,
        )

    def _create_app(self, app_name, app_or_api, template_name, **options):
        if app_or_api == "app":
            target = f"app/{app_name}"
        else:
            target = f'api/{options["api_version"]}/{app_name}'
        top_dir = os.path.abspath(os.path.expanduser(target))
        try:
            self._make_dirs(top_dir)
            options["template"] = "file://" + str(settings.PROJ_DIR / "app" / "common" / "management" / template_name)
            super().handle("app", app_name, target, **options)
        except CommandError as e:
            print(f"에러 : {e}")
            self.stderr.write(f'"{app_name}" {app_or_api} is already exists.')

    def _input_version(self):
        version = None
        while version is None:
            version = input("Enter API Version [default: 1]: ") or "1"
            try:
                return int(version)
            except ValueError:
                self.stderr.write("Version must be type int.")
                return self._input_version()

    @staticmethod
    def _make_dirs(top_dir):
        try:
            os.makedirs(top_dir)
        except FileExistsError:
            raise CommandError("'%s' already exists" % top_dir)
        except OSError as e:
            raise CommandError(e)
