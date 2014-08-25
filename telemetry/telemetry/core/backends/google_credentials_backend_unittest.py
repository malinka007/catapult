# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
from telemetry.core.backends import form_based_credentials_backend_unittest_base
from telemetry.core.backends import google_credentials_backend


class TestGoogleCredentialsBackend(
    form_based_credentials_backend_unittest_base.
    FormBasedCredentialsBackendUnitTestBase):
  def setUp(self):
    self._credentials_type = 'google'

  def testLoginUsingMock(self):
    self._LoginUsingMock(google_credentials_backend.GoogleCredentialsBackend(),
                         'https://accounts.google.com/', 'Email', 'Passwd',
                         'gaia_loginform',
                         'document.getElementById("gb")!== null')
