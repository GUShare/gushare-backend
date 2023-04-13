# This conftest file will be discovered first and summarizes all files in the ./conftest_files directory.
# The conftest file is split up into these files for clarity and brevity.
# Everything is handled according to the pytest documentiation
# found here: https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions

from api.tests.conftest_files.booking_conftest import *  # noqa
from api.tests.conftest_files.building_conftest import *  # noqa
from api.tests.conftest_files.general_conftest import *  # noqa
from api.tests.conftest_files.room_conftest import *  # noqa
from api.tests.conftest_files.user_conftest import *  # noqa
from api.tests.conftest_files.workplace_conftest import *  # noqa
