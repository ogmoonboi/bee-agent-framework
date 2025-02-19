# SPDX-License-Identifier: Apache-2.0

import re


def is_valid_regex(pattern: str) -> bool:
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False
