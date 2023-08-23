#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sentry_sdk

sentry_sdk.init(
  dsn="https://944317269ceca9624ba667df83b91d6b@o4505753015484416.ingest.sentry.io/4505753256329216",

  # Set traces_sample_rate to 1.0 to capture 100%
  # of transactions for performance monitoring.
  # We recommend adjusting this value in production.
  traces_sample_rate=1.0
)

division_by_zero = 1 / 0