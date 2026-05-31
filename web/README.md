# Dirac WebUI

This folder is intentionally thin. The frontend is replaceable and must talk only to the HTTP API exposed by `dirac/api`.

Do not import Python modules from here. Do not depend on runtime storage details. Build an API client first, then UI surfaces.
