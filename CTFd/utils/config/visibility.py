from CTFd.constants.config import (
    AccountVisibilityTypes,
    ChallengeVisibilityTypes,
    ConfigTypes,
    RegistrationVisibilityTypes,
    ScoreVisibilityTypes,
    CTFdFooterVisibilityTypes,
    FlagTabVisibilityTypes,
    ExplanationTabVisibilityTypes,
)
from CTFd.utils import get_config
from CTFd.utils.user import authed, is_admin


def challenges_visible():
    v = get_config(ConfigTypes.CHALLENGE_VISIBILITY)
    if v == ChallengeVisibilityTypes.PUBLIC:
        return True
    elif v == ChallengeVisibilityTypes.PRIVATE:
        return authed()
    elif v == ChallengeVisibilityTypes.ADMINS:
        return is_admin()


def scores_visible():
    v = get_config(ConfigTypes.SCORE_VISIBILITY)
    if v == ScoreVisibilityTypes.PUBLIC:
        return True
    elif v == ScoreVisibilityTypes.PRIVATE:
        return authed()
    elif v == ScoreVisibilityTypes.HIDDEN:
        return False
    elif v == ScoreVisibilityTypes.ADMINS:
        return is_admin()


def accounts_visible():
    v = get_config(ConfigTypes.ACCOUNT_VISIBILITY)
    if v == AccountVisibilityTypes.PUBLIC:
        return True
    elif v == AccountVisibilityTypes.PRIVATE:
        return authed()
    elif v == AccountVisibilityTypes.ADMINS:
        return is_admin()


def registration_visible():
    v = get_config(ConfigTypes.REGISTRATION_VISIBILITY)
    if v == RegistrationVisibilityTypes.PUBLIC:
        return True
    elif v == RegistrationVisibilityTypes.PRIVATE:
        return False
    else:
        return False

def ctfd_footer_visible():
    v = get_config(ConfigTypes.CTFD_FOOTER_VISIBILITY)
    if v == CTFdFooterVisibilityTypes.SHOWN:
        return True
    elif v == CTFdFooterVisibilityTypes.HIDDEN:
        return False
    else:
        return False

def flag_tab_visible( solved_by_me ):
    v = get_config(ConfigTypes.FLAG_TAB_VISIBILITY)
    if v == FlagTabVisibilityTypes.SHOWN:
        return True
    elif v == FlagTabVisibilityTypes.SOLVED:
        return solved_by_me
    elif v == FlagTabVisibilityTypes.SOLVED_OR_ADMINS:
        return solved_by_me or is_admin()
    elif v == FlagTabVisibilityTypes.ADMINS:
        return is_admin()
    elif v == FlagTabVisibilityTypes.HIDDEN:
        return False

def explanation_tab_visible( solved_by_me ):
    v = get_config(ConfigTypes.EXPLANATION_TAB_VISIBILITY)
    if v == ExplanationTabVisibilityTypes.SHOWN:
        return True
    elif v == ExplanationTabVisibilityTypes.SOLVED:
        return solved_by_me
    elif v == ExplanationTabVisibilityTypes.SOLVED_OR_ADMINS:
        return solved_by_me or is_admin()
    elif v == ExplanationTabVisibilityTypes.ADMINS:
        return is_admin()
    elif v == ExplanationTabVisibilityTypes.HIDDEN:
        return False
