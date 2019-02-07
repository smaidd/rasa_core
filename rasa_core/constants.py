DEFAULT_SERVER_PORT = 5005

DEFAULT_SERVER_FORMAT = "http://localhost:{}"

DEFAULT_SERVER_URL = DEFAULT_SERVER_FORMAT.format(DEFAULT_SERVER_PORT)

MINIMUM_COMPATIBLE_VERSION = "0.13.0a6"

DOCS_BASE_URL = "https://rasa.com/docs/core"

DEFAULT_NLU_FALLBACK_THRESHOLD = 0.0

DEFAULT_CORE_FALLBACK_THRESHOLD = 0.0

DEFAULT_FALLBACK_ACTION = "action_default_fallback"

DEFAULT_REQUEST_TIMEOUT = 60 * 5  # 5 minutes

MEMO_SCORE = 1.1

FALLBACK_SCORE = 1.2

FORM_SCORE = 1.3

MAPPING_SCORE = 1.4

REQUESTED_SLOT = 'requested_slot'

# start of special user message section
INTENT_MESSAGE_PREFIX = "/"

USER_INTENT_RESTART = INTENT_MESSAGE_PREFIX + "restart"

USER_INTENT_OUT_OF_SCOPE = 'out_of_scope'
