from django.conf import settings


REQUIRE_BASE_URL = getattr(settings, "REQUIRE_BASE_URL", "js")

REQUIRE_BUILD_PROFILE = getattr(settings, "REQUIRE_BUILD_PROFILE", None)

REQUIRE_JS = getattr(settings, "REQUIRE_JS", "require.js")

REQUIRE_STANDALONE_MODULES = getattr(settings, "REQUIRE_STANDALONE_MODULES", {}) 

REQUIRE_DEBUG = getattr(settings, "REQUIRE_DEBUG", settings.DEBUG)

REQUIRE_EXCLUDE = getattr(settings, "REQUIRE_EXCLUDE", ("build.txt",))