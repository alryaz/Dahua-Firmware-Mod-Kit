from .config import *

DAHUA_FILES = OrderedDict([
    (
        "Install.lua", {
		    "required": True,
            "type": DAHUA_TYPE.Plain
        }
    ), (
        "u-boot.bin.img", {
            "required": True,
            "type": DAHUA_TYPE.Plain,
            "size": 0x00080000
        }
    ), (
        "romfs-x.cramfs.img", {
            "required": True,
            "type": DAHUA_TYPE.uImage | DAHUA_TYPE.CramFS,
            "size": 0x01700000
        }
    ), (
        "web-x.cramfs.img", {
            "required": True,
            "type": DAHUA_TYPE.uImage | DAHUA_TYPE.CramFS,
            "size": 0x00380000
        }
    ), (
        "custom-x.cramfs.img", {
            "required": True,
            "type": DAHUA_TYPE.uImage | DAHUA_TYPE.CramFS,
            "size": 0x00080000
        }
    ), (
        "logo-x.cramfs.img", {
            "required": True,
            "type": DAHUA_TYPE.uImage | DAHUA_TYPE.CramFS,
            "size": 0x000C0000
        }
    ), (
        "config-x.img", {
            "required": False,
            "type": DAHUA_TYPE.Plain,
            "size": 0x00140000
        }
    ), (
        "misc-x.img", {
            "required": False,
            "type": DAHUA_TYPE.Plain,
            "size": 0x00280000
        }
    ), (
        "sign.img", {
            "required": True,
            "type": DAHUA_TYPE.Plain
        }
    )
])
