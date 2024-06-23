from wtforms import BooleanField, FileField, SelectField, StringField, TextAreaField
from wtforms.fields.html5 import IntegerField, URLField
from wtforms.widgets.html5 import NumberInput

from CTFd.constants.config import (
    AccountVisibilityTypes,
    ChallengeVisibilityTypes,
    RegistrationVisibilityTypes,
    ScoreVisibilityTypes,
    CTFdFooterVisibilityTypes,
    FlagTabVisibilityTypes,
    ExplanationTabVisibilityTypes,
)
from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.utils.csv import get_dumpable_tables


class ResetInstanceForm(BaseForm):
    accounts = BooleanField(
        "Accounts",
        description="Deletes all user and team accounts and their associated information",
    )
    submissions = BooleanField(
        "Submissions",
        description="Deletes all records that accounts gained points or took an action",
    )
    challenges = BooleanField(
        "Challenges", description="Deletes all challenges and associated data"
    )
    pages = BooleanField(
        "Pages", description="Deletes all pages and their associated files"
    )
    notifications = BooleanField(
        "Notifications", description="Deletes all notifications"
    )
    submit = SubmitField("Reset CTF")


class AccountSettingsForm(BaseForm):
    domain_whitelist = StringField(
        "Email Domain Allowlist",
        description="Comma-seperated list of allowable email domains which users can register under (e.g. examplectf.com, example.com, *.example.com)",
    )
    team_creation = SelectField(
        "Team Creation",
        description="Control whether users can create their own teams (Teams mode only)",
        choices=[("true", "Enabled"), ("false", "Disabled")],
        default="true",
    )
    team_size = IntegerField(
        widget=NumberInput(min=0),
        description="Maximum number of users per team (Teams mode only)",
    )
    num_teams = IntegerField(
        "Maximum Number of Teams",
        widget=NumberInput(min=0),
        description="Maximum number of teams allowed to register with this CTF (Teams mode only)",
    )
    num_users = IntegerField(
        "Maximum Number of Users",
        widget=NumberInput(min=0),
        description="Maximum number of user accounts allowed to register with this CTF",
    )
    verify_emails = SelectField(
        "Verify Emails",
        description="Control whether users must confirm their email addresses before playing",
        choices=[("true", "Enabled"), ("false", "Disabled")],
        default="false",
    )
    empty_email_allowed = SelectField(
        "Allow Empty Emails",
        description="Control whether users can set their addresses empty before participating",
        choices=[("true", "Enabled"), ("false", "Disabled")],
        default="false",
    )
    set_reset_password_message = SelectField(
        "Set Reset-Password Message",
        description="Add or replace message of reset-password page with following the custom message",
        choices=[("add", "Add"), ("replace", "Replace"), ("disabled", "Disabled")],
        default="disabled",
    )
    reset_password_message = TextAreaField(
        "Reset Password Message",
        description="Text shown on the Reset-Password page according to the choice on previous setting",
    )
    team_disbanding = SelectField(
        "Team Disbanding",
        description="Control whether team captains are allowed to disband their own teams",
        choices=[
            ("inactive_only", "Enabled for Inactive Teams"),
            ("disabled", "Disabled"),
        ],
        default="inactive_only",
    )
    name_changes = SelectField(
        "Name Changes",
        description="Control whether users and teams can change their names",
        choices=[("true", "Enabled"), ("false", "Disabled")],
        default="true",
    )
    incorrect_submissions_per_min = IntegerField(
        "Incorrect Submissions per Minute",
        widget=NumberInput(min=1),
        description="Number of submissions allowed per minute for flag bruteforce protection (default: 10)",
    )

    submit = SubmitField("Update")


class ExportCSVForm(BaseForm):
    table = SelectField("Database Table", choices=get_dumpable_tables())
    submit = SubmitField("Download CSV")


class ImportCSVForm(BaseForm):
    csv_type = SelectField(
        "CSV Type",
        choices=[("users", "Users"), ("teams", "Teams"), ("challenges", "Challenges")],
        description="Type of CSV data",
    )
    csv_file = FileField("CSV File", description="CSV file contents")


class SocialSettingsForm(BaseForm):
    social_shares = SelectField(
        "Social Shares",
        description="Enable or Disable social sharing links for challenge solves",
        choices=[("true", "Enabled"), ("false", "Disabled")],
        default="true",
    )
    submit = SubmitField("Update")


class LegalSettingsForm(BaseForm):
    tos_url = URLField(
        "Terms of Service URL",
        description="External URL to a Terms of Service document hosted elsewhere",
    )
    tos_text = TextAreaField(
        "Terms of Service",
        description="Text shown on the Terms of Service page",
    )
    privacy_url = URLField(
        "Privacy Policy URL",
        description="External URL to a Privacy Policy document hosted elsewhere",
    )
    privacy_text = TextAreaField(
        "Privacy Policy",
        description="Text shown on the Privacy Policy page",
    )
    submit = SubmitField("Update")


class VisibilitySettingsForm(BaseForm):
    challenge_visibility = SelectField(
        "Challenge Visibility",
        description="Control whether users must be logged in to see challenges",
        choices=[
            (ChallengeVisibilityTypes.PUBLIC, "Public"),
            (ChallengeVisibilityTypes.PRIVATE, "Private"),
            (ChallengeVisibilityTypes.ADMINS, "Admins Only"),
        ],
        default=ChallengeVisibilityTypes.PRIVATE,
    )
    account_visibility = SelectField(
        "Account Visibility",
        description="Control whether accounts (users & teams) are shown to everyone, only to authenticated users, or only to admins",
        choices=[
            (AccountVisibilityTypes.PUBLIC, "Public"),
            (AccountVisibilityTypes.PRIVATE, "Private"),
            (AccountVisibilityTypes.ADMINS, "Admins Only"),
        ],
        default=AccountVisibilityTypes.PUBLIC,
    )
    score_visibility = SelectField(
        "Score Visibility",
        description="Control whether solves/score are shown to the public, to logged in users, hidden to all non-admins, or only shown to admins",
        choices=[
            (ScoreVisibilityTypes.PUBLIC, "Public"),
            (ScoreVisibilityTypes.PRIVATE, "Private"),
            (ScoreVisibilityTypes.HIDDEN, "Hidden"),
            (ScoreVisibilityTypes.ADMINS, "Admins Only"),
        ],
        default=ScoreVisibilityTypes.PUBLIC,
    )
    registration_visibility = SelectField(
        "Registration Visibility",
        description="Control whether registration is enabled for everyone or disabled",
        choices=[
            (RegistrationVisibilityTypes.PUBLIC, "Public"),
            (RegistrationVisibilityTypes.PRIVATE, "Private"),
            (RegistrationVisibilityTypes.MLC, "MajorLeagueCyber Only"),
        ],
        default=RegistrationVisibilityTypes.PUBLIC,
    )
    ctfd_footer_visibility = SelectField(
        "CTFd Footer Visibility",
        description="Control whether CTFd footer in each page is shown",
        choices=[
            (CTFdFooterVisibilityTypes.SHOWN, "Shown"),
            (CTFdFooterVisibilityTypes.HIDDEN, "Hidden"),
        ],
        default=CTFdFooterVisibilityTypes.SHOWN,
    )
    flag_tab_visibility = SelectField(
        "Flag Tab Visibility",
        description="Control whether the flag tab in each challenge is shown",
        choices=[
            (FlagTabVisibilityTypes.SHOWN, "Shown"),
            (FlagTabVisibilityTypes.SOLVED, "Solved Only"),
            (FlagTabVisibilityTypes.SOLVED_OR_ADMINS, "Solved or Admins Only"),
            (FlagTabVisibilityTypes.ADMINS, "Admins Only"),
            (FlagTabVisibilityTypes.HIDDEN, "Hidden"),
        ],
        default=FlagTabVisibilityTypes.HIDDEN,
    )
    explanation_tab_visibility = SelectField(
        "Explanation Tab Visibility",
        description="Control whether the explanation tab in each challenge is shown",
        choices=[
            (ExplanationTabVisibilityTypes.SHOWN, "Shown"),
            (ExplanationTabVisibilityTypes.SOLVED, "Solved Only"),
            (ExplanationTabVisibilityTypes.SOLVED_OR_ADMINS, "Solved or Admins Only"),
            (ExplanationTabVisibilityTypes.ADMINS, "Admins Only"),
            (ExplanationTabVisibilityTypes.HIDDEN, "Hidden"),
        ],
        default=ExplanationTabVisibilityTypes.HIDDEN,
    )
