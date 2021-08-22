[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/joplin-server)

# This snap is currently in an alpha state!
This snap is intentionally not distributed in the Snap Store.
Keep backups of your data, make use of Joplins export functionality!
For the time being, I haven't commited to work on this snap properly, there might not be any future releases.
Being in alpha, upgrading to any possible future releases might result in incompatibilities.
SQLite is used as a database backend, not PostgreSQL, to evaluate if PostgreSQL is critical for performance and worth the additional complexity.
Future releases may transition to PostgreSQL, and if this happens, existing users would have to manage this migration manually.
Snaps not downloaded from the Snap Store do not use the package managers update functionality.

Download the latest release from the [releases](https://github.com/MrCarroll/joplin-server-snap/releases) and use `sudo snap install joplin-server_local.snap --dangerous` to install it.

# Main

This repository contains the build files for a snap version of Joplin Server, Joplins own synchronisation platform.
Users who don't wish to self host can use other synchronisation targets (Dropbox, OneDrive, etc) or make use of the [official hosting services](https://joplinapp.org/plans/). 
Joplin Cloud makes use of the Joplin Server software and directly funds Joplin development.

Joplin Server is free for personal use.
Whilst Joplin Server is source available, it is not released under an open source license.
This repository is licensed MIT and covers exclusively the Snap build files.
Joplin Servers' license is viewable [here](https://github.com/laurent22/joplin/blob/dev/packages/server/LICENSE).

# Usage

Simply installing the snap should automatically setup a functioning instance of Joplin Server, accessible at http://localhost:22300
The default username is `admin@localhost` and the default password is `admin`, this password should be changed immediately.
Make a new user account as desired and begin to synchronise with it via normal Joplin clients via the synchronisation settings.

The snap comes with [Caddy](https://caddyserver.com/) built in, which will be enabled automatically when needed.
Caddy will also transparently manage HTTPS certificates, acquiring and renewing them as needed.

The user can run `sudo snap set joplin-server base-url=http://example.com"` to change the URL Joplin Server will respond to.
If the URL begins with `https://`, Caddy will attempt to automatically generate a HTTPS certificate.
If the URL contains `localhost`, Caddy will disable automatically.
If the user does not desire to use the Caddy built into the snap, for example to use their own reverse-proxy, run `sudo snap set joplin-server proxy-enabled=0`

The status of the snap can be viewed with `systemctl status snap.joplin-server.joplin-server` and `systemctl status snap.joplin-server.caddy`.

Logs can be viewed with `journalctl -u snap.joplin-server.joplin-server` and `journalctl -u snap.joplin-server.caddy`
