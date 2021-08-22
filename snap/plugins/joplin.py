from snapcraft.plugins.v2 import PluginV2
from typing import Any, Dict, List, Set


class PluginImpl(PluginV2):

	@classmethod
	def get_schema(cls) -> Dict[str, Any]:
		return {
			"$schema": "http://json-schema.org/draft-04/schema#",
			"type": "object",
			"additionalProperties": False,
		}

	def get_build_snaps(self) -> Set[str]:
		return {"node/16/stable"}

	def get_build_packages(self) -> Set[str]:
		return {"python", "rsync", "libsecret-1-dev", "curl"}

	def get_build_environment(self) -> Dict[str, str]:
		return dict(
			npm_config_unsafe_perm="true",
			SUDO_UID="0",
			SUDO_GID="0",
			SUDO_USER="root",
			npm_config_prefer_offline="true"
		)

	@staticmethod
	def _apply_patches() -> List[str]:
		return [
			"patch -i $SNAPCRAFT_PROJECT_DIR/snap/local/patches/SQLite_directory.patch -p 1"
		]

	@staticmethod
	def _build_commands() -> List[str]:
		return [
			"npm install",
			"mkdir -p $SNAPCRAFT_PART_INSTALL/packages", 
			"cp -r packages/{fork-htmlparser2,lib,renderer,server,tools} ${SNAPCRAFT_PART_INSTALL}/packages",
			"cp -r node_modules/ ${SNAPCRAFT_PART_INSTALL}/node_modules",
		]

	def get_build_commands(self) -> List[str]:
		return self._apply_patches() +  self._build_commands()
